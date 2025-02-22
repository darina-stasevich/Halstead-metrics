import math
from traceback import print_exc

from pygments import lex
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype

def calculate_literals(operands, code):
    try:
        lexer = JavascriptLexer()
        tokens = list(lex(code, lexer))
    except Exception as e:
        return {"error": f"Ошибка токенизации: {str(e)}"}

    for token_type, token_value in tokens:

        if (is_token_subtype(token_type, Token.Comment) or
                is_token_subtype(token_type, Token.Text)):
            continue

        if (is_token_subtype(token_type, Token.Literal.String) or
                is_token_subtype(token_type, Token.Literal.Number) or
                (is_token_subtype(token_type, Token.Keyword) and token_value.strip() in {"true", "false", "null"}) or
                (is_token_subtype(token_type, Token.Name) and token_value.strip() == "undefined")):
            if token_value.strip() not in operands:
                operands[token_value.strip()] = 1
            else:
                operands[token_value.strip()] += 1

    prev = "q"
    prevprev = "q"

    subtype = Token.Keyword
    for token_type, token_value in tokens:
        if is_token_subtype(subtype, Token.Name.Other):
            if prevprev == "." or token_value.strip() == '(' or token_value.strip() == ".":
                prevprev = prev
            else:
                if prev not in operands:
                    operands[prev] = 1
                else:
                    operands[prev] += 1
        prevprev = prev
        prev = token_value.strip()
        subtype = token_type