from .instruction import *
from .typing import Instruction
instructionList = [
    LDAInstruction,
    SEIInstruction,
    CLDInstruction
]
instruction_mapping: Dict[bytes, Instruction] = {}


for instruction_class in instructionList:
    instruction = instruction_class
    instruction_mapping[instruction.identifier_byte] = instruction