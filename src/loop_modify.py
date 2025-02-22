from lib2to3.fixer_util import in_special_context

from pygments import lex
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype

def modify_loop_counts(operators, code):
    try:
        lexer = JavascriptLexer()
        tokens = list(lex(code, lexer))
    except Exception as e:
        return {"error": f"Ошибка токенизации: {str(e)}"}

    for_count = 0
    do_count = 0
    while_count = 0
    of_count = 0
    in_count = 0

    for token_type, token_value in tokens:
        # Игнорируем комментарии, строки, пробелы и текст
        if (is_token_subtype(token_type, Token.Comment) or
                is_token_subtype(token_type, Token.Literal.String) or
                is_token_subtype(token_type, Token.Text)):
            continue

        # Классифицируем токены
        if is_token_subtype(token_type, Token.Keyword):
            if token_value.strip() == "for":
                for_count += 1
            if token_value.strip() == "do":
                do_count += 1
            if token_value.strip() == "while":
                while_count += 1
            if token_value.strip() == "of":
                of_count += 1
            if token_value.strip() == "in":
                in_count += 1

    operators['()'] -= for_count

    # do ... while
    if do_count:
        while_count -= do_count
        operators['do ... while'] = do_count

    # for ... of
    if of_count:
        for_count -= of_count
        operators['for ... of'] = of_count

    # for ... in
    if in_count:
        for_count -= in_count
        operators['for ... in'] = in_count

    if for_count:
        operators['for'] = for_count
