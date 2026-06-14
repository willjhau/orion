from .exceptions import IndexOutOfBoundsError, IllegalTypeError
from .oDataTypes import oData, oDataType


class oDataStructure(oData):
    def __init__(self):
        pass


class oArray(oDataStructure):
    """
    A dynamically-typed fixed-size array for the Orion language.

    Elements may be any oDataType instance (or None for uninitialized slots).
    The array size is fixed at creation time.
    """

    typeName = "oArray"

    def __init__(self, size: int):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Array size must be a positive integer")
        self.__size = size
        self.__data = [None] * size

    # ── Static helpers expected by DataMap ────────────────────────

    @staticmethod
    def isValid(value):
        """Accept oArray instances and None (uninitialized)."""
        return isinstance(value, oArray) or value is None

    # ── Accessors ─────────────────────────────────────────────────

    def getSize(self):
        return self.__size

    def getElement(self, index: int):
        if not isinstance(index, int):
            raise TypeError(f"Array index must be an integer, got {type(index)}")
        if not (0 <= index < self.__size):
            raise IndexOutOfBoundsError(
                f"Index {index} out of bounds for array of size {self.__size}")
        return self.__data[index]

    def setElement(self, index: int, value):
        if not isinstance(index, int):
            raise TypeError(f"Array index must be an integer, got {type(index)}")
        if not (0 <= index < self.__size):
            raise IndexOutOfBoundsError(
                f"Index {index} out of bounds for array of size {self.__size}")
        if value is not None and not isinstance(value, oDataType):
            raise IllegalTypeError(
                f"Array elements must be oDataType instances, got {type(value)}")
        self.__data[index] = value

    def getData(self):
        return list(self.__data)

    def __repr__(self):
        return f'oArray(size={self.__size}, data={self.__data})'
