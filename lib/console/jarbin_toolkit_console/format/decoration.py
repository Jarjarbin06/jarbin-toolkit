# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : decoration.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.format.enums import FormatOrder
from jarbin_toolkit_console.enums import PresetSymbol


class Decoration:


    def _get_decoration_text(
            self,
            decoration,
        ):

        if not getattr(self, "_can_format", False):
            return self

        return self.__class__("".join(map(str, decoration)))


    def f_decoration_prefix(
            self,
            prefix,
        ):

        return self._get_decoration_text(f"{prefix}{self}")


    def f_decoration_suffix(
            self,
            suffix,
        ):

        return self._get_decoration_text(f"{self}{suffix}")


    def f_decoration_wrap(
            self,
            prefix,
            suffix,
        ):

        return self._get_decoration_text(f"{prefix}{self}{suffix}")


    def f_decoration_brackets(
            self,
        ):

        return self.f_decoration_wrap("[", "]")


    def f_decoration_parentheses(
            self,
        ):

        return self.f_decoration_wrap("(", ")")


    def f_decoration_braces(
            self,
        ):

        return self.f_decoration_wrap("{", "}")


    def f_decoration_quotes(
            self,
        ):

        return self.f_decoration_wrap('"', '"')


    def f_decoration_backticks(
            self,
        ):

        return self.f_decoration_wrap("'", "'")


    def f_decoration_angle_brackets(
            self,
        ):

        return self.f_decoration_wrap("<", ">")


    def f_decoration_separator(
            self,
            *,
            fill = "─",
            width = None,
        ):

        return self._get_decoration_text(f"{fill * (width or len(self))}")


    def f_decoration_symbol(
            self,
            symbol,
            *,
            order = FormatOrder.BEFORE,
        ):

        if order == FormatOrder.BEFORE:
            return self._get_decoration_text(f"{symbol} {self}")

        elif order == FormatOrder.AFTER:
            return self._get_decoration_text(f"{self} {symbol}")

        return self


    def f_decoration_check(
            self,
            *,
            order = FormatOrder.BEFORE,
        ):

        return self.f_decoration_symbol(PresetSymbol.CHECK, order=order)


    def f_decoration_cross(
            self,
            *,
            order = FormatOrder.BEFORE,
        ):

        return self.f_decoration_symbol(PresetSymbol.CROSS, order=order)


    def f_decoration_warning(
            self,
            *,
            order = FormatOrder.BEFORE,
        ):

        return self.f_decoration_symbol(PresetSymbol.WARNING, order=order)


    def f_decoration_info(
            self,
            *,
            order = FormatOrder.BEFORE,
        ):

        return self.f_decoration_symbol(PresetSymbol.INFO, order=order)


    def f_decoration_question(
            self,
            *,
            order = FormatOrder.BEFORE,
        ):

        return self.f_decoration_symbol(PresetSymbol.QUESTION, order=order)


    def f_decoration_arrow(
            self,
            *,
            order = FormatOrder.BEFORE,
        ):

        return self.f_decoration_symbol(PresetSymbol.ARROW, order=order)


    def f_decoration_star(
            self,
            *,
            order = FormatOrder.BEFORE,
        ):

        return self.f_decoration_symbol(PresetSymbol.STAR, order=order)


    def f_decoration_ellipsis(
            self,
            *,
            order = FormatOrder.BEFORE,
        ):

        return self.f_decoration_symbol(PresetSymbol.ELLIPSIS, order=order)
