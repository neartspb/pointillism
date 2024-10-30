import os
import math
import multiprocessing

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

def process_file(file_path):
    data = read_coordinates(file_path)
    optimized_data = nearest_neighbor(data)
    output_file = f"optimized_{os.path.basename(file_path)}"
    write_coordinates(output_file, optimized_data)
    print(f'Оптимизация завершена для {file_path}. Результат сохранен в {output_file}')

if __name__ == "__main__":
    for file_name in os.listdir('.'):
        if file_name.endswith('.ngc'):
            process_file(file_name)
