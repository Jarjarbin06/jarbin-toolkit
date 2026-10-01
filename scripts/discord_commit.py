from __future__ import annotations

import json
import os
import sys
import traceback
from datetime import datetime, timezone
from time import sleep
from typing import NoReturn
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


GITHUB_API_URL = "https://api.github.com"
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_EVENT_PATH = os.environ.get("GITHUB_EVENT_PATH")

VERSION_FILE = os.environ.get("VERSION_FILE", "VERSION")
VERSION_MAX_LENGTH = 50

# Network behaviour. Keep this script from ever hanging a CI job forever,
# and tolerate transient blips (GitHub/Discord 5xx, rate limiting) without
# failing the whole notification.
REQUEST_TIMEOUT = 15  # seconds
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = 2.0

# How many commits of a push to touch at all. A huge force-push or initial
# import could otherwise trigger hundreds of GitHub API calls.
MAX_COMMITS_FETCHED = 25
MAX_COMMITS_LISTED = 10
MAX_FILES_DISPLAYED = 30

# Discord's hard embed limits, with a safety margin kept below each one:
# title <= 256, description <= 4096, field value <= 1024, footer <= 2048.
MAX_TITLE_LENGTH = 256
MAX_EMBED_DESCRIPTION = 4000
MAX_FIELD_VALUE = 1000
MAX_FOOTER_TEXT = 2000


def fail(message: str) -> NoReturn:
    """Print an error and terminate the program."""
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def validate_environment() -> None:
    """Fail fast if required configuration is missing, before any network call."""
    required = ("DISCORD_WEBHOOK_URL", "GITHUB_TOKEN", "GITHUB_EVENT_PATH")
    missing = [name for name in required if not os.environ.get(name)]

    if missing:
        fail(f"Missing required environment variable(s): {', '.join(missing)}")


def load_event() -> dict:
    """Load the GitHub Actions event payload."""
    try:
        with open(GITHUB_EVENT_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        fail(f"Unable to read GitHub event: {error}")


def get_repo_version(path: str = VERSION_FILE) -> str | None:
    """Read the repository's VERSION file (e.g. 'v1.0.0'), if present.

    Only the first line is used, and it's capped to a sane length, so an
    unexpected or malformed VERSION file can't distort the notification.
    Any failure here is non-fatal: the script simply continues without one.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            first_line = file.readline()
    except OSError as error:
        print(
            f"WARNING: Unable to read '{path}': {error}. "
            "Continuing without a version.",
            file=sys.stderr,
        )
        return None

    version = first_line.strip()

    if not version:
        print(f"WARNING: '{path}' is empty. Continuing without a version.", file=sys.stderr)
        return None

    if len(version) > VERSION_MAX_LENGTH:
        print(f"WARNING: '{path}' content is unexpectedly long; truncating.", file=sys.stderr)
        version = version[:VERSION_MAX_LENGTH]

    return version


def _clamp(text: str, limit: int, *, suffix: str = "…") -> str:
    """Hard-cap text to `limit` characters, appending `suffix` if truncated."""
    if len(text) <= limit:
        return text

    cut = max(limit - len(suffix), 0)
    return text[:cut] + suffix


def _sanitize_inline(text: str) -> str:
    """Prevent untrusted text from breaking a single-backtick inline code span."""
    return text.replace("`", "ˋ") if text else text


def _sanitize_block(text: str) -> str:
    """Prevent untrusted text from breaking out of a ```diff fenced code block."""
    return text.replace("```", "``\u200b`") if text else text


def _http_request(request: Request, *, context: str) -> bytes:
    """Perform an HTTP request with a timeout and retries on transient failure.

    Retries on HTTP 429 (respecting Retry-After when present), HTTP 5xx, and
    network-level errors. Any other HTTP error is raised immediately.
    """
    last_error: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urlopen(request, timeout=REQUEST_TIMEOUT) as response:
                return response.read()
        except HTTPError as error:
            retryable = error.code == 429 or 500 <= error.code < 600

            if retryable and attempt < MAX_RETRIES:
                if error.code == 429:
                    retry_after = error.headers.get("Retry-After") if error.headers else None
                    try:
                        delay = float(retry_after) if retry_after else RETRY_BACKOFF_SECONDS * attempt
                    except ValueError:
                        delay = RETRY_BACKOFF_SECONDS * attempt
                else:
                    delay = RETRY_BACKOFF_SECONDS * attempt

                print(
                    f"WARNING: {context} returned HTTP {error.code}. "
                    f"Retrying in {delay:.1f}s (attempt {attempt}/{MAX_RETRIES})...",
                    file=sys.stderr,
                )
                sleep(delay)
                last_error = error
                continue

            raise
        except OSError as error:
            if attempt < MAX_RETRIES:
                delay = RETRY_BACKOFF_SECONDS * attempt
                print(
                    f"WARNING: {context} network error ({error}). "
                    f"Retrying in {delay:.1f}s (attempt {attempt}/{MAX_RETRIES})...",
                    file=sys.stderr,
                )
                sleep(delay)
                last_error = error
                continue

            raise

    if last_error is not None:
        raise last_error

    raise RuntimeError(f"{context}: request failed with no response")


def github_request(endpoint: str) -> dict | None:
    """Perform an authenticated GET request to the GitHub API.

    Returns None (after logging a warning) on failure instead of aborting
    the whole script, so callers can degrade gracefully.
    """
    if not GITHUB_TOKEN:
        fail("GITHUB_TOKEN is not defined.")

    request = Request(
        f"{GITHUB_API_URL}{endpoint}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )

    try:
        body = _http_request(request, context=f"GitHub API ({endpoint})")
    except HTTPError as error:
        details = error.read().decode("utf-8", errors="replace") if error.fp else ""
        print(f"WARNING: GitHub API {endpoint} returned HTTP {error.code}: {details}", file=sys.stderr)
        return None
    except OSError as error:
        print(f"WARNING: Unable to reach GitHub API ({endpoint}): {error}", file=sys.stderr)
        return None

    try:
        return json.loads(body.decode("utf-8"))
    except json.JSONDecodeError as error:
        print(f"WARNING: GitHub API ({endpoint}) returned invalid JSON: {error}", file=sys.stderr)
        return None


def discord_request(payload: dict) -> None:
    """Send a JSON payload to the Discord webhook."""
    if not DISCORD_WEBHOOK_URL:
        fail("DISCORD_WEBHOOK_URL is not defined.")

    request = Request(
        DISCORD_WEBHOOK_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "GitHub-Discord-Webhook",
        },
        method="POST",
    )

    try:
        _http_request(request, context="Discord webhook")
    except HTTPError as error:
        body = error.read().decode("utf-8", errors="replace") if error.fp else ""
        fail(f"Discord webhook returned HTTP {error.code}: {body}")
    except OSError as error:
        fail(f"Unable to reach Discord: {error}")


def describe_ref(event: dict) -> tuple[str, str]:
    """Describe the pushed ref as (label, name), e.g. ('Branch', 'main') or ('Tag', 'v1.0.0')."""
    ref = event.get("ref", "")

    if ref.startswith("refs/heads/"):
        return "Branch", ref.removeprefix("refs/heads/")

    if ref.startswith("refs/tags/"):
        return "Tag", ref.removeprefix("refs/tags/")

    return "Ref", ref or "unknown"


def get_commit(repository: str, sha: str) -> dict | None:
    """Retrieve a commit from GitHub, or None if the request failed."""
    return github_request(f"/repos/{repository}/commits/{sha}")


def _fallback_commit(event_commit: dict) -> dict:
    """Build an API-shaped commit object out of webhook data alone.

    Used when the GitHub REST API call for this specific commit fails, so
    the notification can still go out with best-effort data. Renames can't
    be detected from webhook data alone, so a rename is reported as a
    remove + add pair instead, and the author's GitHub login is unavailable
    (only their git-configured name/email is), both acceptable degradations.
    """
    sha = event_commit.get("id", "")
    author = event_commit.get("author", {}) or {}
    author_name = author.get("name", "Unknown")

    files = []
    for filename in event_commit.get("added", []) or []:
        files.append({"status": "added", "filename": filename})
    for filename in event_commit.get("modified", []) or []:
        files.append({"status": "modified", "filename": filename})
    for filename in event_commit.get("removed", []) or []:
        files.append({"status": "removed", "filename": filename})

    return {
        "sha": sha,
        "html_url": event_commit.get("url", ""),
        "commit": {
            "message": event_commit.get("message", ""),
            "author": {
                "name": author_name,
                "email": author.get("email", ""),
                "date": event_commit.get("timestamp", ""),
            },
        },
        "author": {"name": author_name},
        "files": files,
    }


def get_commit_changes(commit: dict) -> list[dict]:
    """Extract file changes from a GitHub commit."""
    return commit.get("files", [])


def format_file_change(file: dict) -> str:
    """Convert a GitHub file change into a diff-style line."""
    status = file.get("status")
    filename = _clamp(_sanitize_block(file.get("filename", "unknown")), 150)

    if status == "added":
        return f"+ {filename}"

    if status == "modified":
        return f"~ {filename}"

    if status == "removed":
        return f"- {filename}"

    if status == "renamed":
        previous = _clamp(_sanitize_block(file.get("previous_filename", "unknown")), 100)
        return f"→ {previous} → {filename}"

    return f"~ {filename}"


def collect_changes(commits: list[dict]) -> tuple[list[str], dict]:
    """Collect and count all file changes from the commits."""
    changes = []
    counts = {
        "added": 0,
        "modified": 0,
        "removed": 0,
        "renamed": 0,
    }

    for commit in commits:
        for file in get_commit_changes(commit):
            status = file.get("status")

            if status in counts:
                counts[status] += 1

            changes.append(format_file_change(file))

    return changes, counts


def build_changes_text(changes: list[str]) -> str:
    """Build the Discord diff block."""
    if not changes:
        return "```diff\nNo file changes available.\n```"

    displayed = changes[:MAX_FILES_DISPLAYED]
    remaining = len(changes) - len(displayed)

    lines = displayed.copy()

    if remaining > 0:
        lines.append(f"... {remaining} more file{'s' if remaining != 1 else ''}")

    text = "\n".join(lines)

    return f"```diff\n{text}\n```"


def timestamp_from_commit(commit: dict) -> int | None:
    """Get the Unix timestamp from a GitHub commit."""
    author = commit.get("commit", {}).get("author", {})
    date = author.get("date")

    if not date:
        return None

    try:
        parsed = datetime.fromisoformat(
            date.replace("Z", "+00:00")
        )
        return int(parsed.timestamp())
    except ValueError:
        return None


def build_commit_list(commits: list[dict], total: int) -> str:
    """Build the commit list for the embed, capped to Discord's field-value limit."""
    displayed = commits[-MAX_COMMITS_LISTED:] if len(commits) > MAX_COMMITS_LISTED else commits

    lines = []

    for commit in displayed:
        sha = commit.get("sha", "")[:7]
        message = (
            commit.get("commit", {})
            .get("message", "")
            .splitlines()[0]
            if commit.get("commit", {}).get("message")
            else ""
        )
        message = _clamp(_sanitize_inline(message), 80)
        lines.append(f"`{sha}` {message}")

    hidden = total - len(displayed)

    if hidden > 0:
        lines.append(f"... {hidden} more commit{'s' if hidden != 1 else ''}")

    return _clamp("\n".join(lines), MAX_FIELD_VALUE)


def build_embed(
    event: dict,
    commits: list[dict],
    changes: list[str],
    counts: dict,
    version: str | None,
    total_commits: int,
) -> dict:
    """Build the Discord embed payload."""
    repository = event.get("repository", {})
    repository_name = repository.get("full_name", "Unknown repository")
    repository_url = repository.get(
        "html_url",
        f"https://github.com/{repository_name}",
    )

    ref_label, ref_name = describe_ref(event)
    ref_name = _clamp(_sanitize_inline(ref_name), 100)
    ref_emoji = "🏷️" if ref_label == "Tag" else "🌿"

    first_commit = commits[0]
    last_commit = commits[-1]

    commit_data = last_commit.get("commit", {})
    author_data = commit_data.get("author", {})

    commit_message = (
        first_commit.get("commit", {})
        .get("message", "")
        .splitlines()[0]
        or "Git push"
    )
    commit_message = _clamp(_sanitize_inline(commit_message), 200)

    author = (
        last_commit.get("author", {}) or {}
    ).get(
        "login",
        author_data.get("name", "Unknown"),
    )
    author = _clamp(_sanitize_inline(author), 100)

    commit_sha = last_commit.get("sha", "")
    commit_url = last_commit.get(
        "html_url",
        f"{repository_url}/commit/{commit_sha}",
    )

    before = event.get("before", "")
    after = event.get("after", "")

    if before and after:
        diff_url = (
            f"{repository_url}/compare/"
            f"{before}...{after}"
        )
    else:
        diff_url = commit_url

    timestamp = timestamp_from_commit(last_commit)

    if timestamp is not None:
        date_text = f"<t:{timestamp}:F>"
    else:
        date_text = "Unknown"

    changes_text = build_changes_text(changes)

    version_text = _clamp(_sanitize_inline(version or "Unknown"), VERSION_MAX_LENGTH)

    summary_parts = [
        f"**{counts['added']}** added",
        f"**{counts['modified']}** modified",
        f"**{counts['removed']}** deleted",
    ]

    if counts.get("renamed"):
        summary_parts.append(f"**{counts['renamed']}** renamed")

    description = (
        f"**{commit_message}**\n\n"
        f"📦 **Version**\n"
        f"`{version_text}`\n\n"
        f"{ref_emoji} **{ref_label}**\n"
        f"`{ref_name}`\n\n"
        f"👤 **Author**\n"
        f"{author}\n\n"
        f"🕐 **Date**\n"
        f"{date_text}\n\n"
        f"🔗 **Commit**\n"
        f"`{commit_sha[:7]}`\n\n"
        f"**Changes**\n"
        f"{'─' * 55}\n"
        f"{changes_text}\n\n"
        f"📊 {' • '.join(summary_parts)}"
    )

    if len(description) > MAX_EMBED_DESCRIPTION:
        description = description[:MAX_EMBED_DESCRIPTION - 30]
        description += "\n...\n*Changes truncated.*"

    title = f"GitHub • {repository_name}"

    if version:
        title += f" • {version_text}"

    title = _clamp(title, MAX_TITLE_LENGTH)

    footer_text = (
        f"{repository_name} • "
        f"{version_text} • "
        f"{ref_name} • "
        f"{commit_sha[:7]}"
    )
    footer_text = _clamp(footer_text, MAX_FOOTER_TEXT)

    embed = {
        "title": title,
        "url": commit_url,
        "description": description,
        "color": 0x24292F,
        "fields": [],
        "footer": {"text": footer_text},
    }

    if len(commits) > 1:
        embed["fields"].append({
            "name": f"Commits ({total_commits})",
            "value": build_commit_list(commits, total_commits),
            "inline": False,
        })

    embed["fields"].append({
        "name": "Links",
        "value": (
            f"[View commit]({commit_url}) • "
            f"[View diff]({diff_url})"
        ),
        "inline": False,
    })

    if timestamp is not None:
        embed["timestamp"] = datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()

    return embed


def main() -> None:
    """Process the GitHub push and send the Discord embed."""
    validate_environment()

    event = load_event()

    if event.get("deleted"):
        print("Branch/tag deletion detected. Skipping.")
        return

    repository = event.get("repository", {}).get("full_name")
    event_commits = event.get("commits", [])

    if not repository:
        fail("Repository information is missing.")

    if not event_commits:
        print("No commits in push event. Skipping.")
        return

    version = get_repo_version()

    if version:
        print(f"Repository version: {version}")
    else:
        print("No VERSION file found; continuing without a version.")

    fetch_list = event_commits

    if len(event_commits) > MAX_COMMITS_FETCHED:
        print(
            f"NOTE: Push contains {len(event_commits)} commits; "
            f"fetching details for the most recent {MAX_COMMITS_FETCHED} only."
        )
        fetch_list = event_commits[-MAX_COMMITS_FETCHED:]

    commits = []

    for event_commit in fetch_list:
        sha = event_commit.get("id")

        if not sha:
            continue

        print(f"Fetching commit {sha}...")
        commit = get_commit(repository, sha)

        if commit is None:
            print(f"WARNING: Falling back to webhook data for commit {sha}.", file=sys.stderr)
            commit = _fallback_commit(event_commit)

        commits.append(commit)

    if not commits:
        fail("Unable to retrieve any commits.")

    changes, counts = collect_changes(commits)

    embed = build_embed(
        event,
        commits,
        changes,
        counts,
        version,
        len(event_commits),
    )

    payload = {
        "username": "GitHub",
        "embeds": [embed],
    }

    print(
        f"Sending {len(commits)} commit(s) "
        f"from {repository} to Discord..."
    )

    discord_request(payload)

    print("Discord notification sent successfully.")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        traceback.print_exc()
        fail("Unexpected error — see traceback above.")
