# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.

import argparse


def main():
    parser = argparse.ArgumentParser(description='Процессинг числа и строки с дополнительными опциями.')
    parser.add_argument('number', type=int, help='Число для вывода')
    parser.add_argument('text', type=str, help='Строка для вывода')
    parser.add_argument('--verbose', action='store_true', help='Вывод дополнительной информации')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')
    args = parser.parse_args()
    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text="{args.text}", repeat={args.repeat}')
    print(f'Число: {args.number}, Строка: {" ".join([args.text] * args.repeat)}')

if __name__ == '__main__':
    main()

#команда в терминал
#python home_task4.py 8 "пример_строки" --repeat 5 --verbose