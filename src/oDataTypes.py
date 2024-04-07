class oData:
    def __init__(self, name: str):
        pass


class oDataType(oData):
    """
    Generic data type class
    """

    def __init__(self, name):
        pass

    @staticmethod
    def isValid(value):
        """
        value: any -> bool

        Returns whether or not the value is valid for the data type
        """
        return False
    
    def getValue(self):
        """
        None -> any

        Getter for the value of an oDataType object
        Returns the integer value
        """
        return self.__value
    
    def setValue(self, value):
        """
        value: any -> None

        Setter for the value of an oDataType object
        """
        self.__value = value

class oInt(oDataType):
    """
    Data type for Orion integers
    """
    typeName = "oInt"

    def __init__(self, value: int):
        """
        value: int -> None

        oInt constructor
        """
        self.__value = value

    @staticmethod
    def isValid(value):
        """
        value: any -> bool

        Returns whether or not the value is an integer
        """
        try:
            if int(value) == value:
                return True
            return False
        except ValueError:
            return False

class oFloat(oDataType):
    """
    Data type for Orion floats
    """

    typeName = "oFloat"

    def __init__(self, value: float):
        self.value = value


    @staticmethod
    def isValid(value):
        """
        value: any -> bool

        Returns whether or not the value is a float
        """

        try:
            float(value)
        except ValueError:
            return False
        
        return True
    
    
class oString(oDataType):
    """
    Data type for Orion strings
    """

    typeName = "oString"

    def __init__(self, s: str):
        self.value = s


    @staticmethod
    def isValid(value):
        """
        value: any -> bool

        Returns whether or not the value is a string
        """
        if type(value) == str:
            return True
        return False
    

    """
    ADD STRING FUNCTIONALITY
    """
    
class oBool(oDataType):
    """
    Data type for Orion booleans
    """

    typeName = "oBool"

    def __init__(self, value:bool):
        self.value = value

    @staticmethod
    def isValid(value):
        """
        value: any -> bool

        Returns whether or not the value is a boolean
        """
        if type(value) == bool:
            return True
        elif value == "true" or value == "false":
            return True
        return False
    
class oChar(oDataType):
    """
    Data type for Orion characters
    """

    typeName = "oChar"

    def __init__(self, value):
        self.value = value

    @staticmethod
    def isValid(value):
        """
        value: any -> bool

        Returns whether or not the value is a character
        """
        if type(value) == str and len(value) == 1:
            return True
        return False
        
