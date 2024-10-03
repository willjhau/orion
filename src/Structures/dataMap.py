class DataMap:
    """
    Stores the data of a scope in a dictionary

    Attributes:
        __data: A dictionary of the data
    
    Data Format:
        'type': The type of the data
        'value': The value of the data
    """
    def __init__(self):
        """
        Constructor for the data map, takes no arguments
        """
        self.__data = {}

    def checkIfDataExists(self, name):
        if name in self.__data:
            return True
        else:
            return False
    
    def addData(self, name, dataType, value):
        """
        name: string, dataType: dataType, value: any -> None

        Adds data to the data map
        """

        # Check if the data already exists
        if name in self.__data:
            # Raise an error
            raise ValueError("Data already exists in data map") 

        # Check if the value is valid within the data type
        if not dataType.isValid(value):
            # Raise an error
            raise ValueError("Value is not valid for data type")

        self.__data[name] = {'type': dataType, 'value': value}

    def getData(self, name):
        """
        name: string -> any

        Returns the data with the given name
        """

        # Check if the data exists
        if name not in self.__data:
            # Raise an error
            raise NameError("Variable is not defined in the scope")

        return self.__data[name]['value']

    def setData(self, name, value):
        """
        name: string, value: any -> None

        Sets the value of the data with the given name
        """

        # Check if the data exists
        if name not in self.__data:
            # Raise an error
            raise NameError("Variable is not defined in the scope")

        # Check if the value is valid within the data type
        if not self.__data[name]['type'].isValid(value):
            # Raise an error
            raise ValueError("Value is not valid for data type")

        self.__data[name]['value'] = value
