import os
import sys
import argparse
from typing import List, Tuple


def calc_stats_from_lines(lines: List[str]) -> Tuple[int]:
    num_lines = num_words = num_chars = 0
    for line in lines:
        num_lines += 1
        num_words += len(line.split(' '))
        num_chars += len(line)
    return num_lines, num_words, num_chars


def calc_stats_one_file(file_path: str) -> Tuple[int]:
    file_name = file_path.split('/')[-1]
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            num_lines, num_words, num_chars = calc_stats_from_lines(lines)
            print(f"{num_lines:5} {num_words:5} {num_chars:5} {file_name}")
            return num_lines, num_words, num_chars
    else:
        assert False, f"File {file_name} doesn't exist"


def calc_stats_multiple_files(file_paths: List[str]):
    total_lines = total_words = total_chars = 0
    for path in file_paths:
        num_lines, num_words, num_chars = calc_stats_one_file(path)
        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars
    print(f"{total_lines:5} {total_words:5} {total_chars:5} total")


def calc_stats_stding(lines: List[str]):
    num_lines, num_words, num_chars = calc_stats_from_lines(lines)
    print(f"{num_lines:5} {num_words:5} {num_chars:5} stdin")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='wc',
        description="""
            Программа работает как скрипт wc в linux
            А именно выводит статистику по файлу / нескольким файлам / stdin
            Статистика формата: СТРОК — СЛОВ — БАЙТ (СИМВОЛОВ) [— ФАЙЛ]

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
            calc_stats_one_file(paths[0])
        else:
            calc_stats_multiple_files(paths)
    else:
        lines = []
        for line in sys.stdin.readlines():
            lines.append(line)
        calc_stats_stding(lines)
