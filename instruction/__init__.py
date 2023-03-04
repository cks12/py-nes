from .instruction import *
from .base import InstructionBase
instructionList = [
    LDAInstruction,
    SEIInstruction,
    CLDInstruction
]
instruction_mapping: Dict[bytes, InstructionBase] = {}


for instruction_class in instructionList:
    instruction = instruction_class()
    instruction_mapping[instruction.identifier_byte] = instruction