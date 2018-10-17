###############################################################################
#                                                                             #
#  TOKEN_EXPRESSIONS                                                          #
#                                                                             #
###############################################################################

# All of the token types.
BICOND = "BICOND"
COND = "COND"
AND = "AND"
OR = "OR"
LETTER = "LETTER"
NOT = "NOT"
LPAR = "LPAR"
RPAR = "RPAR"
COMMA = "COMMA"

# Regular expression used to generate each token type.
token_exprs = [
    (r'[ \n\t]+',               None),
    (r'[=]',                    BICOND),
    (r'[&]',                    AND),
    (r'[~]',                    NOT),
    (r'[,]',                    COMMA),
    (r'[)]',                    RPAR),
    (r'[(]',                    LPAR),
    (r'[>]',                    COND),
    (r'[|]',                    OR),
    (r'[A-Z]',                  LETTER),
    (r'[a-z]',                  LETTER)
]