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

# Проход по всем файлам с расширением .ngc в текущем каталоге
for file_name in os.listdir('.'):
    if file_name.endswith('.ngc'):
        temp_file_name = f"{os.path.splitext(file_name)[0]}_temp.ngc"
        
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        with open(temp_file_name, 'w') as temp_file:
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
        
        # Замена исходного файла новым файлом
        os.replace(temp_file_name, file_name)

print("Обработка файлов завершена.")
