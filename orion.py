import sys
import os
from src.exceptions import AddressError
from src.instructionMemory import InstructionMemory
from src.labelMap import LabelMap
from src.programCounter import ProgramCounter
from src.codeFile import CodeFile
from src.preprocessor import Preprocessor
from src.codeParser import CodeParser
# from src.linker import Linker

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

print(1)
if __name__ == "__main__":
    print(0)
    if len(sys.argv) != 2:
        print("Usage: python3 orion.py <filename>")
        sys.exit(1)
    
    path = sys.argv[1]
    if not validate_orion_file(path):
        print("Invalid file")
        sys.exit(1)
    
    file = CodeFile()
    file.readFromFile(path)

    preprocessor = Preprocessor(file)
    code = preprocessor.getCode()

    parser = CodeParser(code)
    code = parser.getCode()

    linker = Linker(code)
    IM = linker.getInstructionMemory()
    LM = linker.getLabelMap()

    print(IM)
    print(LM)

