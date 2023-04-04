import json
import os
from src.Classes import person as c
import queue


# szukanie Noda na liscie
#TODO przebudować wczytywanie i zapisywanie
def binary_search(arr: list, target: int, l: int = 0, r: int = None) -> c.Node:
    if r is None:
        r = len(arr) - 1

    mid = (l + r) // 2

    if arr[mid].person.person_id == target:
        return arr[mid]

    if arr[mid].person.person_id < target:
        return binary_search(arr, target, mid + 1, r)
    else:
        return binary_search(arr, target, l, mid - 1, )


def read_data(file_name: str, main_person_id: int) -> c.Tree:
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

            for ids in n.person.partners_id:
                n.partner_nodes.append(binary_search(Nodes, ids))

            for ids in n.person.children_id:
                n.partner_nodes.append(binary_search(Nodes, ids))

        root = c.Tree(n)
        if n.person.person_id == main_person_id:
            main_tree_root = root

    return main_tree_root


def save_data(root: c.Tree, file_name: str) -> None:
    file_path = os.path.join(os.getcwd(), "Tree_files", file_name)
    Q = queue.Queue()
    Q.put(root.root)
    to_save = []
    # BFS <3
    while not Q.empty():
        node = Q.get()
        if node.person.to_dict() not in to_save:
            to_save.append(node.person.to_dict())
            if node.mother_node is not None:
                Q.put(node.mother_node)
            if node.father_node is not None:
                Q.put(node.father_node)
            for partner in node.partner_nodes:
                Q.put(partner)
            for child in node.children_nodes:
                Q.put(child)

    with open(file_path, "w+") as f:
        json.dump(to_save, f)
    return


if __name__ == "__main__":
    root = read_data('Zawislak2.json', 1)
    root.print_tree()

    save_data(root, "Zawislak2.json")

    root2 = read_data("Zawislak2.json", 3)
