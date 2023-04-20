import json

from src.definitions.definitions import ROOT_DIR


def read_people_to_list(file_name:str):
    file_path = ROOT_DIR + "\\resources\\Tree_files\\" + file_name

    with open(file_path) as f:
        json_data = json.load(f)

    json_data.sort(key=lambda x: x["person_id"])
    persons_list = []
    for data_dict in json_data:
        first_name=data_dict["first_name"]
        last_name=data_dict["last_name"]
        if first_name[-1] == 'a':
            gender = "W"
        else:
            gender = "M"
        persons_list.append((f"{first_name} {last_name}",data_dict["person_id"], gender))
    return persons_list
