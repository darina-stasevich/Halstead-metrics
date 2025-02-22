import math
from traceback import print_exc

from pygments import lex
from pygments.lexer import default
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype

def calculate_switch(operators, code):
    try:
        lexer = JavascriptLexer()
        tokens = list(lex(code, lexer))
    except Exception as e:
        return {"error": f"Ошибка токенизации: {str(e)}"}

    switch_count = 0
    case_count = 0
    default_count = 0

    for token_type, token_value in tokens:
        # Игнорируем комментарии, строки, пробелы и текст
        if (is_token_subtype(token_type, Token.Comment) or
                is_token_subtype(token_type, Token.Literal.String) or
                is_token_subtype(token_type, Token.Text)):
            continue

        # Классифицируем токены
        if is_token_subtype(token_type, Token.Keyword):
            if token_value.strip() == "switch":
                switch_count += 1
            if token_value.strip() == "case":
                case_count += 1
            if token_value.strip() == "default":
                default_count += 1

    if default_count > 0:
        operators["switch...case...default"] = default_count
    if switch_count - default_count > 0:
        operators["switch...case"] = switch_count - default_count

    operators["switch"] = switch_count
    operators["case"] = case_count
    operators["default"] = default_count

    operators["()"] -= switch_count