from programCounter import ProgramCounter
from exceptions import AddressError

class InstructionMemory:
    """
    Data structure mapping the addresses of instructions to the instructions themselves
    """
    def __init__(self, path):
        """
        path: string -> None

        Constructor for the instruction memory, takes a path to the file as an argument
        """
        self.__instructions = []
        self.__path = path
        self.__pc = ProgramCounter()

    def addInstruction(self, instruction):
        """
        Adds an instruction to the instruction memory
        """
        self.__instructions.append(instruction)
    
    def getCurrentInstruction(self):
        """
        Returns the instruction at the current program counter
        """
        return self.__instructions[self.__pc]
    
    def incrementCounter(self):
        """
        Increments the program counter by 1
        """
        self.__pc.increment()
    
    def jumpTo(self, address):
        """
        address: int -> None

        Sets the program counter to a specific address
        """
        if address < len(self.__instructions):
            # Raise an AddressError
            raise AddressError("Jump address out of range")

        self.__pc.jump(address)

