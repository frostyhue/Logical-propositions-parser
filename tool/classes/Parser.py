from tool.classes.Lexer import *
from tool.classes.Operations import *

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
