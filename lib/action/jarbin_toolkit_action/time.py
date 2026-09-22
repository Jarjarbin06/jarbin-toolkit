# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : time.py
# Class        : ActionTimer
#
# Author       : Jarjarbin06
# ============================================================================


from typing import final

from jarbin_toolkit_time import StopWatch


@final
class ActionTimer(StopWatch):


    def elapsed(
            self,
        ):

        return super().elapsed(auto_update=False)



__all__ = [
    'ActionTimer',
]
