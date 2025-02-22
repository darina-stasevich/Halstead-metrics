from pygments import lex
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype


def count_operators(operands, code):
    try:
        lexer = JavascriptLexer()
        tokens = list(lex(code, lexer))
    except Exception as e:
        return {"error": f"Ошибка токенизации: {str(e)}"}

    operator_keywords = {"return", "break", "continue", "new", "instanceof", "in", "typeof", "delete"}


    for token_type, token_value in tokens:
        if is_token_subtype(token_type, Token.Keyword):
            keyword = token_value.strip()
            if keyword in operator_keywords:
                if keyword not in operands:
                    operands[keyword] = 1
                else:
                    operands[keyword] += 1
