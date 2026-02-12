<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# **Jarbin-ToolKit:Config** v0.1.2.0
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

`jarbin-toolkit:config` is a Python library designed to help you create enhanced terminal interfaces. It's improving the appearance and readability of your command-line interface with lightweight animations, colorful text, and neat formatting. If you want to make your terminal programs more readable and visually structured, this library is for you!

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

To begin , install `jarbin-toolkit:config`:

#### **Prerequisites**:

Make sure you have Python `3.11` or newer installed on your computer.
You can check your Python version by opening a terminal and typing `python --version`.

#### **Install from PyPI** (*recommended*):
	
Open your terminal and run this command:
```bash
pip install jarbin_toolkit_config
```
   This will automatically download and install the library from PyPI.

#### **Install from GitHub**:

If you want the latest version directly from the source, you can install it using `git`:
```bash
git clone -b latest NONE
make -C lib/jarbin_toolkit_config install
```
This downloads the code, then the `install` script handles the installation.
These commands install the `jarbin-toolkit:config` package and its dependencies (datetime).

## Usage

Here are some examples demonstrating how to use `jarbin-toolkit:config`:

### Basic Config

```python
from jarbin_toolkit_config import Config
```

## API-Reference

*   **Config**: INI configuration file manager built on `configparser`.
    *   `Config(path: str, data: dict | None = None, *, file_name: str = "config.ini")`
        Create a new config file if it does not exist, otherwise read it.
        - `path`: directory where the config file is located
        - `data`: optional dictionary used to initialize file content (section → key/value pairs)
        - `file_name`: name of the configuration file (default: `config.ini`)
        - Automatically adapts path separators depending on OS (Windows/Linux)
    *   `set(section: str, option: str, data: Any) -> None`
        Set or update a value in the config file.
        - `section`: section name
        - `option`: key name
        - `data`: value to store (converted to string)
        - Immediately writes changes to disk
    *   `get(section: str, option: str, wanted_type: type = str) -> Any`
        Retrieve a value from the config file.
        - `section`: section name
        - `option`: key name
        - `wanted_type`: type conversion applied to the result (default: `str`)
        - Returns the converted value
    *   `get_bool(section: str, option: str) -> bool`
        Retrieve a value as boolean.
    *   `get_int(section: str, option: str) -> int`
        Retrieve a value as integer.
    *   `get_float(section: str, option: str) -> float`
        Retrieve a value as float.
    *   `delete(cached: bool = False) -> bool`
        Delete the config file from disk.
        - `cached`: if `True`, keeps config data in memory
        - Returns `True` if successfully deleted, `False` otherwise
    *   `exist(path: str, *, file_name: str = "config.ini") -> bool` (staticmethod)
        Check whether a config file exists and is not empty.
        - `path`: directory path
        - `file_name`: name of config file
        - Returns `True` if file exists and contains data, `False` otherwise
    *   `__repr__() -> str`
        Return constructor-style representation of the Config object.

## Release-Notes
* #### v0.1.1:
    *   **[/]** 1rst real release
* #### v0.1.0:
    *   **[UPDATE]** `jarbin_toolkit_config` update (removed unlinked sub-modules)
    *   **[INIT]** add `epitech_console` to jarbin-toolkit (renamed `jarbin_toolkit_config`)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/config/LICENSE) file for details.

## Important-Links

#### Files
*   **Repository**: [https://github.com/Jarjarbin06/jarbin-toolkit](https://github.com/Jarjarbin06/jarbin-toolkit)
*   **PyPI**: [https://pypi.org/project/jarbin-toolkit-config/](https://pypi.org/project/jarbin-toolkit-config/)

#### Wiki
*   **Wiki** (*take a look*): [https://github.com/Jarjarbin06/jarbin-toolkit/wiki](https://github.com/Jarjarbin06/jarbin-toolkit/wiki)
*   **README** (*updated*):  [https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/config/README.md](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/config/README.md)
*   **GitHub**: [https://jarjarbin06.github.io/jarbin-toolkit/](https://jarjarbin06.github.io/jarbin-toolkit/)

## Footer

*   Repository: [https://github.com/Jarjarbin06/jarbin-toolkit](https://github.com/Jarjarbin06/jarbin-toolkit)
*   Author: Nathan Jarjarbin
*   Contact: nathan.amaraggi@epitech.eu

⭐️ Like the project? Give it a star!
🐛 Found a bug? Report it in the issues!
\
\
<small>
Last update : 
**PACKAGE** — *2026/01/21* ; 
**README** — *2026/02/12*
</small>
