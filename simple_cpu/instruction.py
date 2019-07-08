
class Instruction:

    OP_MIN = 0
    OP_MAX = 3

    op = None
    args = []

    def __init__(self, encoded):
        self.instr_encoded = encoded
