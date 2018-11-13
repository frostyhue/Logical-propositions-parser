###############################################################################
#                                                                             #
#  OPERATIONS                                                                 #
#                                                                             #
###############################################################################


# AST class that when finished being iterated through, continues to the next one.
class AST(object):
    pass


# Contingency Operation base.
class ContingOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __str__(self):
        return str("ContingOp({left}, {op}, {right})".format(left=self.left, op=self.op, right=self.right))


# Biconditional Operation base.
class BicondOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __str__(self):
        return str("BicondOp({left}, {op}, {right})".format(left=self.left, op=self.op, right=self.right))


# Conditional Operation base.
class CondOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __str__(self):
        return str("CondOp({left}, {op}, {right})".format(left=self.left, op=self.op, right =self.right))


# Preposition base.
class Prep(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return str("Prep({token}, {value})".format(token=self.token, value=self.value))


# Contradiction Operation base.
class ContradicOp(AST):
    def __init__(self, op, prep):
        self.token = self.op = op
        self.prep = prep

    def __str__(self):
        return str("ContradicOp({op}, {prep})".format(op=self.op, prep=self.prep))
