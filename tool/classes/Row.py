###############################################################################
#                                                                             #
#  TruthTable Row                                                             #
#                                                                             #
###############################################################################

class Row(object):
    def __init__(self, values):
         self.skip = False
         self.values = values

    """
    The method that checks if the current row can be simplified based on the row_compare, where if exactly one value has been simplified,
    returns the new simplified row, but if it wasn't, then returns nothing
    """
    def simplify_row(self, row_compare):
        row_new = []
        simplified_cells_count = 0
        for i in range(len(self.values)):
            if self.values[i] != row_compare.values[i]:
                row_new.append('*')
                simplified_cells_count = simplified_cells_count +1
            else:
                row_new.append(self.values[i])
        if simplified_cells_count == 1:
            return Row(row_new)
        else:
            return None