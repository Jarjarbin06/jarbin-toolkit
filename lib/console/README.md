<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# 📦 Jarbin-ToolKit:Console v0.1.2.3

> Structured terminal interface system providing unified console I/O, ANSI control, text formatting, and animation rendering through a modular Python API

---

## 🔹 Short Description

**Jarbin-ToolKit Console is a structured terminal abstraction library that unifies console I/O, ANSI sequence generation, text formatting, and animation rendering into a modular, deterministic Python interface.**

It provides:

* unified console input/output with format control
* full ANSI sequence generation (color, cursor, line)
* text and animation object model
* progress bar and spinner rendering system
* terminal size and cursor position introspection

It is **not a TUI framework**, but a **structured terminal I/O and rendering abstraction layer**.

---

## 🔹 Authors

* Nathan (Jarjarbin06)
* Jarbin Studio

---

## 🔹 License

GPL v3

---

## 🔹 Target Audience

This library is intended for:

* Python developers building CLI tools requiring structured output
* developers designing terminal-based interfaces or debug consoles
* projects requiring deterministic ANSI color and cursor control
* engineers building animated terminal feedback systems (progress bars, spinners)

---

## 🔹 Platform Support

* Python ≥ 3.10
* Linux / Windows / macOS compatible
* Terminal introspection features (cursor, key press) require a live TTY (not available in piped or non-interactive environments)

---

## 🔹 Purpose

Jarbin-ToolKit Console aims to:

* abstract terminal I/O behind a unified `Console` interface
* generate ANSI sequences in a structured and composable way
* provide a text object model enabling formatting via method chaining
* render frame-based animations and progress bars in a deterministic model
* expose terminal metadata (size, cursor position) in a safe, cross-platform manner

It is **not a curses replacement**, but a **modular terminal control and rendering toolkit**.

---

## 🔹 Key Features

* Unified `Console` static interface for all terminal I/O
* ANSI sequence generation via composable `ANSI` and `Color` objects
* Cursor manipulation through `Cursor` (move, hide, show, save, restore)
* Line manipulation through `Line` (clear, erase, restore)
* `Text` object with format chaining (`bold`, `italic`, `underline`, `error`, `warning`, etc.)
* `Animation` object with step-based frame rendering
* `ProgressBar` object with percent tracking, spinner integration, and style customization
* `Spinner` factory for standalone spinner animations
* `Style` object for configuring animation visual characters
* Base animation packs (`BasePack`) for Animation and ANSI ready-to-use presets
* Alternate screen entry and exit support
* Terminal size and cursor position introspection
* Configurable via `Setting` (banner, log mode, debug, safe mode)
* Optional log file integration

---

## 🔹 Architecture Overview

```
User Code
   │
   ▼
Console (static interface)
   │
   ├──────────────────────────┐
   ▼                          ▼
Text System               ANSI System
   │                          │
   ├── Text                   ├── ANSI
   └── Format (base)          ├── Color
                              ├── Cursor
                              └── Line
   │                          │
   ▼                          ▼
Animation System          System
   │                          │
   ├── Animation              ├── Setting
   ├── ProgressBar            ├── Log
   ├── Spinner                ├── Config
   ├── Style                  ├── Time / StopWatch
   └── BasePack               └── Error
   │
   ▼
Terminal Rendering Output
```

---

## 🔹 Core Concept

The system is organized around a static `Console` class that serves as the entry point for all terminal operations. All subsystems are independently usable but designed to compose through a shared object model.

### Console

Central static interface to the terminal:

```python
Console.print(*value, separator, start, end, file, auto_reset, cut, sleep)
Console.input(msg, separator, wanted_type)
Console.get_key_press()
Console.get_cursor_position()
Console.get_size()
Console.flush(stream)
Console.enter_alternate_screen(hide_cursor)
Console.exit_alternate_screen(show_cursor)
```

Exposes `stdin`, `stdout`, and `stderr` as class properties.

`ConsoleMeta` implements :
* `__len__` to return the current terminal column width.
* `__enter__` and `__exit__` to open and close automatically the alternate screen using `with Console: ...`

---

### Text

Wraps a string with composable format methods:

```python
text = Text("Hello").bold().underline().error()
```

Inherits from `Format`, which provides all formatting operations as instance methods. Compatible with `ANSI`, `Animation`, and `str` through `__add__`.

---

### ANSI

Wraps an ANSI escape sequence as a composable object:

```python
seq = ANSI(f"{ANSI.ESC}31m")
```

Composable with `Text`, `Animation`, `ProgressBar`, and `str` via `__add__`. All ANSI subsystems return `ANSI` objects.

---

### Color

Generates ANSI color sequences from preset constants or raw values:

```python
Color(Color.C_FG_RED)
Color.rgb_fg(0, 145, 211)
Color.color_bg(42)
```

Instantiation via `__new__` directly returns an `ANSI` object.

---

### Animation

Frame-based animation container:

```python
anim = Animation(["frame1", "frame2", "frame3"])
anim.update()
str(anim)
```

Supports composition via `+`, step tracking, auto-reset, and direct indexing.

---

### ProgressBar

Percent-driven animation renderer:

```python
bar = ProgressBar(length=20, style=Style(...), spinner=Spinner.stick())
bar.update(50)
bar.render(delete=True)
```

Configurable percent style (`num`, `bar`, `mix`), percent position (`b`/`a`), and spinner position.

---

## 🔹 API / Function Documentation

### 🔹 Console

| Name                     | Description                                              |
|--------------------------|----------------------------------------------------------|
| `print`                  | Print formatted output with ANSI, cut, and sleep support |
| `input`                  | Read typed user input with type coercion                 |
| `get_key_press`          | Wait and return a single raw key press                   |
| `get_cursor_position`    | Return current cursor `(row, col)` position              |
| `get_size`               | Return terminal `(width, height)` dimensions             |
| `flush`                  | Flush a given output stream                              |
| `enter_alternate_screen` | Switch to alternate terminal screen                      |
| `exit_alternate_screen`  | Return from alternate terminal screen                    |
| `execute`                | Execute a shell command via `os.system`                  |
| `stdin`                  | Class property: `sys.stdin`                              |
| `stdout`                 | Class property: `sys.stdout`                             |
| `stderr`                 | Class property: `sys.stderr`                             |

---

### 🔹 Text

| Name          | Description                                  |
|---------------|----------------------------------------------|
| `__init__`    | Wraps a string, list, or ANSI into a Text    |
| `__add__`     | Concatenates with another Text, ANSI, or str |
| `__mul__`     | Repeats the text `n` times                   |
| `__str__`     | Returns raw string value                     |
| `__len__`     | Returns character count                      |
| `s`           | Property alias for `__str__`                 |
| `url_link`    | Generates a terminal hyperlink sequence      |
| `file_link`   | Generates a JetBrains file navigation link   |

---

### 🔹 Format (inherited by Text, Animation, ProgressBar)

| Name            | Description                                      |
|-----------------|--------------------------------------------------|
| `reset`         | Apply ANSI reset sequence                        |
| `bold`          | Apply bold format                                |
| `italic`        | Apply italic format                              |
| `underline`     | Apply underline format                           |
| `dim`           | Apply dim format                                 |
| `hide`          | Apply hidden format                              |
| `strikethrough` | Apply strikethrough format                       |
| `error`         | Apply error color (title or body variant)        |
| `warning`       | Apply warning color (title or body variant)      |
| `valid`         | Apply valid/success color                        |
| `debug`         | Apply debug color                                |
| `info`          | Apply info color                                 |
| `critic`        | Apply critical color                             |
| `apply`         | Static: apply any ANSI sequence to any object    |
| `tree`          | Static: format a dict/list as a bash-style tree  |
| `module_tree`   | Static: return the module's tree representation  |

---

### 🔹 ANSI

| Name       | Description                                     |
|------------|-------------------------------------------------|
| `__init__` | Wraps a raw ANSI sequence string or list        |
| `__add__`  | Concatenates with ANSI, Text, Animation, or str |
| `__mul__`  | Repeats the sequence `n` times                  |
| `__str__`  | Returns the raw ANSI string                     |
| `__len__`  | Returns sequence string length                  |
| `s`        | Property alias for `__str__`                    |
| `ESC`      | Class constant: `"\x1b["`                       |

---

### 🔹 Color

| Name              | Description                                         |
|-------------------|-----------------------------------------------------|
| `color`           | Generate ANSI sequence from preset `C_*` constant   |
| `color_fg`        | Generate 256-color foreground sequence              |
| `color_bg`        | Generate 256-color background sequence              |
| `rgb_fg`          | Generate RGB foreground sequence                    |
| `rgb_bg`          | Generate RGB background sequence                    |
| `epitech_fg`      | Epitech brand foreground color (`rgb(0, 145, 211)`) |
| `epitech_bg`      | Epitech brand background color                      |
| `epitech_dark_fg` | Epitech dark foreground color (`rgb(31, 72, 94)`)   |
| `epitech_dark_bg` | Epitech dark background color                       |

---

### 🔹 Cursor

| Name            | Description                                        |
|-----------------|----------------------------------------------------|
| `up`            | Move cursor up `n` lines                           |
| `down`          | Move cursor down `n` lines                         |
| `left`          | Move cursor left `n` columns                       |
| `right`         | Move cursor right `n` columns                      |
| `top`           | Move cursor to top-left corner                     |
| `previous`      | Move to beginning of `n`-th previous line          |
| `next`          | Move to beginning of `n`-th next line              |
| `move`          | Move to absolute `(row, col)` position             |
| `move_column`   | Move to absolute column `x`                        |
| `set`           | Save current cursor position                       |
| `reset`         | Restore saved cursor position                      |
| `show`          | Make cursor visible                                |
| `hide`          | Make cursor invisible                              |

---

### 🔹 Line

| Name                  | Description                                          |
|-----------------------|------------------------------------------------------|
| `clear_line`          | Erase entire current line                            |
| `clear_start_line`    | Erase from start of line to cursor                   |
| `clear_end_line`      | Erase from cursor to end of line                     |
| `clear_screen`        | Erase entire screen                                  |
| `clear`               | Erase screen and move cursor to top-left             |
| `clear_previous_line` | Erase `n` previous lines and reposition cursor       |

---

### 🔹 Animation

| Name          | Description                                          |
|---------------|------------------------------------------------------|
| `__init__`    | Build animation from list or `\`-delimited string    |
| `__add__`     | Compose with another Animation, Text, ANSI, or str   |
| `__getitem__` | Access frame by index (clamped to last frame)        |
| `__str__`     | Return current frame as string                       |
| `__call__`    | Advance one step                                     |
| `__len__`     | Return total frame count                             |
| `update`      | Advance step with optional auto-reset                |
| `render`      | Return current frame string with optional line erase |
| `is_last`     | Return whether current step is the last frame        |
| `reset`       | Reset step counter to 0                              |

---

### 🔹 ProgressBar

| Name          | Description                                              |
|---------------|----------------------------------------------------------|
| `__init__`    | Build progress bar with length, style, spinner, options  |
| `__getitem__` | Return frame at given percent index                      |
| `__str__`     | Render full progress bar string with spinner and percent |
| `__call__`    | Increment percent by 1                                   |
| `update`      | Set percent value and optionally advance spinner         |
| `render`      | Return renderable string with optional line deletion     |

---

### 🔹 Spinner

| Name    | Description                                  |
|---------|----------------------------------------------|
| `stick` | Rotating stick spinner (`-`, `\`, `\|`, `/`) |
| `plus`  | Alternating plus spinner (`-`, `\|`)         |
| `cross` | Alternating cross spinner (`/`, `\`)         |

---

### 🔹 Style

| Name       | Description                                                                               |
|------------|-------------------------------------------------------------------------------------------|
| `__init__` | Define `on`, `off`, `arrow_left`, `arrow_right`, `border_left`, `border_right` characters |
| `__str__`  | Return semicolon-separated key=value string                                               |
| `__repr__` | Return constructor-style representation                                                   |

---

### 🔹 BasePack (Animation)

Pre-built animation sequences updated via `BasePack.update(style)`:

| Name         | Description                              |
|--------------|------------------------------------------|
| `P_SLIDE_R`  | Single cell sliding right                |
| `P_SLIDE_L`  | Single cell sliding left                 |
| `P_SLIDER_R` | Multi-cell slider moving right           |
| `P_SLIDER_L` | Multi-cell slider moving left            |
| `P_FILL_R`   | Bar filling from left                    |
| `P_FILL_L`   | Bar filling from right                   |
| `P_EMPTY_R`  | Bar emptying toward right                |
| `P_EMPTY_L`  | Bar emptying toward left                 |
| `P_FULL`     | Static full bar                          |
| `P_EMPTY`    | Static empty bar                         |

---

### 🔹 BasePack (ANSI)

Pre-built color tuples updated via `BasePack.update()`:

| Name        | Description                              |
|-------------|------------------------------------------|
| `P_CRITIC`  | Critical severity color pair             |
| `P_ERROR`   | Error severity color pair                |
| `P_WARNING` | Warning severity color pair              |
| `P_VALID`   | Success/valid color pair                 |
| `P_DEBUG`   | Debug color pair                         |
| `P_INFO`    | Informational color pair                 |

---

## 🔹 Project Structure

```
jarbin_toolkit_console/
├── console.py
├── __init__.py
├── Animation/
│   ├── animation.py
│   ├── basepack.py
│   ├── progressbar.py
│   ├── spinner.py
│   ├── style.py
│   └── __init__.py
├── ANSI/
│   ├── ansi.py
│   ├── basepack.py
│   ├── color.py
│   ├── cursor.py
│   ├── line.py
│   └── __init__.py
├── Text/
│   ├── text.py
│   ├── format.py
│   └── __init__.py
└── System/
    ├── setting.py
    └── __init__.py
```

---

## 🔹 Usage

### 🔹 Basic Print

```python
from jarbin_toolkit_console import Console

Console.print("Hello, world!")
Console.print("Truncated output to terminal size", cut=True)
Console.print("Delayed continuity", sleep=1.5)
```

---

### 🔹 Formatted Text

```python
from jarbin_toolkit_console import Text, Console

msg = Text.Text("Build failed").bold().error()
Console.print(msg)
```

---

### 🔹 ANSI Color

```python
from jarbin_toolkit_console import ANSI, Console

red = ANSI.Color.rgb_fg(200, 50, 50)
reset = ANSI.Color(ANSI.Color.C_RESET)

Console.print(f"{red}Error{reset}: something went wrong")
```

---

### 🔹 Cursor Control

```python
from jarbin_toolkit_console import ANSI, Console

Console.print(ANSI.Cursor.hide(), end="")
Console.print(ANSI.Cursor.move(5, 10), end="")
Console.print("positioned text", end="")
Console.print(ANSI.Cursor.show(), end="")
```

---

### 🔹 Animation

```python
from jarbin_toolkit_console import Animation, Console

anim = Animation.Animation(["[   ]", "[-  ]", "[-- ]", "[---]"])

for _ in range(8):
    Console.print(anim.render(delete=True), sleep=0.2)
    anim.update()
```

---

### 🔹 Progress Bar

```python
from jarbin_toolkit_console import Animation, ANSI, Console

bar = Animation.ProgressBar(20, spinner=Animation.Spinner.stick())

for i in range(101):
    bar.update(i, update_spinner=not(i % 6))
    Console.print(bar.render(hide_spinner_at_end = True) + " " + ANSI.Cursor.previous(), sleep=0.02)

Console.print()
```

---

### 🔹 Alternate Screen

```python
from jarbin_toolkit_console import Console

with Console:
    Console.print("Running in alternate screen...", sleep=2)
```

---

### 🔹 Initialization

```python
import jarbin_toolkit_console as jtc

jtc.init(banner=True)
# ... use the library
jtc.quit()
```

---

## 🔹 Build / Installation

### Installation

```bash
pip install jarbin-toolkit-console
```

---

## 🔹 Execution Behavior

* All `Console` methods are **strictly static** — no instance required
* ANSI sequences are generated lazily at call time — no pre-computation
* `Animation` and `ProgressBar` rendering is **frame-driven and manual** — no background threads
* `get_key_press` and `get_cursor_position` require a live TTY — return safe defaults otherwise
* `Console.print` always returns the final rendered `Text` object
* `Setting.update()` is called at module import — all subsystems self-initialize

---

## 🔹 Memory Model

* `Console` holds no state — all operations are stateless static calls
* `Text`, `ANSI`, and `Animation` are **immutable by composition** — operators always return new objects
* `Animation` and `ProgressBar` maintain internal mutable step/percent state
* `Setting` maintains global configuration as class-level attributes — shared across all imports
* No heap allocation outside standard Python object creation

---

## 🔹 Design Philosophy

* static interface over instantiation for console operations
* composable object model for all output types
* explicit ANSI generation — no implicit terminal state assumption
* safe fallback behavior for non-TTY environments
* modular subsystems with no circular runtime dependencies
* deterministic rendering — output is a function of state only

---

## 🔹 Current State

⚠️ Core interface is stable and functional

Status:

* Console I/O fully implemented
* ANSI color, cursor, and line control fully implemented
* Text and Format system fully implemented
* Animation and ProgressBar system fully implemented
* Spinner factory implemented
* BasePack presets implemented for Animation and ANSI
* Setting and configuration system implemented

Limitations:

* `get_key_press` and `get_cursor_position` unavailable in non-TTY environments
* `cut` option in `Console.print` does not handle ANSI sequences correctly
* `cut` does not adapt dynamically on terminal resize
* No async rendering support
* No layout or grid system

---

## 🔹 Limitations

* TTY-dependent features fail silently in piped or headless environments
* `cut=True` in `Console.print` produces incorrect results with ANSI sequences
* `ProgressBar` and `Animation` rendering assumes single-line output
* No built-in thread safety for shared `Animation` or `ProgressBar` state
* `Setting` is global and shared — not suitable for isolated multi-context use

---

## 🔹 Extension / Contribution

Possible extensions:

* async-compatible animation renderer
* multi-line layout and grid rendering system
* TTY-safe ANSI stripping utility
* structured log output formatter built on `Format`
* theme system layered on `Color` and `BasePack`

---

## 🔹 Notes

This library is designed as a **structured terminal I/O and rendering toolkit**, not a full terminal UI framework.

It prioritizes:

* modularity between subsystems
* explicit and composable output construction
* deterministic rendering without hidden terminal state

---

## 🔹 Identity Summary

Jarbin-ToolKit Console is:

* a structured terminal I/O abstraction layer
* a composable ANSI sequence generation system
* a deterministic animation and progress rendering toolkit
* a modular, extensible terminal control library

---

## 🔹 Final Rule

> If output behavior is not explicitly constructed, it does not exist.

---
