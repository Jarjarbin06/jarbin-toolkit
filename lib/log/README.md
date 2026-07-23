<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# 📦 Jarbin-ToolKit:Log v0.2.3.2

> Deterministic file-based logging system with structured formatting, filtering, and dual output modes (jar-log / JSON)

---

## 🔹 Short Description

**Jarbin-ToolKit Log is a lightweight logging system that writes structured log entries to file-based outputs with support for formatted text logs and JSON logs, including filtering, cleaning, and terminal rendering.**

It provides:

* structured log file creation
* dual format support (`jar-log` / `json`)
* runtime log writing and reading
* filtering and formatting utilities
* log compression and cleaning tools
* terminal-rendered log visualization

It is **not a monitoring system**, but a **deterministic file-based logging abstraction layer**.

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

* Python developers needing structured logging systems
* projects requiring file-based audit trails
* CLI tools needing formatted terminal logs
* systems requiring lightweight observability layers
* developers building debugging or tracing utilities

---

## 🔹 Platform Support

* Python ≥ 3.10
* Standard library only
* Cross-platform (Linux / Windows / macOS)
* No external dependencies

---

## 🔹 Purpose

Jarbin-ToolKit Log aims to:

* provide deterministic log file creation
* support structured and human-readable logging formats
* enable filtering and post-processing of logs
* offer terminal-friendly log visualization
* support lightweight JSON logging pipelines

It is **not a distributed logging system**, but a **local deterministic logging abstraction layer over file I/O**.

---

## 🔹 Key Features

* Dual format logging (`jar-log`, `json`)
* Timestamped structured log entries
* Severity-based log levels (INFO, DEBUG, WARN, ERROR, CRIT, VALID)
* Terminal rendering with ANSI coloring
* Filtering system (keyword-based)
* Log compression and deduplication
* Comment insertion in logs
* File lifecycle management (create, read, close, delete)
* Log existence detection utility

---

## 🔹 Architecture Overview

```
User Code
   │
   ▼
Log(path, file_name, format)
   │
   ├───────────────┐
   ▼               ▼
jar-log        JSON mode
   │               │
   ▼               ▼
Formatted lines   Structured objects
   │               │
   └───────┬───────┘
           ▼
     File storage layer
           │
           ▼
   Read / Filter / Render
```

---

## 🔹 Core Concept

The system is based on a single entity:

### Log

A file-backed logging object responsible for writing, formatting, and managing log entries.

```python
Log(path, file_name=None, json=False)
```

#### Execution model:

* logs are appended immediately to file
* formatting depends on file type
* logs are immutable once written
* post-processing is read-based

---

## 🔹 API / Function Documentation

### 🔹 Log

| Name           | Description                             |
|----------------|-----------------------------------------|
| `__init__`     | Creates log file and initializes format |
| `log`          | Writes structured log entry             |
| `comment`      | Writes non-structured comment lines     |
| `save`         | Internal write operation                |
| `close`        | Finalizes and closes log file           |
| `delete`       | Removes log file                        |
| `read`         | Reads raw log content                   |
| `__str__`      | Returns formatted log view              |
| `str_filtered` | Returns filtered formatted logs         |
| `_jar_log_str` | Terminal rendering for jar-log          |
| `_json_str`    | Terminal rendering for JSON logs        |
| `clean`        | Compresses and simplifies logs          |
| `exist`        | Static file existence checker           |
| `__repr__`     | Debug representation                    |

---

## 🔹 Project Structure

```
jarbin_toolkit_log/
├── log.py
└── __init__.py
```

---

## 🔹 Usage Section

### 🔹 Basic Logging

```python
from jarbin_toolkit_log import Log

log = Log("./logs", "app")

log.log("INFO", "startup", "Application initialized")
log.log("ERROR", "db", "Connection failed")
log.close()
```

---

### 🔹 JSON Mode

```python
log = Log("./logs", "app", json=True)
log.log("INFO", "server", "Started successfully")
log.close()
```

---

### 🔹 Filtering Output

```python
print(log.str_filtered(["ERROR"]))
```

---

### 🔹 Terminal Rendering

```python
print(str(log))
```

---

### 🔹 Cleaning Logs

```python
cleaned = log.clean(compress_repeats=True)
print(cleaned)
```

---

## 🔹 Build / Installation

### Installation

```bash
pip install jarbin-toolkit-log
```

---

## 🔹 Execution Behavior

* log creation is immediate and file-backed
* logs are appended sequentially
* formatting depends on selected backend
* JSON mode produces structured arrays
* jar-log mode produces human-readable streams
* close() finalizes file integrity (especially JSON)

---

## 🔹 Memory Model

* `Log` stores:

  * file path
  * file name
  * format mode (jar-log / json)
  * closed state flag

No in-memory log buffering (writes are immediate).

---

## 🔹 Design Philosophy

* deterministic file output over runtime buffering
* explicit log lifecycle management
* dual-format compatibility
* post-processing over runtime transformation
* minimal dependency design

---

## 🔹 Current State

⚠️ Core logging engine is functional and stable

Status:

* jar-log format implemented
* JSON format implemented
* filtering system implemented
* terminal rendering implemented
* log cleaning and compression implemented

Limitations:

* JSON comment support incomplete
* no asynchronous logging
* no rotation system
* no concurrency protection
* no streaming/log tailing support

---

## 🔹 Limitations

* no multi-process safety
* no automatic log rotation
* JSON format sensitive to manual corruption
* performance not optimized for high-frequency logging
* filtering is post-read only (not indexed)

---

## 🔹 Extension / Contribution

Possible extensions:

* log rotation system
* async logging backend
* multi-thread safe writes
* structured query system
* real-time log streaming
* indexing for faster filtering

---

## 🔹 Notes

This system is designed as a **lightweight deterministic logging abstraction**, not a production-grade distributed observability stack.

It prioritizes:

* simplicity
* transparency
* structured output
* predictable file behavior

---

## 🔹 Identity Summary

Jarbin-ToolKit Log is:

* a structured file logging system
* a deterministic logging abstraction layer
* a dual-format log writer (text + JSON)
* a lightweight debugging and tracing utility

---

## 🔹 Final Rule

> If a log entry is not explicitly written, it does not exist.

---
