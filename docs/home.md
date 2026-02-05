<small>last update : 
**PACKAGE** = *2026/02/05* ; 
**README** = *2026/02/05*</small>\
\
<img src="NONE" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="NONE" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# Jarbin-ToolKit

**Jarbin-ToolKit** is a lightweight Python utility library providing a set of modular tools for building robust CLI applications, managing configuration, logging, timed execution, console manipulation, and structured actions. Inspired by `epitech_console`, this library emphasizes readability, flexibility, and cross-platform compatibility.

---

## Table of Contents

1. [Library Overview](#library-overview)
2. [Main Features](#main-features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Library Components](#library-components)
    - [Action (Stable)](#action)
    - [Config (Stable)](#config)
    - [Error (Stable)](#error)
    - [Log (Stable)](#log)
    - [Time (Stable)](#time)
    - [Console (Evolving)](#console)
6. [Release Notes](#release-notes)
7. [Useful Links](#useful-links)

---

## Library Overview

Jarbin-ToolKit provides a modular set of tools to improve the development of CLI utilities:

- **Console rendering**: animations, progress bars, spinners, and ANSI manipulation.
- **Configuration management**: easy-to-use INI files with typed getters and setters.
- **Action orchestration**: group actions and execute them in flexible ways.
- **Logging**: formatted log files with `.jar-log` or `JSON`.
- **Timing utilities**: precise stopwatch and delay tools.
- **Error handling**: structured errors with optional file/line links and terminal formatting.

---

## Main Features

- **Cross-platform support**: Linux & Windows compatibility.
- **Typed config management**: `.ini` style files with `get_int`, `get_float`, `get_bool`.
- **Structured logging**: JSON and custom `.jar-log` with formatted output.
- **Advanced console control**: cursor manipulation, ANSI styles, line clearing, and progress bars.
- **Animation support**: pre-built spinners, sliders, and filling animations.
- **Precision timing**: `StopWatch` and `Time.wait` / `Time.pause`.
- **Extensible Action system**: group and execute multiple callable tasks easily.

---

## Tech Stack

- Python 3.11+
- Standard Library dependencies only:
  - `time`, `os`, `platform`, `configparser`, `datetime`, `sys`, `typing`
- No external dependencies required

---

## Installation

```
pip install jarbin-toolkit
```

Or, to force reinstall the latest version:

```
pip install --upgrade --force-reinstall jarbin-toolkit
```

---

## Library Components

### Action

Provides tools for **deferring execution** and **grouping callable actions**.

#### Classes

- **`Action`**  
  Represents a single callable action.

  **Usage:**
  ```
  from jarbin_toolkit.action import Action

  def greet():
      print("Hello World!")

  a = Action(greet)
  a()  # Executes the function
  ```

- **`Actions`**  
  Represents a collection of `Action` objects. Supports:
  - Adding actions: `+`
  - Access by index
  - Execution of all actions
  - Checking length

  **Usage:**
  ```
  from jarbin_toolkit.action import Actions, Action

  actions = Actions()
  actions + Action(lambda: print("Action 1"))
  actions + Action(lambda: print("Action 2"))

  actions()  # Executes all actions
  print(len(actions))  # Number of actions
  ```

---

### Config

**`Config`** manages INI-style configuration files with cross-platform support.

**Features:**
- Create or read configuration files
- Typed getters: `get_int`, `get_float`, `get_bool`
- Cross-platform path normalization (Windows / Linux)
- Delete config or keep it cached

**Usage:**
```
from jarbin_toolkit.config import Config

cfg = Config(path="./", data={"Section": {"key": "value"}})
cfg.set("Section", "key2", 42)
val = cfg.get_int("Section", "key2")
cfg.delete()
```

---

### Error

Structured error system with formatted output and optional file/line linking.

**Classes:**
- `Error` (base)
- `ErrorLaunch`
- `ErrorImport`
- `ErrorLog`
- `ErrorConfig`
- `ErrorSetting`
- `ErrorType`
- `ErrorValue`

**Features:**
- Terminal colored messages
- Optional file and line number linking
- Logging hooks (some intentionally no-op)

**Usage:**
```
from jarbin_toolkit.error import ErrorConfig

try:
    raise ErrorConfig("Invalid configuration detected", link=("config.ini", 10))
except ErrorConfig as e:
    print(e)
```

---

### Log

**`Log`** manages formatted logs in `.jar-log` or `JSON` files.

**Features:**
- File creation and lifecycle management
- Log and comment writing
- Terminal-aware rendering with color
- Filtered reading of log types
- Delete and close management

**Usage:**
```
from jarbin_toolkit.log import Log

log = Log(path="./", file_name="mylog")
log.log("INFO", "Initialization", "Log started")
log.comment("This is a comment")
print(log.str_filtered(["INFO"]))
log.close(delete=True)
```

---

### Time

Precision timing utilities.

**StopWatch Class:**
- Start, stop, reset
- Elapsed time measurement
- Comparison operators (`==`, `<`, `>`, `<=`, `>=`)

**Time Utilities:**
- `Time.wait(sleep: float)`: waits for exact time, returns elapsed
- `Time.pause(msg: str)`: pauses execution, returns elapsed

**Usage:**
```
from jarbin_toolkit.time import StopWatch, Time

watch = StopWatch(True)
Time.wait(1.5)
print(watch.elapsed())

Time.pause("Press enter to continue...")
```

---

### Console

Inspired by `epitech_console`, provides **advanced terminal rendering**:

**Submodules:**
- **Animation**: Progress bars, spinners, custom animations
- **ANSI**: ANSI escape sequences, colors, styling
- **Cursor**: Move, hide, show cursor
- **Line**: Clear lines, screen, previous lines
- **Text**: Apply formatting to strings
- **Setting**: Module settings and environment management

**Usage:**
```
from jarbin_toolkit.console import Console, Animation, ProgressBar

pb = ProgressBar(10)
for i in range(11):
    pb.update(i*10)
    Console.print(pb.render(), end="")
```

---

## Release Notes

## v0.1 - 2026-02-05
- Initial release of Jarbin-ToolKit
- ALPHA modules: Action, Config, Error, Log, Time
- BETA modules: Console
- Added StopWatch and Time utilities
- Added structured error handling
- Added formatted logging system
- Added Action orchestration system

---

## Useful Links

- [GitHub Repository](https://github.com/Jarjarbin06/jarbin-toolkit)
- [Issue Tracker](https://github.com/Jarjarbin06/jarbin-toolkit/issues)
- [ANSI Escape Codes Reference](https://en.wikipedia.org/wiki/ANSI_escape_code)

---

> Jarbin-ToolKit *GNU GPL* 2026 **JARJARBIN's STUDIO**
