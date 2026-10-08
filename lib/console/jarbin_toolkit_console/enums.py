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

    # Basic colors
    BLACK = ColorRGB(0, 0, 0)
    RED = ColorRGB(255, 0, 0)
    GREEN = ColorRGB(0, 255, 0)
    YELLOW = ColorRGB(255, 255, 0)
    BLUE = ColorRGB(0, 0, 255)
    MAGENTA = ColorRGB(255, 0, 255)
    CYAN = ColorRGB(0, 255, 255)
    WHITE = ColorRGB(255, 255, 255)

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
class PresetBox(StrEnum):


    # Box Drawing - Light
    LIGHT_HORIZONTAL = "─"
    LIGHT_VERTICAL = "│"

    LIGHT_TEE_UP = "┬"
    LIGHT_TEE_DOWN = "┴"
    LIGHT_TEE_LEFT = "├"
    LIGHT_TEE_RIGHT = "┤"

    LIGHT_CORNER_TOP_LEFT = "┌"
    LIGHT_CORNER_TOP_RIGHT = "┐"
    LIGHT_CORNER_BOTTOM_LEFT = "└"
    LIGHT_CORNER_BOTTOM_RIGHT = "┘"

    LIGHT_CROSS = "┼"

    # Box Drawing - Heavy
    HEAVY_HORIZONTAL = "━"
    HEAVY_VERTICAL = "┃"

    HEAVY_TEE_UP = "┳"
    HEAVY_TEE_DOWN = "┻"
    HEAVY_TEE_LEFT = "┣"
    HEAVY_TEE_RIGHT = "┫"

    HEAVY_CORNER_TOP_LEFT = "┏"
    HEAVY_CORNER_TOP_RIGHT = "┓"
    HEAVY_CORNER_BOTTOM_LEFT = "┗"
    HEAVY_CORNER_BOTTOM_RIGHT = "┛"

    HEAVY_CROSS = "╋"

    # Box Drawing - Double
    DOUBLE_HORIZONTAL = "═"
    DOUBLE_VERTICAL = "║"

    DOUBLE_TEE_UP = "╦"
    DOUBLE_TEE_DOWN = "╩"
    DOUBLE_TEE_LEFT = "╠"
    DOUBLE_TEE_RIGHT = "╣"

    DOUBLE_CORNER_TOP_LEFT = "╔"
    DOUBLE_CORNER_TOP_RIGHT = "╗"
    DOUBLE_CORNER_BOTTOM_LEFT = "╚"
    DOUBLE_CORNER_BOTTOM_RIGHT = "╝"

    DOUBLE_CROSS = "╬"

    # Box Drawing - Rounded
    ROUND_HORIZONTAL = "─"
    ROUND_VERTICAL = "│"

    ROUND_TEE_UP = "┬"
    ROUND_TEE_DOWN = "┴"
    ROUND_TEE_LEFT = "├"
    ROUND_TEE_RIGHT = "┤"

    ROUND_CORNER_TOP_LEFT = "╭"
    ROUND_CORNER_TOP_RIGHT = "╮"
    ROUND_CORNER_BOTTOM_LEFT = "╰"
    ROUND_CORNER_BOTTOM_RIGHT = "╯"

    # Box Drawing - Double
    ASCII_HORIZONTAL = "-"
    ASCII_VERTICAL = "|"

    ASCII_TEE_UP = "+"
    ASCII_TEE_DOWN = "+"
    ASCII_TEE_LEFT = "+"
    ASCII_TEE_RIGHT = "+"

    ASCII_CORNER_TOP_LEFT = "+"
    ASCII_CORNER_TOP_RIGHT = "+"
    ASCII_CORNER_BOTTOM_LEFT = "+"
    ASCII_CORNER_BOTTOM_RIGHT = "+"

    ASCII_CROSS = "+"


@final
class PresetBorder(Enum):


    SINGLE = (
        "─",
        "│",
        "┌",
        "┐",
        "└",
        "┘"
    )
    DOUBLE = (
        "═",
        "║",
        "╔",
        "╗",
        "╚",
        "╝"
    )
    HEAVY = (
        "━",
        "┃",
        "┏",
        "┓",
        "┗",
        "┛"
    )
    ROUNDED = (
        "─",
        "│",
        "╭",
        "╮",
        "╰",
        "╯"
    )
    ASCII = (
        "-",
        "|",
        "+",
        "+",
        "+",
        "+"
    )


@final
class PresetSpinner(Enum):


    LINE = (
        "-",
        "\\",
        "|",
        "/"
    )
    DOTS = (
        ".  ",
        ".. ",
        "...",
        " ..",
        "  .",
        "   "
    )
    BRAILLE = (
        "⠋",
        "⠙",
        "⠹",
        "⠸",
        "⠼",
        "⠴",
        "⠦",
        "⠧",
        "⠇",
        "⠏"
    )
    BLOCK = (
        "▖",
        "▘",
        "▝",
        "▗"
    )


@final
class PresetProgress(Enum):


    BLOCK = (
        "█",
        "░"
    )
    ASCII = (
        "=",
        "-"
    )
    ARROW = (
        ">",
        "-"
    )
    DOT = (
        "●",
        "○"
    )


__all__ = [
    'PresetColor',
    'PresetSymbol',
    'PresetBox',
    'PresetBorder',
    'PresetSpinner',
    'PresetProgress',
]
