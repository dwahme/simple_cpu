
class Memory:

    # The maximum and minumum location values
    MEM_MIN = 0
    MEM_MAX = 2 ** 8

    # The region for holding various memory values
    GEN_MIN = 0
    GEN_MAX = 2 ** 7

    # The region for holding the program in memory
    PROG_MIN = GEN_MAX + 1
    PROG_MAX = MEM_MAX

    # The memory itself
    memory = [0] * MEM_MAX

    def __init__(self):
        pass
    
    # Reads from a certain (valid) location in memory
    def read(self, location):
        if location >= self.MEM_MIN and location < self.MEM_MAX:
            return self.memory[location]

    # Writes to a certain (valid) location in memory
    def write(self, location, value):
        if location >= self.GEN_MIN and location < self.GEN_MAX:
            self.memory[location] = value

    # Loads a list of instructions into memory
    def load(self, instrs):
        counter = 0

        if len(instrs) > self.PROG_MAX:
            print("Too many instructions")
            return None

        for instr in instrs:
            if instr < 0x10000 and instr >= 0:
                self.memory[counter + self.PROG_MIN] = instr
                counter += 1
            else:
                print("Invalid instruction: {}".format(instr))
                memory = [0] * self.MEM_MAX
                return None

        return self

    # Load a file containing instructions into memory
    def load_file(self, file):
        nums = []

        with open(file, "r") as f:
            strs = f.readlines()

            instrs = [x.strip() for x in strs if x.strip()]
            nums = [int(s, 16) for s in instrs]

        return self.load(nums)

    # Prints out a region of memory
    def dump(self, start=-1, stop=-1):
        if start == -1:
            start = self.MEM_MIN
        if stop == -1:
            start = self.MEM_MAX
        
        for instr in self.memory[start:stop]:
            print(str(format(instr, '#06x')))
