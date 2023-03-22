class Person:
    def __init__(self):
        self.person_id = None
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.death_date = None
        self.children = []
        self.partners = []
        # self.photo_path = None
        # self.description = None

class Node:
    def __init__(self, person):
        self.person = person
        self.mother_node = None
        self.father_node = None
        self.partner_nodes = []


class Tree:
    def __init__(self, node):
        self.root = node


person = Person()
person.first_name = "Marek"
tree = Tree(Node(person))

