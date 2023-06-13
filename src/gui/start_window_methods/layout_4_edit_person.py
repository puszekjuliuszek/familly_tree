import json
from functools import partial

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QFont

from src.Funtcions.uodate_partners import update_partners
from src.definitions.definitions import X1, Y1, X2, Y3, WIN_HEIGHT, ROOT_DIR
from src.definitions.ui_css import START_WINDOW_EDIT_PERSON_CLICKED
from src.gui.start_window_methods.layout_2 import update_dicts, \
    prepare_background, unable_inputs, add_items_to_inputs, read_inputs
from src.io_functions.read_data import read_data


def edit_person_clicked(self) -> None:
    prepare_background(self)
    self.verticalLayoutWidget_4.setGeometry(X1, Y1, X2 - X1, Y3 - Y1)
    self.verticalLayoutWidget_7.setGeometry(X1, Y3, X2 - X1,
                                            WIN_HEIGHT - Y3)
    self.MainWindow.setStyleSheet(START_WINDOW_EDIT_PERSON_CLICKED)

    self.edit_person_bt = QtWidgets.QPushButton(parent=self.central_widget)
    self.edit_person_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
    self.edit_person_bt.setObjectName("edit_person_bt")
    self.verticalLayout_6.addWidget(self.edit_person_bt)
    self.edit_person_bt.clicked.connect(partial(edit_person_data,self))
    self.edit_person_bt.setText("na takie zmień dane tej osoby")

    self.choose_tree_bt = QtWidgets.QPushButton(parent=self.central_widget)
    self.choose_tree_bt.setObjectName("choose_tree_bt")
    self.choose_tree_bt.setText("w tym drzewie wybierz \n osobę")
    self.verticalLayout_4.addWidget(self.choose_tree_bt)
    self.choose_tree_bt.clicked.connect(
        partial(import_people_from_tree_to_edit,self))

    self.choose_person_to_edit = QtWidgets.QPushButton(
        parent=self.central_widget)
    self.choose_person_to_edit.setObjectName("choose_person_to_edit")
    self.choose_person_to_edit.setText("tę osobę edytuj")
    self.choose_person_to_edit.clicked.connect(
        partial(choose_person_to_edit_clicked, self))

    person_lbl = QtWidgets.QLabel()
    person_lbl.setText("wybierz osobę do edycji:")
    self.verticalLayout_7.addWidget(person_lbl)
    self.e7 = QtWidgets.QComboBox()
    self.e7.setFont(QFont("Arial", 11))
    self.verticalLayout_7.addWidget(self.e7)
    self.verticalLayout_7.addWidget(self.choose_person_to_edit)

    unable_inputs(self, True)
    self.e7.setDisabled(True)
    self.choose_person_to_edit.setDisabled(True)
    self.edit_person_bt.setDisabled(True)


def edit_person_data(self) -> None:
    # TODO tu mamy redundancje kodu, trzeba coś z tym zrobić, powtarza się
    #  to w jakieś tam metodzie wyżej
    file_path = ROOT_DIR + "\\resources\\Tree_files\\" + self.tree_to_open
    with open(file_path, "r+") as f:
        file_data = json.load(f)
    id_to_remove = None
    for i in range(len(file_data)):
        if file_data[i]['person_id'] == self.id_to_edit:
            id_to_remove = i
    if id_to_remove is not None:
        file_data.pop(id_to_remove)

    read_inputs(self)
    update_partners(self.id_to_edit, self.person_to_edit_partners,
                    file_data)
    person_data_dictionary = {'person_id': self.id_to_edit,
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

    self.error_label.setText("Udało się zmienić dane")


def import_people_from_tree_to_edit(self) -> None:
    update_dicts(self)
    self.e7.setPlaceholderText("wybierz osobę")
    self.e7.setDisabled(False)
    self.choose_person_to_edit.setDisabled(False)
    for person in self.people_dict:
        self.e7.addItem(person)


def choose_person_to_edit_clicked(self) -> None:
    self.id_to_edit = 0
    for person in self.people_dict:
        if person == self.e7.currentText():
            self.id_to_edit = self.people_dict.get(person)
    self.person_to_edit = read_data(self.tree_to_open, self.id_to_edit)
    self.e1.setDisabled(False)
    self.e1.setText(self.person_to_edit.first_name)
    self.e2.setDisabled(False)
    self.e2.setText(self.person_to_edit.last_name)
    self.e3.setDisabled(False)
    birth_date = self.person_to_edit.birth_date.split("-")
    self.e3.setDate(QtCore.QDate(int(birth_date[2]), int(birth_date[1]),
                                 int(birth_date[0])))
    self.is_dead.setDisabled(False)
    if self.person_to_edit.death_date is None:
        self.is_dead.setChecked(True)
        self.e10.setPlaceholderText(" ")
    else:
        self.e4.setDisabled(False)
        if self.person_to_edit.death_reason is not None:
            self.e10.setPlaceholderText(self.person_to_edit.death_reason)
        else:
            self.e10.setPlaceholderText(" ")
    self.e5.setDisabled(False)
    if self.person_to_edit.father is not None:
        self.e5.setPlaceholderText(
            f"{self.person_to_edit.father.first_name} "
            f"{self.person_to_edit.father.last_name}")
    else:
        self.e5.setPlaceholderText(" ")
    self.e6.setDisabled(False)
    if self.person_to_edit.mother is not None:
        self.e6.setPlaceholderText(
            f"{self.person_to_edit.mother.first_name} "
            f"{self.person_to_edit.mother.last_name}")
    else:
        self.e6.setPlaceholderText(" ")
    self.e9.setDisabled(False)
    self.e9.setPlaceholderText(
        "Mężczyzna" if self.person_to_edit.gender == 1 else "Kobieta")
    self.e8.setDisabled(False)
    self.e10.setDisabled(False)
    self.e11.setDisabled(False)
    if self.person_to_edit.birth_place is not None:
        self.e11.setPlaceholderText(self.person_to_edit.birth_place)
    else:
        self.e11.setPlaceholderText(" ")
    self.e12.setDisabled(False)
    self.e13.setDisabled(False)
    self.e14.setDisabled(False)
    self.edit_person_bt.setDisabled(False)
    add_items_to_inputs(self)
    self.e8.set_items(
        [str(person) for person in self.person_to_edit.partners])
    self.e12.set_items(self.person_to_edit.profession)
    self.e13.set_items(self.person_to_edit.illnesses)
    self.e14.set_items(self.person_to_edit.residences)
