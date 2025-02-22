import math
from traceback import print_exc

from pygments import lex
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype

def calculate_booleans(operands, code):
    try:
        lexer = JavascriptLexer()
        tokens = list(lex(code, lexer))
    except Exception as e:
        return {"error": f"Ошибка токенизации: {str(e)}"}

    for token_type, token_value in tokens:
        if is_token_subtype(token_type, Token.Keyword):
            if token_value.strip().lower() == "true":
                if "true" not in operands:
                    operands["true"] = 1
                else:
                    operands["true"] += 1
            elif token_value.strip().lower() == "false":
                if "false" not in operands:
                    operands["false"] = 1
                else:
                    operands["false"] += 1