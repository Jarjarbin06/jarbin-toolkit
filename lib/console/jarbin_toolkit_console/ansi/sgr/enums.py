# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import StrEnum
from typing import final


@final
class SGRAttribute(StrEnum):


    BOLD = "1"
    FAINT = "2"
    ITALIC = "3"
    UNDERLINE = "4"
    SLOW_BLINK = "5"
    FAST_BLINK = "6"
    REVERSE = "7"
    HIDE = "8"
    STRIKETHROUGH = "9"
    GOTHIC = "20"
    DOUBLE_UNDERLINE = "21"
    PROPORTIONAL_SPACING = "26"


@final
class SGRAdvancedUnderline(StrEnum):


    NO = "4:0"
    SINGLE = "4:1"
    DOUBLE = "4:2"
    WAVY = "4:3"
    DOTTED = "4:4"
    DASHED = "4:5"


@final
class SGRFont(StrEnum):


    DEFAULT = "10"
    ALT_1 = "11"
    ALT_2 = "12"
    ALT_3 = "13"
    ALT_4 = "14"
    ALT_5 = "15"
    ALT_6 = "16"
    ALT_7 = "17"
    ALT_8 = "18"
    ALT_9 = "19"


@final
class SGRReset(StrEnum):


    ALL = "0"
    BOLD = "22"
    FAINT = "22"
    ITALIC = "23"
    GOTHIC = "23"
    UNDERLINE = "24"
    BLINK = "25"
    REVERSE = "27"
    HIDE = "28"
    STRIKETHROUGH = "29"
    FOREGROUND_COLOR = "39"
    BACKGROUND_COLOR = "49"
    PROPORTIONAL_SPACING = "50"
    FRAMED = "54"
    ENCIRCLE = "54"
    OVERLINE = "55"
    UNDERLINE_COLOR = "59"
    IDEOGRAM = "65"


@final
class SGRStandardColorForeground(StrEnum):


    BLACK = "30"
    RED = "31"
    GREEN = "32"
    YELLOW = "33"
    BLUE = "34"
    MAGENTA = "35"
    CYAN = "36"
    WHITE = "37"


@final
class SGRStandardColorBackground(StrEnum):


    BLACK = "40"
    RED = "41"
    GREEN = "42"
    YELLOW = "43"
    BLUE = "44"
    MAGENTA = "45"
    CYAN = "46"
    WHITE = "47"


@final
class SGRStandardColorForegroundBright(StrEnum):


    BLACK = "90"
    RED = "91"
    GREEN = "92"
    YELLOW = "93"
    BLUE = "94"
    MAGENTA = "95"
    CYAN = "96"
    WHITE = "97"


@final
class SGRStandardColorBackgroundBright(StrEnum):


    BLACK = "100"
    RED = "101"
    GREEN = "102"
    YELLOW = "103"
    BLUE = "104"
    MAGENTA = "105"
    CYAN = "106"
    WHITE = "107"


@final
class SGRDecoration(StrEnum):


    FRAME = "51"
    ENCIRCLE = "52"
    OVERLINE = "53"


@final
class SGRIdeogram(StrEnum):


    UNDERLINE = "60"
    DOUBLE_UNDERLINE = "61"
    OVERLINE = "62"
    DOUBLE_OVERLINE = "63"
    STRESS = "64"


@final
class SGRPosition(StrEnum):


    SUPERSCRIPT = "73"
    SUBSCRIPT = "74"
    NORMAL = "75"


@final
class SGRColorExtender(StrEnum):


    FOREGROUND = "38"
    BACKGROUND = "48"
    UNDERLINE = "58"


@final
class SGRColorMode(StrEnum):


    RGB = "2"
    INDEXED = "5"


__all__ = [
    'SGRAttribute',
    'SGRAdvancedUnderline',
    'SGRFont',
    'SGRReset',
    'SGRStandardColorForeground',
    'SGRStandardColorBackground',
    'SGRStandardColorForegroundBright',
    'SGRStandardColorBackgroundBright',
    'SGRDecoration',
    'SGRIdeogram',
    'SGRPosition',
    'SGRColorExtender',
    'SGRColorMode',
]
