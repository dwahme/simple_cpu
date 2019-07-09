from instruction import Instruction
from memory import Memory

# Retrieves bits lo through hi (inclusive) from a given number
def get_bits(num, lo, hi):
    mask = ((1 << (hi - lo + 1)) - 1) << lo
    return (num & mask) >> lo

# Breaks up an instruction into its args, delimited by breaks
# Have to do some list reversal since we want to read it backwards
def bitwise_breakdown(num, breaks):
    res = []

    rev = [16 - x for x in breaks[::-1]]

    for idx, stop in enumerate(rev[1:]):
        start = rev[idx]
        res.append(get_bits(num, start, stop - 1))

    return res[::-1]


class CPU:

    # There are 8 registers in this virtual CPU
    # Registers 0-5 (inclusive) are general purpose registers
    # Register 6 holds the program counter 
    # (the memory location of the next instruction)
    # Register 7 is always 0
    registers = [0] * 8
    REG_PC = 6
    REG_ZERO = 7

    # flag_overflow is true if there is overflow when processing in execute
    # flag_zero is set to true if an instruction evaluates to 0 in execute
    flag_overflow = False
    flag_zero = False

    # This simulates the memory in the virtual CPU
    _memory = None

    # This holds the instruction
    encoded_instr = 0
    decoded_instr = None

    # This holds the result from either execute or a load instruction
    result = 0
    
    def __init__(self, memory):
        _memory = memory

    # The Instruction Fetch Stage
    # Gets the instruction pointed to in the program counter register
    def instr_fetch(self):
        # Get the next instruction
        self.encoded_instr = _memory.read(registers[REG_PC])

        # Update the program counter
        self.REG_PC += 1

    # The Instruction decode stage
    # Figures out what the instruction is and extracts the arguments
    def instr_decode(self):
        instr = Instruction()

        # Extract the op bits from the instruction
        op = bin(get_bits(instr.OP_MIN, instr.OP_MAX))
        
        # Arithmetic operators
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
        
        # MOV operators
        elif op == 0b0100:
            instr.op = "MOV"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 16])
        elif op == 0b0101:
            instr.op = "MOVR"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7, 10])
        
        # Memory operators
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
        
        # PC modifiers
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
        
        # Exit
        elif op == 0b1111:
            instr.op = "EXIT"
            instr.args = bitwise_breakdown(encoded_instr, [4, 7])

        self.decoded_instr = instr


    # Runs any computations that need to be made
    def execute(self):

        # For convenience
        instr = self.decoded_instr
        op = self.decoded_instr.op
        reg = self.registers
        
        # Arithmetic operators
        if op == "ADD":
            result = reg[instr.args[1]] + instr.args[2]
        elif op == "ADDR":
            result = reg[instr.args[1]] + reg[instr.args[2]]
        elif op == "SUB":
            result = instr.args[2] - reg[instr.args[1]]
        elif op == "SUBR":
            result = reg[instr.args[2]] - reg[instr.args[1]]

        # MOV operators, Memory operators, PC modifiers, Exit
        # No execution necessary

        # Check overflow and set flags
        self.result = result & 0xFF

        self.flag_overflow = (self.result != result)
        self.flag_zero = (self.result == 0)


    # Performs all memory operations
    def mem(self):

        # For convenience
        instr = self.decoded_instr
        op = self.decoded_instr.op
        reg = self.registers

        if op == "LOAD":
            self.result = self.mem.read(instr.args[1])
        elif op == "LOADR":
            self.result = self.mem.read(reg[instr.args[1]])
        elif op == "STORE":
            self.mem.write(reg[instr.args[0]], instr.args[0])
        elif op == "STORER":
            self.mem.write(reg[instr.args[0]], reg[instr.args[0]])

        # Arithmetic operators, MOV operators, PC modifiers, Exit
        # No memory updates necessary


    # Handles updating the registers
    def writeback(self):

        # For convenience
        instr = self.decoded_instr
        op = self.decoded_instr.op
        reg = self.registers

        if op in ["ADD", "ADDR", "SUB", "SUBR", "LOAD", "LOADR"]:
            reg[instr.args[0]] = self.result

        # No writeback necessary for STORE(R)
        
        elif op == "MOV":
            reg[instr.args[0]] = instr.args[1]
        elif op == "MOVR":
            reg[instr.args[0]] = reg[instr.args[1]]

        elif op == "JMP":
            reg[REG_PC] = reg[instr.args[0]]
        elif op == "JEQ":
            if flag_zero:
                reg[REG_PC] = reg[instr.args[0]]
        elif op == "JNEQ":
            if not flag_zero:
                reg[REG_PC] = reg[instr.args[0]]
        elif op == "JLT":
            if flag_overflow:
                reg[REG_PC] = reg[instr.args[0]]
        elif op == "JGT":
            if not flag_overflow:
                reg[REG_PC] = reg[instr.args[0]]
