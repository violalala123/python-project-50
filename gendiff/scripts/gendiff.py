import argparse  # Импортируем стандартную библиотеку для работы с CLI

from gendiff.generate_diff import generate_diff


def main():
    # 1. Создаем объект-парсер. 
    
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        '-f', '--format',
        choices=['stylish', 'plain'], 
        default='stylish',
        help='set format of output (default: "stylish")'
    )
    # 2. Описываем аргументы, которые программа ОБЯЗАНА получить.
    # Это позиционные аргументы. Их порядок важен.
    parser.add_argument('first_file') 
    parser.add_argument('second_file')

    # 3. Вызываем метод парсинга. 
    # В этот момент argparse проверяет, что ввел пользователь.
    # Если пользователь ввел -h или --help, argparse САМ выведет справку 
    # и завершит работу программы. Нам даже не нужно писать print.
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


# Это стандартная проверка: запускать main() только если файл вызван напрямую
if __name__ == '__main__':
    main()