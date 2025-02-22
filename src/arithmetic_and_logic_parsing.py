import math
from traceback import print_exc

from pygments import lex
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype

def calculate_al_operators(operators, code):

    try:
        lexer = JavascriptLexer()
        tokens = list(lex(code, lexer))
    except Exception as e:
        return {"error": f"Ошибка токенизации: {str(e)}"}

    for token_type, token_value in tokens:
        if (is_token_subtype(token_type, Token.Operator) or
            is_token_subtype(token_type, Token.Punctuation)):
            if token_value.strip() not in operators:
                operators[token_value.strip()] = 1
            else:
                operators[token_value.strip()] += 1

    if ")" in operators:
        operators.pop(")")
        operators["()"] = operators["("]
        operators.pop("(")
    if "]" in operators:
        operators.pop("]")
        operators["[]"] = operators["["]
        operators.pop("[")
    if "}" in operators:
        operators.pop("}")
        operators["{...}"] = operators["{"]
        operators.pop("{")
    if ":" in operators:
        operators["?...:"] = operators[":"]
        operators.pop(":")
        operators["?"] -= operators["?...:"]
        if operators["?"] == 0:
            operators.pop("?")


def fix_operators(operators):
    if operators["()"] == 0:
        operators.pop("()")

    if "?...:" not in operators:
        return
    operators["?...:"] -= operators["case"]
    operators["?...:"] -= operators["default"]
    if "?" not in operators:
        operators["?:"] = 0
    operators["?"] += operators["case"]
    operators["?"] += operators["default"]
    if operators["?"] < 0:
        operators[":"] = -operators["?"]
        operators.pop("?")
    if operators.get("?") == 0:
        operators.pop("?")
    operators.pop("switch")
    operators.pop("case")
    operators.pop("default")