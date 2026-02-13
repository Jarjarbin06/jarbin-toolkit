<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="Jarbin-ToolKit Logo" width="100%">

# Jarbin-ToolKit — Full API Reference

This document provides a complete technical reference for all public modules, classes, and methods available in **Jarbin-ToolKit** and its sub-modules.

---

---

## Table of Contents
1. [Jarbin-ToolKit](#jarbin-toolkit)
2. [Sub-Modules](#sub-modules)
   1. [Action Module](#action-module)
   2. [Config Module](#config-module)
   3. [Error Module](#error-module)
   4. [Log Module](#log-module)
   5. [Time Module](#time-module)
   6. [Console Module](#console-module)
3. [Version Compatibility](#version-compatibility)
4. [LICENSE](#license)

---

---

# Jarbin-ToolKit
### None

---

---

# Sub-Modules

## Action Module

`jarbin_toolkit.Action`

Provides structured execution wrappers for callable objects.

---

### Class: `Action`

Wraps a callable function and allows deferred execution.

#### Constructor

```text
Action(callable_obj: Callable, *args, **kwargs)
```

#### Parameters

- `callable_obj` — Function or callable to execute
- `*args` — Positional arguments passed to callable
- `**kwargs` — Keyword arguments passed to callable

#### Methods

##### `__call__()`

Executes the wrapped callable.

```python
from jarbin_toolkit import Action

action = Action.Action("show hello", print, "Hello")
action()
```

##### `__repr__()`

Returns a debug representation of the action.

---

### Class: `Actions`

Container for multiple `Action` objects.

#### Constructor

```text
Actions()
```

#### Operators

##### `+` (Add Action)

Adds an `Action` to the collection.

```python
from jarbin_toolkit import Action
actions = Action.Actions()
actions += Action.Action("show A", print, "A")

actions()
```

##### `__call__()`

Executes all stored actions sequentially.

##### `__len__()`

Returns number of stored actions.

##### `__getitem__(index)`

Returns action at given index.

---

## Config Module

`jarbin_toolkit.Config`

INI configuration management with typed accessors.

---

### Class: `Config`

#### Constructor

```text
Config(path: str, data: dict | None = None, file_name: str = "config.ini")
```

#### Parameters

- `path` — Directory path
- `data` — Optional initial configuration dictionary
- `file_name` — Configuration filename

---

#### Core Methods

##### `get(section: str, key: str) -> str`

Returns raw string value.

##### `get_int(section: str, key: str) -> int`

Returns value as integer.

##### `get_float(section: str, key: str) -> float`

Returns value as float.

##### `get_bool(section: str, key: str) -> bool`

Returns value as boolean.

##### `set(section: str, key: str, value: Any)`

Sets configuration value.

##### `delete()`

Deletes configuration file from disk.

---

#### Example

```python
from jarbin_toolkit import Config

cfg = Config("./", data={"App" : {"debug" : False}})
cfg.set("App", "debug", True)
debug = cfg.get_bool("App", "debug")
print(debug, type(debug))
```

---

## Error Module

`jarbin_toolkit.Error`

Structured error system with optional file/line linking.

---

### Base Class: `Error`

#### Constructor

```text
Error(message: str, link: tuple[str, int] | None = None)
```

#### Parameters

- `message` — Error message
- `link` — Optional `(file, line)` tuple

---

### Derived Errors

- `ErrorLaunch`
- `ErrorImport`
- `ErrorLog`
- `ErrorConfig`
- `ErrorSetting`
- `ErrorType`
- `ErrorValue`

All inherit from `Error`.

---

#### Example

```python
from jarbin_toolkit import Error

raise Error.ErrorConfig("Invalid section", link=("config.ini", 42))
```

---

## Log Module

`jarbin_toolkit.Log`

Structured logging system supporting `.jar-log` and JSON formats.

---

### Class: `Log`

#### Constructor

```text
Log(path: str, file_name: str = "log", format: str = "jar-log")
```

#### Parameters

- `path` — Directory path
- `file_name` — Log filename (without extension)
- `format` — `"jar-log"` or `"json"`

---

#### Methods

##### `log(level: str, title: str, message: str)`

Writes structured log entry.

##### `comment(message: str)`

Writes comment line.

##### `str_filtered(levels: list[str]) -> str`

Returns filtered log entries.

##### `close(delete: bool = False)`

Closes file. Deletes if `delete=True`.

---

#### Example

```python
from jarbin_toolkit import Log

log = Log("./", "app")
log.log("INFO", "Start", "Application started")
log.close()
print(log)
```

---

## Time Module

`jarbin_toolkit.Time`

Precise timing utilities.

---

### Class: `StopWatch`

#### Constructor

```text
StopWatch(auto_start: bool = False)
```

#### Methods

##### `start()`

Starts timer.

##### `stop()`

Stops timer.

##### `reset()`

Resets timer.

##### `elapsed() -> float`

Returns elapsed seconds.

---

#### Comparison Operators

- `==`
- `<`
- `>`
- `<=`
- `>=`

---

### Class: `Time`

Static time utilities.

#### Methods

##### `wait(seconds: float) -> float`

Waits exact duration and returns elapsed time.

##### `pause(message: str) -> float`

Pauses execution until input.

---

#### Example

```python
from jarbin_toolkit import Time

watch = Time.StopWatch(True)
Time.Time.wait(2)
print(watch.elapsed())
```

---

## Console Module

`jarbin_toolkit.Console`

Advanced terminal rendering system.

---

### Submodules Overview

- `Animation`
- `ANSI`
- `Cursor`
- `Line`
- `Text`
- `Setting`

---

### Console Class

#### `Console.print(*args, **kwargs)`

Enhanced print with terminal control.

---

### Animation Module

Provides spinners and progress bars.

#### Class: `ProgressBar`

```text
ProgressBar(total: int)
```

##### `update(value: int)`

Updates progress.

##### `render() -> str`

Returns formatted progress string.

---

### ANSI Module

ANSI escape sequence utilities.

Common features:

- Colors
- Bold / Underline
- Reset formatting

---

### Cursor Module

Cursor manipulation utilities:

- Move up/down
- Move to position
- Hide / Show cursor

---

### Line Module

Line management:

- Clear current line
- Clear screen
- Clear previous lines

---

### Text Module

Text formatting utilities.

Example:

```python
from jarbin_toolkit import Console

Text = Console.Text.Text
print(Text.bold("Hello"))
my_text = Text("World")
print(my_text.underline())
```

---

### Setting Module

Console environment configuration and internal settings management.

---

---

# Version Compatibility

| Module  | Status   | Stability |
|---------|----------|-----------|
| Action  | Released | Stable    |
| Config  | Released | Stable    |
| Error   | Released | Stable    |
| Log     | Released | Stable    |
| Time    | Released | Stable    |
| Console | Released | Stable    |

---

---

# License

Jarbin-ToolKit is licensed under **GNU GPL (2026)**.

---

<small>
Last update :
**API Reference** — 2026/02/12
</small>
