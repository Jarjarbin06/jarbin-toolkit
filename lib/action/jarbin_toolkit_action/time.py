# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : time.py
# Class        : ActionTimer
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_time import StopWatch


class ActionTimer(StopWatch):


    def elapsed(
            self,
        ):

        return super().elapsed(auto_update=False)



__all__ = [
    'ActionTimer',
]
