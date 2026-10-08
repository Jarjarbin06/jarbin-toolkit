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
__github__ = "https://github.com/Jarjarbin06/jarbin-toolkit"


import jarbin_toolkit_console.ansi as ANSI

from jarbin_toolkit_console.text import Text

import jarbin_toolkit_console.format as Format

import jarbin_toolkit_console.console as Console

import jarbin_toolkit_console.animation as Animation

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

from jarbin_toolkit_console.error import ConsoleJError

from jarbin_toolkit_console.color import Color as _Color


print = Console.Console.print


def _banner(
    ):

    from time import sleep

    BANNER_WIDTH = 60  #Set to custom width

    line = (
        Text(PresetBox.LIGHT_HORIZONTAL * BANNER_WIDTH)
        .f_color_foreground(PresetColor.SECONDARY.value)
    )

    title = (
        Text("Jarbin-ToolKit")
        .f_layout_align_center(BANNER_WIDTH)
        .f_style_bold()
        .f_color_foreground(PresetColor.PRIMARY.value)
    )

    subtitle = (
        Text("console")
        .f_layout_align_center(BANNER_WIDTH)
        .f_style_faint()
        .f_style_italic()
        .f_color_foreground(PresetColor.SECONDARY.value)
    )

    description = (
        Text(
            "A Python toolkit for rich and interactive terminals."
        )
        .f_layout_align_center(BANNER_WIDTH)
        .f_style_italic()
        .f_color_foreground(PresetColor.FOREGROUND.value)
    )

    features = (
        Text(
            "Text • Format • Color • ANSI • Console • Animation"
        )
        .f_layout_align_center(BANNER_WIDTH)
        .f_color_foreground(PresetColor.FOREGROUND.value)
    )

    features_2 = (
        Text(
            "Progress • Input / Output • Layout"
        )
        .f_layout_align_center(BANNER_WIDTH)
        .f_color_foreground(PresetColor.FOREGROUND.value)
    )

    version = (
        Text(f"v{__version__}")
        .f_layout_align_center(BANNER_WIDTH)
        .f_style_bold()
        .f_color_foreground(PresetColor.PRIMARY.value)
    )

    github = (
        Text("github.com/Jarjarbin06/jarbin-toolkit")
        .f_layout_align_center(BANNER_WIDTH)
        .f_layout_hyperlink(link=__github__)
        .f_color_foreground(PresetColor.SECONDARY.value)
    )

    final_banner = (
        line
        + "\n\n"
        + title
        + "\n"
        + subtitle
        + "\n\n"
        + description
        + "\n\n\n"
        + features
        + "\n"
        + features_2
        + "\n\n"
        + version
        + "\n"
        + github
        + "\n\n"
        + line
    )

    print(final_banner)

    sleep(1)


if True:  #Set to 'False' to disable banner
    _banner()


__all__ = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',
    '__github__',

    'ANSI',

    'Text',

    'Format',

    'Console',

    'Animation',

    'Color256',
    'ColorRGB',
    'ColorHEX',

    'PresetSymbol',
    'PresetBorder',
    'PresetColor',
    'PresetBox',
    'PresetProgress',
    'PresetSpinner',

    'ConsoleJError',

    'print',

    '_Color',
]
