from collections import deque

class Person:
    def __init__(self):
        self.person_id = None
        self.father_id = None
        self.mother_id = None
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.death_date = None
        self.children = []
        self.partners = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    #dodałem dwie metody do czytania i sprawdzania danych
    def update_from_dict(self, data: dict):
        self.person_id = data.get('person_id', self.person_id)
        self.father_id = data.get('father_id', self.father_id)
        self.mother_id = data.get('mother_id', self.mother_id)
        self.first_name = data.get('first_name', self.first_name)
        self.last_name = data.get('last_name', self.last_name)
        self.birth_date = data.get('birth_date', self.birth_date)
        self.death_date = data.get('death_date', self.death_date)
        self.children = data.get('children', self.children)
        self.partners = data.get('partners', self.partners)

    def print_person(self):
        print(f"Person ID: {self.person_id}")
        print(f"Father ID: {self.father_id}")
        print(f"Mother ID: {self.mother_id}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Birth date: {self.birth_date}")
        print(f"Death date: {self.death_date}")
        print(f"Children: {self.children}")
        print(f"Partners: {self.partners}")

    def to_dict(self) -> dict:
        return {
            "person_id": self.person_id,
            "father_id": self.father_id,
            "mother_id": self.mother_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "death_date": self.death_date,
            "children": self.children,
            "partners": self.partners,
        }

class Node:
    def __init__(self, person: Person):
        self.person = person
        self.mother_node = None
        self.father_node = None
        self.partner_nodes = []
        self.children_nodes = []  # dodałem skierowania na nody dzieci, chyba nam potrzebne


class Tree:
    def __init__(self, node: Node):
        self.root = node

    def print_tree(self):
        print(f"Głowna osoba w drzewie to {self.root.person}")
        print(f"Jego ojciec to {self.root.father_node.person}")
        print(f"Jego matka to {self.root.mother_node.person}")
        queue = deque()
        if self.root.father_node.father_node is not None:
            queue.append((self.root.father_node, self.root.father_node.father_node, "F"))
        if self.root.father_node.mother_node is not None:
            queue.append((self.root.father_node, self.root.father_node.mother_node, "M"))
        if self.root.mother_node.father_node is not None:
            queue.append((self.root.mother_node, self.root.mother_node.father_node, "F"))
        if self.root.mother_node.mother_node is not None:
            queue.append((self.root.mother_node, self.root.mother_node.mother_node, "M"))
        while len(queue)>0:
            main_pearson, parent, parent_type = queue.pop()
            if parent_type == "F":
                print(f"Ojciec {main_pearson.person} to {parent.person}")
            else:
                print(f"Matka {main_pearson.person} to {parent.person}")
            if parent.father_node is not None:
                queue.append((parent, parent.father_node, "F"))
            if parent.mother_node is not None:
                queue.append((parent, parent.mother_node, "M"))
