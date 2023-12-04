import sys
import os
from src.exceptions import AddressError

def validate_filename(filename):
    """
    filename: string -> boolean
    Checks if the filename has the correct extension

    """
    if filename.endswith('.orion'):
        return True
    return False

def validate_path(path):
    """
    path: string -> boolean
    Checks if the path exists
    """
    if os.path.exists(path):
        return True
    return False

def validate_orion_file(path):
    """
    path: string -> boolean
    Checks if the  whole file and path is valid
    """
    if validate_path(path) and validate_filename(path):
        return True
    return False

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
        self__pc += 1
    
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

# Define a class for the instruction memory
class InstructionMemory:
    """
    Data structure mapping the addresses of instructions to the instructions themselves
    """
    def __init__(self, path):
        self.__instructions = []
        self.__path = path
        self.__pc = ProgramCounter()

    # When instructions are parsed, they are added to the instruction memory
    def addInstruction(self, instruction):
        """
        Adds an instruction to the instruction memory
        """
        self.__instructions.append(instruction)
    
    # Retrieves the instruction at the current program counter
    def getCurrentInstruction(self):
        return self.__instructions[self.__pc]
    
    # Adds 1 to the program counter
    def incrementCounter(self):
        self.__pc.increment()
    
    # Sets the program counter to a specific address
    def jumpTo(self, address):
        # check if the address is valid
        if address < len(self.__instructions):
            # Raise an AddressError
            raise AddressError("Jump address out of range")

        self.__pc.jump(address)