import tkinter as tk
from tkinter import ttk, messagebox

from halstead_metrics import calculate_halstead_metrics
from config import BASE_DIR


def display_metrics(filename_entry, tree):
    """Обрабатывает ввод файла и вычисляет метрики Холстеда."""

    # Очищаем таблицу перед новым анализом
    for row in tree.get_children():
        tree.delete(row)

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
        "Сложность (D)": f"{metrics['difficulty']:.2f}",
        "Уровень (L)": f"{metrics['level']:.2f}",
        "Усилия (E)": f"{metrics['effort']:.2f}",
        "Примерное время разработки (T)": f"{metrics['time']:.2f} сек",
    }

    for key, value in metrics_data.items():
        tree.insert("", tk.END, values=(key, value))


def create_ui():
    """Создает UI-приложение для анализа метрик Холстеда."""

    root = tk.Tk()
    root.title("Метрики Холстеда")
    root.geometry("600x440")
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
        command=lambda: display_metrics(filename_entry, tree),
        font=("Helvetica", 12),
        bg="#4CAF50",
        fg="white"
    )
    display_button.pack(pady=15)

    # Таблица для отображения метрик
    columns = ("Metric", "Value")
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading("Metric", text="Метрика")
    tree.heading("Value", text="Значение")
    tree.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    tree.column("Metric", width=300)
    tree.column("Value", width=200)

    # Настройки стиля таблицы
    style = ttk.Style()
    style.configure("Treeview", font=("Helvetica", 12))
    style.configure("Treeview.Heading", font=("Helvetica", 12, 'bold'))

    root.mainloop()
