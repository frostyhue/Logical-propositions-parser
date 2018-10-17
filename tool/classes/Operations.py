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


# Biconditional Operation base.
class BicondOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


# Conditional Operation base.
class CondOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


# Preposition base.
class Prep(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


# Contradiction Operation base.
class ContradicOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr
