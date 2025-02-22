from arithmetic_and_logic_parsing import *
from condition_parsing import *
from function_declaration_and_calls import *
from built_in_functions_calls import *
from switch_parsing import *
from loop_modify import *
from literals_parsing import *

def calculate_halstead_metrics(code: str) -> dict:
    """Вычисляет метрики Холстеда для заданного JavaScript-кода."""

    operators = {}
    operands = {}

    operators["()"] = 0

    calculate_al_operators(operators, code)
    find_conditions(operators, code)
    calculate_functions(operators, operands, code)
    calculate_switch(operators, code)
    calculate_built_in_functions(operators, operands, code)
    modify_loop_counts(operators, code)
    fix_operators(operators)
    calculate_literals(operands, code)
    print("operators")
    for name in operators:
        print(name, operators[name])
    print("operands")
    for name in operands:
        print(name, operands[name])

    # Рассчитываем уникальные и общие количества
    n1 = len(operators) if operators else 0
    n2 = len(operands) if operands else 0
    N1 = 0
    N2 = 0

    for operator in operators:
        N1 += operators[operator]
    for operand in operands:
        N2 += operands[operand]

    # Вычисляем метрики
    vocabulary = n1 + n2
    length = N1 + N2
    volume = length * math.log2(vocabulary) if vocabulary > 0 else 0

    return {
        "n1": n1,
        "n2": n2,
        "N1": N1,
        "N2": N2,
        "vocabulary": vocabulary,
        "length": length,
        "volume": round(volume, 2),
        "operators": operators,
        "operands": operands
    }


# Пример использования
if __name__ == "__main__":

    with (open('../js/code.js', 'r', encoding='utf-8') as file):
        code = file.read()

    metrics = calculate_halstead_metrics(code)

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