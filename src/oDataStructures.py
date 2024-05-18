from exceptions import *
from oDataTypes import *

class oDataStructure(oData):
    def __init__(self, name: str):
        pass


class oArray(oDataStructure):
    """
    Data structure class for Orion arrays
    """

    typeName = "oArray"

    def __init__(self, data: list):
        """
        data: oDataType[] -> None
        
        Constructor for oArray data structure
    
        data argument should be a list of objects of a single oDataType.

        Inconsistent data types raise an ArrayTypeMismatchError

        Attempting to create an array with a non-oDataType raises an IllegalTypeError
        """
        dType = type(data[0])
        for element in data:
            if not (isinstance(element, oData)):
                raise IllegalTypeError("Only data of an oDataType can be used in an oArray")
            if not (type(element) == dType):
                raise ArrayTypeMismatchError("All elements of must be of the same type")
            
        self.__dataType = dType
        self.__size = len(data)
        self.__data = data

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
