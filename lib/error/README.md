<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# 📦 Jarbin-ToolKit:Error v0.1.3

> Structured exception hierarchy system providing deterministic error modeling, contextual linking, and extensible error classification.

---

## 🔹 Short Description

**Jarbin-ToolKit Error is a structured exception framework that extends Python’s base exception system with contextual linking, categorized error types, and standardized formatting for deterministic error reporting.**

It provides:

* structured exception hierarchy
* contextual file/line linking system
* specialized error subclasses
* standardized string formatting for logs and CLI output

It is **not a logging system**, but a **structured error abstraction layer over Python exceptions**.

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

* Python developers building structured frameworks
* systems requiring standardized error reporting
* CLI tools needing formatted exception output
* modular applications with layered exception handling

---

## 🔹 Platform Support

* Python ≥ 3.10
* Standard library only (no external dependencies required)
* Cross-platform (Linux / Windows / macOS)

---

## 🔹 Purpose

Jarbin-ToolKit Error aims to:

* provide structured and extensible exception types
* standardize error representation across systems
* attach contextual metadata (file / line references)
* improve debugging clarity through formatted output

It is **not a logging framework**, but a **deterministic exception modeling system built on Python exceptions**.

---

## 🔹 Key Features

* Base `Error` exception class
* Structured error subclasses (Type, Value, Import, Config, etc.)
* Contextual linking via file and line metadata
* ANSI-formatted terminal output
* Standardized string and debug representations
* Optional logging integration hook (disabled by default)

---

## 🔹 Architecture Overview

```
Application Layer
        │
        ▼
   Error(Exception)
        │
   ┌────┴────────────────────────────┐
   ▼                                 ▼
ErrorType                      ErrorValue
ErrorImport                   ErrorConfig
ErrorLog                     ErrorSetting
ErrorAttribute              ErrorLaunch
        │
        ▼
Context System (link_data)
        │
        ▼
Formatted Output (ANSI CLI / logs)
```

---

## 🔹 Core Concept

The system is built around a **single base exception class** extended by specialized error types.

### Error

Base exception class:

```python
Error(message, error, link)
```

Supports:

* custom error message
* error category label
* optional file/line linkage
* formatted terminal output

---

### Error Subclasses

Each subclass represents a semantic category:

```python
ErrorType
ErrorValue
ErrorImport
ErrorConfig
ErrorLog
ErrorSetting
ErrorAttribute
ErrorLaunch
```

All inherit from `Error` and append a deterministic identifier.

---

### Link System

Optional contextual metadata:

```python
("file.py", 42)
```

Converted into:

* `File "file.py"`
* or `File "file.py", line 42`

Used to improve debugging traceability.

---

## 🔹 API / Function Documentation

### 🔹 Error

| Name          | Description                                       |
|---------------|---------------------------------------------------|
| `__init__`    | Initializes error with message, type, and link    |
| `log`         | Optional logging hook (disabled in current state) |
| `create_link` | Builds human-readable file/line reference         |
| `__str__`     | ANSI-formatted runtime error output               |
| `__repr__`    | Debug representation                              |

---

### 🔹 Error Subclasses

| Class            | Description                  |
|------------------|------------------------------|
| `ErrorType`      | Type-related errors          |
| `ErrorValue`     | Value-related errors         |
| `ErrorImport`    | Import failures              |
| `ErrorConfig`    | Configuration-related errors |
| `ErrorLog`       | Logging system errors        |
| `ErrorSetting`   | Runtime setting errors       |
| `ErrorAttribute` | Attribute access errors      |
| `ErrorLaunch`    | Initialization/boot errors   |

---

## 🔹 Project Structure

```
jarbin_toolkit_error/
├── error.py
└── __init__.py
```

---

## 🔹 Usage Section

### 🔹 Basic Error Raising

```python
from jarbin_toolkit_error import Error

raise Error("Something went wrong", error="RuntimeError")
```

---

### 🔹 Structured Error Types

```python
from jarbin_toolkit_error import ErrorValue

raise ErrorValue("Invalid input provided")
```

---

### 🔹 Contextual Linking

```python
raise ErrorType(
    "Type mismatch detected",
    link=("main.py", 42)
)
```

---

### 🔹 Exception Display Output

Errors are formatted with:

* ANSI color coding
* structured message blocks
* optional file/line context

---

## 🔹 Build / Installation

### Installation

```bash
pip install jarbin-toolkit-error
```

---

## 🔹 Execution Behavior

* Errors are **synchronous exceptions**
* No automatic capture system
* Logging is disabled by default (`log()` is a stub)
* Context generation is optional and explicit

---

## 🔹 Memory Model

* Each `Error` stores:

  * message (str)
  * error type label (str)
  * link metadata (tuple or None)
  * formatted link string

No external state is required.

---

## 🔹 Design Philosophy

* explicit error classification over generic exceptions
* structured debugging context over raw messages
* deterministic formatting for CLI consistency
* extensible error taxonomy

---

## 🔹 Current State

⚠️ Core error hierarchy is stable and functional

Status:

* base exception system implemented
* structured subclasses implemented
* link system implemented
* formatted output implemented

Limitations:

* logging integration incomplete
* no stack trace enhancement layer
* ANSI formatting not configurable
* no serialization support

---

## 🔹 Limitations

* no integrated logging backend
* no JSON export of errors
* limited runtime introspection
* ANSI formatting may not be portable in all environments
* logging hooks currently disabled

---

## 🔹 Extension / Contribution

Possible extensions:

* structured logging integration
* JSON / YAML error serialization
* stack trace enrichment system
* centralized error registry
* log file integration layer

---

## 🔹 Notes

This module is designed as a **deterministic error abstraction layer**, not a full logging or monitoring system.

It prioritizes:

* clarity
* structured classification
* debugging precision

---

## 🔹 Identity Summary

Jarbin-ToolKit Error is:

* a structured exception hierarchy
* a deterministic error modeling system
* a contextual debugging abstraction layer
* a CLI-friendly formatted error framework

---

## 🔹 Final Rule

> If an error is not classified or contextualized, it is not structured.

---
