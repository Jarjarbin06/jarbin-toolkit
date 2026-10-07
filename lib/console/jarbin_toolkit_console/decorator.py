# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console
# File         : decorator.py
#
# Author       : Jarjarbin06
# ============================================================================


class classproperty:


    def __init__(self, func):
        self.func = func


    def __get__(self, instance, owner):
        return self.func(owner)


    def __set__(self, instance, value):
        raise AttributeError("Can't set class property")


__all__ = [
    'classproperty',
]
