<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# **Jarbin-ToolKit:Action** v0.1.2.0
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

## Description

`jarbin-toolkit:action` is a Python library designed to help you create enhanced terminal interfaces. It's improving the appearance and readability of your command-line interface with lightweight animations, colorful text, and neat formatting. If you want to make your terminal programs more readable and visually structured, this library is for you!

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

## Tech-Stack

*   **Language**: Python - Chosen for its readability and versatility.
*   **Frameworks**: Python -  Entirely implemented in Python.

## Installation

To begin , install `jarbin-toolkit:action`:

#### **Prerequisites**:

Make sure you have Python `3.11` or newer installed on your computer.
You can check your Python version by opening a terminal and typing `python --version`.

#### **Install from PyPI** (*recommended*):
	
Open your terminal and run this command:
```bash
pip install jarbin_toolkit_action
```
   This will automatically download and install the library from PyPI.

#### **Install from GitHub**:

If you want the latest version directly from the source, you can install it using `git`:
```bash
git clone -b latest NONE
make -C lib/jarbin_toolkit_action install
```
This downloads the code, then the `install` script handles the installation.
These commands install the `jarbin-toolkit:action` package and its dependencies (datetime).

## Usage

Here are some examples demonstrating how to use `jarbin-toolkit:action`:

### Basic Error

```python
from jarbin_toolkit_action import Action, Actions
```

## API-Reference

*   **Action**: Callable object storing a function and its arguments for deferred execution.
    *   `Action(name: str, function: Callable, *args: Any, **kwargs: Any)`
        Save a function and its arguments.
        - `name`: logical name of the action
        - `function`: callable to execute
        - `*args`: positional arguments for the function
        - `**kwargs`: keyword arguments for the function
    *   `__call__() -> Any`
        Execute the stored function with its saved arguments.
        Returns the function’s return value.
    *   `__add__(other: Action) -> Actions`
        Combine two `Action` objects into an `Actions` collection.
    *   `__str__() -> str`
        Return readable string representation:
        `'name' : function(*args = [...], **kwargs = {...})`
    *   `__repr__() -> str`
        Return constructor-style representation of the Action object.


*   **Actions**: Collection of multiple `Action` objects.
    *   `Actions(actions: list[Action] | Action | None = None)`
        Create a collection of actions.
        - `actions`: optional single `Action` or list of `Action`
    *   `__call__() -> dict[str, Any]`
        Execute all stored actions sequentially.
        Returns a dictionary:
        `{ action_name: return_value }`
    *   `__add__(other: Actions | Action) -> Actions`
        Merge:
        - `Actions + Actions`
        - `Actions + Action`
    *   `__len__() -> int`
        Return number of stored actions.
    *   `__getitem__(item: int) -> Action`
        Return the `Action` at given index.
    *   `__str__() -> str`
        Return formatted multi-line representation of all stored actions.
    *   `__repr__() -> str`
        Return constructor-style representation of the Actions object.

## Release-Notes
* #### v0.1.1:
    *   **[/]** 1rst real release 

* #### v0.1.0:
    *   **[UPDATE]** `jarbin_toolkit_action` update (removed unlinked sub-modules)
    *   **[INIT]** add `epitech_console` to jarbin-toolkit (renamed `jarbin_toolkit_action`)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/action/LICENSE) file for details.

## Important-Links

#### Files
*   **Repository**: [https://github.com/Jarjarbin06/jarbin-toolkit](https://github.com/Jarjarbin06/jarbin-toolkit)
*   **PyPI**: [https://pypi.org/project/jarbin-toolkit-action/](https://pypi.org/project/jarbin-toolkit-action/)

#### Wiki
*   **Wiki** (*take a look*): [https://github.com/Jarjarbin06/jarbin-toolkit/wiki](https://github.com/Jarjarbin06/jarbin-toolkit/wiki)
*   **README** (*updated*):  [https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/action/README.md](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/action/README.md)
*   **GitHub**: [https://jarjarbin06.github.io/jarbin-toolkit/](https://jarjarbin06.github.io/jarbin-toolkit/)

## Footer

*   Repository: [https://github.com/Jarjarbin06/jarbin-toolkit](https://github.com/Jarjarbin06/jarbin-toolkit)
*   Author: Nathan Jarjarbin
*   Contact: nathan.amaraggi@epitech.eu

⭐️ Like the project? Give it a star!
🐛 Found a bug? Report it in the issues!
\
\
<small>last update : 
**PACKAGE** = *2026/01/21* ; 
**README** = *2026/02/12*</small>
