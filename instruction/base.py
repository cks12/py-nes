class InstructionBase():
    def __init__(self):
        self.identifier_byte = None
        self.instruction_length = 1

    def set(self, byte:bytes):    
        self.identifier_byte

    def process(self):
        print ("Identifier byte: {}".format(self.identifier_byte.hex()))