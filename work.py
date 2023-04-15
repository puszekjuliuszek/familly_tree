import json
from collections import deque
class Person:
    def __init__(self, data_dict=None):
        self.person_id = None
        self.father = None
        self.mother = None
        self.children = []
        self.partners = []
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.death_date = None
        if data_dict is not None:
            self.person_id = data_dict.get('person_id')
            self.first_name = data_dict.get('first_name')
            self.last_name = data_dict.get('last_name')
            self.birth_date = data_dict.get('birth_date')
            self.death_date = data_dict.get('death_date')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def read_data(main_person_id: int = 3):
    main_person = None

    with open("Zawislak2.json") as f:
        json_data = json.load(f)

    json_data.sort(key=lambda x: x["person_id"])
    persons_list = []
    for data_dict in json_data:
        persons_list.append(Person(data_dict=data_dict))

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

    main_person = persons_list[1]
    return main_person


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


P = read_data()


# tu dodawać do tree_window_ui
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

def on_node_click(event):
    node_text = event.artist.get_text()
    node_num = str(node_text)
    print(f"Kliknięto węzeł {node_num}")

def setup_ui(person):
    G = nx.Graph()
    G.add_node(str(person))

    already_added = set()
    queue = deque()
    queue.append(person)
    already_added.add(person)

    while len(queue) > 0:
        person_tmp = queue.pop()
        print(person_tmp)
        for person_partner in person_tmp.partners:
            if person_partner not in already_added:
                already_added.add(person_partner)
                queue.append(person_partner)
            G.add_node(str(person_partner))
            G.add_edge(str(person_tmp), str(person_partner))

        for person_child in person_tmp.children:
            if person_child not in already_added:
                already_added.add(person_child)
                queue.append(person_child)
            G.add_node(str(person_child))
            G.add_edge(str(person_tmp), str(person_child))

        if person_tmp.mother is not None:
            if person_tmp.mother not in already_added:
                already_added.add(person_tmp.mother)
                queue.append(person_tmp.mother)
            G.add_node(str(person_tmp.mother))
            G.add_edge(str(person_tmp), str(person_tmp.mother))

        if person_tmp.father is not None:
            if person_tmp.father not in already_added:
                already_added.add(person_tmp.father)
                queue.append(person_tmp.father)
            G.add_node(str(person_tmp.father))
            G.add_edge(str(person_tmp), str(person_tmp.father))



    pos = nx.spring_layout(G)
    nx.draw(G,pos)
    ax = plt.gca()

    for node in G.nodes:
        button = ax.annotate(str(node), xy=pos[node], ha="center", va="center")
        button.set_picker(True)

    fig = plt.gcf()
    fig.canvas.mpl_connect('pick_event', on_node_click)
    canvas = FigureCanvas(fig)


    # TODO podłączyć do wysztkiego
    app = QApplication([])
    window = QMainWindow()
    widget = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(canvas)
    widget.setLayout(layout)
    window.setCentralWidget(widget)
    window.show()
    app.exec()

    return G

G = setup_ui(P)
