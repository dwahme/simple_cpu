# simple_cpu
A simple virtual CPU for demonstration purposes

## About
This is a small virtual built to run instructions in a custom assembly language, called Simplified Assembly Language (SAL). See `SAL_specifications.md` for more information about the assembly language.

`simple_cpu/` is a small python package containing all the code for the CPU.

`samples/` contains some small sample programs.

## Usage
Load and run a SAL program by running `python runner.py -f <filename>` for a given file.

Run `python runner.py -h` for more options.
