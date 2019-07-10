
class Assembler:

    def __init__(self):
        pass

    # Converts an instruction to binary
    def encode(self, opcode, num_args, starts, args):
        instr = opcode << 12

        if num_args != len(args):
            strs = [str(x) for x in args]
            print("Invalid number of arguments: " + " ".join(strs))
            return -1

        for idx, start in enumerate(starts[:-1]):
            if args[idx + 1] >= 2 ** (starts[idx + 1] - start):
                strs = [str(x) for x in args]
                print("Argument {} too large: ".format(args[idx + 1]) + 
                    " ".join(strs))
                return -1
            else:
                instr += args[idx + 1] << 16 - starts[idx + 1]

        return instr

    # Converts a file to binary
    def assemble(self, file, outfile=""):

        out = []

        with open(file, "r") as f:

            for line in f.readlines():
                splits = line.split()
                op = splits[0]
                nums = [int(x) for x in splits[1:]]

                if len(splits) == 0 or  op[:2] == "//":
                    # Comment or empty line
                    pass

                elif op == "ADD":
                    out.append(self.encode(0, 4, [4, 7, 10, 16], [op] + nums))
                elif op == "ADDR":
                    out.append(self.encode(1, 4, [4, 7, 10, 13], [op] + nums))
                elif op == "SUB":
                    out.append(self.encode(2, 4, [4, 7, 10, 16], [op] + nums))
                elif op == "SUBR":
                    out.append(self.encode(3, 4, [4, 7, 10, 13], [op] + nums))

                elif op == "MOV":
                    out.append(self.encode(4, 3, [4, 7, 16], [op] + nums))
                elif op == "MOVR":
                    out.append(self.encode(5, 3, [4, 7, 10], [op] + nums))

                elif op == "LOAD":
                    out.append(self.encode(6, 3, [4, 7, 16], [op] + nums))
                elif op == "LOADR":
                    out.append(self.encode(7, 3, [4, 7, 10], [op] + nums))
                elif op == "STORE":
                    out.append(self.encode(8, 3, [4, 7, 16], [op] + nums))
                elif op == "STORER":
                    out.append(self.encode(9, 3, [4, 7, 10], [op] + nums))

                elif op == "JMP":
                    out.append(self.encode(10, 2, [4, 7], [op] + nums))
                elif op == "JEQ":
                    out.append(self.encode(11, 2, [4, 7], [op] + nums))
                elif op == "JNE":
                    out.append(self.encode(12, 2, [4, 7], [op] + nums))
                elif op == "JLT":
                    out.append(self.encode(13, 2, [4, 7], [op] + nums))
                elif op == "JGT":
                    out.append(self.encode(14, 2, [4, 7], [op] + nums))

                elif op == "EXIT":
                    out.append(self.encode(15, 1, [4], [op] + nums))

                if out[-1] == -1:
                    return []

        if outfile != "":
            with open(outfile, "w") as f:
                f.writelines([str(format(x, '#06x'))[2:] + "\n" for x in out])

        return out
