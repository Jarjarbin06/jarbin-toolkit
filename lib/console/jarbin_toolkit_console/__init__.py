# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


__author__ = 'Nathan Jarjarbin'
__email__ = 'nathan.amaraggi@epitech.eu'
__version__ = "1.0.0.0"
__license__ = "GPL"


import jarbin_toolkit_console.ansi as ANSI

from jarbin_toolkit_console.text import Text

from jarbin_toolkit_console.console import Console

import jarbin_toolkit_console.format as Format

from jarbin_toolkit_console.color import (
    Color256,
    ColorRGB,
    ColorHEX,
)

from jarbin_toolkit_console.enums import (
    PresetSymbol,
    PresetBorder,
    PresetColor,
    PresetBox,
    PresetProgress,
    PresetSpinner,
)

import jarbin_toolkit_console.console as _Console

from jarbin_toolkit_console.color import Color as _Color


__all__ = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',

    'ANSI',

    'Text',

    'Console',

    'Format',

    'Color256',
    'ColorRGB',
    'ColorHEX',

    'PresetSymbol',
    'PresetBorder',
    'PresetColor',
    'PresetBox',
    'PresetProgress',
    'PresetSpinner',

    '_Color',
    '_Console',

]
