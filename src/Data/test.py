import json
import os
from src.Classes import Tree_Classes as c
from typing import List


# szukanie Noda na liscie
def binary_search(arr: List[c.Node], target: int, l: int = 0, r: int = None) -> c.Node:
    if r is None:
        r = len(arr) - 1

    mid = (l + r) // 2

    if arr[mid].person.person_id == target:
        return arr[mid]

    if arr[mid].person.person_id < target:
        return binary_search(arr, target, mid + 1, r)
    else:
        return binary_search(arr, target, l, mid - 1, )


def readData(file_name: str, main_person_id: int) -> c.Tree:
    # file name, id of main person, zwaraca obiekt Tree osoby o id równemu main_person_id
    file_path = os.path.join(os.getcwd(), "Tree_files", file_name)
    main_tree_root = None

    with open(file_path) as f:
        data = json.load(f)

    Nodes = []

    for dict in data:
        p = c.Person()  # stworzenie osoby
        p.update_from_dict(dict)
        n = c.Node(p)  # stworzenie noda z tą osoba
        Nodes.append(n)

    Nodes.sort(key=lambda x: x.person.person_id)  # sortowanie po id zeby binary search zadziałał

    # podpinanie nodów do kadego noda po id i tworzenie obiektów drzewa
    for n in Nodes:
        if n.person.person_id != 0:
            if n.person.father_id != 0 and n.person.father_id is not None:
                n.father_node = binary_search(Nodes, n.person.father_id)
            if n.person.mother_id != 0 and n.person.mother_id is not None:
                n.mother_node = binary_search(Nodes, n.person.mother_id)

            for ids in n.person.partners:
                n.partner_nodes.append(binary_search(Nodes, ids))

            for ids in n.person.children:
                n.partner_nodes.append(binary_search(Nodes, ids))

        root = c.Tree(n)
        if n.person.person_id == main_person_id:
            main_tree_root = root

    return main_tree_root


if __name__ == "__main__":
    readData('ZawislakTree.json', 3)