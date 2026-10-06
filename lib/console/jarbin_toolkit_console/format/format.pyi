class Format():


    _can_format: bool = True
    _sgr: object = None
    _cursor: object = None


    @classmethod
    def _get_sgr(
            cls,
        ) -> object:
        ...


    @classmethod
    def _get_cursor(
            cls,
        ) -> object:
        ...


__all__: list[str]
