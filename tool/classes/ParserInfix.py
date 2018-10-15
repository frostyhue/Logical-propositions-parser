from Parser import *

###############################################################################
#                                                                             #
#  PARSER Infix Notation                                                      #
#                                                                             #
###############################################################################


class ParserInfix(Parser):

    def op_statement(self):
        token = self.current_token
        node = ""
        if token.type == LETTER:
            self.pred_list.append(token.value)
            node = Prep(self.current_token)
            self.pop_token(LETTER)
            if self.current_token.type == COMMA:
                self.pop_token(COMMA)
            elif self.current_token.type == RPAR:
                if not self.lexer.expr_end():
                    self.pop_token(RPAR)
            return node

        elif token.type == NOT:
            op = token
            self.pop_token(NOT)
            if self.current_token == LPAR:
                self.pop_token(LPAR)
            node = ContradicOp(op=op, expr=self.op_statement())
            return node

        elif token.type in (COND, BICOND, AND, OR):
            if token.type == COND:
                op = Token(type=COND, value=u'\u2192')
            elif token.type == BICOND:
                op = Token(type=BICOND, value=u'\u2194')
            elif token.type == AND:
                op = Token(type=AND, value=u'\u2227')
            elif token.type == OR:
                op = Token(type=OR, value=u'\u2228')
            self.pop_token(token.type)
            self.pop_token(LPAR)
            node = ContingOp(left=self.op_statement(), op=op, right=self.op_statement())
            return node

        elif token.type == RPAR:
                self.pop_token(RPAR)
                node = self.op_statement()
                return node

        elif token.type == COMMA:
            self.pop_token(COMMA)
            node = self.op_statement()
            return node
        return node

    def compound_prop(self):
        node = self.op_statement()
        return node

    def parse(self):
        return self.compound_prop()
