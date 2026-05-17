import argparse  # Импортируем стандартную библиотеку для работы с CLI

from gendiff.generate_diff import generate_diff


def main():
        
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        '-f', '--format',
        choices=['stylish', 'plain', 'json'], 
        default='stylish',
        help='set format of output (default: "stylish")'
    )
    # Описываем аргументы, которые программа должна получить.
    # Это позиционные аргументы. Их порядок важен.
    parser.add_argument('first_file') 
    parser.add_argument('second_file')

    # Вызываем метод парсинга. 
    
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()