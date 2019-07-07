from instruction import Instruction
from memory import Memory

class CPU:

    # There are 8 registers in this virtual CPU
    # Registers 0-5 (inclusive) are general purpose registers
    # Register 6 holds the program counter 
    # (the memory location of the next instruction)
    # Register 7 is always 0
    registers = [0] * 8

    # flag_negative is true if there is overflow when processing in execute
    # flag_zero is set to true if an instruction evaluates to 0 in execute
    flag_negative = False
    flag_zero = False

    # This simulates the memory in the virtual CPU
    _memory = None

    # This holds the instruction after it is decoded
    decoded_instr = None
    
    def __init__(self):
        pass

    def instr_fetch():
        pass

    def intr_decode():
        pass

    def execute():
        pass

    def mem():
        pass

    def writeback():
        pass

