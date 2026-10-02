from .style import Style


class Format(Style):


    @classmethod
    def _get_sgr(
            cls,
        ) -> object:
        ...


    _can_format: bool = True
    _sgr: object = None
