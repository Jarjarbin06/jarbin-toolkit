<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# 📦 Jarbin-ToolKit:Config v0.1.2.2

> Deterministic configuration management system based on structured INI file abstraction over Python ConfigParser

---

## 🔹 Short Description

**Jarbin-ToolKit Config is a lightweight configuration management layer that provides deterministic read/write access to INI-based configuration files through a structured object-oriented interface.**

It enables:

* structured configuration creation and persistence
* typed retrieval of configuration values
* safe modification of configuration entries
* filesystem-backed deterministic state management

It is **not a database system**, but a **lightweight deterministic file-based configuration abstraction layer**.

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

* Python developers requiring persistent configuration systems
* system-level tool developers
* CLI application designers
* automation and workflow engineers
* projects requiring deterministic file-based state storage

---

## 🔹 Platform Support

* Python ≥ 3.10
* Standard library only (`configparser`, `os`, `platform`)
* Cross-platform support:

  * Linux
  * Windows
  * macOS

---

## 🔹 Purpose

Jarbin-ToolKit Config aims to:

* provide structured access to INI configuration files
* abstract Python’s `ConfigParser` into a deterministic interface
* ensure persistent and reproducible configuration state
* unify read/write/config lifecycle handling

It is **not a database abstraction layer**, but a **file-based deterministic configuration system**.

---

## 🔹 Key Features

* INI-based configuration management
* automatic file creation and initialization
* typed getters (`str`, `int`, `float`, `bool`)
* persistent write-through updates
* static existence validation
* platform-aware path normalization

---

## 🔹 Architecture Overview

```
User Code
   │
   ▼
Config(path, file_name, data)
   │
   ▼
ConfigParser Layer
   │
   ├───────────────┐
   ▼               ▼
Read Mode      Write Mode
   │               │
   ▼               ▼
Memory State   File System (.ini)
   │
   ▼
Typed Access API (get / set)
```

---

## 🔹 Core Concept

The system is based on a **dual-state model**:

### 1. In-Memory Configuration

Stored using Python `ConfigParser`:

```python
self.config
```

### 2. Persistent File State

Stored as an `.ini` file:

```python
path/file_name
```

---

## 🔹 Configuration Lifecycle

### Creation

If file does not exist:

* file is created
* empty or provided structure is written

### Loading

If file exists:

* content is read into `ConfigParser`
* memory state is synchronized

### Persistence

Every modification is immediately written to disk.

---

## 🔹 API / Function Documentation

### 🔹 Config

| Name        | Description                                                          |
|-------------|----------------------------------------------------------------------|
| `__init__`  | Initializes configuration file and loads or creates persistent state |
| `set`       | Updates a configuration value and persists it                        |
| `get`       | Retrieves a value with optional type casting                         |
| `get_bool`  | Retrieves a boolean value                                            |
| `get_int`   | Retrieves an integer value                                           |
| `get_float` | Retrieves a float value                                              |
| `delete`    | Removes configuration file from filesystem                           |
| `exist`     | Static check for configuration file existence and validity           |
| `__repr__`  | Debug representation of configuration object                         |

---

## 🔹 Project Structure

```
jarbin_toolkit_config/
├── config.py
└── __init__.py
```

---

## 🔹 Usage Section

### 🔹 Create Configuration

```python
from jarbin_toolkit_config import Config

cfg = Config(
    path="./config",
    data={
        "database": {
            "host": "localhost",
            "port": "5432"
        }
    },
    file_name="app.ini"
)
```

---

### 🔹 Set Value

```python
cfg.set("database", "user", "admin")
```

---

### 🔹 Get Value

```python
host = cfg.get("database", "host")
port = cfg.get_int("database", "port")
```

---

### 🔹 Boolean / Float Access

```python
enabled = cfg.get_bool("feature", "enabled")
ratio = cfg.get_float("config", "ratio")
```

---

### 🔹 Delete Configuration

```python
cfg.delete()
```

---

## 🔹 Build / Installation

### Installation

```bash
pip install jarbin-toolkit-config
```

---

## 🔹 Execution Behavior

* Configuration is loaded at initialization
* Any `set()` operation triggers immediate file write
* File system is the source of truth after initialization
* No background synchronization exists

---

## 🔹 Memory Model

* `ConfigParser` is the in-memory state container
* file system is persistent storage layer
* no caching layer beyond runtime object
* optional in-memory retention after deletion (`cached=True`)

---

## 🔹 Design Philosophy

* deterministic file-state synchronization
* explicit read/write separation
* minimal abstraction over standard library
* cross-platform compatibility by design
* immediate persistence over lazy writes

---

## 🔹 Current State

⚠️ Core configuration system is functional but requires robustness improvements

Status:

* INI file creation implemented
* typed getters implemented
* write-through persistence implemented
* file existence validation implemented

Limitations:

* no schema validation
* no encryption support
* no concurrent access protection
* no transaction system
* limited error handling robustness

---

## 🔹 Limitations

* no atomic write mechanism
* no multi-process locking
* no configuration schema enforcement
* no rollback system
* platform path handling partially inconsistent in edge cases

---

## 🔹 Extension / Contribution

Possible extensions:

* schema-based configuration validation
* transaction-based config updates
* file locking system for concurrency safety
* encrypted configuration storage layer
* JSON/YAML backend support

---

## 🔹 Notes

This system is designed as a **minimal deterministic abstraction over INI configuration files**, not a full configuration framework.

It prioritizes:

* simplicity
* explicit behavior
* direct filesystem mapping

---

## 🔹 Identity Summary

Jarbin-ToolKit Config is:

* a deterministic INI configuration manager
* a structured persistence abstraction layer
* a lightweight system-level configuration tool
* a minimal interface over Python ConfigParser

---

## 🔹 Final Rule

> If configuration state is not explicitly written, it does not exist.

---
