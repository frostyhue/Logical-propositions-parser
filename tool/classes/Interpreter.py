from tool.classes.ParserBoolExpr import *
from tool.classes.ParserInfix import *
from tool.classes.NodeVisitor import *

###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################

"""The interpreter class that inherits from the class NodeVisitor and contains all of the logic
        for visiting each node type and returning the final version of the expression 
                                depending on the desired type."""

class Interpreter(NodeVisitor):

    """Method that whenever an object of the class has been created,
    assigns the values asked to their corresponding variables(base method in python)."""
    def __init__(self, parser):
        self.parser = parser

    # Method that processes the node and returns the format for the Contingency Operations for both expression.
    def visit_ContingOp(self, node):
        return '(' + str(self.visit(node.left)) + str(node.op.value) + str(self.visit(node.right)) + ')'

    # Method that processes the node and returns the format for the Conditional Operations for the boolean expression.
    def visit_CondOp(self, node):
        return '~(' + str(self.visit(node.left)) + str(node.op.value) + '~' + str(self.visit(node.right)) + ')'

    # Method that processes the node and returns the format for the Biconditional Operations for the boolean expression.
    def visit_BicondOp(self, node):
        return '(' + str(self.visit(node.left)) + str(node.op.value) + '~' + str(self.visit(node.right)) + ')'

    # Method that processes the node and returns the format for the Contradiction Operations for both expression.
    def visit_ContradicOp(self, node):
        return node.op.value + self.visit(node.prep)

    # Method that processes the node and returns the format for the Preposition for both expression.
    def visit_Prep(self, node):
        return str(node.value)

    # Method that returns the final AST tree for the infix expression notation.
    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

    # Method that returns the final AST tree for the boolean expression notation.
    def bexpr(self):
        tree = self.parser.bitwise_parse()
        return self.visit(tree)



