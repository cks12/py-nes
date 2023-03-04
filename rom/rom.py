# rom.py
from typing import List

NUM_PRG_BLOCKS = 2
HEADER_SIZE = 16
KB_SIZE = 1024

class ROM(object):
    def __init__(self, rom_bytes: bytes):
        self.num_prg_blocks = NUM_PRG_BLOCKS
        self.header_size = HEADER_SIZE
        self.rom_bytes = rom_bytes
        self.pgr_bytes = rom_bytes[HEADER_SIZE:HEADER_SIZE + (16 * KB_SIZE * self.num_prg_blocks)]
        self.current_position = 0

    def get_byte(self, s) -> bytes:
        byte = self.pgr_bytes[self.current_position:self.current_position + 1]
        self.current_position += 1
        return byte
