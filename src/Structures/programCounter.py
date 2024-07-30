class ProgramCounter:
    """
    Class for the program counter, tracks the current instruction
    """
    def __init__(self):
        """
        Constructor for the program counter, takes no arguments
        """
        self.__pc = 0
    
    def increment(self):
        """
        Increments the program counter by 1
        """
        self.__pc += 1
    
    def get(self):
        """
        Returns the current value of the program counter
        """
        return self.__pc

    def jump(self, address):
        """
        address: int -> None

        Modify the program counter to a specific address
        """
        self.__pc = address