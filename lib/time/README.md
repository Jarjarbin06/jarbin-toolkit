<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# **Jarbin-ToolKit:Time** v0.1.2.0
<details>
<summary>Latest versions</summary>
🟠 UNDER DEVELOPMENT 🟠 None 🟠

🟢 RELEASED 🟢 v0.1.2.0 🟢
</details>

[![CodeQL Advanced](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/codeql.yml/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/codeql.yml)
[![Python package tester](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/test-package.yml/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/test-package.yml)
[![pages-build-deployment](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/pages/pages-build-deployment)

---

---

## Description

`jarbin-toolkit:time` is a Python library designed to help you create enhanced terminal interfaces. It's improving the appearance and readability of your command-line interface with lightweight animations, colorful text, and neat formatting. If you want to make your terminal programs more readable and visually structured, this library is for you!

---

---

## Table of Contents

1.  [Description](#Description)
2.  [Features](#Features)
3.  [Tech Stack](#Tech-Stack)
4.  [Installation](#Installation)
5.  [Usage](#Usage)
6.  [Project Structure](#Project-Structure)
7.  [API Reference](#API-Reference)
8.  [Release Notes](#Release-Notes)
9.  [License](#License)
10. [Important Links](#Important-Links)
11. [Footer](#Footer)

## Features

*   **Timers**: Use the built-in stopwatch to measure how long parts of your code take to run.

---

---

## Tech-Stack

*   **Language**: Python - Chosen for its readability and versatility.
*   **Frameworks**: Python -  Entirely implemented in Python.

---

---

## Installation

To begin , install `jarbin-toolkit:time`:

#### **Prerequisites**:

Make sure you have Python `3.11` or newer installed on your computer.
You can check your Python version by opening a terminal and typing `python --version`.

---

#### **Install from PyPI** (*recommended*):
	
Open your terminal and run this command:
```bash
pip install jarbin_toolkit_time
```
   This will automatically download and install the library from PyPI.

---

#### **Install from GitHub**:

If you want the latest version directly from the source, you can install it using `git`:
```bash
git clone -b latest NONE
make -C lib/jarbin_toolkit_time install
```
This downloads the code, then the `install` script handles the installation.
These commands install the `jarbin-toolkit:time` package and its dependencies (datetime).

---

---

## Usage

Here are some examples demonstrating how to use `jarbin-toolkit:time`:

### Basic Error

```python
from jarbin_toolkit_time import Time, StopWatch
```

---

---

## API-Reference

*   **Time**: Static time utility helpers (waiting, pausing, precise elapsed measurement).
    *   `wait(sleep: int | float) -> float` (staticmethod)
        Wait for a given number of seconds.
        - `sleep`: duration in seconds
        - Uses internal `StopWatch`
        - Returns the exact measured elapsed time
    *   `pause(msg: str = "Press enter to continue...") -> float` (staticmethod)
        Pause program execution until user presses Enter.
        - `msg`: message displayed to the user
        - Returns the exact elapsed pause time


*   **StopWatch**: Lightweight elapsed time tracker.
    *   `StopWatch(start: bool = False)`
        Create a stopwatch.
        - `start`: if `True`, automatically start at initialization
    *   `start() -> None`
        Reset and start the stopwatch.
    *   `stop() -> None`
        Stop the stopwatch (freezes elapsed value).
    *   `update() -> None`
        Update internal elapsed time (if running).
    *   `elapsed(auto_update: bool = True) -> float`
        Return elapsed time in seconds.
        - `auto_update`: automatically refresh before returning value
    *   `reset() -> None`
        Reset elapsed time and stop the stopwatch.
    *   `__str__() -> str`
        Return string representation of elapsed time.
    *   `__repr__() -> str`
        Return constructor-style representation of the StopWatch object.
    *   `__eq__(other: float) -> bool`
        Compare elapsed time with float (`==`).
    *   `__gt__(other: float) -> bool`
        Compare elapsed time with float (`>`).
    *   `__ge__(other: float) -> bool`
        Compare elapsed time with float (`>=`).
    *   `__lt__(other: float) -> bool`
        Compare elapsed time with float (`<`).
    *   `__le__(other: float) -> bool`
        Compare elapsed time with float (`<=`).

---

---

## Release-Notes
* #### v0.1.1:
    *   **[/]** 1rst real release
* #### v0.1.0:
    *   **[UPDATE]** `jarbin_toolkit_time` update (removed unlinked sub-modules)
    *   **[INIT]** add `epitech_console` to jarbin-toolkit (renamed `jarbin_toolkit_time`)

---

---

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/time/LICENSE) file for details.

---

---

## Important-Links

#### Files
*   **Repository**: [https://github.com/Jarjarbin06/jarbin-toolkit](https://github.com/Jarjarbin06/jarbin-toolkit)
*   **PyPI**: [https://pypi.org/project/jarbin-toolkit-time/](https://pypi.org/project/jarbin-toolkit-time/)

#### Wiki
*   **Wiki** (*take a look*): [https://github.com/Jarjarbin06/jarbin-toolkit/wiki](https://github.com/Jarjarbin06/jarbin-toolkit/wiki)
*   **README** (*updated*):  [https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/time/README.md](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/time/README.md)
*   **GitHub**: [https://jarjarbin06.github.io/jarbin-toolkit/](https://jarjarbin06.github.io/jarbin-toolkit/)

---

---

## Footer

*   Repository: [https://github.com/Jarjarbin06/jarbin-toolkit](https://github.com/Jarjarbin06/jarbin-toolkit)
*   Author: Nathan Jarjarbin
*   Contact: nathan.amaraggi@epitech.eu

---

⭐️ Like the project? Give it a star!
🐛 Found a bug? Report it in the issues!

---

<small>
last update : 
**PACKAGE** — *2026/01/21* ;
**README** — *2026/02/12*
</small>
