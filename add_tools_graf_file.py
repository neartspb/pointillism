import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Текст для добавления в начало файла
header = "G00 F7000 Z30\n"
header2 = "G00 F6000\n"

# Текст для добавления после каждой строки
addText1 = "G01 F7000 Z10\n"
addText2 = "G01 F2000 Z1\n"
addText3 = "G00 F2000 Z10\n"
addText4 = "G00 F7000 Z30\n"
addText5 = "G00 F6000\n"

# Текст для добавления в конец файла
footer = "G0 X0 Y0\n"

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as temp_file:
        # Добавление заголовка
        temp_file.write(header)
        temp_file.write(header2)

        # Чтение исходного файла и добавление текста после каждой строки
        for line in lines:
            temp_file.write(line)
            temp_file.write(addText1)
            temp_file.write(addText2)
            temp_file.write(addText3)
            temp_file.write(addText4)
            temp_file.write(addText5)

        # Добавление нижнего колонтитула
        temp_file.write(footer)

    messagebox.showinfo("Успех", "Обработка файла завершена.")

def choose_files():
    input_file = filedialog.askopenfilename(title="Выберите входящий файл", filetypes=[("NGC files", "*.ngc")])
    if input_file:
        output_file = filedialog.asksaveasfilename(title="Выберите файл для сохранения", defaultextension=".ngc", filetypes=[("NGC files", "*.ngc")])
        if output_file:
            process_file(input_file, output_file)

# Создание графического интерфейса
root = tk.Tk()
root.title("NGC File Processor")
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)
button = tk.Button(frame, text="Выбрать файлы и обработать", command=choose_files)
button.pack()
root.mainloop()
