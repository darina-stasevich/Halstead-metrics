import math
from traceback import print_exc

from pygments import lex
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype

def calculate_functions(operators, operands, code):

    try:
        lexer = JavascriptLexer()
        tokens = list(lex(code, lexer))
    except Exception as e:
        return {"error": f"Ошибка токенизации: {str(e)}"}

    cnt_brackets = 0
    functions = {}
    previous_token = "no"
    function_count = 0
    for token_type, token_value in tokens:
        if (is_token_subtype(token_type, Token.Comment) or
                is_token_subtype(token_type, Token.Literal.String) or
                is_token_subtype(token_type, Token.Text)):
            continue

        if is_token_subtype(token_type, Token.Keyword) and token_value.strip() == "function":
            function_count += 1
        if token_value.strip() in functions:
            functions[token_value.strip()] += 1
            cnt_brackets += 1
        if previous_token == "function":
            functions[token_value.strip()] = 1
            cnt_brackets += 1
        previous_token = token_value.strip()

    operators["function"] = function_count
    for function in functions:
        operands[function] = functions[function] - 1
        operators[function + "()"] = 1

    operators["()"] -= cnt_brackets