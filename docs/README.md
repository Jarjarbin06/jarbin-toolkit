<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# Jarbin-ToolKit

**Jarbin-ToolKit** is a lightweight Python utility library providing a modular set of tools for building robust CLI applications, managing configuration, logging, timed execution, console manipulation, and structured actions. Inspired by `epitech_console`, it emphasizes readability, flexibility, and cross-platform compatibility.

---

---

## Pages

1. [API REFERENCE](API_REFERENCE.md)

---

---

## Table of Contents

1. [Library Overview](#library-overview)
2. [Main Features](#main-features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Library Components](#library-components)
    - [Action](#action-stable)
    - [Config](#config-stable)
    - [Error](#error-stable)
    - [Log](#log-stable)
    - [Time](#time-stable)
    - [Console](#console-stable)
6. [Release Notes](#release-notes)
7. [Useful Links](#useful-links)

---

---

## Library Overview

Jarbin-ToolKit provides modular tools to improve the development of CLI utilities:

- **Console rendering**: animations, progress bars, spinners, ANSI manipulation
- **Configuration management**: easy-to-use INI files with typed getters/setters
- **Action orchestration**: group and execute actions flexibly
- **Logging**: formatted logs with `.jar-log` or `JSON` support
- **Timing utilities**: precise stopwatch and delay tools
- **Error handling**: structured errors with optional file/line links and terminal formatting

---

---

## Main Features

- **Cross-platform support**: Linux & Windows
- **Typed config management**: `.ini` style files with `get_int`, `get_float`, `get_bool`
- **Structured logging**: JSON and custom `.jar-log` with formatted output
- **Advanced console control**: cursor manipulation, ANSI styles, line clearing, progress bars
- **Animation support**: spinners, sliders, and filling animations
- **Precision timing**: `StopWatch` and `Time.wait` / `Time.pause`
- **Extensible Action system**: group and execute multiple callable tasks

---

---

## Tech Stack

- **Python**: 3.11+
- **Standard Library Dependencies**: `time`, `os`, `platform`, `configparser`, `datetime`, `sys`, `typing`
- **External Dependencies**:
  - `jarbin-toolkit-action`,
  - `jarbin-toolkit-config`,
  - `jarbin-toolkit-error`,
  - `jarbin-toolkit-log`,
  - `jarbin-toolkit-time`,
  - `jarbin-toolkit-console`

---

---

## Installation

```bash
pip install jarbin-toolkit
```

Or to force reinstall the latest version:

```bash
pip install --upgrade --force-reinstall jarbin-toolkit
```

---

---

## Library Components

### Action (Stable)

Provides tools for **deferring execution** and **grouping callable actions**.

#### Classes

- **`Action`** — Represents a single callable action

```python
from jarbin_toolkit_action import Action

def greet():
    print("Hello World!")

a = Action("do greeting", greet)
a()    # Executes the function
```

- **`Actions`** — Represents a collection of `Action` objects

```python
from jarbin_toolkit_action import Actions, Action

actions = Actions()
actions += Action("act1", lambda: print("Action 1"))
actions += Action("act2", lambda: print("Action 2"))

actions()    # Executes all actions
print(len(actions))    # Number of actions
```

---

### Config (Stable)

Manages INI-style configuration files with typed getters and cross-platform support.

```python
from jarbin_toolkit_config import Config

cfg = Config(path="./", data={"Section": {"key": "null"}})
cfg.set("Section", "key2", 42)    # Set "key2" in "Section" to 42
val = cfg.get_int("Section", "key2")    # Get value of "key2" in "Section"
print(val) 
cfg.delete()    # Delete the config file
```

---

### Error (Stable)

Structured error system with terminal formatting and optional file/line linking.

```python
from jarbin_toolkit_error import ErrorConfig

try:
    raise ErrorConfig("Invalid configuration detected", link=("config.ini", 10))
except ErrorConfig as e:
    print(e)    # Print the Error
```

---

### Log (Stable)

Manages formatted logs in `.jar-log` or JSON format.

```python
from jarbin_toolkit_log import Log

log = Log(path="./", file_name="mylog")
log.log("INFO", "Init", "Log started")    # Add a log
log.comment("This is a comment")    # Add a comment
log.close()    # End the formating
print(log.str_filtered("INFO"))    # Print the log file formated and filtered
log.delete()
```

---

### Time (Stable)

Precision timing utilities.

```python
from jarbin_toolkit_time import StopWatch, Time

watch = StopWatch(True)
Time.wait(1.5)
print(watch.elapsed())    # Print elapsed time after 1.5 seconds waiting

Time.pause('Press enter to continue...')    # Pause program until user press 'enter'
```

---

### Console (Stable)

Provides **advanced terminal rendering** inspired by `epitech_console`.

```python
from jarbin_toolkit_console import Console, Animation, ANSI

pb = Animation.ProgressBar(20)
for i in range(21):
    pb.update(i*5)
    Console.print(pb.render() + ANSI.Cursor.previous(), sleep=0.05)
Console.print()
```

---

---

## Release Notes

### v1.1 - /
- Doc Update (modules usage)
- New Log release
> ⚠️ In Development

### v1.0 - 2026-02-05
- All modules updated and released  
> First official release

### v0.2 - 2026-02-05
- New Log release
- Fixed all modules
- JSON format support for logs  
> Working library

### v0.1 - 2026-01-22
- Initial release
- Stable modules: Action, Config, Error, Log, Time
- Evolving module: Console
- Added StopWatch, Time, structured error handling, logging, and Action orchestration  
> ⚠️ Library not functional yet

---

---

## Useful Links

- [GitHub Repository](https://github.com/Jarjarbin06/jarbin-toolkit)  
- [Issue Tracker](https://github.com/Jarjarbin06/jarbin-toolkit/issues)  
- [ANSI Escape Codes Reference](https://en.wikipedia.org/wiki/ANSI_escape_code)

---

> Jarbin-ToolKit [*GNU GPL*](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/LICENSE) 2026 [**JARJARBIN's STUDIO**](https://github.com/Jarjarbin06)

---

<small>
Last update:
**README** — *2026/02/12**
</small>
