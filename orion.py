import sys
import os
from src.LangData.exceptions import AddressError
from src.Structures.instructionMemory import InstructionMemory
from src.Structures.labelMap import LabelMap
from src.Structures.programCounter import ProgramCounter
from src.Structures.codeFile import CodeFile
from src.Processing.preprocessor import Preprocessor
from src.Processing.codeParser import CodeParser
from src.Processing.linker import Linker
from src.Processing.interpreter import Interpreter

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

if __name__ == "__main__":
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
    code = parser.getCodeFile()

    linker = Linker(code.getCodeTrees(), path)

    IM = linker.getInstructionMemory()
    LM = linker.getLabelMap()

    # IM.printInstructions()
    # LM.printLabels()

    interpreter = Interpreter(IM, LM)
    interpreter.run()

