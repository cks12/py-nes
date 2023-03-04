# main.py
NUM_PRG_BLOCKS = 2
HEADER_SIZE = 16

import argparse
from CPU.cpu import CPU
from rom.rom import ROM

def main():
    parser = argparse.ArgumentParser(description="NES Emulator.")
    parser.add_argument('room_path', metavar="r", type=str, help="path to nes room")
    args = parser.parse_args()

    print(args.room_path)

    with open(args.room_path, 'rb') as file:
        # Ignore the first 16 bytes (the header)
        file.seek(HEADER_SIZE)
        rom_bytes = file.read()

    cpu = CPU()
    rom = ROM(rom_bytes)
    cpu.run_rom(rom)

if __name__ == "__main__":
    main()