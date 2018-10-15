from ParserBoolExpr import *
from ParserInfix import *
from NodeVisitor import *

###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################

# The interpreter class that inherits from the class object.
class Interpreter(NodeVisitor):

    # Method that whenever an object of the class has been created, assigns the values asked to their corresponding varuables(base method in python).
    def __init__(self, parser):
        self.parser = parser

    def visit_ContingOp(self, node):
        return '(' + str(self.visit(node.left)) + str(node.op.value) + str(self.visit(node.right)) + ')'

    def visit_CondOp(self, node):
        return '~(' + str(self.visit(node.left)) + str(node.op.value) + '~' + str(self.visit(node.right)) + ')'

    def visit_BicondOp(self, node):
        return '(' + str(self.visit(node.left)) + str(node.op.value) + '~' + str(self.visit(node.right)) + ')'

    def visit_ContradicOp(self, node):
        return u'\u00AC' + self.visit(node.expr)

    def visit_Prep(self, node):
        return str(node.value)

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

    def bexpr(self):
        tree = self.parser.bitwise_parse()
        return self.visit(tree)



