# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Log
# File         : renderer.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import final


@final
class LogRenderer:


    WAITING_MARKER = "[waiting for log...]"
    SEPARATOR = "─" * 76
    BORDER = "═" * 76


    @staticmethod
    def header(
            run_id,
            start,
            metadata = None,
        ):
        lines = [
            LogRenderer.BORDER,
            f"jar-log v2  run={run_id}  start={start}",
        ]

        if metadata:
            for key, value in metadata.items():
                lines.append(
                    f'{key}="{value}"'
                    if isinstance(value, str)
                    else f"{key}={value}"
                )

        lines.extend([
            LogRenderer.SEPARATOR,
            "seq    timestamp                     level     scope        message",
            LogRenderer.SEPARATOR,
            LogRenderer.WAITING_MARKER,
        ])

        return "\n".join(lines) + "\n"


    @staticmethod
    def footer(
            run_id,
            end,
            duration,
            result,
            errors = 0,
            warnings = 0,
            criticals = 0,
        ):
        return "\n".join([
            LogRenderer.SEPARATOR,
            (
                f"run={run_id}  "
                f"end={end}  "
                f"duration_ms={duration}\n"
                f"result={result}  "
                f"errors={errors}  "
                f"warnings={warnings}  "
                f"criticals={criticals}"
            ),
            LogRenderer.BORDER,
        ]) + "\n"


__all__ = [
    'LogRenderer',
]
