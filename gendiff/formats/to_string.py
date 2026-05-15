def to_string(value, depth=1):
    if not isinstance(value, dict): 
            
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
        return str(value)
        
    result = []
    nl = '\n'
    spaces_not_marker = ' ' * (depth * 4)
    spaces_end = ' ' * (depth * 4 - 4)
    
    for key, val in value.items():
        result.append(f'{spaces_not_marker}{key}: {to_string(val, depth + 1)}')
        
    final = '\n'.join(result)
    return f"{{{nl}{final}{nl}{spaces_end}}}"  