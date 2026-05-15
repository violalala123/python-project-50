def to_str(value):
    
    if isinstance(value, (dict, list)):
        return '[complex value]'
    
    if isinstance(value, bool):
        return str(value).lower()
    
    if value is None:
        return 'null'
    
    if isinstance(value, str):
        return f"'{value}'"
    
    return str(value)


def render(data, path=''):
    
    result = []
    
    for item in data:
        t = item['type']
        property_path = f"{path}{item['key']}"
        if t == 'nested':
            result.append(render(item['children'], f'{property_path}.'))
        
        elif t == 'added':
            val = f'was added with value: {to_str(item["value"])}'
            result.append(f"Property '{property_path}' {val}")
           
        elif t == 'removed':
            
            result.append(f"Property '{property_path}' was removed")
            
        elif t == 'changed':
            old = to_str(item["old_value"])
            new = to_str(item["new_value"])
            val = f'From {old} to {new}'
            result.append(f"Property '{property_path}' was updated. {val}")
            
    finish = '\n'.join(result)
        
    return f'{finish}'