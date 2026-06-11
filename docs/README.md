<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# 📦 Jarbin-ToolKit v1.1

> Modular deterministic Python toolkit aggregating structured utilities for execution, testing, timing, console rendering, and system interaction

---

## 🔹 Short Description

**Jarbin-ToolKit is a modular Python toolkit that aggregates multiple deterministic utility libraries into a unified structured environment, providing execution systems, testing frameworks, timing tools, console rendering, and system interaction modules.**

It provides:

* execution abstraction (`Action`)
* structured testing (`JarTest`)
* time measurement (`Time`)
* console rendering utilities (`Console`)
* error handling systems (`Error`)
* system interaction tools (`Log`, `Config`)

It is **not a monolithic framework**, but a **modular aggregation of independent deterministic libraries**.

---

## 🔹 Authors

* Nathan (Jarjarbin06)
* Jarbin Studio

---

## 🔹 License

GPL v3

---

## 🔹 Target Audience

This toolkit is intended for:

* Python developers building modular systems
* developers designing deterministic execution pipelines
* engineers creating internal tooling frameworks
* projects requiring structured testing and benchmarking
* developers needing unified low-level utilities

---

## 🔹 Platform Support

* Python ≥ 3.10
* Standard library (core modules)
* Internal modules:

  * `jarbin_toolkit_action`
  * `jarbin_toolkit_config`
  * `jarbin_toolkit_console`
  * `jarbin_toolkit_error`
  * `jarbin_toolkit_jartest`
  * `jarbin_toolkit_log`
  * `jarbin_toolkit_time`

* Linux / Windows / macOS compatible

---

## 🔹 Purpose

Jarbin-ToolKit aims to:

* unify multiple independent utility libraries
* provide a consistent deterministic API across modules
* enable structured execution, testing, and debugging workflows
* reduce boilerplate in tool-oriented Python projects

It is **not a framework enforcing architecture**, but a **modular toolbox of composable systems**.

---

## 🔹 Key Features

* Modular architecture (independent sub-libraries)
* Deterministic execution systems
* Integrated testing and benchmarking framework
* High-resolution timing utilities
* Console rendering and formatting system
* Structured error handling
* Output and subprocess capture utilities
* Zero hidden state between modules

---

## 🔹 Architecture Overview

```
                 Jarbin-ToolKit
                        │
    ┌───────────────────┼───────────────────┐
    ▼                   ▼                   ▼
Action              Config              Console
(execution)         (config manager)    (render/output control)

    │                   │                   │
    ▼                   ▼                   ▼
Error               JarTest             Log
(error)             (testing system)    (log manager)

    │
    ▼
Time
(time util)
```

---

## 🔹 Core Concept

Jarbin-ToolKit is based on **modular independence + deterministic composition**.

Each module:

* is **self-contained**
* exposes a **clear API**
* has **no hidden coupling**
* can be used independently or combined

---

## 🔹 Project Structure

```
jarbin_toolkit/
└── __init__.py
```

---

## 🔹 Usage Section

### 🔹 Combined Example

```python
from jarbin_toolkit import JarTest

def JT_add():
    result = 2 + 2
    JarTest.Assertion.eq(result, 4)

JTT_example = JarTest.JarTest()
JTT_example()
```

---

### 🔹 Execution + Timing

```python
from jarbin_toolkit import Action
from jarbin_toolkit import Time

def compute():
    return sum(range(100000))

a = Action.Action("compute", compute)

sw = Time.StopWatch(True)
result = a()
print(sw.elapsed())
```

---

### 🔹 Output Capture

```python
from jarbin_toolkit import JarTest

def hello():
    print("Hello")

out, ret = JarTest.Get.Redirect.stdout(hello)
print(out)
```

---

## 🔹 Build / Installation

### Installation

```bash
pip install jarbin-toolkit
```

---

## 🔹 Execution Behavior

* All modules operate **independently**

* No global orchestration layer

* Execution is always:

  * explicit
  * deterministic
  * user-controlled

* No automatic background processes

---

## 🔹 Memory Model

* Each module manages its own state:

  * `Action` → callable + args
  * `JarTest` → dictionary of benchmarks
  * ...

* No shared mutable global state between modules

---

## 🔹 Design Philosophy

* deterministic behavior over implicit logic
* modular architecture over monolithic design
* explicit execution over automation
* composability over coupling
* minimal abstraction overhead

---

## 🔹 Current State

⚠️ Core modules are functional and integrated

Status:

* execution system implemented
* testing framework implemented
* timing utilities implemented
* console system integrated
* IO utilities implemented

Limitations:

* no unified high-level orchestration API
* no plugin system
* no dependency injection system

---

## 🔹 Limitations

* modules are loosely coupled (no enforced integration)
* no async ecosystem support
* no configuration system
* no global lifecycle manager
* some modules depend on others implicitly (e.g. `JarTest` → `Time`)

---

## 🔹 Extension / Contribution

Possible extensions:

* unified module registry
* plugin architecture
* async-compatible modules
* dependency graph execution system
* configuration layer

---

## 🔹 Notes

Jarbin-ToolKit is designed as a **foundation toolkit**, not an end-user framework.

It is intended to:

* accelerate development of internal tools
* provide reusable deterministic components
* standardize utility patterns across projects

Each module can evolve independently while maintaining a consistent philosophy.

---

## 🔹 Identity Summary

Jarbin-ToolKit is:

* a modular Python utility ecosystem
* a deterministic execution and testing toolkit
* a structured collection of independent systems
* a foundation layer for advanced tooling

---

## 🔹 Final Rule

> If a module interaction is not explicitly defined, it does not exist.

---
