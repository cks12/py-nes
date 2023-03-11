# instruction.py
from typing import Dict
from .base import instruction_base

# immediate	LDA #oper	A9	2	2 
class lda_immediate_instruction(instruction_base):
    def __init__(self):
        super().__init__()
        self.instruction_length = 2
        self.identifier_byte = bytes.fromhex('A9')

    def execute(self):
        self.process()
        self.register.A = self.data_bytes[0]
    
# implied	SEI	78	1	2  
class sei_instruction(instruction_base):
    def __init__(self):
        super().__init__()
        self.instruction_length = 1
        self.identifier_byte = bytes.fromhex('78')

    def execute(self):
        self.process()
        self.register.status.I = True

# implied	CLD	D8	1	2
class cld_instruction(instruction_base):
    def __init__(self):
        super().__init__()
        self.instruction_length = 1
        self.identifier_byte = bytes.fromhex('D8')
    
    def execute(self):
        self.process()
        self.register.status.D = True

# absolute	STA oper	8D	3	4  
class sta_abs_instruction(instruction_base):
    def __init__(self):
        super().__init__()
        self.instruction_length = 3
        self.identifier_byte = bytes.fromhex('8D')
    
    def execute(self):
        self.process()
        mem = self.data_bytes[1:2] + self.data_bytes[0:1]
        x = 1