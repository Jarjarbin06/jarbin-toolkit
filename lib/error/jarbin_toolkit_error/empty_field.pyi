from typing import (
    final,
)

@final
class _EmptyField:
    """
        Singleton used to dissociate None from no-argument
    """


    _instance: _EmptyField | None


    def __new__(
            cls
        ) -> _EmptyField:
        """
            Create a new instance

            Returns
            ----------
            _EmptyField
                New instance
        """


EmptyField: _EmptyField


__all__: list[str] = [
    'EmptyField',
]
