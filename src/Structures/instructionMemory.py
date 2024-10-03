from .programCounter import ProgramCounter
from ..LangData.exceptions import AddressError

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

        Exits the program if the program counter is out of range
        """
        if self.__pc.get() >= len(self.__instructions):
            exit()
        return self.__instructions[self.__pc.get()]
    
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
        if address >= len(self.__instructions):
            print(address)
            # Raise an AddressError
            raise AddressError("Jump address out of range")

        self.__pc.jump(address)
    
    def printInstructions(self):
        """
        Prints all the instructions
        """
        for i, instruction in enumerate(self.__instructions):
            print(f"{i}: {instruction}")

    def __repr__(self):
        for i, instruction in enumerate(self.__instructions):
            print(f"{i}: {instruction}")

    def __str__(self):
        return self.__instructions

