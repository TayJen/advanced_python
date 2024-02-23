import os
import sys
import argparse
from typing import List


def num_lines(lines: List[str]) -> None:
    for i in range(len(lines)):
        new_line = f"{i+1:5}  {lines[i][:-1]}"
        print(new_line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='nl -b a',
        description="""
            Программа работает как скрипт nl -b a в linux, а именно нумерует строки и выводит их

            Аргументы: 
            -f --from_file  Флаг, указываем если хотим нумеровать строки из файла
            -p --path       Путь до файла, если хотим нумеровать строки из файла

            Использование:
            В случае если считываем инпут из командной строки в последней строке необходимо поставить символ Ctrl+Z
            Таким образом программа определит что достигнут конец инпута
        """
    )
    parser.add_argument("-f", "--from_file", help="Используем как вход файл или консоль", type=bool, default=False)
    parser.add_argument("-p", "--path", help="Путь до файла если используем файл", type=str, default=None)

    args = parser.parse_args()

    from_file = args.from_file
    if from_file:
        file_path = args.path
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        else:
            assert False, "File doesn't exist"
    else:
        lines = []
        for line in sys.stdin.readlines():
            lines.append(line)

    num_lines(lines)
