from TruthTable import *

###############################################################################
#                                                                             #
#  Simplified TruthTable                                                      #
#                                                                             #
###############################################################################

class SimplifiedTT(object):

    def __init__(self, predicates, truth_table):
        self.simplified = False
        self.truth_table = truth_table
        self.predicates = predicates
        self.simplified_table = []

    # print predicates
    def print_predicates(self):
        print('\n' + ' '.join(self.predicates))

    # get simplified truth table
    def print_simplified(self):
        print('\n' + ' '.join(self.predicates))
        for values in self.simplified_table.truth_table:
            print(' '.join(str(v) for v in values.values))

    # get the truth table
    def print_tt(self):
        print('\n' + ' '.join(self.predicates))
        for values in self.truth_table:
            print(' '.join(str(v) for v in values.values))

    def simplify_once(self, row_index):
        tempTable = []
        n_index = row_index+1
        for index in range(n_index, len(self.simplified_table)):
            simplified_row = self.simplified_table[row_index].simplify_row(self.simplified_table[index])
            if simplified_row is not None:
                tempTable.append(simplified_row)
                self.simplified_table[index].skip = True
        return tempTable

    def check_empty(self, list):
        if not list:
            return True
        else:
            return False

    def simplify_tt(self):
        simplified = False
        temp_table = []
        for i in range(0, len(self.simplified_table)):
            simplified_rows = self.simplify_once(i)
            if not self.check_empty(simplified_rows):
                simplified = True
                temp_table.extend(simplified_rows)
            else:
                temp_table.append(self.simplified_table[i])
        filtered_rows = []
        for row in temp_table:
            if not row.skip and not row in filtered_rows:
                filtered_rows.append(row)
        final_table = SimplifiedTT(predicates=self.predicates, truth_table=filtered_rows)
        final_table.simplified = simplified
        return final_table

    def simplify(self):
        temp_table = self.simplify_tt()
        while temp_table.simplified:
            temp_table.remove_rows_ending_0()
            temp_table = temp_table.simplify_tt()
        self.simplified_table = temp_table

    def comp_rows(self, row, row_comp):
        for i in range(0, len(row.values)):
            if row.values[i] != row_comp.values[i]:
                return False
            return True

    def remove_rows_ending_0(self):
        for row in self.truth_table:
            if row.values[len(row.values) - 1] == 1:
                self.simplified_table.append(row)