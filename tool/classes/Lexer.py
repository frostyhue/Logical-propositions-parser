import sys
import re

def lex(characters, token_exprs):
    error_message = ''
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
            if not match:
                sys.stderr.write('Illegal characters: %s\\' % characters[pos])
                error_message = 'Illegal characters: %s\\' % characters[pos]
                sys.exit(1)
            else:
                pos = match.end(0)
            return tokens