import tkinter as tk
from tkinter import filedialog, messagebox
import os
import math

def read_coordinates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    coordinates = []
    for line in lines:
        if line.startswith('G0'):
            parts = line.split()
            x = float(parts[1][1:])
            y = float(parts[2][1:])
            coordinates.append((x, y))
    return coordinates

def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def nearest_neighbor(coords):
    if not coords:
        return []
    path = [coords.pop(0)]
    while coords:
        nearest = min(coords, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        coords.remove(nearest)
    return path

def write_coordinates(file_path, coordinates):
    with open(file_path, 'w') as file:
        for coord in coordinates:
            file.write(f'G0 X{coord[0]} Y{coord[1]}\n')

def process_file(input_path, output_path):
    data = read_coordinates(input_path)
    optimized_data = nearest_neighbor(data)
    write_coordinates(output_path, optimized_data)
    messagebox.showinfo("Успех", f"Оптимизация завершена. Результат сохранен в {output_path}")

def choose_file():
    input_path = filedialog.askopenfilename(filetypes=[("NGC files", "*.ngc")])
    if input_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".ngc", filetypes=[("NGC files", "*.ngc")])
        if output_path:
            process_file(input_path, output_path)

# Создание графического интерфейса
root = tk.Tk()
root.title("NGC Path Optimizer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

button = tk.Button(frame, text="Выбрать и оптимизировать файл", command=choose_file)
button.pack()

root.mainloop()
