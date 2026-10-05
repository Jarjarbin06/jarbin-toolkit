# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import StrEnum
from typing import final


@final
class FormatPaddingPosition(StrEnum):


    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


@final
class FormatAlignPosition(StrEnum):


    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
