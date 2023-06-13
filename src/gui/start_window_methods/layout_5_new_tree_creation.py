import json
import os
from functools import partial

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit
from PyQt6.uic.properties import QtGui

from src.definitions.definitions import X2, Y1, X1, WIN_WIDTH, \
    NEW_PARAMETER_WINDOW_HEIGHT, Y4, ROOT_DIR
from src.definitions.ui_css import START_WINDOW_ADD_TREE_CSS
from src.gui.start_window_methods.layout_10_find_relation import \
    load_saved_trees
from src.gui.start_window_methods.start_window_ui_static import \
    add_tree_to_saved_trees


def add_tree_main_clicked(self):
    # TODO redundancja
    self.clear_ui()
    self.error_label.setText(" ")
    self.MainWindow.setStyleSheet(START_WINDOW_ADD_TREE_CSS)
    self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
    self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1,
                                            NEW_PARAMETER_WINDOW_HEIGHT)
    self.verticalLayoutWidget_7.setGeometry(X1,
                                            Y1 +
                                            NEW_PARAMETER_WINDOW_HEIGHT,
                                            WIN_WIDTH - X1,
                                            Y4 -
                                            NEW_PARAMETER_WINDOW_HEIGHT -
                                            Y1)

    self.name_lbl.setText("podaj nazwę drzewa:")
    self.verticalLayout_6.addWidget(self.name_lbl)

    self.e1 = QLineEdit(self.verticalLayoutWidget_6)
    self.e1.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e1)

    self.add_tree_main_bt.setAutoDefault(False)
    self.add_tree_main_bt.setObjectName("add_tree_main")
    self.add_tree_main_bt.clicked.connect(partial(make_new_tree, self))
    self.verticalLayout_6.addWidget(self.add_tree_main_bt)
    self.add_tree_main_bt.setText("Utwórz drzewo o takiej nazwie")


def make_new_tree(self):
    if self.e1.text().strip() != "":
        load_saved_trees(self)
        if self.e1.text() in self.trees_list:
            # TODO czy to działa?
            self.error_label.setText(
                "Drzewo o takiej nazwie już istnieje, wybierz inną nazwę")
        else:
            with open(
                    ROOT_DIR + "\\resources\\Tree_files\\" + self.e1.text()
                    + ".json", "w") as file:
                json.dump([], file)
            os.mkdir(
                ROOT_DIR + "\\resources\\information\\" + self.e1.text())
            with open(
                    ROOT_DIR + "\\resources\\information\\" +
                    self.e1.text() + "\\death_reasons.json", "w") as file:
                json.dump([], file)
            with open(
                    ROOT_DIR + "\\resources\\information\\" +
                    self.e1.text() + "\\illnesses.json", "w") as file:
                json.dump([], file)
            with open(
                    ROOT_DIR + "\\resources\\information\\" +
                    self.e1.text() + "\\professions.json", "w") as file:
                json.dump([], file)
            with open(
                    ROOT_DIR + "\\resources\\information\\" +
                    self.e1.text() + "\\cities.json", "w") as file:
                json.dump([], file)
            add_tree_to_saved_trees(
                ROOT_DIR + "\\resources\\Tree_files\\" + self.e1.text() +
                ".json")
            self.error_label.setText(
                f"Udało się dodać drzewo {self.e1.text()}")
    else:
        self.error_label.setText(
            "Wpisz te nazwe drzewa, bo jeszcze się apka wywali")
