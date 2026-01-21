<small>last update : 
**PACKAGE** = *2026-01-21 09:20 UTC+1(Paris)* ; 
**README** = *2026-01-21 09:20 UTC+1(Paris)*</small>\
\
<img src="NONE" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="NONE" alt="error loading Jarbin-ToolKit:Error Logo" width="49%" style="display:inline-block;">

# **jarbin-toolkit:error** v0.1.0.0
<details>
<summary>Latest development version</summary>
🟠 UNDER DEVELOPMENT 🟠 v0.1.0.0 🟠
</details>
<details>
<summary>Latest release</summary>
🟢 RELEASED 🟢 vNone 🟢
</details>

[![Python package](None)](None)
[![License: GPL v3](None)](None)
[![Stars](None)](None)

## Description

`jarbin-toolkit:error` is a Python library designed to help you create enhanced terminal interfaces. It's improving the appearance and readability of your command-line interface with lightweight animations, colorful text, and neat formatting. If you want to make your terminal programs more readable and visually structured, this library is for you!

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

*   **Cool Text Effects**: Easily add colors, bold text, italics, underlines, and even strike through to your terminal text.
*   **Animations**: Display simple animations. Useful for loading indicators or status displays.
*   **Progress Bars**: Show the progress of long tasks with customizable progress bars. Provides clear and configurable visual feedback.
*   **Timers**: Use the built-in stopwatch to measure how long parts of your code take to run.
*   **Configuration**: Easily manage settings for your applications.
*   **Error Handling**:  Provides structured and readable error messages.
*   **Cursor Control**:  Provides methods to move, show, and hide the cursor.
*   **Line Control**:  Features for clearing lines or the entire screen.
*   **ANSI Escape Sequence Handling**: Provides classes for generating ANSI escape sequences to control text color, formatting, and cursor movement.

## Tech-Stack

*   **Language**: Python - Chosen for its readability and versatility.
*   **Frameworks**: Python -  Entirely implemented in Python.

## Installation

To begin , install `jarbin-toolkit:error`:

#### **Prerequisites**:

Make sure you have Python `3.11` or newer installed on your computer.
You can check your Python version by opening a terminal and typing `python --version`.

#### **Install from PyPI** (*recommended*):
	
Open your terminal and run this command:
```bash
pip install jarbin_toolkit_error
```
   This will automatically download and install the library from PyPI.

#### **Install from GitHub**:

If you want the latest version directly from the source, you can install it using `git`:
```bash
git clone -b latest NONE
make -C jarbin_toolkit_error install
```
This downloads the code, then the `install` script handles the installation.
These commands install the `jarbin-toolkit:error` package and its dependencies (datetime).

## Usage

Here are some examples demonstrating how to use `jarbin-toolkit:error`:

### Basic Error

```python
from jarbin_toolkit_error import Error
```

## Project-Structure

```
error/
├── demo/
│   └── ...
├── jarbin_toolkit_error/
│   ├── Error/
│   │   ├── __init__.py
│   │   └── error.py
│   ├── __init__.py
│   └── config.ini
├── script/
│   └── ...
├── source/
│   └── ...
├── tests/
│   └── ...
├── Makefile
├── MANIFEST.in
├── pyproject.toml
└── README.md
```

## API-Reference
`.` = *function* ; `+` = *class constructor* ; `_` = *class method* ; `@` = *static method* ; `#` = *class variable*


### Error Module

*   **Error**: Class for custom error handling.
    *   `+Error(message: str = "an error occurred", error: str = "Error", link: tuple[str, int] | None = None)`: Constructor to create an error object.


## Release-Notes
* #### v0.1.0:
    *   **[UPDATE]** `jarbin_toolkit_error` update (removed unlinked sub-modules)
    *   **[INIT]** add `epitech_console` to jarbin-toolkit (renamed `jarbin_toolkit_error`)

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
