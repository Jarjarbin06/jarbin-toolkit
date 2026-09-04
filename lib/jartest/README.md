<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# 📦 Jarbin-ToolKit:JarTest v0.1.5.4

> Deterministic test execution framework based on structured assertions, benchmarking, and controlled test discovery

---

## 🔹 Short Description

**Jarbin-ToolKit JarTest is a lightweight testing and benchmarking framework that executes Python test functions through structured `Benchmark` containers, records assertions, measures execution time, and aggregates results in a deterministic reporting system.**

It provides:

* automatic test discovery based on naming conventions
* structured assertion tracking with contextual recording
* execution benchmarking with precise timing
* stdout/stderr capture utilities
* hierarchical test execution and reporting

It is **not a unit testing clone of pytest**, but a **deterministic execution and benchmarking harness with integrated assertion tracking**.

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

* Python developers building custom test frameworks
* developers requiring deterministic benchmarking pipelines
* engineers designing structured validation systems
* projects needing lightweight alternatives to full testing ecosystems

---

## 🔹 Platform Support

* Python ≥ 3.10
* Standard library only (except internal Jarbin-ToolKit dependencies)
* Linux / Windows / macOS compatible

---

## 🔹 Purpose

Jarbin-ToolKit JarTest aims to:

* execute test functions in isolated benchmarking environments
* capture execution time with high-resolution measurement
* collect structured assertion results during execution
* aggregate errors, exceptions, and outputs in a unified model
* provide deterministic reporting across multiple test runs

It is **not a general-purpose testing framework**, but a **structured benchmarking and assertion orchestration layer over Python callables**.

---

## 🔹 Key Features

* automatic test discovery via `JT_` prefix
* benchmark execution wrapper (`Benchmark`)
* assertion system with contextual collection
* execution timing with adaptive formatting (ns → s → min)
* stdout/stderr capture via `Get.Redirect`
* CLI-style test runner with formatted terminal output
* recursive test collection across modules

---

## 🔹 Architecture Overview

```
User Test Module
      │
      ▼
JarTest.fetch()
      │
      ▼
Benchmark(test_function)
      │
      ├───────────────┐
      ▼               ▼
StopWatch        AssertionContext
      │               │
      ▼               ▼
Execution        AssertionResult list
      │
      ▼
Result Aggregation
      │
      ▼
JarTest.run()
      │
      ▼
Console Reporting Layer
```

---

## 🔹 Core Concept

The system is based on four core entities:

---

### Benchmark

Encapsulates a test execution unit:

```python
Benchmark(test_function)
```

Responsible for:

* executing test functions
* measuring execution time
* capturing exceptions and assertion failures
* storing returned values

---

### Assertion System

Assertions are recorded during execution using a context variable:

```python
Assertion.eq(a, b)
Assertion.neq(a, b)
Assertion.contain(a, b)
Assertion.ncontain(a, b)
```

Each assertion produces an `AssertionResult`:

| Field    | Description              |
|----------|--------------------------|
| name     | assertion type           |
| passed   | boolean result           |
| values   | input tuple              |
| expected | expected value           |
| actual   | observed value           |
| meta     | operator + type metadata |

Assertions are automatically collected via `AssertionContext`.

---

### JarTest

Main orchestrator:

```python
JarTest.fetch()
JarTest.run()
```

Responsible for:

* discovering test functions
* wrapping them into benchmarks
* executing batches of tests
* generating structured CLI reports

---

### Get Utility

Provides execution introspection:

* stdout/stderr capture
* subprocess execution wrapper
* controlled output redirection

---

## 🔹 API / Function Documentation

---

### 🔹 Assertion

| Method     | Description                            |
|------------|----------------------------------------|
| `eq`       | equality check with type enforcement   |
| `neq`      | inequality check with type enforcement |
| `contain`  | membership check                       |
| `ncontain` | non-membership check                   |

---

### 🔹 Benchmark

| Method          | Description              |
|-----------------|--------------------------|
| `__call__(n)`   | executes test n times    |
| `benchmark()`   | static execution wrapper |
| `time_to_str()` | formats execution time   |

---

### 🔹 JarTest

| Method          | Description                            |
|-----------------|----------------------------------------|
| `fetch()`       | discovers test functions in module     |
| `fetch_tests()` | recursive module test collection       |
| `run()`         | executes all benchmarks with reporting |
| `__call__()`    | fetch + run shortcut                   |

---

### 🔹 Get

#### Redirect: 

| Method          | Description                                |
|-----------------|--------------------------------------------|
| `stdout()`      | capture stdout + return from function      |
| `stderr()`      | capture stderr + return from function      |
| `all_std()`     | capture stdout + stderr + return           |
| `cmd_stdout()`  | run shell command (stdout + exit)          |
| `cmd_stderr()`  | run shell command (stderr + exit)          |
| `cmd_all_std()` | run shell command (stdout + stderr + exit) |

---

## 🔹 Project Structure

```
jarbin_toolkit_jartest/
├── assertion.py
├── benchmark.py
├── get.py
├── jartest.py
└── __init__.py
```

---

## 🔹 Usage Section

---

### 🔹 Defining a Test

```python
from jarbin_toolkit_jartest import Assertion

def JT_example():
    Assertion.eq(2 + 2, 4)
    Assertion.contain("a", "abc")
```

---

### 🔹 Running Tests

> Auto test fetch & run

```python
from jarbin_toolkit_jartest import JarTest

JTT_example = JarTest()
JTT_example()
```

---

### 🔹 Capturing Output

```python
from jarbin_toolkit_jartest import Get, Assertion

def foo():
    print("bar")

def JT_example():
    out, ret = Get.Redirect.stdout(foo)
    Assertion.contain("bar", out, '"bar" not printed')
```

### 🔹 Full test

> Manual test fetch & run

```python
from jarbin_toolkit_jartest import JarTest, Get, Assertion

def foo(message: str):
    print("msg = " + message)

def JT_failing():
    out, ret = Get.Redirect.stdout(foo)
    Assertion.contain("...", out, 'missing argument')

def JT_valid():
    out, ret = Get.Redirect.stdout(foo, "hello world")
    Assertion.contain("hello world", out)

JTT_example = JarTest()
JTT_example.fetch()
JTT_example.run()
```

---

## 🔹 Execution Behavior

* Each test runs inside a `Benchmark` wrapper
* Assertions are collected via `contextvars`
* Execution timing is measured using `StopWatch`
* Exceptions are captured but do not stop reporting unless fatal
* Multiple test runs accumulate results

---

## 🔹 Memory Model

* `AssertionResult` objects are stored per test execution
* `Benchmark` maintains:

  * time history
  * error history
  * assertion history
  * traceback history
* `JarTest` maintains a registry of benchmarks indexed by name

No implicit global state outside controlled context variables.

---

## 🔹 Design Philosophy

* deterministic execution over dynamic behavior
* structured assertion tracking instead of boolean-only tests
* explicit benchmarking integration
* modular separation of execution, assertion, and reporting
* reproducible test runs

---

## 🔹 Current State

⚠️ Core test execution and benchmarking system is functional

Status:

* assertion system implemented
* benchmark engine implemented
* test discovery implemented
* CLI reporting implemented
* stdout/stderr capture implemented

Limitations:

* no parallel test execution
* no test isolation sandboxing
* limited assertion set
* no fixtures system
* no mocking framework

---

## 🔹 Limitations

* synchronous execution only
* no dependency injection system
* no advanced test lifecycle hooks
* no distributed execution
* console output tightly coupled to terminal UI system

---

## 🔹 Extension / Contribution

Possible extensions:

* fixture system for reusable test contexts
* parallel benchmark execution
* richer assertion library
* mocking utilities
* JUnit/XML export support
* test filtering and tagging system

---

## 🔹 Notes

JarTest is designed as a **deterministic hybrid between testing and benchmarking**, not a strict replacement for pytest.

It prioritizes:

* execution traceability
* performance measurement
* structured assertion metadata

---

## 🔹 Identity Summary

Jarbin-ToolKit JarTest is:

* a deterministic test execution engine
* a structured assertion tracking system
* a benchmarking-oriented testing framework
* a lightweight test orchestration layer

---

## 🔹 Final Rule

> If a test behavior is not executed inside Benchmark, it is not part of the system.

---
