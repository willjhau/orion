from src.exceptions import *
from src.oDataTypes import *

class oDataStructure(oData):
    def __init__(self, name: str):
        pass


class oArray(oDataStructure):
    """
    Data structure class for Orion arrays
    """

    typeName = "oArray"

    def __init__(self, length: int, dataType: oDataType):
        """        
        length: int -> None

        Constructor for oArray data structure
    
        length must be a positive integer

        Attempting to create an array with a non-oDataType raises an IllegalTypeError
        """
        if not isinstance(dataType, oDataType):
            raise IllegalTypeError("oArray objects must contain oData")

        if not isinstance(length, int):
            raise TypeError("Length must be an integer")
        
        if length <= 0:
            raise ValueError("Length must be a positive integer")
            
        self.__dataType = oDataType
        self.__size = length
        self.__data = [None] * length

    def getDataType(self):
        """
        None -> oDataType

        Getter for the type of the oArray

        Returns the specific oDataType class
        """
        return self.__dataType
    
    def getSize(self):
        """
        None -> int

        Getter for the size of the array

        returns the size of the array
        """
        return self.__size
    
    def getData(self):
        """
        None -> oDataType[]

        Getter for the entire array data

        returns the data in a python list of oDataType instances
        """
        return self.__data
    
    def getElement(self, index: int):
        """
        index: int -> oData

        Returns the oDataType object at index [index] in the oArray

        Attempting to retrieve the index greater than or equal to the size of the array raises an IndexOutOfBoundsError

        Attempting to pass a type other than int as an index raises a TypeError
        """
        if not isinstance(index, int):
            raise TypeError(f"Parameter index: {index} must be an integer")
        
        if index >= self.getSize():
            raise IndexOutOfBoundsError(f"Parameter index: {index} out of bounds for array of size {self.getSize()}")
        
        if not(-self.getSize() > self.getSize()):
            raise IndexOutOfBoundsError(f"Parameter index: {index} out of bounds for array of size {self.getSize()}")
        
        return self.__data[index]
    
    def setElement(self, index: int, value: oData):
        """
        index, value: int -> oData -> None

        Sets the data at index [index] to the value [value]

        Attempting to set a value of an oDataType different to the defined one raises an ArrayTypeMismatchError
        """
        if not isinstance(index, int):
            raise TypeError("Array index must be an integer")

        if not (0 <= index < self.getSize()):
            raise IndexOutOfBoundsError(f"Parameter index: {index} out of bounds for array of size {self.getSize()}")

        if not isinstance(value, oData):
            raise IllegalTypeError("oArray objects must contain oData")
        
        if not isinstance(value, self.getDataType()):
            raise ArrayTypeMismatchError(f"Cannot add value: {value} to oArray of type: {self.getDataType.typeName}")
        
        self.__data[index] = value
