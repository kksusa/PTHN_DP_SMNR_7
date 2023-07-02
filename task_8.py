# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# * при переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>


import os

__all__ = ['rename_files']


def rename_files(final_name, start_ext, final_ext, directory):
    os.chdir(directory)
    current_files = os.listdir()
    count = 1
    for i in current_files:
        name_div = i.split(i[i.rfind(".")])
        if name_div[1] == start_ext:
            os.rename(i, name_div[0] + "_" + final_name + "_" + str(count) + "." + final_ext)
            count += 1


while True:
    required_directory = input("Введите путь к папке.\nЕсли папка исходная, то оставьте поле пустым: ")
    if required_directory == "":
        required_directory = os.getcwd()
        break
    elif os.path.exists(required_directory):
        break
    else:
        print("Такой папки нет. Попробуйте снова.")
desired_name = input("Введите желаемое новое имя файлов: ")
selected_required_extension = input("Введите расширение для выборки: ")
new_extension = input("Введите новое расширение для выборки: ")
rename_files(desired_name, selected_required_extension, new_extension, required_directory)
