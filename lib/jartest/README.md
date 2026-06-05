<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

---

# 📦 JarTest

> Lightweight Python testing framework inspired by **pytest**, designed for structured, deterministic, and composable test execution.

---

## 🔹 Short Description

**JarTest is a minimal Python testing framework designed to define, organize, and execute test functions in a structured and deterministic way.**

It provides a lightweight alternative to traditional testing tools, focusing on simplicity, explicit execution flow, and composability of test suites.

* Python functions and modules
* Libraries and APIs
* CLI programs (optional use case, not a core constraint)
* System behavior and integrations

---

## 🔹 Authors

* Nathan (Jarjarbin06)
* EPITECH Project

---

## 🔹 License

GPL v3

---

## 🔹 Target Audience

This framework is designed for:

* Python developers building test suites
* Students learning software testing principles
* Developers needing lightweight testing infrastructure
* Projects requiring explicit and controllable test execution
* CLI / library / system testing

---

## 🔹 Platform Support

* Python 3.11+
* Cross-platform (Linux, macOS, Windows)
* No external dependencies (standard library only)

---

## 🔹 Purpose

JarTest provides a structured way to:

* Define test functions using plain Python
* Register and collect tests automatically
* Execute grouped test suites deterministically
* Organize tests into modular components
* Provide a lightweight alternative to pytest-like workflows
* Support both unit testing and system/integration testing

---

## 🔹 Key Features

* Automatic test collection (`fetch_tests()` / `fetch()`)
* Test grouping via `JarTest` containers
* Simple Python function-based tests
* Deterministic execution order
* Modular test suite architecture
* Assertion utilities (`Assertion`)
* Output and error redirection (`stdout` & `stderr`)
* Optional system interaction support (CLI, subprocess, etc.)
* Lightweight design (no dependencies other than `Jarbin-ToolKit`)
* Multiple independent test suites support

---

## 🔹 Architecture Overview

```
            ┌────────────────────────┐
            │    Test Functions      │
            │   (JT_xxx methods)     │
            └──────────┬─────────────┘
                       │
                       ▼
            ┌────────────────────────┐
            │       JarTest()        │
            │   (Test Collector)     │
            └──────────┬─────────────┘
                       │
             fetch_tests() / fetch()
                       │
                       ▼
            ┌────────────────────────┐
            │  Registered Test List  │
            │    [callable tests]    │
            └──────────┬─────────────┘
                       │
                       ▼
            ┌────────────────────────┐
            │  Sequential Execution  │
            │   deterministic run    │
            └──────────┬─────────────┘
                       │
                       ▼
            ┌────────────────────────┐
            │  Assertion Validation  │
            │  pass / fail behavior  │
            └────────────────────────┘
```

---

## 🔹 Core Concept

### Test Definition Model

Each test is a **plain Python function**:

```python
def JT_example():
    Assertion.eq(1, 1)
```

No decorators required. No magic runtime injection.

---

### Test Collection Model

Tests are grouped using:

```python
JTT_example = JarTest()
JTT_example.fetch()
```

This automatically registers functions following naming rules (typically `JT_` prefix convention).

---

### Master Test Collection

JarTest can be grouped for single execution using:

```python
JTT_main = JarTest()
JTT_main.fetch_tests()
```

This automatically registers JarTest objects inside the file or imported from another.

---

### Execution Model

1. Define test functions
2. Register them via `JarTest`
3. Collect tests (`fetch()`)
4. Execute suite
5. Validate assertions

---

## 🔹 API Overview

### 🧪 JarTest

#### Constructor

```python
JarTest()
```

Creates a new independent test suite container.

---

#### Test Collection

```python
fetch()
```

* Scans and registers test functions
* Adds them to execution queue

```python
fetch_tests()
```

* Scans and registers test collections

---

#### Execution

```python
run() -> None | dict
```

* Executes all registered tests
* Runs sequentially
* Uses assertion system for validation

> [!NOTE]  
> While run don't have clear args, there are actually some taken in count (`*kwargs`)
> - `n`: int (default `1`) - How many times will each test run

---

## 🔹 Assertion System

### Assertion

```python
Assertion.eq(a, b)
Assertion.neq(a, b)
Assertion.contain(a, b)
Assertion.ncontain(a, b)
```

Provides simple deterministic validation helpers.

Designed for:

* readability
* minimal boilerplate
* explicit failure points
* assertions arguments and results registering

---

## 🔹 Usage

### Basic Example

```python
from jarbin_toolkit_jartest import JarTest, Assertion

def JT_add():
    Assertion.eq(2 + 2, 4)

def JT_sub():
    Assertion.eq(5 - 3, 2)

JTT_my_tests = JarTest()
JTT_my_tests.fetch()
JTT_my_tests.run()
```

---

### Example with external module testing

```python
from jarbin_toolkit_jartest import JarTest, Assertion
import my_module

def JT_function():
    result = my_module.compute(2, 3)
    Assertion.eq(result, 5)

JTT_my_tests = JarTest()
JTT_my_tests.fetch()
JTT_my_tests.run()
```

---

### Example (CLI usage is optional, not required)

```python
from jarbin_toolkit_jartest import JarTest, Assertion, Get
def JT_cli():
    out, err, code = Get.Redirect.cmd_all_std("my_program", "--help")

    Assertion.eq(code, 0)
    Assertion.contain("usage", out)

JTT_my_tests = JarTest()
JTT_my_tests.fetch()
JTT_my_tests.run()
```

---

## 🔹 Memory Model

* Tests are plain Python functions
* No hidden runtime state manipulation
* Assertions raise controlled failures
* Execution is sequential and deterministic

---

## 🔹 Installation

### From PyPI (if available)

```bash
pip install jarbin_toolkit_jartest
```

---

### From source

Clone the GitHub repository

```bash
make -C lib/jarbin_toolkit_jartest install
```

---

## 🔹 Build System

```bash
make install
make uninstall
make reinstall
```

---

## 🔹 Design Philosophy

* Minimal and explicit testing model
* No decorator-heavy syntax
* Deterministic execution order
* Easy debugging of test flows
* Lightweight alternative to pytest
* Flexible usage (unit, integration, system tests)

---

## 🔹 Current State

⚠️ The framework is **stable and functional but minimal**

Status:

* Test collection system implemented
* Assertion system implemented
* Multi-suite support possible
* Sequential execution model

Known limitations:

* No parallel execution
* No test discovery UI
* No built-in reporting dashboard
* No fixtures system (yet)
* No mocking framework included

---

## 🔹 File Structure

```
jarbin_toolkit_jartest/
├── jar_test.py
├── assertion.py
├── collector.py
└── __init__.py
```

---

## 🔹 Notes

* Inspired by pytest-style workflows
* Designed for clarity over complexity
* Works well for student and project-level testing systems
* Can scale into more advanced frameworks if extended

---
