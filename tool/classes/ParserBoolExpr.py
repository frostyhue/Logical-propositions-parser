from tool.classes.Parser import *

###############################################################################
#                                                                             #
#  PARSER Boolean Expressions                                                 #
#                                                                             #
###############################################################################


class ParserBoolExpr(Parser):

    """
    Method that is used to iterate through the expression and converting it into separate pieces of node types,
    that will be iterated through by the Iterator.
    """
    def bool_expr_statement(self):
        token = self.current_token
        node = ""

        # Logic if the current token is a letter.
        if token.type == LETTER:

            self.pred_list.append(token.value)
            node = Prep(self.current_token)
            self.pop_token(LETTER)

            if self.current_token.type == COMMA:
                self.pop_token(COMMA)

            elif self.current_token.type == RPAR:
                self.pop_token(RPAR)

            return node

        # Logic if the current token is a negation.
        elif token.type == NOT:
            op = Token(type=NOT, value='~')
            self.pop_token(NOT)
            if self.current_token == LPAR:
                self.pop_token(LPAR)
            node = ContradicOp(op=op, expr=self.bool_expr_statement())
            return node

        # Logic if the current token is one of the Contingency operators.
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

        # Logic if the current token is a right parentheses.
        elif token.type == RPAR:
                self.pop_token(RPAR)
                node = self.bool_expr_statement()
                return node

        # Logic if the current token is a comma.
        elif token.type == COMMA:
            self.pop_token(COMMA)
            node = self.bool_expr_statement()
            return node

        return node

    # Method that returns the final node that is a combination of all of the operation nodes.
    def compound_expr(self):
        node = self.bool_expr_statement()
        return node

    # Method that returns the final compound proposition that is in the form of an AST.
    def parse(self):
        return self.compound_expr()
