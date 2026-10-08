# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : progress.py
#
# Author       : Jarjarbin06
# ============================================================================


from numbers import Real

from jarbin_toolkit_console.enums import PresetProgress
from jarbin_toolkit_console.text import Text


class Progress:


    def __init__(
            self,
            *,
            minimum = 0,
            maximum = 100,
            value = 0,
        ):

        if maximum <= minimum:
            raise ValueError(
                "Maximum must be greater than minimum"
            )

        self._minimum = minimum
        self._maximum = maximum
        self._value = value

        self._validate_value(value)


    def _validate_value(
            self,
            value,
        ):

        if not isinstance(value, Real) or isinstance(value, bool):
            raise TypeError("Progress value must be a number")

        if value < self._minimum or value > self._maximum:
            raise ValueError("Progress value out of range")


    @property
    def value(
            self,
        ):

        return self._value


    @property
    def minimum(
            self,
        ):

        return self._minimum


    @property
    def maximum(
            self,
        ):

        return self._maximum


    @property
    def percentage(
            self,
        ):

        return (
            (self._value - self._minimum)
            / (self._maximum - self._minimum)
            * 100
        )


    @property
    def finished(
            self,
        ):

        return self._value >= self._maximum


    def set(
            self,
            value,
        ):

        self._validate_value(value)

        self._value = value


    def increment(
            self,
            amount = 1,
        ):

        self.set(self._value + amount)


    def decrement(
            self,
            amount = 1,
        ):

        self.set(self._value - amount)


    def reset(
            self,
        ):

        self._value = self._minimum


class ProgressRenderer:


    def __init__(
            self,
            *,
            width = 20,
            preset = PresetProgress.BLOCK,
            filled = None,
            empty = None,
            show_percentage = True,
        ):

        if width <= 0:
            raise ValueError("Width must be greater than zero")

        if filled is not None or empty is not None:

            if filled is None or empty is None:
                raise ValueError(
                    "Both filled and empty must be provided"
                )

        else:
            if not isinstance(preset, PresetProgress):
                raise TypeError(
                    "Preset must be a PresetProgress"
                )

            filled, empty = preset.value

        self._width = width
        self._filled = filled
        self._empty = empty
        self._show_percentage = show_percentage


    @property
    def width(
            self,
        ):

        return self._width


    def set_width(
            self,
            width,
        ):

        if width <= 0:
            raise ValueError("Width must be greater than zero")

        self._width = width


    def render(
            self,
            progress,
        ):

        if not isinstance(progress, Progress):
            raise TypeError("Progress must be a Progress")

        filled = round(
            progress.percentage / 100 * self._width
        )

        empty = self._width - filled

        result = (
            f"[{self._filled * filled}"
            f"{self._empty * empty}]"
        )

        if self._show_percentage:
            result += f" {progress.percentage:.0f}%"

        return Text(result)


__all__ = [
    'Progress',
    'ProgressRenderer',
]
