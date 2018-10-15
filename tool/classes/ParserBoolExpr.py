from Parser import *

###############################################################################
#                                                                             #
#  PARSER Boolean Expressions                                                 #
#                                                                             #
###############################################################################


class ParserBoolExpr(Parser):

    def bool_expr_statement(self):
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
            node = ContradicOp(op=op, expr=self.bool_expr_statement())
            return node
        elif token.type in (COND, BICOND, AND, OR):

            if token.type == COND:
                op = Token(type=COND, value='&')
                self.pop_token(token.type)
                self.pop_token(LPAR)
                node = CondOp(left=self.bool_expr_statement(), op=op, right=self.bool_expr_statement())
            elif token.type == BICOND:
                op = Token(type=BICOND, value='^')
                self.pop_token(token.type)
                self.pop_token(LPAR)
                node = BicondOp(left=self.bool_expr_statement(), op=op, right=self.bool_expr_statement())
            elif token.type == AND:
                op = Token(type=AND, value='&')
                self.pop_token(token.type)
                self.pop_token(LPAR)
                node = ContingOp(left=self.bool_expr_statement(), op=op, right=self.bool_expr_statement())
            elif token.type == OR:
                op = Token(type=OR, value='|')
                self.pop_token(token.type)
                self.pop_token(LPAR)
                node = ContingOp(left=self.bool_expr_statement(), op=op, right=self.bool_expr_statement())
            return node
        elif token.type == RPAR:
                self.pop_token(RPAR)
                node = self.bool_expr_statement()
                return node
        elif token.type == COMMA:
            self.pop_token(COMMA)
            node = self.bool_expr_statement()
            return node
        return node

    def compound_expr(self):
        node = self.bool_expr_statement()
        return node

    def parse(self):
        return self.compound_expr()
