import json

'''
def generate_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    def to_string(value):
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
        return str(value)
    keys = sorted(data1 | data2)
    result = ['{']
    for key in keys:

        if key in data1 and key not in data2:
            result += [f'  - {key}: {to_string(data1[key])}']

        elif key in data1 and key in data2:
            if data1[key] == data2[key]:
                result += [f'    {key}: {to_string(data1[key])}']
            else:
                result += [f'  - {key}: {to_string(data1[key])}']
                result += [f'  + {key}: {to_string(data2[key])}']
        
        elif key in data2:
            result +=[f'  + {key}: {to_string(data2[key])}']
    result +=['}']
    return "\n".join(result)

    return f"Read {(data1)} and {(data2)} keys"'''

DIFF_TEMPLATES = {
    'removed': '  - {key}: {value}',
    'added': '  + {key}: {value}',
    'unchanged': '    {key}: {value}',
    'changed': '  - {key}: {old_value}\n  + {key}: {new_value}'
}


def to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def render(data):
    result = []
    for item in data:
        # создаю новый словарь для отфармотированных данных
        formated_item = {}
        for key, value in item.items():
            if key in ['value', 'old_value', 'new_value']:
                formated_item[key] = to_string(value)
            else:
                formated_item[key] = value
        temp = DIFF_TEMPLATES[item['type']]            
        result.append(temp.format(**formated_item))
    final = ['{'] + result + ['}']
    return '\n'.join(final)       


def generate_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    
    keys = sorted(data1 | data2)
    result = []
    for key in keys:

        if key in data1 and key not in data2:
            result.append({'key': key, 'type': 'removed', 'value': data1[key]})

        elif key in data1 and key in data2:
            if data1[key] == data2[key]:
                result.append({
                    'key': key,
                    'type': 'unchanged',
                    'value': data1[key]
                    })
            else:
                result.append({
                    'key': key,
                    'type': 'changed',
                    'old_value': data1[key],
                    'new_value': data2[key]
                    })
                
        elif key in data2:
            result.append({'key': key, 'type': 'added', 'value': data2[key]})

    return render(result)