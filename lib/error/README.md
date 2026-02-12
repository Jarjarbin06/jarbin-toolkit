<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# **Jarbin-ToolKit:Error** v0.1.2.0
<details>
<summary>Latest development version</summary>
🟠 UNDER DEVELOPMENT 🟠 None 🟠
</details>
<details>
<summary>Latest release</summary>
🟢 RELEASED 🟢 v0.1.2.0 🟢
</details>

[![CodeQL Advanced](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/codeql.yml/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/codeql.yml)
[![Python package tester](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/test-package.yml/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/test-package.yml)
[![pages-build-deployment](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/pages/pages-build-deployment)

---

---

## Description

`jarbin-toolkit:error` is a Python library designed to help you create enhanced terminal interfaces. It's improving the appearance and readability of your command-line interface with lightweight animations, colorful text, and neat formatting. If you want to make your terminal programs more readable and visually structured, this library is for you!

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

---

---

## Features

*   **Error Handling**:  Provides structured and readable error messages.

---

---

## Tech-Stack

*   **Language**: Python - Chosen for its readability and versatility.
*   **Frameworks**: Python -  Entirely implemented in Python.

---

---

## Installation

To begin , install `jarbin-toolkit:error`:

#### **Prerequisites**:

Make sure you have Python `3.11` or newer installed on your computer.
You can check your Python version by opening a terminal and typing `python --version`.

---

#### **Install from PyPI** (*recommended*):
	
Open your terminal and run this command:
```bash
pip install jarbin_toolkit_error
```
   This will automatically download and install the library from PyPI.

---

#### **Install from GitHub**:

If you want the latest version directly from the source, you can install it using `git`:
```bash
git clone -b latest NONE
make -C lib/jarbin_toolkit_error install
```
This downloads the code, then the `install` script handles the installation.
These commands install the `jarbin-toolkit:error` package and its dependencies (datetime).

---

---

## Usage

Here are some examples demonstrating how to use `jarbin-toolkit:error`:

---

---

### Basic Error

```python
from jarbin_toolkit_error import Error
```

---

---

## API-Reference

*   **Error**: Base exception class with formatted terminal output and optional file/line linking.
    *   `Error(message: str = "an error occurred", *, error: str = "Error", link: tuple[str, int | None] | None = None)`
        Create a custom error.
        - `message`: detailed error message
        - `error`: error type/title
        - `link`: optional `(file, line)` reference to indicate origin

        Automatically:
        - Builds a formatted error link (if provided)
        - Calls internal logging system (if enabled)
    *   `create_link() -> None`
        Build human-readable file/line reference string.
    *   `log() -> None`
        Log the error (implementation depends on global settings).
    *   `lauch_error() -> str` (staticmethod)
        Return formatted launch failure message (used when toolkit fails to initialize).
    *   `__str__() -> str`
        Return ANSI-formatted multi-line error message ready for terminal display.
    *   `__repr__() -> str`
        Return constructor-style representation of the Error object.

---

### Specialized Error Types
All subclasses inherit from `Error` and predefine their `error` type.
*   **ErrorLaunch**
    *   `ErrorLaunch(message: str = "an error occurred during the launch", *, link: tuple[str, int | None] | None = None)`
        Raised when a launch/initialization error occurs.
*   **ErrorImport**
    *   `ErrorImport(message: str = "an error occurred during an import", *, link: tuple[str, int | None] | None = None)`
        Raised when an import-related error occurs.
*   **ErrorLog**
    *   `ErrorLog(message: str = "an error occurred on/in a log file", *, link: tuple[str, int | None] | None = None)`
        Raised for logging system failures.
        Overrides `log()` to prevent recursive logging.
*   **ErrorConfig**
    *   `ErrorConfig(message: str = "an error occurred on/in a config file", *, link: tuple[str, int | None] | None = None)`
        Raised for configuration file errors.
*   **ErrorSetting**
    *   `ErrorSetting(message: str = "an error occurred during setting's update", *, link: tuple[str, int | None] | None = None)`
        Raised when settings update fails.
*   **ErrorType**
    *   `ErrorType(message: str = "an error occurred on a type", *, link: tuple[str, int | None] | None = None)`
        Raised for type-related errors.
*   **ErrorValue**
    *   `ErrorValue(message: str = "an error occurred on a value", *, link: tuple[str, int | None] | None = None)`
        Raised for invalid value errors.

---

---

## Release-Notes
* #### v0.1.1:
    *   **[/]** 1rst real release
* #### v0.1.0:
    *   **[UPDATE]** `jarbin_toolkit_error` update (removed unlinked sub-modules)
    *   **[INIT]** add `epitech_console` to jarbin-toolkit (renamed `jarbin_toolkit_error`)

---

---

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/error/LICENSE) file for details.

---

---

## Important-Links

#### Files
*   **Repository**: [https://github.com/Jarjarbin06/jarbin-toolkit](https://github.com/Jarjarbin06/jarbin-toolkit)
*   **PyPI**: [https://pypi.org/project/jarbin-toolkit-error/](https://pypi.org/project/jarbin-toolkit-error/)

---

#### Wiki
*   **Wiki** (*take a look*): [https://github.com/Jarjarbin06/jarbin-toolkit/wiki](https://github.com/Jarjarbin06/jarbin-toolkit/wiki)
*   **README** (*updated*):  [https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/error/README.md](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/error/README.md)
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
Last update : 
**PACKAGE** — *2026/02/12* ; 
**README** — *2026/02/12*
</small>
