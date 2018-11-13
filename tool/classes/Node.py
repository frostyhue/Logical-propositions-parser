###############################################################################
#                                                                             #
#  Node                                                                       #
#                                                                             #
###############################################################################


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, node):
        self.children.append(node)


class TokenNode(Node):
    pass
