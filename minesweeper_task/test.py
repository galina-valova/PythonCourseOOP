import tkinter as tk

def create_table_with_header():
    root = tk.Tk()
    root.title("Таблица с заголовком и прокруткой")

    # Создаем фрейм для заголовка (две метки)
    header_frame = tk.Frame(root)
    header_frame.pack(fill=tk.X, padx=5, pady=5)

    # Добавляем две метки (колонки заголовка)
    label1 = tk.Label(header_frame, text="Колонка 1", borderwidth=1, relief="solid", width=20)
    label1.pack(side=tk.LEFT, padx=(0, 2))  # padx - небольшой отступ между колонками

    label2 = tk.Label(header_frame, text="Колонка 2", borderwidth=1, relief="solid", width=20)
    label2.pack(side=tk.LEFT)

    # Фрейм для таблицы (Text + Scrollbar)
    table_frame = tk.Frame(root)
    table_frame.pack(fill=tk.BOTH, expand=True)

    # Scrollbar для прокрутки
    scrollbar = tk.Scrollbar(table_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Виджет Text для таблицы
    text = tk.Text(
        table_frame,
        yscrollcommand=scrollbar.set,
        wrap=tk.NONE,
        font=("Courier New", 10)  # Моноширинный шрифт для ровных колонок
    )
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Привязка Scrollbar к Text
    scrollbar.config(command=text.yview)

    # Заполнение таблицы данными (15 строк, 2 колонки)
    for i in range(1, 16):
        text.insert(tk.END, f"Строка {i}\tЗначение {i * 10}\n")

    # Настройка табуляции для выравнивания колонок
    text.configure(tabs=("150", "300"))  # Позиции в пикселях

    root.mainloop()

create_table_with_header()