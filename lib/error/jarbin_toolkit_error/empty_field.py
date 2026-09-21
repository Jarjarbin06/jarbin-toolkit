# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : empty_field.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import final


@final
class _EmptyField:


    _instance = None


    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


EmptyField = _EmptyField()

__all__ = [
    '_EmptyField',
    'EmptyField',
]