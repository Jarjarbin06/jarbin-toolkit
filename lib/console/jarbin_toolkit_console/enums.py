# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import (
    Enum,
    StrEnum,
)
from typing import final

from jarbin_toolkit_console.color import ColorRGB


@final
class PresetColor(Enum):


    # Log colors
    DEBUG = ColorRGB(0, 0, 255)
    INFO = ColorRGB(0, 255, 0)
    NOTICE = ColorRGB(0, 180, 180)
    WARNING = ColorRGB(255, 255, 0)
    ERROR = ColorRGB(255, 0, 0)
    CRITICAL = ColorRGB(255, 0, 255)

    # Status colors
    SUCCESS = ColorRGB(0, 200, 0)
    FAILURE = ColorRGB(200, 0, 0)
    QUESTION = ColorRGB(0, 180, 255)
    DISABLED = ColorRGB(128, 128, 128)
    MUTED = ColorRGB(100, 100, 100)
    HIGHLIGHT = ColorRGB(255, 165, 0)

    # UI colors
    PRIMARY = ColorRGB(0, 145, 211)
    SECONDARY = ColorRGB(31, 72, 94)
    ACCENT = ColorRGB(255, 165, 0)
    BACKGROUND = ColorRGB(20, 20, 20)
    FOREGROUND = ColorRGB(230, 230, 230)

    # Syntax colors
    KEYWORD = ColorRGB(255, 100, 255)
    STRING = ColorRGB(100, 200, 100)
    NUMBER = ColorRGB(100, 180, 255)
    COMMENT = ColorRGB(100, 100, 100)
    OPERATOR = ColorRGB(255, 200, 100)

    # Epitech colors
    EPITECH_LIGHT = ColorRGB(0, 145, 211)
    EPITECH_DARK = ColorRGB(31, 72, 94)


@final
class PresetSymbol(StrEnum):


    # Status
    CHECK = "✓"
    CROSS = "✗"
    WARNING = "⚠"
    INFO = "ℹ"
    QUESTION = "?"

    # Navigation
    LEFT = "←"
    RIGHT = "→"
    UP = "↑"
    DOWN = "↓"

    # Formatting
    BULLET = "•"
    DOT = "·"
    ELLIPSIS = "…"

    # UI
    POINTER = ">"
    ARROW = "➜"
    STAR = "★"

    # Checkbox
    UNCHECKED = "☐"
    CHECKED = "☑"


@final
class PresetBorder(Enum):


    SINGLE = ("─", "│", "┌", "┐", "└", "┘")
    DOUBLE = ("═", "║", "╔", "╗", "╚", "╝")
    HEAVY = ("━", "┃", "┏", "┓", "┗", "┛")
    ROUNDED = ("─", "│", "╭", "╮", "╰", "╯")
    ASCII = ("-", "|", "+", "+", "+", "+")


@final
class PresetSpinner(Enum):


    LINE = ("-", "\\", "|", "/",)
    DOT = (".  ", ".. ", "...", " ..", "  .", "   ")
    BRAILLE = ("⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏")
    BLOCK = ("▖", "▘", "▝", "▗")


@final
class PresetProgress(Enum):


    BLOCK = ("█", "░")
    ASCII = ("=", "-")
    ARROW = (">", "-")
    DOT = ("●", "○")


__all__ = [
    'PresetColor',
    'PresetSymbol',
    'PresetBorder',
    'PresetSpinner',
    'PresetProgress',
]
