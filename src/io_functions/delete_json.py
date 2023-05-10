

def delete_json(file_name:str)->str:
    if file_name.endswith('.json'):
        return file_name[:-5]
    else:
        return file_name