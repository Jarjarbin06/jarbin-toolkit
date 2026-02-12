<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Epitech_logo.png" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="https://raw.githubusercontent.com/Jarjarbin06/jarbin-toolkit/refs/heads/main/source/Jarbin-Toolkit_logo.jpg" alt="error loading Jarbin-ToolKit Logo" width="49%" style="display:inline-block;">

# **Jarbin-ToolKit:Console** v0.1.1.0
<details>
<summary>Latest development version</summary>
🟠 UNDER DEVELOPMENT 🟠 None 🟠
</details>
<details>
<summary>Latest release</summary>
🟢 RELEASED 🟢 v0.1.1.0 🟢
</details>

[![CodeQL Advanced](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/codeql.yml/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/codeql.yml)
[![Python package tester](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/test-package.yml/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/test-package.yml)
[![pages-build-deployment](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Jarjarbin06/jarbin-toolkit/actions/workflows/pages/pages-build-deployment)

## Description

`jarbin-toolkit:console` is a Python library designed to help you create enhanced terminal interfaces. It's improving the appearance and readability of your command-line interface with lightweight animations, colorful text, and neat formatting. If you want to make your terminal programs more readable and visually structured, this library is for you!

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
*   **Cursor Control**:  Provides methods to move, show, and hide the cursor.
*   **Line Control**:  Features for clearing lines or the entire screen.
*   **ANSI Escape Sequence Handling**: Provides classes for generating ANSI escape sequences to control text color, formatting, and cursor movement.

## Tech-Stack

*   **Language**: Python - Chosen for its readability and versatility.
*   **Frameworks**: Python -  Entirely implemented in Python.

## Installation

To begin , install `jarbin-toolkit:console`:

#### **Prerequisites**:

Make sure you have Python `3.11` or newer installed on your computer.
You can check your Python version by opening a terminal and typing `python --version`.

#### **Install from PyPI** (*recommended*):
	
Open your terminal and run this command:
```bash
pip install jarbin_toolkit_console
```
   This will automatically download and install the library from PyPI.

#### **Install from GitHub**:

If you want the latest version directly from the source, you can install it using `git`:
```bash
git clone -b latest NONE
make -C lib/jarbin_toolkit_console install
```
This downloads the code, then the `install` script handles the installation.
These commands install the `jarbin-toolkit:console` package and its dependencies (datetime).

## Usage

Here are some examples demonstrating how to use `jarbin-toolkit:console`:

### Basic Text Formatting

```python
from jarbin_toolkit_console import *
```

## API-Reference

### Animation

*   **Animation**: Step-based console animation handler.
    *   `Animation(animation: list[Any] | str = "")`
        Create an animation from a list of steps or a `"\\"`-separated string.
    *   `update(auto_reset: bool = True) -> None`
        Advance to next animation step.
        - `auto_reset`: reset automatically at last step
    *   `render(color: ANSI | int = RESET, delete: bool = False) -> str`
        Render current step.
        - `color`: ANSI color or color code
        - `delete`: move cursor up after rendering
    *   `is_last() -> bool`
        Return `True` if animation reached final step.
    *   `reset() -> None`
        Reset animation to first step.
    *   `__call__() -> None`
        Shortcut for `update()`.
    *   `__len__() -> int`
        Return number of steps.
    *   `__getitem__(index: int) -> str`
        Return step at given index.
    *   `__str__(color: ANSI = RESET) -> str`
        Return colored current frame.
    *   `__add__(other) -> Animation`
        Merge with another Animation or compatible object.
    *   `__repr__() -> str`
        Constructor-style representation.


*   **BasePack**: Predefined animation packs for bars and sliders.
    *   Class attributes (after `update()`):
        - `P_SLIDE_R`, `P_SLIDE_L`
        - `P_SLIDER_R`, `P_SLIDER_L`
        - `P_FILL_R`, `P_FILL_L`
        - `P_EMPTY_R`, `P_EMPTY_L`
        - `P_FULL`, `P_EMPTY`
    *   `update(style: Style) -> None` (staticmethod)
        Initialize all predefined animation sequences using given style.


*   **ProgressBar**: Animated and customizable console progress bar.
    *   `ProgressBar(length: int, *, animation: Animation | None = None, style: Style = default, percent_style: str = "bar", spinner: Animation | None = None, spinner_position: str = "a")`
        Create a progress bar.
        - `length`: bar length
        - `animation`: custom Animation
        - `style`: Style object
        - `percent_style`: `"bar" | "num" | "mix"`
        - `spinner`: optional spinner animation
        - `spinner_position`: `"a"` (after) or `"b"` (before)
    *   `update(percent: int = 0, update_spinner: bool = True, auto_reset: bool = True) -> None`
        Update bar percentage and optionally spinner.
    *   `render(color: ANSI | tuple = RESET, hide_spinner_at_end: bool = True, delete: bool = False) -> Text`
        Render progress bar.
        - `color`: single ANSI or tuple (bar, spinner, percent)
        - `hide_spinner_at_end`: hide spinner at 100%
        - `delete`: clear previous line
    *   `__call__() -> None`
        Increment percentage by 1.
    *   `__getitem__(index: int) -> str`
        Get animation frame.
    *   `__str__(color: tuple = RESET, hide_spinner: bool = False) -> str`
        String representation.
    *   `__repr__() -> str`
        Constructor-style representation.


*   **Spinner**: Predefined spinner animations.
    *   `stick(style: Style = default) -> Animation` (staticmethod)
        Rotating stick spinner (`- \ | /`).
    *   `plus(style: Style = default) -> Animation` (staticmethod)
        Plus-style spinner (`- |`).
    *   `cross(style: Style = default) -> Animation` (staticmethod)
        Cross-style spinner (`/ \`).


*   **Style**: Visual configuration for animations and progress bars.
    *   `Style(on: str = "#", off: str = "-", arrow_left: str = "<", arrow_right: str = ">", border_left: str = "|", border_right: str = "|")`
        Create a style configuration.

        - `on`: filled character
        - `off`: empty character
        - `arrow_left`: left arrow
        - `arrow_right`: right arrow
        - `border_left`: left border
        - `border_right`: right border
    *   `__str__() -> str`
        Return formatted style description.
    *   `__repr__() -> str`
        Constructor-style representation.

### ANSI Module

*   **ANSI**: Tool for handling ANSI sequences (inherits `Format`).
    *   `ESC: str` – ANSI escape sequence starter (`\x1b[`).
    *   `__init__(sequence: list[Any|str] | Any | str = "")`
        Initialize an ANSI sequence.
    *   `__add__(other: Any) -> ANSI`
        Concatenate with another `ANSI`/`Text`/`Animation`/`ProgressBar`/`StopWatch`/`str` object.
    *   `__mul__(other: int) -> ANSI`
        Repeat ANSI sequence `other` times.
    *   `__str__() -> str`
        Convert to string.
    *   `__len__() -> int`
        Length of sequence.
    *   `__repr__() -> str`
        Representation as `ANSI(...)`.


*   **BasePack**: Ready-to-use ANSI animation/color pack.
    *   `P_ERROR: tuple[ANSI|str, ANSI|str]`
    *   `P_WARNING: tuple[ANSI|str, ANSI|str]`
    *   `P_VALID: tuple[ANSI|str, ANSI|str]`
    *   `P_INFO: tuple[ANSI|str, ANSI|str]`
    *   `update() -> None`
        Initialize colors using `Color` class.


*   **Color**: ANSI coloring system.
    *   Standard attributes: `C_RESET, C_BOLD, C_ITALIC, C_UNDERLINE, C_FLASH_SLOW, C_FLASH_FAST, C_HIDDEN, C_STRIKETHROUGH`
    *   Foreground colors: `C_FG_DARK, C_FG_DARK_GREY, ..., C_FG_WHITE`
    *   Background colors: `C_BG, C_BG_DARK_GREY, ..., C_BG_WHITE`
    *   `__new__(*args) -> ANSI` – calls `Color.color()`.
    *   `color(color: Any|str|int) -> ANSI` – get ANSI sequence for a color.
    *   `color_fg(color: int) -> ANSI` – foreground 0–255.
    *   `color_bg(color: int) -> ANSI` – background 0–255.
    *   `rgb_fg(r: int, g: int, b: int) -> ANSI` – RGB foreground.
    *   `rgb_bg(r: int, g: int, b: int) -> ANSI` – RGB background.
    *   `epitech_fg() -> ANSI`, `epitech_bg() -> ANSI` – Epitech theme colors.
    *   `epitech_dark_fg() -> ANSI`, `epitech_dark_bg() -> ANSI` – Epitech dark theme colors.


*   **Cursor**: Control console cursor position.
    *   `up(n: int = 1) -> ANSI` – move cursor up.
    *   `down(n: int = 1) -> ANSI` – move cursor down.
    *   `left(n: int = 1) -> ANSI` – move cursor left.
    *   `right(n: int = 1) -> ANSI` – move cursor right.
    *   `top() -> ANSI` – move to top-left corner.
    *   `previous(n: int = 1) -> ANSI` – beginning of previous line.
    *   `next(n: int = 1) -> ANSI` – beginning of next line.
    *   `move(y: int = 0, x: int = 0) -> ANSI` – move to column x, row y.
    *   `move_column(x: int = 0) -> ANSI` – move to column x.
    *   `set() -> ANSI` – save cursor position.
    *   `reset() -> ANSI` – return to saved position.
    *   `show() -> ANSI` – show cursor.
    *   `hide() -> ANSI` – hide cursor.


*   **Line**: Manage console lines and screen.
    *   `clear_line() -> ANSI` – clear current line.
    *   `clear_start_line() -> ANSI` – clear from start to cursor.
    *   `clear_end_line() -> ANSI` – clear from cursor to end.
    *   `clear_screen() -> ANSI` – clear entire screen.
    *   `clear() -> ANSI` – clear screen and move cursor to top-left.
    *   `clear_previous_line(n: int = 1) -> ANSI` – clear previous line(s).

### Setting

*   **Setting**: Module-wide configuration and environment handler.
    *   `Setting`
        Holds all module settings, package information, and system references.
    *   `S_OS: str | None`
        Operating system name (`"Windows"`, `"Linux"`, etc.).
    *   `S_CONFIG_FILE: Config | None`
        Configuration file object.
    *   `S_LOG_FILE: Log | None`
        Log file object.
    *   `S_PACKAGE_PATH: str`
        Path to the package.
    *   `S_PACKAGE_NAME: str`
        Package name.
    *   `S_PACKAGE_VERSION: str`
        Package version.
    *   `S_PACKAGE_DESCRIPTION: str`
        Package description.
    *   `S_PACKAGE_REPOSITORY: str`
        Package repository URL.
    *   `S_SETTING_SHOW_BANNER: bool`
        Show module banner.
    *   `S_SETTING_AUTO_COLOR: bool`
        Enable automatic color detection.
    *   `S_SETTING_SAFE_MODE: bool`
        Enable safe mode.
    *   `S_SETTING_MINIMAL_MODE: bool`
        Enable minimal mode.
    *   `S_SETTING_DEBUG_MODE: bool`
        Enable debug mode.
    *   `S_SETTING_LOG_MODE: bool`
        Enable logging.
    *   `S_SETTING_OPENED_LOG: str`
        Name of currently opened log file.
    *   `update() -> None`
        Initialize system settings and load configuration.
        - Detects OS and sets `S_PACKAGE_PATH`.
        - Loads configuration from `S_CONFIG_FILE`.
        - Updates package metadata.
        - Initializes logging if `S_SETTING_LOG_MODE` is enabled.

### Text

*   **Format**: Text and console formatting utility.
    *   `Format`
        Base class for applying ANSI-based formatting to `Text`, `Animation`, `ProgressBar`, `ANSI` objects, or strings.
    *   `reset() -> Any`
        Apply reset format.
    *   `bold() -> Any`
        Apply bold format.
    *   `italic() -> Any`
        Apply italic format.
    *   `underline() -> Any`
        Apply underline format.
    *   `hide() -> Any`
        Apply hidden format.
    *   `strikethrough() -> Any`
        Apply strikethrough format.
    *   `error(title: bool = False) -> Any`
        Apply error format; optionally for a title.
    *   `warning(title: bool = False) -> Any`
        Apply warning format; optionally for a title.
    *   `valid(title: bool = False) -> Any`
        Apply success/valid format; optionally for a title.
    *   `info(title: bool = False) -> Any`
        Apply info format; optionally for a title.
    *   `apply(obj: Any, sequence: Any | None = None) -> Any` (staticmethod)
        Apply a given ANSI sequence to an object (`Text`, `Animation`, `ProgressBar`, `ANSI`, or `str`).
    *   `tree(d: dict | str | list, title: str | None = None, indent: int = 0) -> str` (staticmethod)
        Convert a dictionary, list, or string into a bash-style tree string.
    *   `module_tree() -> str` (staticmethod)
        Returns the full module tree formatted as a string.


*   **Text**: Enhanced string handling with formatting support.
    *   `Text(text: list[Any | str] | Any | str = "")`
        Create a `Text` object.
        - Accepts string, list of strings, or `ANSI` object.
    *   `__add__(other: Any | str) -> Text`
        Concatenate `Text` with another `Text`, `ANSI`, or string.
    *   `__mul__(other: int) -> Text`
        Repeat the `Text` sequence.
    *   `__str__() -> str`
        Convert `Text` object to string.
    *   `__len__() -> int`
        Return the length of the `Text` string.
    *   `__repr__() -> str`
        Constructor-style representation.
    *   `url_link(url: str, text: str | None = None) -> Text` (staticmethod)
        Format a clickable URL link (may not work in all consoles).
    *   `file_link(path: str, line: int | None = None) -> Text` (staticmethod)
        Format a clickable file link (supports JetBrains IDEs like CLion).

### Console

*   **ConsoleMeta**: Metaclass for `Console`.
    *   `__len__() -> int`
        Return the width of the current terminal in columns (default 100 if unavailable).


*   **Console**: Console input/output utility.
    *   `execute() -> None`
        Placeholder for executing code in the console (not implemented).
    *   `print(*args, separator: str = " ", start: str = "", end: str = "\n", file: Any = stdout, auto_reset: bool = True, cut: bool = False, sleep: int | float | None = None) -> Text`
        Print formatted text to the console.
        - `*args`: values to print
        - `separator`: string between values
        - `start`: prepended string
        - `end`: appended string
        - `file`: file-like object
        - `auto_reset`: reset ANSI sequences automatically
        - `cut`: truncate output to terminal width
        - `sleep`: delay after printing
        - Returns: `Text` object of printed content
    *   `input(msg: str = "Input", separator: str = " >>> ", wanted_type: type = str) -> Any`
        Prompt user input from console.
        - `msg`: message to display
        - `separator`: string between message and input
        - `wanted_type`: type to convert input
        - Returns: user input of specified type
    *   `get_key_press() -> str`
        Wait for a key press and return it.
        - Handles single key and escape sequences.
    *   `get_cursor_position() -> tuple[int, int]`
        Get current cursor position in the console as `(row, col)`.
    *   `get_size() -> tuple[int, int]`
        Get current terminal size as `(width, height)`.
    *   `flush(stream: Any = stdout) -> None`
        Flush output of the given stream.

## Release-Notes
* #### v0.1.1:
    *   **[/]** 1rst real release
* #### v0.1.0:
    *   **[UPDATE]** `jarbin_toolkit_console` update (removed unlinked sub-modules)
    *   **[INIT]** add `epitech_console` to jarbin-toolkit (renamed `jarbin_toolkit_console`)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/console/LICENSE) file for details.

## Important-Links

#### Files
*   **Repository**: [https://github.com/Jarjarbin06/jarbin-toolkit](https://github.com/Jarjarbin06/jarbin-toolkit)
*   **PyPI**: [https://pypi.org/project/jarbin-toolkit-console/](https://pypi.org/project/jarbin-toolkit-console/)

#### Wiki
*   **Wiki** (*take a look*): [https://github.com/Jarjarbin06/jarbin-toolkit/wiki](https://github.com/Jarjarbin06/jarbin-toolkit/wiki)
*   **README** (*updated*):  [https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/console/README.md](https://github.com/Jarjarbin06/jarbin-toolkit/blob/main/lib/console/README.md)
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
**PACKAGE** = *2026/02/12* ; 
**README** = *2026/02/12*</small>
