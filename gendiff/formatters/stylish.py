from gendiff.formatters.to_string import to_string


def render(data, depth=1):
    spaces_not_marker = ' ' * (depth * 4)
    
    spaces_and_marker = ' ' * (depth * 4 - 2)
    
    spaces_end = ' ' * (depth * 4 - 4)
    
    result = []
    
    nl = '\n'
    
    for item in data:
        t = item['type']
        
        if t == 'nested':
            nested_outpud = render(item['children'], depth + 1)
            result.append(f'{spaces_not_marker}{item["key"]}: {nested_outpud}')
        
        elif t == 'added':
            val = to_string(item["value"], depth + 1)
            result.append(f'{spaces_and_marker}+ {item["key"]}: {val}')
           
        elif t == 'removed':
            val = to_string(item["value"], depth + 1)
            result.append(f'{spaces_and_marker}- {item["key"]}: {val}')
            
        elif t == 'unchanged':
            val = to_string(item["value"], depth + 1)
            result.append(f'{spaces_and_marker}  {item["key"]}: {val}')
            
        elif t == 'changed':
            old_val = to_string(item["old_value"], depth + 1)
            new_val = to_string(item["new_value"], depth + 1)
            result.append(f'{spaces_and_marker}- {item["key"]}: {old_val}')
            result.append(f'{spaces_and_marker}+ {item["key"]}: {new_val}')
        
    finish = '\n'.join(result)
        
    return f'{{{nl}{finish}{nl}{spaces_end}}}'