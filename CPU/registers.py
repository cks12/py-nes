# Register.py
class Register:
    def __init__(self):
        # status registers 
        self.PC = None # PROGRAM COUNTER
        self.SP = None # Stack Pointer
        self.P = None # STATUS REGISTER

        # data registers
        self.X = None # X INDICE REGISTER 
        self.Y = None # Y INDICE REGISTER
        self.A = None # CPU ACCUMULATOR
    
    def start(self):
        self.status = bytes.fromhex('34')
        
        # data default registers default
        self.X = bytes.fromhex("00")
        self.Y = bytes.fromhex("00") 
        self.A = bytes.fromhex("00")

        self.SP = bytes.fromhex('FD')