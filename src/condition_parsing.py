import math
from traceback import print_exc

from pygments import lex
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype

def find_conditions(operators, code):
    if_calc = 0
    else_calc = 0

    try:
        lexer = JavascriptLexer()
        tokens = list(lex(code, lexer))
    except Exception as e:
        return {"error": f"Ошибка токенизации: {str(e)}"}

    for token_type, token_value in tokens:
        # Игнорируем комментарии, строки, пробелы и текст
        if (is_token_subtype(token_type, Token.Comment) or
                is_token_subtype(token_type, Token.Literal.String) or
                is_token_subtype(token_type, Token.Text)):
            continue

        # Классифицируем токены
        if is_token_subtype(token_type, Token.Keyword):
            if token_value.strip() == "if":
                if_calc += 1
            elif token_value.strip() == "else":
                else_calc += 1

    substring = "else if"
    else_if_calc = code.count(substring)
    else_calc -= else_if_calc
    if_calc -= else_if_calc
    if_else_calc = else_calc
    if_calc -= else_calc

    if else_if_calc != 0:
        operators["else if()"] = else_if_calc
    if if_else_calc != 0:
        operators["if()..else"] = if_else_calc
    if if_calc != 0:
        operators["if()"] = if_calc


    operators["()"] -= (else_if_calc + if_else_calc + if_calc)