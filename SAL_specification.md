
This contains information about SAL (SIMPLE ASSEMBLY LANGUAGE), the assembly language in the virtual CPU.

The bit-wise breakdown key is as follows:
- O: opcode bit
- R: register bit
- I: immediate (constant) bit
- X: unused bit

Instructions:
- ADD: OOOO RRR RRR IIIIII
    - 0-3: opcode 0000
    - 4-6: destination register
    - 7-9: source register
    - 10-15: immediate

- ADDR: OOOO RRR RRR RRR XXX
    - 0-3: opcode 0001
    - 4-6: destination register
    - 7-9: source register 1
    - 10-12: source register 2
    - 13-15: unused
    
- SUB: OOOO RRR RRR IIIIII
    - 0-3: opcode 0010
    - 4-6: destination register
    - 7-9: source register
    - 10-15: immediate

- SUBR: OOOO RRR RRR RRR XXX
    - 0-3: opcode 0011
    - 4-6: destination register
    - 7-9: source register 1
    - 10-12: source register 2
    - 13-15: unused

- MOV: OOOO RRR IIIIIII
    - 0-3: opcode 0100
    - 4-6: destination register
    - 7-15: immediate

- MOVR: OOOO RRR RRR XXXXXX
    - 0-3: opcode 0101
    - 4-6: destination register
    - 7-9: source register
    - 10-15: unused

- LOAD: OOOO RRR IIIIIII
    - 0-3: opcode 0110
    - 4-6: destination register
    - 7-15: immediate
    
- LOADR: OOOO RRR RRR XXXXXX
    - 0-3: opcode 0111
    - 4-6: destination register
    - 7-9: source register
    - 10-15: unused

- STORE: OOOO RRR IIIIIII
    - 0-3: opcode 1000
    - 4-6: destination register
    - 7-15: immediate

- STORER: OOOO RRR RRR XXXXXX
    - 0-3: opcode 1001
    - 4-6: destination register
    - 7-9: source register
    - 10-15: unused

- JMP: OOOO RRR XXXXXXXXX
    - 0-3: opcode 1010
    - 4-6: destination register
    - 7-15: unused

- JEQ: OOOO RRR XXXXXXXXX
    - 0-3: opcode 1011
    - 4-6: destination register
    - 7-15: unused

- JNE: OOOO RRR XXXXXXXXX
    - 0-3: opcode 1100
    - 4-6: destination register
    - 7-15: unused

- JLT: OOOO RRR XXXXXXXXX
    - 0-3: opcode 1101
    - 4-6: destination register
    - 7-15: unused

- JGT: OOOO RRR XXXXXXXXX
    - 0-3: opcode 1110
    - 4-6: destination register
    - 7-15: unused

- EXIT: OOOO XXXXXXXXXXXXX
    - 0-3: opcode 1111
    - 4-15: unused
