<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# 📦 Jarbin-ToolKit:Time v0.1.2.2

> Deterministic time abstraction layer providing precise timing utilities, monotonic timestamps, and structured stopwatch-based measurement tools

---

## 🔹 Short Description

**Jarbin-ToolKit Time is a lightweight timing utility library that provides deterministic time measurement primitives such as monotonic timestamps, stopwatches, and blocking timing utilities using a structured and predictable interface.**

It provides:

* monotonic timestamp retrieval
* high-resolution stopwatch measurement
* blocking wait utility based on active polling
* pause utility for controlled execution flow

It is **not a scheduling system**, but a **deterministic time measurement and control abstraction layer**.

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

* Python developers requiring precise timing measurements
* developers building simulation or game-loop systems
* engineers designing deterministic execution flows
* systems requiring controlled blocking or pause behavior

---

## 🔹 Platform Support

* Python ≥ 3.10
* Standard library only (`time`, `typing`)
* Cross-platform (Linux / Windows / macOS)

---

## 🔹 Purpose

Jarbin-ToolKit Time aims to:

* provide monotonic and reliable timestamp access
* offer a lightweight stopwatch abstraction
* enable deterministic blocking delays
* support controlled execution pausing

It is **not a scheduling framework**, but a **low-level deterministic timing abstraction layer over Python time primitives**.

---

## 🔹 Key Features

* monotonic timestamp retrieval via `get_timestamp()`
* high-precision stopwatch (`StopWatch`)
* manual and automatic elapsed time tracking
* blocking wait based on active polling
* controlled pause with optional input blocking
* comparison operators on elapsed time

---

## 🔹 Architecture Overview

```
System Time (time.monotonic / time.time)
            │
            ▼
   get_timestamp()
            │
            ▼
   Time Utilities Layer
            │
   ┌────────┴────────┐
   ▼                 ▼
StopWatch        Time class
   │                 │
   ▼                 ▼
Elapsed tracking   wait / pause
   │
   ▼
Deterministic timing control
```

---

## 🔹 Core Concept

The system is based on three core primitives:

---

### get_timestamp

Returns a monotonic timestamp:

```python
get_timestamp() -> float
```

Uses:

* `time.monotonic()` for stability
* avoids system clock drift issues

---

### StopWatch

A stateful timing object used for measuring elapsed time.

Creation:

```python
StopWatch(start: bool = False)
```

Key behavior:

* starts optionally at initialization
* tracks elapsed time manually or automatically
* uses `time.time()` for measurement

Core methods:

| Method      | Description                      |
|-------------|----------------------------------|
| `start()`   | Starts stopwatch                 |
| `stop()`    | Stops and finalizes elapsed time |
| `update()`  | Updates elapsed time             |
| `reset()`   | Resets stopwatch state           |
| `elapsed()` | Returns current elapsed time     |

Comparison operators:

* `==`, `!=`
* `>`, `<`
* `>=`, `<=`

allow direct comparison with floats.

---

### Time

Static utility class providing blocking primitives:

#### wait

```python
Time.wait(sleep: int | float) -> float
```

Performs active waiting using a `StopWatch` until target duration is reached.

#### pause

```python
Time.pause(msg: str = "...", force_enter: bool = True) -> float
```

Blocks execution until user input is received, optionally enforcing enter confirmation loop.

---

## 🔹 API / Function Documentation

### 🔹 get_timestamp

| Name            | Description                       |
|-----------------|-----------------------------------|
| `get_timestamp` | Returns monotonic timestamp float |

---

### 🔹 StopWatch

| Name       | Description                             |
|------------|-----------------------------------------|
| `__init__` | Initializes stopwatch                   |
| `start`    | Starts timing                           |
| `stop`     | Stops timing                            |
| `update`   | Updates elapsed value                   |
| `elapsed`  | Returns elapsed time                    |
| `reset`    | Resets internal state                   |
| `__str__`  | Returns elapsed time as string          |
| `__repr__` | Debug representation                    |
| comparison | Compares elapsed time with float values |

---

### 🔹 Time

| Name    | Description                          |
|---------|--------------------------------------|
| `wait`  | Blocking active wait using stopwatch |
| `pause` | Blocking user-controlled pause       |

---

## 🔹 Project Structure

```
jarbin_toolkit_time/
├── time.py
├── stopwatch.py
└── __init__.py
```

---

## 🔹 Usage Section

### 🔹 Get Timestamp

```python
from jarbin_toolkit_time import get_timestamp

print(get_timestamp())
```

---

### 🔹 Stopwatch Usage

```python
from jarbin_toolkit_time import StopWatch

sw = StopWatch(start=True)

# ... some processing
print(sw.elapsed())
```

---

### 🔹 Comparison Usage

```python
sw = StopWatch(start=True)

# wait some time

if sw > 1.0:
    print("More than 1 second elapsed")
```

---

### 🔹 Blocking Wait

```python
from jarbin_toolkit_time import Time

elapsed = Time.wait(2.0)
print(elapsed)
```

---

### 🔹 Pause Execution

```python
from jarbin_toolkit_time import Time

Time.pause("Press Enter to continue...")
```

---

## 🔹 Build / Installation

### Installation

```bash
pip install jarbin-toolkit-time
```

---

## 🔹 Execution Behavior

* Stopwatch uses active polling for elapsed updates
* `Time.wait()` is a busy-wait loop based on `StopWatch.update()`
* No threading or async mechanisms are used
* Execution is deterministic but CPU-active during waits

---

## 🔹 Memory Model

* `StopWatch` stores:

  * `_start` timestamp (float)
  * `_elapsed` accumulated time (float)

* `Time` is stateless utility class

* `get_timestamp` is a pure function wrapper over monotonic clock

No external state or hidden caching mechanisms are used.

---

## 🔹 Design Philosophy

* deterministic timing over system-dependent variability
* explicit time control instead of implicit scheduling
* minimal abstraction over Python time primitives
* lightweight and dependency-free design
* predictable blocking behavior

---

## 🔹 Current State

⚠️ Core timing utilities are stable and functional

Status:

* StopWatch implemented
* monotonic timestamp function implemented
* blocking wait implemented
* pause utility implemented

Limitations:

* no async timing support
* no event scheduling system
* wait uses busy-loop (CPU active)
* no high-resolution sleep abstraction layer
* no drift correction for long waits

---

## 🔹 Limitations

* active polling in `Time.wait` consumes CPU
* no integration with asyncio or threading timers
* `pause` is blocking and interactive only
* no precision guarantees beyond system clock resolution
* no timer cancellation mechanism

---

## 🔹 Extension / Contribution

Possible extensions:

* async-aware StopWatch
* sleep-based wait instead of busy loop
* event scheduler built on StopWatch
* timer callbacks system
* CPU-efficient timing backend

---

## 🔹 Notes

This module prioritizes **deterministic control flow over performance optimization**.

It is designed for:

* simulations
* controlled execution flows
* debugging environments
* deterministic timing measurements

---

## 🔹 Identity Summary

Jarbin-ToolKit Time is:

* a deterministic timing abstraction layer
* a stopwatch-based measurement system
* a lightweight blocking time utility toolkit
* a low-level wrapper over Python time primitives

---

## 🔹 Final Rule

> If time behavior is not explicitly controlled, it is not part of the system.

---
