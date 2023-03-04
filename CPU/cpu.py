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
            identifier_byte = self.rom.get_byte(self.cpu_registers.PC)
            instruction_class = self.instruction_mapping.get(identifier_byte, None)
           
            if instruction_class is not None: 
                instruction = instruction_class
                instruction.set(identifier_byte)
                instruction.execute()
            else:
                pass
                # print('not config:')

    def process_instructions(self, instruction: InstructionBase):
        instruction.process()
    
    def process_instructions(self):
        pass