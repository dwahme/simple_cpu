
This contains information about SAL (SIMPLE ASSEMBLY LANGUAGE), the assembly language in the virtual CPU.

All instructions are fixed-length 16 bit instructions. Unused bits are for filling in placeholders. The most significant bit is referred to as bit 0, and the least significant bit is referred to as bit 15, so that instructions can be read from left to right.

There are 8 registers in this virtual CPU. Registers 0-5 (inclusive) are general purpose registers. Register 6 holds the program counter. Register 7 is always 0. The zero flag is true if an operation evaluates to zero. The overflow flag is true if an operation would yield less than 0 or more than 255, and has to be reset.

Immediate is a constant value. Source means get the value in the register pointed to by source. Destination means set the register pointed to by destination.

The bit-wise breakdown key is as follows:
- O: opcode bit
- R: register bit
- I: immediate (constant) bit
- X: unused bit

Instructions:
- ADD: OOOO RRR RRR IIIIII
    - Add source and immediate and place in destination. Sets overflow/zero flags
    - 0-3: opcode 0000
    - 4-6: destination register
    - 7-9: source register
    - 10-15: immediate

- ADDR: OOOO RRR RRR RRR XXX
    - Add source 1 and source 2 and place in destination. Sets overflow/zero flags
    - 0-3: opcode 0001
    - 4-6: destination register
    - 7-9: source register 1
    - 10-12: source register 2
    - 13-15: unused
    
- SUB: OOOO RRR RRR IIIIII
    - Subtract source and immediate and place in destination. Sets overflow/zero flags
    - 0-3: opcode 0010
    - 4-6: destination register
    - 7-9: source register
    - 10-15: immediate

- SUBR: OOOO RRR RRR RRR XXX
    - Subtract source 1 and source 2 and place in destination. Sets overflow/zero flags
    - 0-3: opcode 0011
    - 4-6: destination register
    - 7-9: source register 1
    - 10-12: source register 2
    - 13-15: unused

- MOV: OOOO RRR IIIIIII
    - Set destination register to immediate
    - 0-3: opcode 0100
    - 4-6: destination register
    - 7-15: immediate

- MOVR: OOOO RRR RRR XXXXXX
    - Set destination register to source
    - 0-3: opcode 0101
    - 4-6: destination register
    - 7-9: source register
    - 10-15: unused

- LOAD: OOOO RRR IIIIIII
    - Retrieve memory location immediate and place in destination
    - 0-3: opcode 0110
    - 4-6: destination register
    - 7-15: immediate
    
- LOADR: OOOO RRR RRR XXXXXX
    - Retrieve memory location source and place in destination
    - 0-3: opcode 0111
    - 4-6: destination register
    - 7-9: source register
    - 10-15: unused

- STORE: OOOO RRR IIIIIII
    - Set memory location to immediate
    - 0-3: opcode 1000
    - 4-6: destination register
    - 7-15: immediate

- STORER: OOOO RRR RRR XXXXXX
    - Set memory location to source
    - 0-3: opcode 1001
    - 4-6: destination register
    - 7-9: source register
    - 10-15: unused

- JMP: OOOO RRR XXXXXXXXX
    - Unconditional jump to instruction in source
    - 0-3: opcode 1010
    - 4-6: destination register
    - 7-15: unused

- JEQ: OOOO RRR XXXXXXXXX
    - Jump to instruction in source if zero flag set
    - 0-3: opcode 1011
    - 4-6: destination register
    - 7-15: unused

- JNE: OOOO RRR XXXXXXXXX
    - Jump to instruction in source if zero flag not set
    - 0-3: opcode 1100
    - 4-6: destination register
    - 7-15: unused

- JLT: OOOO RRR XXXXXXXXX
    - Jump to instruction in source if overflow flag set
    - 0-3: opcode 1101
    - 4-6: destination register
    - 7-15: unused

- JGT: OOOO RRR XXXXXXXXX
    - Jump to instruction in source if overflow flag not set
    - 0-3: opcode 1110
    - 4-6: destination register
    - 7-15: unused

- EXIT: OOOO XXXXXXXXXXXXX
    - End program
    - 0-3: opcode 1111
    - 4-15: unused
