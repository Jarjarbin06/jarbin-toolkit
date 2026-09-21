from typing import (
    final,
    Optional,
)


@final
class _EmptyField:
    """
        Singleton used to dissociate None from no-argument
    """


    _instance: Optional[_EmptyField]


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
        ...


EmptyField: _EmptyField


__all__: list[str]
