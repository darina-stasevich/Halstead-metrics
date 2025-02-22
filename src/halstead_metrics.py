import math

from pygments import lex
from pygments.lexers import JavascriptLexer
from pygments.token import Token, is_token_subtype

operators = []
operands = []
operators_dictionary = {}
operands_dictionary = {}

def calculate_halstead_metrics(code: str) -> dict:
    """Вычисляет метрики Холстеда для заданного JavaScript-кода."""

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

    # Рассчитываем уникальные и общие количества
    n1 = len(set(operators)) if operators else 0
    n2 = len(set(operands)) if operands else 0
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
