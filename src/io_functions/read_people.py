import json

from src.definitions.definitions import ROOT_DIR


# TODO, mozna poprawic bo juz mamy plec w klasie Person
def read_people_to_dict(file_name: str) -> dict:
    file_path = ROOT_DIR + "\\resources\\Tree_files\\" + file_name

    with open(file_path) as f:
        json_data = json.load(f)

    json_data.sort(key=lambda x: x["person_id"])
    persons_dict = {}
    for data_dict in json_data:
        first_name = data_dict["first_name"]
        last_name = data_dict["last_name"]
        persons_dict[f"{first_name} {last_name}"] = data_dict['person_id']
    return persons_dict
