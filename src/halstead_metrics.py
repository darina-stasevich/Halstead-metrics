import math
import pprint
from collections import Counter
from typing import OrderedDict

from pygments import lex
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype

from loop_modify import modify_loop_counts


def calculate_halstead_metrics(code: str) -> dict:
    """Вычисляет метрики Холстеда для заданного JavaScript-кода."""
    operators = []
    operands = []

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
        if (is_token_subtype(token_type, Token.Keyword) or
                is_token_subtype(token_type, Token.Operator) or
                is_token_subtype(token_type, Token.Punctuation)):
            operators.append(token_value.strip())
        elif (is_token_subtype(token_type, Token.Name) or
              is_token_subtype(token_type, Token.Literal.Number)):
            operands.append(token_value.strip())

    operators_count = Counter(operators)
    operands_count = Counter(operands)

    operators_dict = dict(operators_count)
    operands_dict = dict(operands_count)

    modify_loop_counts(operators_dict)

    print(operands_dict)
    print(operators_dict)

    # Рассчитываем уникальные и общие количества
    n1 = len(OrderedDict.fromkeys(operators).keys()) if operators else 0
    n2 = len(OrderedDict.fromkeys(operands).keys()) if operands else 0
    N1 = len(operators)
    N2 = len(operands)

    # Вычисляем метрики
    vocabulary = n1 + n2
    length = N1 + N2
    volume = length * math.log2(vocabulary) if vocabulary > 0 else 0
    difficulty = (n1 / 2) * (N2 / n2) if n2 > 0 else 0
    level = 1 / difficulty if difficulty > 0 else 0
    effort = volume * difficulty
    time = effort / 18 if effort > 0 else 0  # 18 — эмпирическая константа

    return {
        "n1": n1,
        "n2": n2,
        "N1": N1,
        "N2": N2,
        "vocabulary": vocabulary,
        "length": length,
        "volume": round(volume, 2),
        "difficulty": round(difficulty, 2),
        "level": round(level, 2),
        "effort": round(effort, 2),
        "time": round(time, 2)
    }


if __name__ == "__main__":
    with (open('../js/code.js', 'r', encoding='utf-8') as file):
        js_code = file.read()

    metrics = calculate_halstead_metrics(js_code)

    if "error" in metrics:
        print(f"Ошибка: {metrics['error']}")
    else:
        print("Метрики Холстеда")
        print(f"Уникальные операторы (n1): {metrics['n1']}")
        print(f"Уникальные операнды (n2): {metrics['n2']}")
        print(f"Общее количество операторов (N1): {metrics['N1']}")
        print(f"Общее количество операндов (N2): {metrics['N2']}")
        print(f"Словарь программы (n): {metrics['vocabulary']}")
        print(f"Длина программы (N): {metrics['length']}")
        print(f"Объем (V): {metrics['volume']}")
        print(f"Сложность (D): {metrics['difficulty']}")
        print(f"Уровень (L): {metrics['level']}")
        print(f"Усилия (E): {metrics['effort']}")
        print(f"Примерное время разработки (T): {metrics['time']} сек")
