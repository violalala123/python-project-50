import json

import yaml


# Читаем данные из файла и возвращаем результат в зависимости от формата.
def parse(data, data_format):
    
    if data_format == '.json':
        return json.loads(data)
    
    if data_format in ('.yml', '.yaml'):

        return yaml.safe_load(data)
    
    else:
        raise ValueError(f'Неизвестный формат{data_format}')