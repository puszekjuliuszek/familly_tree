import json
from functools import partial

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit

from src.Funtcions.uodate_partners import update_partners
from src.definitions.definitions import X1, Y1, X2, WIN_HEIGHT, WIN_WIDTH, Y3, \
    ROOT_DIR
from src.definitions.ui_css import START_WINDOW_PREPARE_BACKGROUND_CSS
from src.gui.multi_combobox import CheckableComboBox
from src.gui.start_window_methods.start_window_ui_static import \
    pyqt_date_to_json_date
from src.io_functions.json_to_list import json_to_dict
from src.io_functions.read_people import read_people_to_dict


def prepare_background(self):
    self.clear_ui()
    self.error_label.setText(" ")

    self.MainWindow.setStyleSheet(START_WINDOW_PREPARE_BACKGROUND_CSS)
    self.tree_to_open = None
    self.add_saved_trees()
    self.verticalLayoutWidget_4.setGeometry(X1, Y1, X2 - X1,
                                            WIN_HEIGHT - Y1)
    self.verticalLayoutWidget_6.setGeometry(X2, Y1, WIN_WIDTH - X2,
                                            WIN_HEIGHT - Y1)
    self.verticalLayoutWidget_7.setGeometry(X2, Y3, 0, 0)
    self.name_lbl.setText("imię:")
    self.verticalLayout_6.addWidget(self.name_lbl)
    self.e1 = QLineEdit(self.verticalLayoutWidget_6)
    self.e1.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e1)

    surname_lbl = QtWidgets.QLabel()
    surname_lbl.setText("nazwisko:")
    self.verticalLayout_6.addWidget(surname_lbl)
    self.e2 = QLineEdit()
    self.e2.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e2)

    birth_lbl = QtWidgets.QLabel()
    birth_lbl.setText("data urodzenia:")
    self.verticalLayout_6.addWidget(birth_lbl)
    self.e3 = QtWidgets.QDateEdit()
    self.e3.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e3)

    death_lbl = QtWidgets.QLabel()
    death_lbl.setText("data śmierci:")
    self.is_dead = QtWidgets.QCheckBox()
    self.is_dead.setText("ten człowiek żyje")
    self.verticalLayout_6.addWidget(death_lbl)
    self.verticalLayout_6.addWidget(self.is_dead)
    self.e4 = QtWidgets.QDateEdit()
    self.e4.setFont(QFont("Arial", 11))
    self.is_dead.clicked.connect(partial(is_dead_clicked,self))
    self.verticalLayout_6.addWidget(self.e4)

    father_lbl = QtWidgets.QLabel()
    father_lbl.setText("ojciec:")
    self.verticalLayout_6.addWidget(father_lbl)
    self.e5.clear()
    self.e5.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e5)

    mother_lbl = QtWidgets.QLabel()
    mother_lbl.setText("matka:")
    self.verticalLayout_6.addWidget(mother_lbl)
    self.e6.clear()
    self.e6.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e6)

    partners_lbl = QtWidgets.QLabel()
    partners_lbl.setText("partnerzy:")
    self.verticalLayout_6.addWidget(partners_lbl)
    self.e8 = CheckableComboBox()
    self.e8.clear()
    self.verticalLayout_6.addWidget(self.e8)

    gender_lbl = QtWidgets.QLabel()
    gender_lbl.setText("płeć:")
    self.verticalLayout_6.addWidget(gender_lbl)
    self.e9 = QtWidgets.QComboBox()
    self.e9.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e9)

    death_reason_lbl = QtWidgets.QLabel()
    death_reason_lbl.setText("przyczyna śmierci:")
    self.verticalLayout_6.addWidget(death_reason_lbl)
    self.e10.clear()
    self.e10.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e10)

    birth_place_lbl = QtWidgets.QLabel()
    birth_place_lbl.setText("miejsce urodzenia:")
    self.verticalLayout_6.addWidget(birth_place_lbl)

    self.e11.clear()
    self.e11.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e11)

    professions_lbl = QtWidgets.QLabel()
    professions_lbl.setText("zawody:")
    self.verticalLayout_6.addWidget(professions_lbl)

    self.e12.clear()
    self.verticalLayout_6.addWidget(self.e12)

    illnesses_lbl = QtWidgets.QLabel()
    illnesses_lbl.setText("choroby:")
    self.verticalLayout_6.addWidget(illnesses_lbl)

    self.e13.clear()
    self.verticalLayout_6.addWidget(self.e13)

    residences_lbl = QtWidgets.QLabel()
    residences_lbl.setText("miejsca zamieszkania:")
    self.verticalLayout_6.addWidget(residences_lbl)

    self.e14.clear()
    self.verticalLayout_6.addWidget(self.e14)

    unable_inputs(self, True)


def is_dead_clicked(self) -> None:
    if self.is_dead.isChecked():
        self.e4.setDisabled(True)
        self.e10.setDisabled(True)
    else:
        self.e4.setDisabled(False)
        self.e10.setDisabled(False)


def unable_inputs(self, val: bool):
    self.e1.setDisabled(val)
    self.e2.setDisabled(val)
    self.e3.setDisabled(val)
    self.is_dead.setDisabled(val)
    self.e4.setDisabled(val)
    self.e5.setDisabled(val)
    self.e6.setDisabled(val)
    self.e8.setDisabled(val)
    self.e9.setDisabled(val)
    self.e10.setDisabled(val)
    self.e11.setDisabled(val)
    self.e12.setDisabled(val)
    self.e13.setDisabled(val)
    self.e14.setDisabled(val)


def import_data_from_tree(self) -> None:
    unable_inputs(self, False)
    update_dicts(self)
    put_people_to_combobox(self)


def put_people_to_combobox(self) -> None:
    self.e5.setPlaceholderText(" ")
    self.e6.setPlaceholderText(" ")
    self.e9.setPlaceholderText(" ")
    self.e10.setPlaceholderText(" ")
    self.e11.setPlaceholderText(" ")
    add_items_to_inputs(self)
    set_multiombobox_placeholder_texts(self)


def add_items_to_inputs(self):
    # ojcowie
    self.e5.clear()
    self.e5.addItems(self.man_list)

    # matki
    self.e6.clear()
    self.e6.addItems(self.woman_list)

    # partnerzy
    self.e8.clear()
    self.e8.addItems(self.people_dict.keys())

    # płeć
    self.e9.clear()
    self.e9.addItem("Mężczyzna")
    self.e9.addItem("Kobieta")

    # przyczyna śmierci
    self.e10.clear()
    self.e10.addItems(self.death_reasons)

    # miejsce urodzenia
    self.e11.clear()
    self.e11.addItems(self.places)

    # robota
    self.e12.clear()
    self.e12.addItems(self.professions)

    # choroby
    self.e13.clear()
    self.e13.addItems(self.illnesses)

    # miejsca zamieszkania
    self.e14.clear()
    self.e14.addItems(self.places)


def update_dicts(self) -> None:
    if self.tree_to_open is not None:
        file_path = ROOT_DIR + "\\resources\\information\\" + \
                    self.tree_to_open.split(".")[0]
        self.people_dict = read_people_to_dict(self.tree_to_open)
        self.woman_list = [person for person in self.people_dict.keys() if
                           person.split(" ")[0][-1] == "a"]
        self.man_list = [person for person in self.people_dict.keys() if
                         person.split(" ")[0][-1] != "a"]
        self.places_dicts = json_to_dict(file_path + "\\cities.json")
        self.places = [place for place in self.places_dicts.keys()]
        self.death_reasons_dicts = json_to_dict(
            file_path + "\\death_reasons.json")
        self.death_reasons = [death for death in
                              self.death_reasons_dicts.keys()]
        self.illnesses_dicts = dict(
            json_to_dict(file_path + "\\illnesses.json"))
        self.illnesses = [illness for illness in
                          self.illnesses_dicts.keys()]
        self.professions_dicts = json_to_dict(
            file_path + "\\professions.json")
        self.professions = [profession for profession in
                            self.professions_dicts.keys()]
    else:
        self.error_label.setText(
            "Wiedziałem, że coś źle poklikasz, drzewo wybierz")


def set_multiombobox_placeholder_texts(self):
    self.e8.setPlaceholderText(" ")
    self.e12.setPlaceholderText(" ")
    self.e13.setPlaceholderText(" ")
    self.e14.setPlaceholderText(" ")


def read_inputs(self):
    # father
    self.person_to_edit_father_id = 0
    if self.e5.currentText() != '':
        self.person_to_edit_father_id = self.people_dict.get(
            self.e5.currentText())
    elif self.e5.placeholderText() != ' ':
        self.person_to_edit_father_id = self.people_dict.get(
            self.e5.placeholderText())

    # mother
    self.person_to_edit_mother_id = 0
    if self.e6.currentText() != '':
        self.person_to_edit_mother_id = self.people_dict.get(
            self.e6.currentText())
    elif self.e6.placeholderText() != ' ':
        self.person_to_edit_mother_id = self.people_dict.get(
            self.e6.placeholderText())

    # birthdate
    self.person_to_edit_birth_date = pyqt_date_to_json_date(self.e3.text())

    # death date
    if self.is_dead.isChecked():
        self.person_to_edit_death_date = None
        self.person_to_edit_death_reason = None
    else:
        self.person_to_edit_death_date = pyqt_date_to_json_date(
            self.e4.text())
        self.person_to_edit_death_reason = None
        if self.e10.currentText() != '':
            self.person_to_edit_death_reason = \
                self.death_reasons_dicts.get(self.e10.currentText())
        elif self.e10.placeholderText() != ' ':
            self.person_to_edit_death_reason = \
                self.death_reasons_dicts.get(self.e10.placeholderText())

    # partners
    self.person_to_edit_partners = set()
    for partner in self.e8.currentText().split(", "):
        self.person_to_edit_partners.add(self.people_dict.get(partner))

    # gender
    if self.e9.currentText() == "Kobieta" or self.e9.placeholderText() == \
            "Kobieta":
        self.person_to_edit_gender = 0
    else:
        self.person_to_edit_gender = 1

    # birthplace
    self.person_to_edit_birth_place = None
    if self.e11.currentText() != '':
        self.person_to_edit_birth_place = self.places_dicts.get(
            self.e11.currentText())
    elif self.e11.placeholderText() != ' ':
        self.person_to_edit_birth_place = self.places_dicts.get(
            self.e11.placeholderText())

    # professions
    self.person_to_edit_professions = []
    for profession in self.e12.currentText().split(", "):
        self.person_to_edit_professions.append(
            self.professions_dicts.get(profession))

    # illnesses
    self.person_to_edit_illnesses = []
    for illness in self.e13.currentText().split(", "):
        self.person_to_edit_illnesses.append(
            self.illnesses_dicts.get(illness))

    # residences
    self.person_to_edit_residences = []
    for residence in self.e14.currentText().split(", "):
        self.person_to_edit_residences.append(
            self.places_dicts.get(residence))

    if len(self.person_to_edit_professions) == 1 and \
            self.person_to_edit_professions[0] is None:
        self.person_to_edit_professions = []
    if len(self.person_to_edit_illnesses) == 1 and \
            self.person_to_edit_illnesses[0] is None:
        self.person_to_edit_illnesses = []
    if len(self.person_to_edit_residences) == 1 and \
            self.person_to_edit_residences[0] is None:
        self.person_to_edit_residences = []
    # TODO ciągle nie działa
    if len(self.person_to_edit_partners) == 1 and \
            self.person_to_edit_partners == {None}:
        self.person_to_edit_partners = []


# $$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 2 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def add_person_clicked(self) -> None:
    prepare_background(self)
    self.add_person_bt = QtWidgets.QPushButton(parent=self.central_widget)
    self.add_person_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
    font = QtGui.QFont()
    font.setFamily("Calibri")
    font.setPointSize(12)
    self.add_person_bt.setFont(font)
    self.add_person_bt.setObjectName("add_person_bt")
    self.verticalLayout_6.addWidget(self.add_person_bt)
    self.add_person_bt.clicked.connect(partial(enter_person, self))
    self.add_person_bt.setDisabled(True)

    choose_tree_bt = QtWidgets.QPushButton(parent=self.central_widget)
    font = QtGui.QFont()
    font.setFamily("Calibri")
    font.setPointSize(12)
    choose_tree_bt.setFont(font)
    choose_tree_bt.setObjectName("add_person_bt")
    choose_tree_bt.setText("do tego drzewa dodaj")
    self.verticalLayout_4.addWidget(choose_tree_bt)
    choose_tree_bt.clicked.connect(partial(_choose_tree_bt_clicked, self))

    self.add_person_bt.setText("Dodaj tę osobę")


def _choose_tree_bt_clicked(self):
    import_data_from_tree(self)
    self.add_person_bt.setDisabled(False)


def enter_person(self) -> None:
    """ Dopisywanie nowej osoby do pliku drzewa """
    # TODO czy to nie jest redundancja kodu?
    file_path = ROOT_DIR + "\\resources\\Tree_files\\" + self.tree_to_open
    read_inputs(self)
    with open(file_path, "r+") as f:
        file_data = json.load(f)

    new_id = 0
    # file_data.sort(key=lambda x: x["person_id"])
    for person_data in file_data:
        new_id = max(new_id, person_data['person_id'])
    new_id += 1
    update_partners(new_id, self.person_to_edit_partners, file_data)
    person_data_dictionary = {'person_id': new_id,
                              'father_id': self.person_to_edit_father_id,
                              'mother_id': self.person_to_edit_mother_id,
                              'first_name': self.e1.text(),
                              'last_name': self.e2.text(),
                              'birth_date': self.person_to_edit_birth_date,
                              'death_date': self.person_to_edit_death_date,
                              'partners_id': list(
                                  self.person_to_edit_partners),
                              'gender': self.person_to_edit_gender,
                              'death_reason':
                                  self.person_to_edit_death_reason,
                              'birth_place':
                                  self.person_to_edit_birth_place,
                              'profession':
                                  self.person_to_edit_professions,
                              'illnesses': self.person_to_edit_illnesses,
                              'residences': self.person_to_edit_residences}

    file_data.append(person_data_dictionary)
    with open(file_path, "w+") as f:
        json.dump(file_data, f)

    self.error_label.setText("Udało się dodać tę osobę")