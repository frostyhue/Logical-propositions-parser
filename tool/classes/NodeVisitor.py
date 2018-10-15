
###############################################################################
#                                                                             #
#  NodeVisitor                                                                #
#                                                                             #
###############################################################################
class NodeVisitor(object):
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