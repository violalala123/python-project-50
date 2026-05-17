from pathlib import Path

from gendiff.build_tree import build_tree
from gendiff.formats.json import render as render_json
from gendiff.formats.plain import render as render_plain
from gendiff.formats.stylish import render as render_stylish
from gendiff.parser import parse


def generate_diff(file1, file2, format_name='stylish'):
    # Получаем данные
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
    data1 = parse(content1, Path(file1).suffix)
    data2 = parse(content2, Path(file2).suffix)
    
    # Строим внутреннее дерево
    
    diff = build_tree(data1, data2)
    
    # Выбираем стиль
    if format_name == 'stylish':
        return render_stylish(diff)
    
    if format_name == 'plain':
        return render_plain(diff)
     
    if format_name == 'json':
        return render_json(diff)