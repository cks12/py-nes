# cpu.py

from instruction import *
from rom.rom import ROM
from .registers import Register

class CPU:
    def __init__(self):

        self.registers = []
        self.rom = None
        self.running = False
        self.instruction_mapping = instruction_mapping
        self.cpu_registers = Register()

    def run_rom(self, rom: ROM):

        self.rom = rom
        self.cpu_registers.PC = self.rom.header_size
        self.running = True
        self.cpu_registers.start()

        while self.running:
            self.process_instructions()
                
    def process_instructions(self):

        # Get byte in rom and find corresponding instruction
        identifier_byte = self.rom.get_bytes(self.cpu_registers.PC)
        instruction_class = self.instruction_mapping.get(identifier_byte, None)
           
        if instruction_class is None: 
            self.cpu_registers.add_program_counter(1)
            return 

        # get instruction
        instruction = instruction_class

        # rom bytes
        num_data_bytes: int = instruction.instruction_length - 1
        data_bytes = self.rom.get_bytes(self.cpu_registers.PC + 1, num_data_bytes)

        # instructions sets

        instruction.set_data_bytes(data_bytes)
        instruction.set_identifier_byte(identifier_byte)
        instruction.set_register(self.cpu_registers)
        
        instruction.execute()

        self.cpu_registers.add_program_counter(instruction.instruction_length)