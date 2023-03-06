from .instruction import *
from .base import instruction_base

instructionList = [
    lda_instruction,
    sei_instruction,
    cld_instruction
]
instruction_mapping: Dict[bytes, instruction_base] = {}


for instruction_class in instructionList:
    instruction = instruction_class()
    instruction_mapping[instruction.identifier_byte] = instruction