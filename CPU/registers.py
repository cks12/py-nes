# Register.py
class Register:
    def __init__(self):
        # status registers 
        self.PC = None
        self.SP = None
        self.P = None

        # data registers
        self.X = None
        self.Y = None
        self.A = None