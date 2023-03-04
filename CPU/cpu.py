# cpu.py

from instruction import *
from rom.rom import ROM

class CPU:
    def __init__(self):
        self.registers = []
        self.rom = None
        self.running = False
        self.pc = None
        self.instruction_mapping = instruction_mapping
    
    def run_rom(self, rom: ROM):
        self.rom = rom
        self.pc = self.rom.header_size

        self.running = True
        while self.running:
            identifier_byte = self.rom.get_byte(self.pc)
            instruction_class = self.instruction_mapping.get(identifier_byte, None)
           
            if instruction_class is not None: 
                instruction = instruction_class
                instruction.set(identifier_byte)
                instruction.execute()
            else:
                pass
                # print('not config:')

    def process_instructions(self, instruction: Instruction):
        instruction.process()
    
    def process_instructions(self):
        pass