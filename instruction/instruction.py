# instruction.py
from typing import Dict
from .base import InstructionBase

class LDAInstruction(InstructionBase):
    def __init__(self):
        super().__init__()
        self.instruction_length = 1
        self.identifier_byte = bytes.fromhex('78')
    def execute(self):
        self.process()
    
class SEIInstruction(InstructionBase):
    def __init__(self):
        super().__init__()
        self.instruction_length = 1
        self.identifier_byte = bytes.fromhex('D8')

    def execute(self):
        self.process()

class CLDInstruction(InstructionBase):
    def __init__(self):
        super().__init__()
        self.instruction_length = 1
        self.identifier_byte = bytes.fromhex('A9')
    def execute(self):
        self.process()

