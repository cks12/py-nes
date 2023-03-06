# Register.py
from .status import CPUStatus

class Register:
    def __init__(self):

        self.status = CPUStatus()

        # status registers 
        self.PC = None # PROGRAM COUNTER
        self.SP = None # Stack Pointer
        self.P = None # STATUS REGISTER

        # data registers
        self.X = None # X INDICE REGISTER 
        self.Y = None # Y INDICE REGISTER
        self.A = None # CPU ACCUMULATOR

    def add_program_counter(self, instructionLength: int):
        self.PC += instructionLength

    def start(self):
        # self.old_status = bytes.fromhex('34')
        
        # data default registers default
        self.X = bytes.fromhex("00")
        self.Y = bytes.fromhex("00") 
        self.A = bytes.fromhex("00")

        self.SP = bytes.fromhex('FD')