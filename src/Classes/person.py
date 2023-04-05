from collections import deque


class Person:
    # TODO wykorzystać __new__, ni umie

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

    def get_id_list(self, ref_list: list) -> list:
        return_list = []
        for person in ref_list:
            return_list.append(person.person_id)
        return return_list

    def print_person(self):
        print(f"Self: {self}")
        print(f"Person ID: {self.person_id}")
        print(f"Father: {self.father}")
        print(f"Mother: {self.mother}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Birth date: {self.birth_date}")
        print(f"Death date: {self.death_date}")
        print(f"Children ID: {self.get_id_list(self.children)}")
        print(f"Partners ID: {self.get_id_list(self.partners)}")

    def to_dict(self) -> dict:
        if self.father is None:
            father_id = 0
        else:
            father_id = self.father.person_id

        if self.mother is None:
            mother_id = 0
        else:
            mother_id = self.mother.person_id

        return {
            "person_id": self.person_id,
            "father_id": father_id,
            "mother_id": mother_id,
            "partners_id": self.get_id_list(self.partners),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "death_date": self.death_date,
        }

    # TODO wypisywanie na konsolę drzewa, weryfikacja czy działa tak jak trzbea
    def print_tree(self):
        print(f"Głowna osoba w drzewie to {self}")
        if self.father is not None:
            print(f"Jego ojciec to {self.father}")
        if self.mother is not None:
            print(f"Jego matka to {self.mother}")

        queue = deque()
        if self.father.father is not None:
            queue.append((self.father, self.father.father, "F"))
        if self.father.mother is not None:
            queue.append((self.father, self.father.mother, "M"))
        if self.mother.father is not None:
            queue.append((self.mother, self.mother.father, "F"))
        if self.mother.mother is not None:
            queue.append((self.mother, self.mother.mother, "M"))

        while len(queue) > 0:
            main_pearson, parent, parent_type = queue.pop()
            if parent_type == "F":
                print(f"Ojciec {main_pearson} to {parent}")
            else:
                print(f"Matka {main_pearson} to {parent}")

            if parent.father is not None:
                queue.append((parent, parent.father, "F"))
            if parent.mother_node is not None:
                queue.append((parent, parent.mother, "M"))

# class Node:
#     def __init__(self, person: Person):
#         self.person = person
#         self.mother_node = None
#         self.father_node = None
#         self.partner_nodes = []
#         self.children_nodes = []  # dodałem skierowania na nody dzieci, chyba nam potrzebne


# class Tree:
#     def __init__(self, node: Node):
#         self.root = node
#
#     def print_tree(self):
#         print(f"Głowna osoba w drzewie to {self.root.person}")
#         print(f"Jego ojciec to {self.root.father_node.person}")
#         print(f"Jego matka to {self.root.mother_node.person}")
#         queue = deque()
#         if self.root.father_node.father_node is not None:
#             queue.append((self.root.father_node, self.root.father_node.father_node, "F"))
#         if self.root.father_node.mother_node is not None:
#             queue.append((self.root.father_node, self.root.father_node.mother_node, "M"))
#         if self.root.mother_node.father_node is not None:
#             queue.append((self.root.mother_node, self.root.mother_node.father_node, "F"))
#         if self.root.mother_node.mother_node is not None:
#             queue.append((self.root.mother_node, self.root.mother_node.mother_node, "M"))
#         while len(queue)>0:
#             main_pearson, parent, parent_type = queue.pop()
#             if parent_type == "F":
#                 print(f"Ojciec {main_pearson.person} to {parent.person}")
#             else:
#                 print(f"Matka {main_pearson.person} to {parent.person}")
#             if parent.father_node is not None:
#                 queue.append((parent, parent.father_node, "F"))
#             if parent.mother_node is not None:
#                 queue.append((parent, parent.mother_node, "M"))
