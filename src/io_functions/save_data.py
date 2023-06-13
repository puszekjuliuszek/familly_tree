import json
from src.Classes import person
import queue

from src.definitions.definitions import ROOT_DIR


def save_data(start_person: person.Person, file_name: str) -> None:
    file_path = ROOT_DIR + "\\resources\\Tree_files\\" + file_name
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
