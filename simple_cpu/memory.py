
class Memory:

    # The maximum and minumum location values
    MEM_MIN = 0
    MEM_MAX = 2 ** 8

    # The region for holding the program in memory
    MEM_MIN = 0
    PROG_MAX = 2 ** 7

    # The region for holding various memory values
    GEN_MIN = PROG_MAX + 1
    GEN_MAX = MEM_MAX

    # The memory itself
    memory = [0] * MEM_MAX

    def __init__(self):
        pass
    
    # Reads from a certain (valid) location in memory
    def read(self, location):
        if location >= MEM_MIN and location <= MEM_MAX:
            return memory[location]

    def write(self):
        pass
