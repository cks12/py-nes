# instruction.py
from typing import Dict
from .typing import Instruction

class LDAInstruction(Instruction):
    identifier_byte = bytes.fromhex('78')
    instruction_length = 1
    def __init__(self):
        super().__init__()
    def execute(self):
        self.process()
    
class SEIInstruction(Instruction):
    identifier_byte = bytes.fromhex('D8')
    instruction_length = 1
    def __init__(self):
        super().__init__()

    def execute(self):
        self.process()

class CLDInstruction(Instruction):
    instruction_length = 1
    identifier_byte = bytes.fromhex('A9')
    def __init__(self):
        super().__init__()
    def execute(self):
        self.process()