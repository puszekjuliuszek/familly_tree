from collections import deque
from src.io_functions import read_informations as RI
from src.io_functions import save_infromations as SI


class Person:
    def __init__(self, tree_name, data_dict=None):
        self.person_id = None
        self.father = None
        self.mother = None
        self.children = []
        self.partners = []
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.death_date = None

        self.gender = None
        self.death_reason = None
        self.brith_place = None
        self.profession = None
        self.illnesses = []
        self.residences = []
        self.tree_name = tree_name

        if data_dict is not None:
            self.person_id = data_dict.get('person_id')
            self.first_name = data_dict.get('first_name')
            self.last_name = data_dict.get('last_name')
            self.birth_date = data_dict.get('birth_date')
            self.death_date = data_dict.get('death_date')
            self.gender = data_dict.get('gender')
            self.death_reason = RI.read_informations(f'{self.tree_name}\\death_reasons.json',
                                                     data_dict.get('death_reason'))
            self.birth_place = RI.read_informations(f'{self.tree_name}\\cities.json', data_dict.get('birth_place'))
            self.profession = RI.read_informations(f'{self.tree_name}\\professions.json', data_dict.get('profession'))
            # TODO nie działa jak illnesses puste
            self.illnesses = RI.read_informations(f'{self.tree_name}\\illnesses.json', data_dict.get('illnesses'))
            self.residences = RI.read_informations(f'{self.tree_name}\\cities.json', data_dict.get('residences'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def get_id_list(ref_list: list) -> list:
        return_list = []
        for person in ref_list:
            return_list.append(person.person_id)
        return return_list

    def print_person(self):
        print(f"Person ID: {self.person_id}")
        print(f"Father: {self.father}")
        print(f"Mother: {self.mother}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Birth date: {self.birth_date}")
        if self.death_date is not None:
            print(f"Death date: {self.death_date}")
        else:
            print(f"Death date: Alive")
        if self.gender == 1:
            print("Gender: Male")
        else:
            print("Gender: Female")
        print(f"Children ID: {self.get_id_list(self.children)}")
        print(f"Partners ID: {self.get_id_list(self.partners)}")

        print(f"Birth place: {self.birth_place}")
        if self.death_date is not None:
            print(f"Death reason: {self.death_reason}")
        print(f"Residences: {self.residences}")
        if self.profession != []:
            print(f"Profession: {self.profession}")
        print(f"Illnesses: {self.illnesses}")
        print(f"Family Tree Name: {self.tree_name}")

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
            "children_id": self.get_id_list(self.children),
            "partners_id": self.get_id_list(self.partners),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "death_date": self.death_date,
            "gender": self.gender,
            "death_reason": SI.save_informations(f'{self.tree_name}\\death_reasons.json', self.death_reason),
            "birth_place": SI.save_informations(f'{self.tree_name}\\cities.json', self.birth_place),
            "profession": SI.save_informations(f'{self.tree_name}\\professions.json', self.profession),
            "illnesses": SI.save_informations(f'{self.tree_name}\\illnesses.json', self.illnesses),
            "residences": SI.save_informations(f'{self.tree_name}\\cities.json', self.residences)
        }

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
            if parent.mother is not None:
                queue.append((parent, parent.mother, "M"))
