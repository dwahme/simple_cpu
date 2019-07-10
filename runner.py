import sys
from simple_cpu import CPU, Assembler, Memory

if __name__ == "__main__":
    a = Assembler()
    a.assemble("samples/simple.sal", "out.txt")

    m = Memory()
    m.load_file("out.txt")
    m.dump(stop=10)

    c = CPU(m)
    c.run(True)