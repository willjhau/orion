class DataMap:
    """
    Stores the data local to a particular proccess

    Attributes:
        __data: A dictionary of the data
        __parent: The parent of the data map
    
    Data Format:
        'type': The type of the data
        'value': The value of the data
    """
    def __init__(self):
        """
        Constructor for the data map, takes no arguments
        """
        self.__data = {}
        self.__parent = None
    
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

    def getParent(self):
        """
        Returns the parent of the data map
        """

        return self.__parent

    def checkParent(self):
        """
        Checks if the data map has a parent
        """

        return self.__parent != None
    
    def setParent(self, parent):
        """
        parent: DataMap -> None

        Sets the parent of the data map
        """

        self.__parent = parent