from CPU.registers import Register
class instruction_base():
    def __init__(self):
        self.identifier_byte = None
        self.instruction_length = 1
        self.register = None
        self.data_bytes = None

    def set_data_bytes(self, data_bytes):
        self.data_bytes = data_bytes

    def set_identifier_byte(self, byte:bytes):    
        self.identifier_byte

    def set_register(self, register: Register):
        self.register = register
    

    def execute(self):
        raise NotImplementedError()

    def process(self):
        print ("Identifier byte: {}".format(self.identifier_byte.hex()))