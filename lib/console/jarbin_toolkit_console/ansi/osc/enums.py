# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/OSC
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import StrEnum
from typing import final


@final
class OSCClipboardSelection(StrEnum):


    CLIPBOARD = "c"
    PRIMARY = "p"
    SECONDARY = "q"
    SELECT = "s"
    CUT_BUFFER_0 = "0"
    CUT_BUFFER_1 = "1"
    CUT_BUFFER_2 = "2"
    CUT_BUFFER_3 = "3"
    CUT_BUFFER_4 = "4"
    CUT_BUFFER_5 = "5"
    CUT_BUFFER_6 = "6"
    CUT_BUFFER_7 = "7"


__all__ = [
    'OSCClipboardSelection',
]
