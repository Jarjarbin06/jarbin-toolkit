<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# 📦 Jarbin-ToolKit:Action v0.1.2.3

> Deterministic function execution system based on deferred callable actions and structured action composition

---

## 🔹 Short Description

**Jarbin-ToolKit Action is a lightweight execution framework that encapsulates Python callables into structured Action objects, enabling deferred execution, composition, and batch processing through a deterministic interface.**

It provides:

* function encapsulation into executable objects
* delayed execution model
* composable action pipelines
* structured batch execution system

It is **not a task scheduler**, but a **deterministic function execution abstraction layer**.

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

* Python developers building execution pipelines
* developers designing modular automation systems
* projects requiring deferred execution models
* engineers building structured workflow abstractions

---

## 🔹 Platform Support

* Python ≥ 3.10
* Standard library only (no external dependencies required)
* Linux / Windows / macOS compatible

---

## 🔹 Purpose

Jarbin-ToolKit Action aims to:

* encapsulate functions into executable objects
* enable deferred execution of logic
* allow composition of multiple execution units
* provide structured batch execution through `Actions`

It is **not a concurrency framework**, but a **deterministic execution abstraction layer over Python callables**.

---

## 🔹 Key Features

* Callable encapsulation via `Action`
* Deferred execution using `__call__`
* Batch execution with `Actions`
* Action composition via operator overloading (`+`)
* Ordered execution pipeline
* Structured return aggregation

---

## 🔹 Architecture Overview

```
User Code
   │
   ▼
Action(name, function, args, kwargs)
   │
   ▼
Deferred Execution Model
   │
   ├───────────────┐
   ▼               ▼
__call__       Actions(list)
   │               │
   ▼               ▼
Function exec   Batch execution
   │               │
   └───────┬───────┘
           ▼
   Structured return dict
```

---

## 🔹 Core Concept

The system is based on two core entities:

### Action

Encapsulates a callable:

```python
Action(name, function, *args, **kwargs)
```

Execution is delayed until explicitly called:

```python
action()
```

---

### Actions

Container of multiple `Action` objects:

```python
Actions([action1, action2])
```

Supports:

* sequential execution
* aggregation of results
* indexing access
* composition via `+`

---

## 🔹 API / Function Documentation

### 🔹 Action

| Name       | Description                               |
|------------|-------------------------------------------|
| `__init__` | Stores callable and arguments             |
| `__call__` | Executes stored function                  |
| `__add__`  | Combines with another Action into Actions |
| `__repr__` | Debug representation                      |
| `__str__`  | Human-readable representation             |

---

### 🔹 Actions

| Name          | Description                           |
|---------------|---------------------------------------|
| `__init__`    | Initializes action list               |
| `__call__`    | Executes all actions and returns dict |
| `__add__`     | Combines Actions or Action            |
| `__getitem__` | Access action by index                |
| `__len__`     | Returns number of actions             |
| `__repr__`    | Debug representation                  |
| `__str__`     | Structured print output               |

---

## 🔹 Project Structure

```
jarbin_toolkit_action/
├── action.py
└── __init__.py
```

---

## 🔹 Usage Section

### 🔹 Single Action Execution

```python
from jarbin_toolkit_action import Action

def hello(name):
    return f"Hello {name}"

a = Action("greet", hello, "Nathan")
print(a())  # Hello Nathan
```

---

### 🔹 Batch Execution

```python
from jarbin_toolkit_action import Action, Actions

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

a1 = Action("add", add, 2, 3)
a2 = Action("mul", mul, 2, 3)

batch = Actions([a1, a2])
print(batch())
```

Output:

```python
{
    "add": 5,
    "mul": 6
}
```

---

### 🔹 Composition

```python
combined = a1 + a2
print(combined())
```

---

## 🔹 Build / Installation

### Installation

```bash
pip install jarbin-toolkit-action
```

---

## 🔹 Execution Behavior

* Execution is strictly **manual and explicit**
* No automatic scheduling
* Functions are executed only via:

  * `Action()`
  * `Actions()`
* Batch execution preserves insertion order

---

## 🔹 Memory Model

* `Action` stores:

  * function reference
  * positional arguments (list)
  * keyword arguments (dict)

* `Actions` stores:

  * ordered list of `Action`

No hidden state or dynamic mutation outside explicit operations.

---

## 🔹 Design Philosophy

* deterministic execution over implicit behavior
* explicit function encapsulation
* modular execution units
* composition over duplication
* predictable batch processing

---

## 🔹 Current State

⚠️ Core execution model is stable and functional

Status:

* Action encapsulation implemented
* Batch execution implemented
* Composition operator implemented

Limitations:

* No async support
* No cancellation mechanism
* No dependency graph execution
* No parallel execution engine

---

## 🔹 Limitations

* synchronous execution only
* no concurrency model
* no runtime scheduling system
* no error isolation between batch actions
* minimal validation on inputs

---

## 🔹 Extension / Contribution

Possible extensions:

* async Action support
* execution pipelines with dependencies
* retry mechanisms
* parallel execution backend
* failure isolation per Action

---

## 🔹 Notes

This system is designed as a **minimal deterministic execution abstraction layer**, not a full workflow engine.

It prioritizes:

* clarity
* predictability
* structural simplicity

---

## 🔹 Identity Summary

Jarbin-ToolKit Action is:

* a structured function encapsulation system
* a deterministic execution model
* a lightweight batch execution framework
* a composable action abstraction layer

---

## 🔹 Final Rule

> If execution behavior is not explicitly defined, it does not exist.

---
