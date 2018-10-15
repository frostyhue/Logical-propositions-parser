import sys
import re
from token_expressions import *
from Token import *

###############################################################################
#                                                                             #
#  LEXER                                                                      #
#                                                                             #
###############################################################################

class Lexer(object):
    def __init__(self, expression):
        self.token_exprs = token_exprs
        self.expression = expression
        self.pos = 0
        self.tokens = []
        self.current_token = ''

    def lex(self):
        pos = 0
        tokens = []
        while pos < len(self.expression):
            match = None
            for token_expr in self.token_exprs:
                pattern, type = token_expr[0], token_expr[1]
                regex = re.compile(pattern)
                match = regex.match(self.expression, pos)
                if match:
                    value = match.group(0)
                    if type:
                        tokens.append(Token(type, value))
                    break
            if not match:
                sys.stderr.write('Illegal character: %s' % self.expression[pos])
                sys.exit(1)
            else:
                pos = match.end(0)
        self.tokens = tokens
        self.current_token = self.tokens[self.pos]
        return tokens

    def get_tokens(self):
        return self.tokens

    def expr_end(self):
        if self.pos == len(self.tokens)-1:
            return True
        else:
            return False

    def get_initial_token(self):
        return self.tokens[0]

    def get_next_token(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos]
        return self.current_token
