from itertools import *
from tool.classes.Row import *
###############################################################################
#                                                                             #
#  TruthTable                                                                 #
#                                                                             #
###############################################################################

class TruthTable(object):

    def __init__(self, expr):
        self.expr = expr
        self.code = compile(self.expr, 'expr', 'eval')
        self.predicates = self.code.co_names
        self.exp_pred = self.predicates + (expr, )
        self.bin = ''
        self.hex = ''
        self.truth_table = []

    def populate_tt(self):
        for values in product(range(2), repeat=len(self.predicates)):
            self.env = dict(zip(self.predicates, values))
            self.bin = self.bin + str(bin(eval(self.code, self.env) & 0xff)[-1:])
            values = values + (int(bin(eval(self.code, self.env) & 0xff)[-1:]), )
            self.truth_table.append(Row(list(values)))
        self.bin = str(self.bin)[::-1]
        self.hex = hex(int(self.bin, 2))[2:]

    def remove_rows_ending_0(self):
        for row in self.truth_table:
            if row[len(row) - 1] == 1:
                self.simplified_table.append(Row(row[:len(row)-1]))

    def print_simplified_tt(self):
        for values in self.simplified_table:
            print(' '.join(str(v) for v in values.values))