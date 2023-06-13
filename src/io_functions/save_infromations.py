import json
from src.definitions.definitions import ROOT_DIR


def save_information(file_name: str, given_names):
    if given_names is None:
        return None
    if given_names is []:
        return []

    file_path = ROOT_DIR + "\\resources\\information\\" + file_name

    with open(file_path) as f:
        json_data = json.load(f)

    if isinstance(given_names, list):
        found_ids = []
        for information_data in json_data:
            if information_data['name'] in given_names:
                found_ids.append(information_data['id'])
        return found_ids
    else:
        for information_data in json_data:
            if information_data['name'] == given_names:
                return information_data['id']

    return None
