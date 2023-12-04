class dataType:
    """
    Generic data type class
    """
    
    @staticmethod
    def isValid(value):
        """
        value: any -> bool

        Returns whether or not the value is valid for the data type
        """
        return False

class oInt(dataType):
    """
    Data type for Orion integers
    """

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

class oFloat(dataType):
    """
    Data type for Orion floats
    """

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
    
class oString(dataType):
    """
    Data type for Orion strings
    """

    @staticmethod
    def isValid(value):
        """
        value: any -> bool

        Returns whether or not the value is a string
        """
        if type(value) == str:
            return True
        return False
    
class oBool(dataType):
    """
    Data type for Orion booleans
    """

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
    
class oChar(dataType):
    """
    Data type for Orion characters
    """

    @staticmethod
    def isValid(value):
        """
        value: any -> bool

        Returns whether or not the value is a character
        """
        if type(value) == str and len(value) == 1:
            return True
        return False
        
