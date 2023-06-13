from _csv import reader

from PyQt6 import QtWidgets

from src.Funtcions.find_family_relation import find_family_relation
from src.definitions.definitions import X2, Y1, X1, WIN_WIDTH, Y4, \
    NEW_PARAMETER_WINDOW_HEIGHT, ROOT_DIR
from src.definitions.ui_css import START_WINDOW_FIND_RELATION_CSS
from src.gui.start_window_methods.layout_2 import update_dicts


def find_relation_clicked(self):
    self.clear_ui()
    self.error_label.setText(" ")
    self.MainWindow.setStyleSheet(START_WINDOW_FIND_RELATION_CSS)
    self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
    self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, Y4)
    self.verticalLayoutWidget_7.setGeometry(X1,
                                            Y1 +
                                            NEW_PARAMETER_WINDOW_HEIGHT,
                                            0, 0)

    self.tree_lbl.setText("wybierz drzewo w którym szukamy relację:")
    self.verticalLayout_6.addWidget(self.tree_lbl)

    load_saved_trees(self)
    self.trees = QtWidgets.QComboBox()
    self.trees.setPlaceholderText("wybierz drzewo")
    self.trees.addItems(self.trees_list)
    self.verticalLayout_6.addWidget(self.trees)

    self.verticalLayout_6.addWidget(self.choose_tree_to_find)

    self.name_lbl.setText("wybierz pierwszą osobę:")
    self.verticalLayout_6.addWidget(self.name_lbl)

    self.e5.clear()
    self.verticalLayout_6.addWidget(self.e5)
    self.e5.setDisabled(True)

    self.name2_lbl.setText("wybierz drugą osobę:")
    self.verticalLayout_6.addWidget(self.name2_lbl)

    self.e6.clear()
    self.verticalLayout_6.addWidget(self.e6)
    self.e6.setDisabled(True)

    self.find_relation_inside.setAutoDefault(False)
    self.verticalLayout_6.addWidget(self.find_relation_inside)
    self.find_relation_inside.setDisabled(True)

    self.info_label.setText("")
    self.verticalLayout_6.addWidget(self.info_label)


def find_relation_inside_clicked(self):
    first_person = self.e5.currentText()
    second_person = self.e6.currentText()
    first_id = self.people_dict.get(first_person)
    second_id = self.people_dict.get(second_person)
    text_to_show = find_family_relation(first_id, second_id,
                                        self.tree_to_open)
    self.info_label.setText(text_to_show)


def chose_tree_to_find_relation_clicked(self):
    self.tree_to_open = self.trees.currentText()
    update_dicts(self)
    self.e6.addItems(self.people_dict.keys())
    self.e5.addItems(self.people_dict.keys())
    self.e5.setDisabled(False)
    self.e6.setDisabled(False)
    self.find_relation_inside.setDisabled(False)


def load_saved_trees(self):
    self.trees_list = []
    with open(ROOT_DIR + "\\resources\\saved_trees.csv", "r") as file:
        csvreader = reader(file)
        for row in csvreader:
            self.trees_list.append(row[1].strip())
