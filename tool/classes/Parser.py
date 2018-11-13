from tool.classes.Lexer import *
from tool.classes.Operations import *
from tool.classes.Node import *


###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################
class Parser(object):

    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens_list = self.lexer.lex()
        self.current_token = self.tokens_list[0]
        self.pred_list = []

        self.root = None
        self.current_node = None

    # Method that raises and error.
    def error(self):
        print('Expression is incorrect!')

    # Method that goes to the next token if the current one has already been processed.
    def pop_token(self, token_type):
        if self.current_token.type == token_type:
            if not self.lexer.expr_end():
                self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    # Method that returns the predicate_list sorted.
    def sorted_pred_list(self):
        pred_list = list(set(self.pred_list))
        pred_list.sort()
        return pred_list

    def assign_graph_node(self, node):
        graph_node = TokenNode(node.value)
        if node.type in (COND, BICOND, AND, OR):
            if self.root is None:
                self.root = graph_node
                self.current_node = graph_node
            else:
                self.current_node.add(graph_node)
                self.current_node = graph_node
        elif node.type == LETTER:
            self.current_node.add(graph_node)
