
###############################################################################
#                                                                             #
#  NodeVisitor                                                                #
#                                                                             #
###############################################################################


# The NodeVisitor class is used to be the base of the Interpreter.
class NodeVisitor(object):

    """
    Method that distinguishes the node type and depending on it,
    returns the function that should be used to handle the node type.
    """
    def visit(self, node):
        node_type = type(node).__name__
        if node_type == 'Prep':
            return self.visit_Prep(node)

        elif node_type == 'ContradicOp':
            return self.visit_ContradicOp(node)

        elif node_type == 'ContingOp':
            return self.visit_ContingOp(node)

        elif node_type == 'CondOp':
            return self.visit_CondOp(node)

        elif node_type == 'BicondOp':
            return self.visit_BicondOp(node)

    def generic_visit(self, node):
        raise Exception("No visit_{} method".format(type(node).__name__))
