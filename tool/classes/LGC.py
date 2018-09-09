import Lexer

Reserved = 'Reserved'
INT = 'INT'
ID = 'ID'

token_exprs = [
    (r'[ \n\t]+',               None),
    (r'#[^\n]*+',               None),
    (r'\=',                     Reserved),
    (r'\~',                     Reserved),
    (r'\>',                     Reserved),
    (r'\&',                     Reserved),
    (r'\|',                     Reserved),
    (r'\(',                     Reserved),
    (r'\)',                     Reserved),
    (r'\,',                     Reserved),
    (r'[0-9]+',                 INT),
    (r'[A-Za-z][A-Za-z0-9_]*',  ID),

]

def lgc_lex(characters):
    return Lexer.lex(characters, token_exprs)