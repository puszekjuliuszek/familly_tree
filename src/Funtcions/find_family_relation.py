from src.io_functions import read_data as RD
from src.Classes import person
import queue

from enum import Enum


class Relations(Enum):
    CHILDREN = ([[-1, 0, 0]], ("Daughter", "Son"))
    PARENTS = ([[1, 0, 1]], ("Mother", "Father"))
    GRANDPARENTS = ([[2, 0, 2]], ("Grandmother", "Grandfather"))
    GRANDCHILDREN = ([[-2, 0, 0]], ("Granddaughter", "Grandson"))
    SIBLINGS = ([[0, 0, 1]], ("Sister", "Brother"))
    COUSINS = ([[0, 0, 2]], ("Cousin", "Cousin"))
    AUNTandUNCLE = ([[1, 0, 2], [1, 1, 2]], ("Aunt", "Uncle"))
    NEPHEWS = ([[-1, 0, 1], [-1, 1, 1]], ("Nephew", "Nephew"))
    PARTNERS = ([[0, 1, 0]], ("Wife", "Husband"))
    INLAWS = ([[1, 1, 1]], ("Mother-in-law", "Father-in-law"))

    @classmethod
    def get_relation(cls, value: list, personTo: person.Person) -> (bool, str):
        for relation_type in cls:
            for relation_array in relation_type.value[0]:
                if value == relation_array:
                    return True, relation_type.value[1][personTo.gender]
        return False, "[Error] Cannot find family relation between this people"


def BFS(personFirst: person.Person, personSecond: person.Person = None):
    # print("From: ", personFirst)
    # print("To: ", personSecond)

    visited = set()
    graph_path = {personFirst: None}
    Q = queue.Queue()
    Q.put(personFirst)
    visited.add(personFirst)

    while not Q.empty():
        person_now = Q.get()

        if person_now.father is not None and person_now.father != 0:
            if person_now.father not in visited:
                visited.add(person_now.father)
                graph_path[person_now.father] = person_now
                Q.put(person_now.father)

        if person_now.mother is not None and person_now.mother != 0:
            if person_now.mother not in visited:
                visited.add(person_now.mother)
                graph_path[person_now.mother] = person_now
                Q.put(person_now.mother)

        for person_partner in person_now.partners:
            if person_partner not in visited:
                visited.add(person_partner)
                graph_path[person_partner] = person_now
                Q.put(person_partner)

        for person_child in person_now.children:
            if person_child not in visited:
                visited.add(person_child)
                graph_path[person_child] = person_now
                Q.put(person_child)

    pointer = personSecond
    path = []
    while pointer is not None:
        path.append(pointer)
        pointer = graph_path.get(pointer)

    return path[::-1]


def get_relation_array(path: list):
    relation_array = [0, 0, 0]

    person_tmp = path[0]
    for person_next in path[1:]:
        if person_tmp.mother == person_next or person_tmp.father == person_next:
            relation_array[0] += 1
            relation_array[2] = max(relation_array[0], relation_array[2])
        if person_next in person_tmp.partners:
            relation_array[1] += 1

        if person_next in person_tmp.children:
            relation_array[0] -= 1
            relation_array[2] = max(relation_array[0], relation_array[2])
        person_tmp = person_next

    return relation_array


def find_family_relation(personFrom_id: int, personTo_id: int, file_name: str) -> str:

    if personTo_id == personFrom_id:
        return "Received same person on both sides!"

    personFrom, personTo = RD.read_data(file_name, personFrom_id, personTo_id, True)


    if personFrom is None or personTo is None:
        return "Something went wrong during finding people in tree"

    path_between = BFS(personFrom, personTo)
    relation_array = get_relation_array(path_between)
    relation_found, relation_type = Relations.get_relation(relation_array, personTo)

    if relation_found:
        return f'{personTo} is {relation_type.lower()} to {personFrom}'
    else:
        return relation_type


if __name__ == "__main__":
    find_family_relation(1, 5, "Zawislak2.json")

    # main_person, person_list = RD.read_data("Zawislak2.json", flag=True)
    # print("From read:")
    # for p in range(len(person_list)):
    #     print(p, ":", person_list[p])
    # print("Start:")
    # find_family_relation(person_list[1], person_list[7])
