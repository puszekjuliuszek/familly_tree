import json
from src.definitions.definitions import ROOT_DIR


def get_id(file_name: str) -> int:
    file_path = ROOT_DIR + "\\resources\\informations\\" + file_name

    with open(file_path) as f:
        json_data = json.load(f)

    json_data.sort(key=lambda x: x['id'])
    new_id = 1

    for dict in json_data:
        if dict['id'] != new_id:
            break
        new_id += 1

    return new_id
