import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Текст для добавления в начало каждого файла
header = "G00 F7000 Z30\n"
header2 = "G00 F6000\n"

# Текст для добавления после каждой строки
addText1 = "G01 F7000 Z10\n"
addText2 = "G01 F2000 Z1\n"
addText3 = "G00 F2000 Z10\n"
addText4 = "G00 F7000 Z30\n"
addText5 = "G00 F6000\n"

# Текст для добавления в конец каждого файла
footer = "G0 X0 Y0\n"

def process_files(input_dir, output_dir):
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.ngc'):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)
            
            with open(input_path, 'r') as file:
                lines = file.readlines()
            
            with open(output_path, 'w') as temp_file:
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
    
    messagebox.showinfo("Успех", "Обработка файлов завершена.")

def choose_directories():
    input_dir = filedialog.askdirectory(title="Выберите входящий каталог")
    if input_dir:
        output_dir = filedialog.askdirectory(title="Выберите каталог для сохранения")
        if output_dir:
            process_files(input_dir, output_dir)

# Создание графического интерфейса
root = tk.Tk()
root.title("NGC File Processor")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

button = tk.Button(frame, text="Выбрать каталоги и обработать файлы", command=choose_directories)
button.pack()

root.mainloop()
