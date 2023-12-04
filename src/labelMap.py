class LabelMap:
    """
    Class for the label map, maps labels to addresses

    This class controls jumps and branches around the program
    """
    def __init__(self):
        """
        Constructor for the label map, takes no arguments
        """
        self.__labels = {}
    
    def addLabel(self, label, address):
        """
        label: string, address: int -> None
        """
        self.__labels[label] = address
    
    def getAddressFromLabel(self, label):
        """
        label: string -> int

        Returns the address of a label
        """
        return self.__labels[label]