class CPUStatus:
    def __init__(self):
        self.C = False  # Carry
        self.Z = False  # Zero
        self.I = False  # Interrupt
        self.D = False  # Decimal Mode
        self.B = False  # Break Command
        self.U = True   # Unused
        self.V = False  # Overflow
        self.N = False  # Negative

def status_from_byte(byte):
    status = CPUStatus()
    status.C = bool(byte & 0b00000001)
    status.Z = bool(byte & 0b00000010)
    status.I = bool(byte & 0b00000100)
    status.D = bool(byte & 0b00001000)
    status.B = bool(byte & 0b00010000)
    status.V = bool(byte & 0b01000000)
    status.N = bool(byte & 0b10000000)
    return status