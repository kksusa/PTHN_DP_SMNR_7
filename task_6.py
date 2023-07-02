# * Генерируйте файлы в указанную директорию — отдельный параметр функции.
# * Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# * Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


import os
import random
from task_4 import create_files_with_extension
import check_numbers

__all__ = ['create_amount_of_files_in_folder']


def create_amount_of_files_in_folder(extensions_list, amount_of_files, directory):
    new_dir_name = input("Введите название папки: \n"
                         "Для использования текущей директории оставьте поле пустым: ")
    dir_path = str(directory) + "\\" + new_dir_name
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    os.chdir(dir_path)
    for _ in range(amount_of_files):
        extension = random.choice(extensions_list)
        create_files_with_extension(extension)


extensions = []
num_of_extensions = check_numbers.more("Введите количество расширений файлов:", 0)
num_of_files = check_numbers.more("Введите количество файлов для генерации:", 0)
for i in range(num_of_extensions):
    extensions.append(input(f'Введите {i + 1} расширение: '))
while True:
    folder = input("Введите директорию для сохранения файлов.\n"
                   "Для использования текущей директории оставьте поле пустым: ")
    if os.path.isdir(folder):
        break
    elif folder == '':
        folder = os.getcwd()
        break
    else:
        print("Вы ввели неправильный путь.")

create_amount_of_files_in_folder(extensions, num_of_files, folder)
