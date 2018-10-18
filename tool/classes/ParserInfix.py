from tool.classes.Parser import *

###############################################################################
#                                                                             #
#  PARSER Infix Notation                                                      #
#                                                                             #
###############################################################################


class ParserInfix(Parser):

    """
    Method that is used to iterate through the expression and converting it into separate pieces of node types,
    that will be iterated through by the Iterator.
    """
    def op_statement(self):
        token = self.current_token
        node = ""

        # Logic if the current token is a letter.
        if token.type == LETTER:

            self.pred_list.append(token.value)
            node = Prep(self.current_token)
            self.pop_token(LETTER)

            if self.current_token.type == COMMA:
                self.pop_token(COMMA)

            if self.current_token.type == RPAR:
                self.pop_token(RPAR)

            return node

        # Logic if the current token is a negation.
        elif token.type == NOT:
            op = Token(type=NOT, value=u'\u00AC')
            self.pop_token(NOT)
            if self.current_token.type == LPAR:
                self.pop_token(LPAR)
            node = ContradicOp(op=op, expr=self.op_statement())
            return node

        # Logic if the current token is one of the Contingency operators.
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

        # Logic if the current token is a right parentheses.
        elif token.type == RPAR:
            self.pop_token(RPAR)
            node = self.op_statement()
            return node

        # Logic if the current token is a comma.
        elif token.type == COMMA:
            self.pop_token(COMMA)
            node = self.op_statement()
            return node

        return node

    # Method that returns the final node that is a combination of all of the operation nodes.
    def compound_prop(self):
        node = self.op_statement()
        return node

    # Method that returns the final compound proposition that is in the form of an AST.
    def parse(self):
        return self.compound_prop()
