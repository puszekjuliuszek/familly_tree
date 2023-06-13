import json
from src.Classes import person
from src.definitions.definitions import ROOT_DIR
from src.io_functions import delete_json as DJ


def read_data(file_name: str, main_person_id: int = 1, personTo_id: int = -1,
              flag: bool = False) -> person.Person:
    file_path = ROOT_DIR + "\\resources\\Tree_files\\" + file_name
    main_person = None
    personTo = None

    with open(file_path) as f:
        json_data = json.load(f)

    json_data.sort(key=lambda x: x["person_id"])
    persons_list = []
    for data_dict in json_data:
        persons_list.append(
            person.Person(DJ.delete_json(file_name), data_dict=data_dict))

    for iterator in range(len(json_data)):
        now_person = persons_list[iterator]
        father_id = json_data[iterator].get("father_id")
        mother_id = json_data[iterator].get("mother_id")
        partners_id = json_data[iterator].get("partners_id")

        if father_id != 0:
            mid = binary_search(json_data, father_id)
            now_person.father = persons_list[mid]
            persons_list[mid].children.append(now_person)

        if mother_id != 0:
            mid = binary_search(json_data, mother_id)
            now_person.mother = persons_list[mid]
            persons_list[mid].children.append(now_person)

        for index in partners_id:
            mid = binary_search(json_data, index)
            now_person.partners.append(persons_list[mid])

        if now_person.person_id == main_person_id:
            main_person = now_person
        if now_person.person_id == personTo_id and personTo_id != -1:
            personTo = now_person

    if personTo_id != -1:
        return main_person, personTo

    if main_person is None:
        main_person = persons_list[0]

    if flag:
        return main_person, persons_list

    return main_person


def binary_search(arr: list, target: int, left: int = 0,
                  right: int = None) -> int:
    if right is None:
        right = len(arr) - 1

    mid = (left + right) // 2

    if arr[mid].get("person_id") == target:
        return mid

    if arr[mid].get("person_id") < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1, )
