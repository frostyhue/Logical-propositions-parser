from tool.classes.TruthTable import *

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

    # Simplify the row once
    def simplify_once(self, row_index):
        tempTable = []
        n_index = row_index+1
        for index in range(n_index, len(self.simplified_table)):
            simplified_row = self.simplified_table[row_index].simplify_row(self.simplified_table[index])
            if simplified_row is not None:
                tempTable.append(simplified_row)
                self.simplified_table[index].skip = True
        return tempTable

    # Check if the list is empty
    def check_empty(self, list):
        if not list:
            return True
        else:
            return False

    # Method that simplifies the rows of the truth table once.
    def simplify_tt(self):
        simplified = False
        temp_table = []
        # Attempt to simplify each row and add it to the temp_table, if it wasn't simplified, add it raw.
        for i in range(0, len(self.simplified_table)):
            simplified_rows = self.simplify_once(i)
            if not self.check_empty(simplified_rows):
                simplified = True
                temp_table.extend(simplified_rows)
            else:
                temp_table.append(self.simplified_table[i])
        filtered_rows = []

        # Only add rows that are not yet in the filtered table and should not be skipped.
        for row in temp_table:
            if not row.skip and not row in filtered_rows:
                filtered_rows.append(row)

        # Create the simplified truth table that should be passed on
        final_table = SimplifiedTT(predicates=self.predicates, truth_table=self.remove_dups(filtered_rows))
        final_table.simplified = simplified
        return final_table

    """Method that is used to remove all of the duplicate rows of the truth table
            by creating it into a tuple and the mapping the values."""
    def remove_dups(self, simplifiedTT):
        values_list = []
        for row in simplifiedTT:
            values_list.append(row.values)
        temp_table_set = set(map(tuple, values_list))
        temp_table = map(list, temp_table_set)
        final_table = []
        for item in temp_table:
            final_table.append(Row(item))
        return final_table

    """Method that loops through the simplified truth table until the simplified boolean is false
             meaning that the table was not simplified bu the last iteration."""
    def simplify(self):
        temp_table = self.simplify_tt()
        while temp_table.simplified:
            temp_table.remove_rows_ending_0()
            temp_table = temp_table.simplify_tt()
        self.simplified_table = temp_table

    # Method that checks if two rows are the same and returns a boolean.
    def comp_rows(self, row, row_comp):
        for i in range(0, len(row.values)):
            if row.values[i] != row_comp.values[i]:
                return False
            return True

    # Method that removes all of the rows from the truth table that have 0s in their result column.
    def remove_rows_ending_0(self):
        for row in self.truth_table:
            if row.values[len(row.values) - 1] == 1:
                self.simplified_table.append(row)

    # Create the dnf of the simplified truth table
    def dnf(self):
        temp_table = []
        for row in self.simplified_table.truth_table:
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
                    elif row.values[i] == '*':
                        dnf_result = dnf_result + u'\u00AC' +self.predicates[i] + u'\u2227'+self.predicates[i] + u'\u2227'
                else:
                    dnf_result = dnf_result[:-1] + ')'
            dnf.append(dnf_result)
        result = ''
        for expr in dnf:
            result = result + expr + u'\u2228'
        result = result[:-1]
        return result