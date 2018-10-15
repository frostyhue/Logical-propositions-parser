###############################################################################
#                                                                             #
#  OPERATIONS                                                                 #
#                                                                             #
###############################################################################
class AST(object):
    pass

class ContingOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class BicondOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class CondOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Prep(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class ContradicOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr
