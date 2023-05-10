import json
from src.definitions.definitions import ROOT_DIR


def binary_search(arr: list, target: int, l: int = 0, r: int = None) -> int:
    if r is None:
        r = len(arr) - 1

    mid = (l + r) // 2

    if arr[mid].get("id") == target:
        return mid

    if arr[mid].get("id") < target:
        return binary_search(arr, target, mid + 1, r)
    else:
        return binary_search(arr, target, l, mid - 1, )


def read_informations(file_name: str, given_id):
    if given_id is None:
        return None
    if given_id is []:
        return []

    file_path = ROOT_DIR + "\\resources\\information\\" + file_name

    with open(file_path) as f:
        json_data = json.load(f)

    json_data.sort(key=lambda x: x['id'])

    if isinstance(given_id, list):
        elements = []
        for id in given_id:
            index = binary_search(json_data, id)
            dict = json_data[index]
            name = dict['name']
            elements.append(name)
        if len(elements) == 1:
            return elements[0]
        return elements
    else:
        index = binary_search(json_data, given_id)
        dict = json_data[index]
        name = dict['name']
        return name

