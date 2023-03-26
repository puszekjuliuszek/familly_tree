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
