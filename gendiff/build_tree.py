def build_tree(data1, data2):
       
    keys = sorted(data1 | data2)
    result = []
    
    for key in keys:
        
        if key in data1 and key not in data2:
            result.append({'key': key, 'type': 'removed', 'value': data1[key]})
            
        elif key not in data1 and key in data2:
            result.append({'key': key, 'type': 'added', 'value': data2[key]}) 

        elif key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result.append({
                    'key': key,
                    'type': 'nested',
                    'children': build_tree(data1[key], data2[key])
                })
                    
            elif data1[key] == data2[key]:
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
                
    return result