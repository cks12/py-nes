# instruction.py
from typing import Dict
from .base import instruction_base

class lda_instruction(instruction_base):
    def __init__(self):
        super().__init__()
        self.instruction_length = 1
        self.identifier_byte = bytes.fromhex('78')

    def execute(self):
        self.process()
    
class sei_instruction(instruction_base):
    def __init__(self):
        super().__init__()
        self.instruction_length = 1
        self.identifier_byte = bytes.fromhex('D8')

    def execute(self):
        self.process()
        self.register.status.I = True

class cld_instruction(instruction_base):
    def __init__(self):
        super().__init__()
        self.instruction_length = 1
        self.identifier_byte = bytes.fromhex('A9')
    
    def execute(self):
        self.process()
        self.register.status.D = True

