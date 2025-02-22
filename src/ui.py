import tkinter as tk
from tkinter import ttk, messagebox
from halstead_metrics import calculate_halstead_metrics
from config import BASE_DIR

def display_metrics(filename_entry, metrics_tree, operators_tree, operands_tree):
    """Обрабатывает ввод файла и вычисляет метрики Холстеда."""

    # Очищаем таблицы перед новым анализом
    for row in metrics_tree.get_children():
        metrics_tree.delete(row)
    for row in operators_tree.get_children():
        operators_tree.delete(row)
    for row in operands_tree.get_children():
        operands_tree.delete(row)

    filename = filename_entry.get().strip()
    filepath = BASE_DIR / "js" / filename_entry.get().strip()

    if not filename:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите имя файла.")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            js_code = file.read()
    except FileNotFoundError:
        messagebox.showwarning("Ошибка", f"Файл '{filepath}' не найден.")
        return
    except PermissionError:
        messagebox.showwarning("Ошибка", f"Нет доступа к файлу '{filepath}'.")
        return
    except UnicodeDecodeError:
        messagebox.showwarning("Ошибка", f"Файл '{filepath}' не является UTF-8.")
        return

    metrics = calculate_halstead_metrics(js_code)

    if "error" in metrics:
        messagebox.showwarning("Ошибка", "Пожалуйста, повторите попытку заново.")
        return

    # Отображаем метрики в таблице
    metrics_data = {
        "Имя файла": filename,
        "Уникальные операторы (n1)": metrics['n1'],
        "Уникальные операнды (n2)": metrics['n2'],
        "Общее количество операторов (N1)": metrics['N1'],
        "Общее количество операндов (N2)": metrics['N2'],
        "Словарь программы (n)": metrics['vocabulary'],
        "Длина программы (N)": metrics['length'],
        "Объем (V)": f"{metrics['volume']:.2f}",
    }

    for key, value in metrics_data.items():
        metrics_tree.insert("", tk.END, values=(key, value))

    for key, value in metrics['operators'].items():
        operators_tree.insert("", tk.END, values=(key, value))

    for key, value in metrics['operands'].items():
        operands_tree.insert("", tk.END, values=(key, value))



def create_ui():
    """Создает UI-приложение для анализа метрик Холстеда."""

    root = tk.Tk()
    root.title("Метрики Холстеда")
    root.geometry("800x655")
    root.resizable(False, False)

    # Поле ввода имени файла
    filename_label = tk.Label(root, text="Введите имя файла в папке 'js':", font=("Helvetica", 12))
    filename_label.pack(pady=10)

    filename_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
    filename_entry.pack(pady=5)

    # Кнопка анализа
    display_button = tk.Button(
        root,
        text="Показать метрики",
        command=lambda: display_metrics(filename_entry, metrics_tree, operators_tree, operands_tree),
        font=("Helvetica", 12),
        bg="#4CAF50",
        fg="white"
    )
    display_button.pack(pady=15)

    # Таблица для отображения метрик
    columns = ("Metric", "Value")
    metrics_tree = ttk.Treeview(root, columns=columns, show='headings', height=8)  # Увеличена высота
    metrics_tree.heading("Metric", text="Метрика")
    metrics_tree.heading("Value", text="Значение")
    metrics_tree.pack(padx=20, pady=(10, 0), fill=tk.X)  # fill=tk.X для ширины

    metrics_tree.column("Metric", width=400)  # Установите ширину для колонки метрик
    metrics_tree.column("Value", width=200)

    frame = tk.Frame(root)
    frame.pack(pady=10, fill=tk.X)  # fill=tk.X для заполнения по ширине

    # Таблицы для операторов и операндов
    operators_tree = ttk.Treeview(frame, columns=("Operator", "Count"), show='headings', height=14)
    operators_tree.heading("Operator", text="Оператор")
    operators_tree.heading("Count", text="Количество")
    operators_tree.column("Operator", width=200)  # Установите ширину для колонки операторов
    operators_tree.column("Count", width=100)
    operators_tree.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')  # Используйте sticky для заполнения

    operands_tree = ttk.Treeview(frame, columns=("Operand", "Count"), show='headings', height=14)
    operands_tree.heading("Operand", text="Операнд")
    operands_tree.heading("Count", text="Количество")
    operands_tree.column("Operand", width=200)
    operands_tree.column("Count", width=100)
    operands_tree.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')  # Используйте sticky для заполнения

    # Настройки стиля таблицы
    style = ttk.Style()
    style.configure("Treeview", font=("Helvetica", 12))
    style.configure("Treeview.Heading", font=("Helvetica", 12, 'bold'))

    # Настройка растяжения столбцов в фрейме
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    root.mainloop()


create_ui()
