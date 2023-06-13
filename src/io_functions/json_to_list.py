import json


def json_to_dict(path: str) -> dict:
    output = {}
    with open(path) as file:
        dicts_list = json.load(file)
    for dictionary in dicts_list:
        output[dictionary['name']] = dictionary['id']
        # TODO jakoś, żeby nie było zależne od id oraz name
    return output
