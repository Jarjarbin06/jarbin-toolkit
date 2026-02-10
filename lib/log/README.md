<small>last update : 
**PACKAGE** = *2026/02/05* ; 
**README** = *2026/02/05*</small>\
\
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# **Jarbin-ToolKit:Log** v0.2.1.0
<details>
<summary>Latest development version</summary>
🟠 UNDER DEVELOPMENT 🟠 v0.2.1.0 🟠
</details>
<details>
<summary>Latest release</summary>
🟢 RELEASED 🟢 v0.2.0.0 🟢
</details>

[![CodeQL Advanced](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/codeql.yml/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/codeql.yml)
[![Python package tester](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/test-package.yml/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/test-package.yml)
[![pages-build-deployment](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/pages/pages-build-deployment)

## Description

`jarbin-toolkit:log` is a Python library designed to help you create enhanced terminal interfaces. It's improving the appearance and readability of your command-line interface with lightweight animations, colorful text, and neat formatting. If you want to make your terminal programs more readable and visually structured, this library is for you!

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

To begin , install `jarbin-toolkit:log`:

#### **Prerequisites**:

Make sure you have Python `3.11` or newer installed on your computer.
You can check your Python version by opening a terminal and typing `python --version`.

#### **Install from PyPI** (*recommended*):
	
Open your terminal and run this command:
```bash
pip install jarbin_toolkit_log
```
   This will automatically download and install the library from PyPI.

#### **Install from GitHub**:

If you want the latest version directly from the source, you can install it using `git`:
```bash
git clone -b latest NONE
make -C lib/jarbin_toolkit_log install
```
This downloads the code, then the `install` script handles the installation.
These commands install the `jarbin-toolkit:log` package and its dependencies (datetime).

## Usage

Here are some examples demonstrating how to use `jarbin-toolkit:log`:

### Basic Log

```python
from jarbin_toolkit_log import Log
```

## API-Reference
`.` = *function* ; `+` = *class constructor* ; `_` = *class method* ; `@` = *static method* ; `#` = *class variable*


### Error Module

*   **Error**: Class for custom error handling.
    *   `+Error(message: str = "an error occurred", error: str = "Error", link: tuple[str, int] | None = None)`: Constructor to create an error object.


## Release-Notes
* #### v0.2.0:
    *   **[UPDATE]** change log file extension to custom extension (`jar-log`)
    *   **[ADD]** modification not allowed after closing or after opening and existing file
    *   **[UPDATE]** add option to choose between `.log` or `log.json` file\
(`.log` for more human readability, `.json` for more computer readability)
* #### v0.1.0:
    *   **[UPDATE]** `jarbin_toolkit_log` update (removed unlinked sub-modules)
    *   **[INIT]** add `epitech_console` to jarbin-toolkit (renamed `jarbin_toolkit_log`)

## License

This project is licensed under the GNU General Public License v3.0 - see the [NONE](NONE) file for details.

## Important-Links

#### Files
*   **Repository**: [NONE](NONE)
*   **PyPI**: [NONE](NONE)

#### Wiki
*   **Wiki** (*take a look*): [NONE](NONE)
*   **README**: [NONE](NONE)
*   **GitHub**: [NONE](NONE)

## Footer

*   Repository: [NONE](NONE)
*   Author: Nathan Jarjarbin
*   Contact: nathan.amaraggi@epitech.eu

⭐️ Like the project? Give it a star!
🐛 Found a bug? Report it in the issues!
