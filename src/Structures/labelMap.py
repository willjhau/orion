from ..LangData.exceptions import LabelNameError

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
        # Check if the label already exists
        if label in self.__labels:
            raise LabelNameError(f"Label `{label}` already exists")
        self.__labels[label] = address
    
    def getAddressFromLabel(self, label):
        """
        label: string -> int

        Returns the address of a label
        """
        return self.__labels[label]

    def printLabels(self):
        """
        Prints all the labels
        """
        for label, address in self.__labels.items():
            print(f"{label}: {address}")

    def __repr__(self):
        for label, address in self.__labels.items():
            print(f"{label}: {address}")

    def __str__(self):
        return self.__labels