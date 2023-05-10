import json


def json_to_list(path):
    with open(path) as file:
        output = json.load(file)
    return output
