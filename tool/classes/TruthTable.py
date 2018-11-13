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

    # Create the dnf of the truth table.
    def dnf(self):
        temp_table = []
        for row in self.truth_table:
            if row.values[len(row.values) - 1] == 1:
                temp_table.append(row)
        dnf = []
        for row in temp_table:
            dnf_result = '('
            for i in range(len(row.values)):
                if not i == len(row.values)-1:
                    if row.values[i] == 1:
                        dnf_result = dnf_result  + self.predicates[i] + u'\u2227'
                    elif row.values[i] == 0:
                        dnf_result = dnf_result + u'\u00AC' +self.predicates[i] + u'\u2227'
                else:
                    dnf_result = dnf_result[:-1] + ')'
            dnf.append(dnf_result)
        result = ''
        for expr in dnf:
            result = result + expr + u'\u2228'
        result = result[:-1]
        return result