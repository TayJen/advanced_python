import os
import sys
import argparse
from typing import List


def print_last_n_lines(lines: List[str], n: int) -> List[str]:
    for line in lines[-n:]:
        print(line[:-1])


def open_file_and_print_last_lines(file_path: str):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print_last_n_lines(lines, 10)
    else:
        assert False, "File doesn't exist"



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='tail',
        description="""
            Программа работает как скрипт tail в linux
            А именно выводит последние 10 строк из файла либо последние 17 строк из stdin

            Аргументы: 
            -f --from_file  Флаг, указываем если хотим использовать файл как вход, иначе cmd
            -p --path(-s)   Путь до файла (пути до файлов), если хотим использовать файл(-ы)

            Использование:
            В случае если считываем инпут из командной строки в последней строке необходимо поставить символ Ctrl+Z
            Таким образом программа определит что достигнут конец инпута
        """
    )
    parser.add_argument("-f", "--from_file", help="Используем как вход файл или консоль", type=bool, default=False)
    parser.add_argument("-p", "--path", help="Пути файлов у которых используем функцию", type=str, default=None, nargs='+')

    args = parser.parse_args()

    from_file = args.from_file
    if from_file:
        paths = args.path
        if len(paths) == 1:
            open_file_and_print_last_lines(paths[0])
        else:
            for path in paths:
                print(f"==> {path.split('/')[-1]} <==")
                open_file_and_print_last_lines(path)
                print()
    else:
        lines = []
        for line in sys.stdin.readlines():
            lines.append(line)
        print_last_n_lines(lines, 17)
