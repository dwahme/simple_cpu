from instruction import Instruction
from memory import Memory

# Retrieves bits lo through hi (inclusive) from a given number
def get_bits(num, lo, hi):
    mask = ((1 << (hi - lo + 1)) - 1) << lo
    return (num & mask) >> lo

# Breaks up an instruction into its args, delimited by breaks
def bitwise_breakdown(num, breaks):
    res = []

    for idx, stop in enumerate(breaks[1:]):
        start = breaks[idx]
        res.append(get_bits(num, start, stop - 1))

    return res


class CPU:

    # There are 8 registers in this virtual CPU
    # Registers 0-5 (inclusive) are general purpose registers
    # Register 6 holds the program counter 
    # (the memory location of the next instruction)
    # Register 7 is always 0
    registers = [0] * 8
    REG_PC = 6
    REG_ZERO = 7

    # flag_negative is true if there is overflow when processing in execute
    # flag_zero is set to true if an instruction evaluates to 0 in execute
    flag_negative = False
    flag_zero = False

    # This simulates the memory in the virtual CPU
    _memory = None

    # This holds the instruction
    encoded_instr = 0
    decoded_instr = None
    
    def __init__(self, memory):
        _memory = memory

    # The Instruction Fetch Stage
    # Gets the instruction pointed to in the program counter register
    def instr_fetch(self):
        # Get the next instruction
        self.encoded_instr = _memory.read(registers[REG_PC])

        # Update the program counter
        self.REG_PC += 1

    def instr_decode(self):
        instr = Instruction()

        # Extract the op bits from the instruction
        op = bin(get_bits(instr.OP_MIN, instr.OP_MAX))
        
        if op == 0b0000:
            instr.op = "ADD"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 10, 16])

        elif op == 0b0001:
            instr.op = "ADDR"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 10, 13])
        
        elif op == 0b0010:
            instr.op = "SUB"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 10, 16])

        elif op == 0b0011:
            instr.op = "SUBR"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 10, 13])
        
        elif op == 0b0100:
            instr.op = "MOV"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 16])
        
        elif op == 0b0101:
            instr.op = "MOVR"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 10])
        
        elif op == 0b0110:
            instr.op = "LOAD"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 16])
        
        elif op == 0b0111:
            instr.op = "LOADR"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 10])
        
        elif op == 0b1000:
            instr.op = "STORE"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 16])
        
        elif op == 0b1001:
            instr.op = "STORER"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 10])
        
        elif op == 0b1010:
            instr.op = "JMP"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7])
        
        elif op == 0b1011:
            instr.op = "JEQ"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7])
        
        elif op == 0b1100:
            instr.op = "JNE"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7])
        
        elif op == 0b1101:
            instr.op = "JLT"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7])
        
        elif op == 0b1110:
            instr.op = "JGT"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7])
        
        elif op == 0b1111:
            instr.op = "EXIT"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7])

        self.decoded_instr = instr


    def execute(self):
        pass

    def mem(self):
        pass

    def writeback(self):
        pass
