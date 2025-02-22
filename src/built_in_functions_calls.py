import math
from traceback import print_exc
def calculate_built_in_functions(operators, operands, code):

    cnt_brackets = 0

    functions = {}
    for index in [i for i, c in enumerate(code) if c == '(']:
        current = ''
        j = index - 1
        if j >= 0 and code[j] == ' ':
            j -= 1

        while j >= 0 and (code[j].isalpha() or code[j].isdigit() or code[j] == '.' or code[j] == '_' or code[j] == '$'):
            current = code[j] + current
            j -= 1
        if len(current) != 0 and (current+"()" not in operators) and current != "if" and current != "for" and current != "while" and current != "switch":
            if current + "()" not in functions:
                functions[current + "()"] = 1
            else:
                functions[current + "()"] += 1
            cnt_brackets = cnt_brackets + 1
    for key, value in functions.items():
        operators[key] = value

    operators["()"] -= cnt_brackets