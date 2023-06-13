import json
from functools import partial

from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit

from src.definitions.definitions import X2, Y1, X1, WIN_WIDTH, \
    NEW_PARAMETER_WINDOW_HEIGHT, Y4, ROOT_DIR
from src.definitions.ui_css import START_WINDOW_ADD_CITY_CSS, \
    START_WINDOW_ADD_DEATH_REASON_CSS, START_WINDOW_ADD_ILLNESS_CSS, \
    START_WINDOW_ADD_PROFESSION_CSS
from src.gui.start_window_methods.layout_10_find_relation import \
    load_saved_trees
from src.io_functions.json_to_list import json_to_dict


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przyciski 6,7,8,9 $$$$$$$$$$$$$$$$
def append_parameter_to_file(self, file_path):
        parameter = self.e1.text()
        # TODO niedodawalne jak nie wybierzesz drzewa
        if parameter.strip() != "":
            file_path = ROOT_DIR + "\\resources\\information\\" + \
                        self.trees.currentText().split(".")[0] + file_path
            parameters = json_to_dict(file_path)
            if parameters.get(parameter) is not None:
                self.error_label.setText(
                    "dodawanie nie powiodło się, taka nazwa już istnieje")
            else:
                with open(file_path, "r+") as f:
                    file_data = json.load(f)
                if len(parameters.values()) > 0:
                    dictionary = {'id': max(parameters.values()) + 1,
                                  'name': parameter}
                else:
                    dictionary = {'id': 1, 'name': parameter}
                file_data.append(dictionary)
                with open(file_path, "w+") as f:
                    json.dump(file_data, f)

                self.error_label.setText("dodawanie powiodło się")
        else:
            self.set_error_label_text(
                "prawie apka spadła z rowerka, uff, wybierz drzewo")


# $$$$$$$$$$$$$$$$$$$$$ Przycisk 6 - dodawanie miasta $$$$$$$$$$$$$$$$$$$$$
def add_city_clicked(self):
    # TODO redundancja
    self.clear_ui()
    self.error_label.setText(" ")
    self.MainWindow.setStyleSheet(START_WINDOW_ADD_CITY_CSS)
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

    self.tree_lbl.setText("wybierz drzewo do którego dodajemy miasto:")
    self.verticalLayout_6.addWidget(self.tree_lbl)

    load_saved_trees(self)
    self.trees = QtWidgets.QComboBox()
    self.trees.setPlaceholderText("wybierz drzewo")
    self.trees.addItems(self.trees_list)
    self.verticalLayout_6.addWidget(self.trees)

    self.name_lbl.setText("podaj nazwę miasta:")
    self.verticalLayout_6.addWidget(self.name_lbl)

    self.e1 = QLineEdit(self.verticalLayoutWidget_6)
    self.e1.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e1)

    self.add_city_main_bt.setAutoDefault(False)
    self.add_city_main_bt.clicked.connect(
        partial(append_parameter_to_file, self, "\\cities.json"))
    self.verticalLayout_6.addWidget(self.add_city_main_bt)
    self.add_city_main_bt.setText("Dodaj miasto o takiej nazwie")


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 7 - dodawanie powodu śmierci $$$$$$$
def add_death_reason_clicked(self):
    # TODO redundancja
    self.error_label.setText(" ")
    self.clear_ui()
    self.MainWindow.setStyleSheet(START_WINDOW_ADD_DEATH_REASON_CSS)
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

    self.tree_lbl.setText("wybierz drzewo do którego dodajemy powód "
                          "śmierci:")
    self.verticalLayout_6.addWidget(self.tree_lbl)

    load_saved_trees(self)
    self.trees.setPlaceholderText("wybierz drzewo")
    self.trees.addItems(self.trees_list)
    self.verticalLayout_6.addWidget(self.trees)

    self.name_lbl.setText("podaj nazwę powodu śmierci:")
    self.verticalLayout_6.addWidget(self.name_lbl)

    self.e1 = QLineEdit(self.verticalLayoutWidget_6)
    self.e1.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e1)

    self.add_death_reason_main_bt.setAutoDefault(False)
    self.verticalLayout_6.addWidget(self.add_death_reason_main_bt)
    self.add_death_reason_main_bt.setText(
        "Dodaj powód śmierci o powyższej nazwie")


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 8 - dodawanie choroby $$$$$$$$$$
def add_illness_clicked(self):
    self.clear_ui()
    self.error_label.setText(" ")
    self.MainWindow.setStyleSheet(START_WINDOW_ADD_ILLNESS_CSS)
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

    self.tree_lbl.setText("wybierz drzewo do którego dodajemy chorobę:")
    self.verticalLayout_6.addWidget(self.tree_lbl)

    load_saved_trees(self)
    self.trees.setPlaceholderText("wybierz drzewo")
    self.trees.addItems(self.trees_list)
    self.verticalLayout_6.addWidget(self.trees)

    self.name_lbl.setText("podaj nazwę choroby:")
    self.verticalLayout_6.addWidget(self.name_lbl)

    self.e1 = QLineEdit(self.verticalLayoutWidget_6)
    self.e1.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e1)

    self.add_illness_main_bt.setAutoDefault(False)
    self.verticalLayout_6.addWidget(self.add_illness_main_bt)
    self.add_illness_main_bt.setText("Dodaj chorobę o takiej nazwie")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 9 - dodawanie zawodu $
def add_profession_clicked(self):
    self.clear_ui()
    self.error_label.setText(" ")
    self.MainWindow.setStyleSheet(START_WINDOW_ADD_PROFESSION_CSS)
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

    self.tree_lbl.setText("wybierz drzewo do którego dodajemy zawód:")
    self.verticalLayout_6.addWidget(self.tree_lbl)

    load_saved_trees(self)
    self.trees = QtWidgets.QComboBox()
    self.trees.setPlaceholderText("wybierz drzewo")
    self.trees.addItems(self.trees_list)
    self.verticalLayout_6.addWidget(self.trees)

    self.name_lbl.setText("podaj nazwę zawodu:")
    self.verticalLayout_6.addWidget(self.name_lbl)

    self.e1 = QLineEdit(self.verticalLayoutWidget_6)
    self.e1.setFont(QFont("Arial", 11))
    self.verticalLayout_6.addWidget(self.e1)

    self.add_profession_main_bt.setAutoDefault(False)

    self.verticalLayout_6.addWidget(self.add_profession_main_bt)
    self.add_profession_main_bt.setText("Dodaj zawód o takiej nazwie")