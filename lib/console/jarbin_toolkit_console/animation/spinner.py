# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : spinner.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.animation.animation import Animation
from jarbin_toolkit_console.animation.enums import AnimationMode
from jarbin_toolkit_console.enums import PresetSpinner


class Spinner:


    @staticmethod
    def _create(
            preset,
            *,
            duration = 0.1,
            mode = AnimationMode.LOOP,
        ):

        return Animation(
            preset.value,
            duration=duration,
            mode=mode,
        )


    @staticmethod
    def line(
            *,
            duration = 0.1,
            mode = AnimationMode.LOOP,
        ):

        return Spinner._create(
            PresetSpinner.LINE,
            duration=duration,
            mode=mode,
        )


    @staticmethod
    def dot(
            *,
            duration = 0.15,
            mode = AnimationMode.LOOP,
        ):

        return Spinner._create(
            PresetSpinner.DOTS,
            duration=duration,
            mode=mode,
        )


    @staticmethod
    def braille(
            *,
            duration = 0.1,
            mode = AnimationMode.LOOP,
        ):

        return Spinner._create(
            PresetSpinner.BRAILLE,
            duration=duration,
            mode=mode,
        )


    @staticmethod
    def block(
            *,
            duration = 0.1,
            mode = AnimationMode.LOOP,
        ):

        return Spinner._create(
            PresetSpinner.BLOCK,
            duration=duration,
            mode=mode,
        )


__all__ = [
    'Spinner',
]
