import json
import os
from src.Classes import person
import queue


def save_data(start_person: person.Person, file_name: str) -> None:
    file_path = os.path.join(os.getcwd(), "Tree_files", file_name)
    Q = queue.Queue()
    Q.put(start_person)
    dict_list = []
    # BFS <3
    while not Q.empty():
        now_person = Q.get()
        if now_person.to_dict() not in dict_list:
            dict_list.append(now_person.to_dict())
            if now_person.mother is not None:
                Q.put(now_person.mother)
            if now_person.father is not None:
                Q.put(now_person.father)

            for partner in now_person.partners:
                Q.put(partner)

            for child in now_person.children:
                Q.put(child)

    with open(file_path, "w+") as f:
        json.dump(dict_list, f)
    return


def binary_search(arr: list, target: int, l: int = 0, r: int = None) -> int:
    if r is None:
        r = len(arr) - 1

    mid = (l + r) // 2

    if arr[mid].get("person_id") == target:
        return mid

    if arr[mid].get("person_id") < target:
        return binary_search(arr, target, mid + 1, r)
    else:
        return binary_search(arr, target, l, mid - 1, )


def read_data(file_name: str, main_person_id: int) -> person.Person:
    file_path = os.path.join(os.getcwd(), "Tree_files", file_name)
    main_person = None

    with open(file_path) as f:
        json_data = json.load(f)

    json_data.sort(key=lambda x: x["person_id"])
    persons_list = []
    for data_dict in json_data:
        persons_list.append(person.Person(data_dict=data_dict))

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

        for id in partners_id:
            mid = binary_search(json_data, id)
            now_person.partners.append(persons_list[mid])

        if now_person.person_id == main_person_id:
            main_person = now_person

    return main_person


if __name__ == "__main__":
    main_person = read_data('Zawislak2.json', 10)
    main_person.print_tree()
    save_data(main_person, "Zawislak3.json")
