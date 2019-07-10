import argparse
import sys
from simple_cpu import CPU, Assembler, Memory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a SAL program")

    parser.add_argument('-f', action='store', dest='file', type=str, 
                        help='The file to process')
    parser.add_argument('-a', action='store', dest='assembled', type=str, default="",
                        help='Where to store the assembled code')
    parser.add_argument('-q', action='store_true', default=False,
                        dest='quiet',
                        help='Only print final CPU state')
    parser.add_argument('-s', action='store_true', default=0,
                        dest='lo',
                        help='Low end of memory region to dump')
    parser.add_argument('-e', action='store_true', default=10,
                        dest='hi',
                        help='High end of memory region to dump')

    results = parser.parse_args()

    a = Assembler()
    if results.assembled == "":
        assembled = a.assemble(results.file)
    else:
        assembled = a.assemble(results.file, results.assembled)

    m = Memory()
    m.load(assembled)

    c = CPU(m)
    c.run(not results.quiet, results.lo, results.hi)