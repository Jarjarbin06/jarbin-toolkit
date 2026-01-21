<small>last update : 
**PACKAGE** = *2026-01-21 09:20 UTC+1(Paris)* ; 
**README** = *2026-01-21 09:20 UTC+1(Paris)*</small>\
\
<img src="NONE" alt="error loading Epitech Logo" width="49%" style="display:inline-block; margin-right:1%;">
<img src="NONE" alt="error loading Jarbin-ToolKit:Console Logo" width="49%" style="display:inline-block;">

# **Jarbin-ToolKit:Console** v0.1.0.0
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
from jarbin_toolkit_console.Text import Text
from jarbin_toolkit_console.ANSI import Color
from jarbin_toolkit_console import init, quit

init()

epitech_color = Color.epitech_fg() + Color.rgb_bg(0, 0 ,0)
reset = Color(Color.C_RESET)
my_text = epitech_color + Text("hi").bold() + reset

print(my_text)

quit(delete_log=True)
```

### Creating an Animation

```python
from jarbin_toolkit_console.Animation import Animation, BasePack
from jarbin_toolkit_console.System import Console
from jarbin_toolkit_console import init, quit

init()

my_animation = Animation(BasePack.P_FILL_R)
for i in range(5):
    Console.print(my_animation.render(delete=True), sleep=0.5)
    my_animation.update()

quit(delete_log=True)
```

### Creating a custom Animation

```python
from jarbin_toolkit_console.Animation import Animation
from jarbin_toolkit_console.System import Console
from jarbin_toolkit_console import init, quit

init()

my_animation = Animation(['Frame 1', 'Frame 2', 'Frame 3'])
for i in range(5):
    Console.print(my_animation.render(delete=True), sleep=0.5)
    my_animation.update()

quit(delete_log=True)
```

### Using simple Progress Bar 

```python
from jarbin_toolkit_console.Animation import ProgressBar, Spinner
from jarbin_toolkit_console.System import Console
from jarbin_toolkit_console import init, quit

init()

my_spinner = Spinner.stick()
my_progress_bar = ProgressBar(length=20, percent_style="mix", spinner=my_spinner)
for i in range(101):
    my_progress_bar.update(percent=i, update_spinner=(i % 5 == 0))
    Console.print(my_progress_bar.render(delete=True), sleep=0.05)

quit(delete_log=True)
```

### Using advanced Progress Bar with variable size

```python
from jarbin_toolkit_console.Animation import ProgressBar, Style
from jarbin_toolkit_console.ANSI import Line
from jarbin_toolkit_console.System import Console
from jarbin_toolkit_console import init, quit

init()

style : Style = Style(on="=", off=" ", border_left="[", border_right="]")
bar : ProgressBar

for i in range(1001):
	bar = ProgressBar(len(Console) - 15, percent_style="mix", style=style)
	bar.update(i/10)
	Console.print(bar.render(delete=True), sleep=0.01, cut=True)

quit(delete_log=True)
```

## API-Reference
`.` = *function* ; `+` = *class constructor* ; `_` = *class method* ; `@` = *static method* ; `#` = *class variable*

*   `.init()`: Initializes the module, BasePacks and Setting classes and the log file (if activated in the config file).
*   `.quit(show: bool = False, delete_log: bool = False)`: Uninitializes the module and the log file (if activated in the config file).

### Animation Module

*   **Animation**: Class for creating animations.
    *   `+Animation(animation: list[Any] | str = "")`: Constructor to create an animation.
    *   `_update(auto_reset: bool = True)`: Advances the animation by one step.
    *   `_render(delete: bool = False)`: Renders the current frame of the animation.
    *   `_is_last()`: Returns whether the current step is the last one.
    *   `_reset()`: Resets the current step to `0`.

*   **BasePack**: Predefined animation packs.
	*   `@update(style: Style = Style("#", "-", "<", ">", "|", "|"))`: Update the BasePack animations to fit with the given Style (or the default one if no Style given).
	*   `#P_SLIDE_R`: Character sliding to the right.
	*   `#P_SLIDE_L`: Character sliding to the left.
	*   `#P_SLIDER_R`: Slider going right.
	*   `#P_SLIDER_L`: Slider going left.
	*   `#P_FILL_R`: Filling to the right.
	*   `#P_FILL_R`: Filling to the left.
	*   `#P_EMPTY_R`: Emptying to the right.
	*   `#P_EMPTY_L`: Emptying to the left.
	*   `#P_FULL`: Full.
	*   `#P_EMPTY`: Empty.

*   **ProgressBar**: Class for creating progress bars.
    *   `+ProgressBar(length: int, animation: Animation | None = None, style: Style = Style("#", "-", "<", ">", "|", "|"), percent_style: str = "bar", spinner: Animation | None = None, spinner_position: str = "a")`: Constructor to create a progress bar.
    *   `_update(percent: int = 0, update_spinner: bool = True, auto_reset: bool = True)`: Updates the progress bar to a specified percentage.
    *   `_render(color: ANSI | tuple[ANSI, ANSI, ANSI] = Color.color(Color.C_RESET), hide_spinner_at_end: bool = True, delete: bool = False)`: Renders the progress bar.

*   **Spinner**: Class with pre-built spinner animations.
    *   `@stick(style: Style = Style("#", " ", "#", "#", "", ""))`: Creates a stick spinner.
    *   `@plus(style: Style = Style("#", " ", "#", "#", "", ""))`: Creates a plus spinner.
    *   `@cross(style: Style = Style("#", " ", "#", "#", "", ""))`: Creates a cross spinner.

*   **Style**: Class for styling progress bars.
    *   `+Style(on: str = "#", off: str = "-", arrow_left: str = "<", arrow_right: str = ">", border_left: str = "|", border_right: str = "|")`: Constructor to create a style.

### ANSI Module

*   **ANSI**: Class for creating ANSI escape sequences.
    *   `+ANSI(sequence: list[Any | str] | Any | str = "")`: Constructor to create an ANSI sequence.
    *   `#ESC`: ANSI escape character.

*   **BasePack**: Ready-to-use ANSI escape sequences.
	*   `@update()`: Update the BasePack escape sequences (currently reserved for future extensions).
    *   `#P_ERROR`: Colors for error title and body.
    *   `#P_WARNING`: Colors for warning title and body.
    *   `#P_VALID`: Colors for valid title and body.
    *   `#P_INFO`: Colors for information title and body.

*   **Color**: Class for ANSI color codes.
	*   `@color(color: int)`: Returns ANSI sequence for pre-made color codes.
    *   `@color_fg(color: int)`: Returns ANSI sequence for a foreground color.
    *   `@color_bg(color: int)`: Returns ANSI sequence for a background color.
    *   `@rgb_fg(r: int, g: int, b: int)`: Returns ANSI sequence for a foreground RGB color.
    *   `@rgb_bg(r: int, g: int, b: int)`: Returns ANSI sequence for a background RGB color.
    *   `@epitech_fg()`: Returns ANSI sequence for a foreground colored as Epitech (light).
    *   `@epitech_bg()`: Returns ANSI sequence for a background colored as Epitech (light).
    *   `@epitech_dark_fg()`: Returns ANSI sequence for a foreground colored as Epitech (dark).
    *   `@epitech_dark_bg()`: Returns ANSI sequence for a background colored as Epitech (dark).
    *   `#C_RESET`: Reset color code.
    *   `#C_BOLD`: Bold color code.
    *   `#C_ITALIC`: Italic color code.
    *   `#C_UNDERLINE`: Underline color code.
    *   `#C_FLASH_SLOW`: Slow flashing color code.
    *   `#C_FLASH_FAST`: Fast flashing color code.
    *   `#C_HIDDEN`: Hidden color code.
    *   `#C_STRIKETHROUGH`: Strikethrough color code.
    *   `#C_FG_...`: Foreground colors.
    *   `#C_BG_...`: Background colors.

*   **Cursor**: Class for cursor manipulation.
    *   `@up(n: int = 1)`: Moves the cursor up `n` lines.
    *   `@down(n: int = 1)`: Moves the cursor down `n` lines.
    *   `@left(n: int = 1)`: Moves the cursor left `n` columns.
    *   `@right(n: int = 1)`: Moves the cursor right `n` columns.
    *   `@top()`: Moves the cursor to the top left corner.
    *   `@previous(n: int = 1)`: Moves the cursor to the beginning of `n` lines before.
    *   `@next(n: int = 1)`: Moves the cursor to the beginning of `n` lines after.
    *   `@move(x: int = 0, y: int = 0)`: Moves the cursor at position (`x`, `y`).
    *   `@move_column(x: int = 0)`: Moves the cursor at position `x` on the same line.
    *   `@set()`: Save the position of the cursor.
    *   `@reset()`: Load the saved position of the cursor.
    *   `@show()`: Shows the cursor.
    *   `@hide()`: Hides the cursor.

*   **Line**: Class for line manipulation.
    *   `@clear_line()`: Clears the current line.
    *   `@clear_start_line()`: Clears the current line from the beginning to the cursor.
    *   `@clear_end_line()`: Clears the current line from the cursor to the end.
    *   `@clear_screen()`: Clears the entire screen.
    *   `@clear()`: Clears the entire screen and move the cursor to the top-left corner.
    *   `@clear_previous_line(n: int = 1)`: Go to the previous `n` lines, clear it and bring the cursor to the beginning of the previous line.

### System Module

*   **Console**: Class for console output.
    *   `@print(*args, separator: str = " ", start: str = "", end: str = "\n", file: Any = stdout, auto_reset: bool = True, sleep: int | float | None = None, cut: bool = False)`: Print any objects in the terminal (or in any other `file`), starting with `start` and ending with `end`, if multiple value are to be printed, they will be separated by `separator`, if `cut` then the text will be cut to fit in the terminal, optional waiting after printing of `sleep` seconds.
    *   `@input(msg: str = "Input", separator: str = " >>> ", wanted_type: type = str)`: Returns a user text input changed to `wanted_type`.
    *   `@flush(stream: Any = stdout)`: Flush any content in `stream`.

*   **Setting**: Class for module's settings.
	*   `@update()`: Update the Settings.
    *   `#S_PACKAGE_NAME`: Package's name.
    *   `#S_PACKAGE_VERSION`: Package's version.
    *   `#S_PACKAGE_DESCRIPTION`: Package's description.
    *   `#S_PACKAGE_REPOSITORY`: Package's repository URL.
    *   `#S_SETTING_SHOW_BANNER`: Package's show-banner setting.
    *   `#S_SETTING_AUTO_COLOR`: Package's auto-color setting.
    *   `#S_SETTING_SAFE_MODE`: Package's safe-mode setting.
    *   `#S_SETTING_MINIMAL_MODE`: Package's minimal-mode setting.
    *   `#S_SETTING_DEBUG`: Package's debug setting.
    *   `#S_SETTING_LOG`: Package's log setting.
    *   `#S_LOG_FILE`: Package's log_file.

### Text Module

*   **Format**: Class for handling text's format.
    *   `_reset()`: Clear the format of a text.
    *   `_bold()`: Make a text bold.
    *   `_italic()`: Make a text italic.
    *   `_underline()`: Make a text underlined.
    *   `_hide()`: Make a text hidden.
    *   `_strikthrough()`: Make a text strikethrough.
    *   `_error(title: bool = False)`: Make a text styled as an ERROR (background is colored if title, foreground otherwise).
    *   `_warning(title: bool = False)`: Make a text styled as a WARNING (background is colored if title, foreground otherwise).
    *   `_ok(title: bool = False)`: Make a text styled as an OK (background is colored if title, foreground otherwise).
    *   `_info(title: bool = False)`: Make a text styled as an INFO (background is colored if title, foreground otherwise).
    *   `@apply(obj: Any, sequence: Any | None = None)`: Apply anything to an object (Text, ANSI, Animation, ProgressBar or str).
    *   `@tree(d: dict | str | list, title: str | None = None, indent: int = 0`: Get a formated version of a dictionary as bash "tree" command does).
    *   `@module_tree()`: Get module's file tree.

*   **Text**: Class for handling text.
    *   `+Text(text: Any | str = "")`: Constructor to create a text object.
    *   `@url_link(url: str, text: str | None = None)`: Creates a link to a url.
    *   `@file_link(path: str, line: int | None = None)`: Creates a link to a file and line number.

## Release-Notes
* #### v0.1.0:
    *   **[UPDATE]** `jarbin_toolkit_console` update (removed unlinked sub-modules)
    *   **[INIT]** add `epitech_console` to jarbin-toolkit (renamed `jarbin_toolkit_console`)

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
