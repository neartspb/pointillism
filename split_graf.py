import tkinter as tk
from tkinter import filedialog, messagebox
import os

def split_file(input_path, lines_per_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    for i in range(0, len(lines), lines_per_file):
        part_lines = lines[i:i + lines_per_file]
        part_file_name = os.path.join(output_dir, f'part_{i // lines_per_file + 1}.ngc')
        with open(part_file_name, 'w') as part_file:
            part_file.writelines(part_lines)
    
    messagebox.showinfo("Успех", "Разделение файла завершено.")

def choose_file():
    input_path = filedialog.askopenfilename(filetypes=[("NGC files", "*.ngc")])
    if input_path:
        output_dir = filedialog.askdirectory()
        if output_dir:
            lines_per_file = int(lines_entry.get())
            split_file(input_path, lines_per_file, output_dir)

# Создание графического интерфейса
root = tk.Tk()
root.title("File Splitter")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

lines_label = tk.Label(frame, text="Количество строк на файл:")
lines_label.pack()

lines_entry = tk.Entry(frame)
lines_entry.pack()

button = tk.Button(frame, text="Выбрать и разделить файл", command=choose_file)
button.pack()

root.mainloop()
