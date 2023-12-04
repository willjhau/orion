import sys
import os
from src.exceptions import AddressError
from src.instructionMemory import InstructionMemory
from src.labelMap import LabelMap
from src.programCounter import ProgramCounter

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

