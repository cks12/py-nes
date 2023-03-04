class Instruction():
    def __init__(self):
        pass
    def set(self, byte:bytes):    
        self.identifier_byte

    def process(self):
        print ("Identifier byte: {}".format(self.identifier_byte.hex()))