from functools import partial

from PyQt6 import QtCore, QtGui, QtWidgets

from src.definitions.ui_css import START_WINDOW_FIND_PERSON_CSS
from src.gui.person_window import PersonWindow
from src.gui.start_window_methods.layout_2 import prepare_background, \
    import_data_from_tree
from src.io_functions.read_data import read_data


def find_person_clicked(self) -> None:
    prepare_background(self)
    self.MainWindow.setStyleSheet(START_WINDOW_FIND_PERSON_CSS)

    self.find_person_bt = QtWidgets.QPushButton(parent=self.central_widget)
    self.find_person_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
    self.find_person_bt.setObjectName("find_person_bt")
    self.verticalLayout_6.addWidget(self.find_person_bt)
    self.find_person_bt.clicked.connect(partial(find_person_in_tree, self))
    self.find_person_bt.setText("szukaj taką osobę")
    self.find_person_bt.setDisabled(True)

    choose_tree_bt = QtWidgets.QPushButton(parent=self.central_widget)
    font = QtGui.QFont()
    font.setFamily("Calibri")
    font.setPointSize(12)
    choose_tree_bt.setFont(font)
    choose_tree_bt.setObjectName("choose_tree_bt")
    choose_tree_bt.setText("w tym drzewie szukaj")
    self.verticalLayout_4.addWidget(choose_tree_bt)
    choose_tree_bt.clicked.connect(partial(_choose_tree_bt_to_find_in,self))


def _choose_tree_bt_to_find_in(self):
    self.find_person_bt.setDisabled(False)
    import_data_from_tree(self)


def find_person_in_tree(self) -> None:
    main_person_list = read_data(self.tree_to_open, 1, flag=True)[1]
    output_list = []
    visited = set()
    for i in range(len(main_person_list)):
        person_tmp = main_person_list[i]

        if person_tmp.first_name == self.e1.text():
            output_list.append(person_tmp)
        if person_tmp.last_name == self.e2.text():
            output_list.append(person_tmp)
        # TODO szukanie po datach urodzenia i śmierci
        if str(person_tmp.father) == self.e5.currentText():
            output_list.append(person_tmp)
        if str(person_tmp.mother) == self.e6.currentText():
            output_list.append(person_tmp)
        # TODO szukanie po partnerach
        if person_tmp.gender == (
                1 if self.e9.currentText() == "Mężczyzna" else 0):
            output_list.append(person_tmp)
        if person_tmp.birth_place == self.e10.currentText():
            output_list.append(person_tmp)
        if person_tmp.death_reason == self.e11.currentText():
            output_list.append(person_tmp)
        for illness in self.e12.currentText().split(", "):
            if illness in person_tmp.illnesses:
                output_list.append(person_tmp)
        for profession in self.e13.currentText().split(", "):
            if profession in person_tmp.profession:
                output_list.append(person_tmp)
        for residence in self.e14.currentText().split(", "):
            if residence in person_tmp.residences:
                output_list.append(person_tmp)
        visited.add(person_tmp.person_id)

    output_set = set()
    for person in output_list:
        is_ok = True
        if self.e1.text() != '' and person.first_name != self.e1.text():
            is_ok = False
        if self.e2.text() != '' and person.last_name != self.e2.text():
            is_ok = False
        # TODO sprawdzanie ludzi po datach urodzenia i śmierci
        if self.e5.currentText() != '' and str(
                person.father) != self.e5.currentText():
            is_ok = False
        if self.e6.currentText() != '' and str(
                person.mother) == self.e6.currentText():
            is_ok = False
        # TODO sprawdzanie po partnerach
        if self.e9.currentText() != '' and person.gender != (
                1 if self.e9.currentText() == "Mężczyzna" else 0):
            is_ok = False
        if self.e10.currentText() != '' and person.birth_place != \
                self.e10.currentText():
            is_ok = False
        if self.e11.currentText() != '' and person.death_reason != \
                self.e11.currentText():
            is_ok = False
        for illness in self.e12.currentText().split(", "):
            if illness != ' ' and illness not in person.illnesses:
                is_ok = False
        for profession in self.e13.currentText().split(", "):
            if profession != ' ' and profession not in person.profession:
                is_ok = False
        for residence in self.e14.currentText().split(", "):
            if residence != ' ' and residence not in person.residences:
                is_ok = False
        if is_ok:
            output_set.add(person)

    for person in output_set:
        attr_name = "window" + str(person)
        setattr(self, attr_name, PersonWindow(person, self.tree_to_open))
        attr = getattr(self, attr_name)
        attr.show()

    if len(output_set) == 0:
        self.error_label.setText(
            "Nie ma ani jednej osoby speniającej te kryteria")