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

    def get_bytes(self, PC, size = 1) -> bytes:
        byte = self.rom_bytes[PC:PC + size]
        return byte
