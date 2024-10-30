input_file = "0.ngc"
lines_per_file = 15000
output_dir = "output"

import os

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, 'r') as file:
    lines = file.readlines()

for i in range(0, len(lines), lines_per_file):
    part_lines = lines[i:i + lines_per_file]
    part_file_name = os.path.join(output_dir, f'part_{i // lines_per_file + 1}.ngc')
    with open(part_file_name, 'w') as part_file:
        part_file.writelines(part_lines)

print("Разделение файла завершено.")
