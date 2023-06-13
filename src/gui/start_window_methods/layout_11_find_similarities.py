from functools import partial

from PyQt6 import QtWidgets

from src.Funtcions.compare_tree import compare_tree
from src.definitions.definitions import X2, Y1, X1, WIN_WIDTH, Y4
from src.definitions.ui_css import START_WINDOW_FIND_SIMILARITIES_CSS
from src.gui.start_window_methods.layout_10_find_relation import \
    load_saved_trees


def find_similarities_clicked(self):
    self.error_label.setText(" ")
    self.clear_ui()
    self.MainWindow.setStyleSheet(START_WINDOW_FIND_SIMILARITIES_CSS)
    self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
    self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, Y4)

    self.tree_lbl.setText("wybierz pierwsze drzewo do znalezienia "
                          "podobieństw:")
    self.verticalLayout_6.addWidget(self.tree_lbl)

    load_saved_trees(self)
    self.trees = QtWidgets.QComboBox()
    self.trees.setPlaceholderText("wybierz drzewo")
    self.trees.addItems(self.trees_list)
    self.verticalLayout_6.addWidget(self.trees)

    tree_lbl2 = QtWidgets.QLabel()
    tree_lbl2.setText("wybierz drugie drzewo do znalezienia podobieństw:")
    tree_lbl2.setObjectName("lbl2")
    self.verticalLayout_6.addWidget(tree_lbl2)

    load_saved_trees(self)
    self.trees2.setPlaceholderText("wybierz drzewo")
    self.trees2.addItems(self.trees_list)
    self.verticalLayout_6.addWidget(self.trees2)

    self.choose_tree_to_similarities.setAutoDefault(False)
    self.choose_tree_to_similarities.clicked.connect(
        partial(choose_tree_to_similarities_clicked, self))

    self.verticalLayout_6.addWidget(self.choose_tree_to_similarities)
    self.choose_tree_to_similarities.setText(
        "W tym drzewie znajdź podobieństwa")

    self.info_label.setText("")
    self.verticalLayout_6.addWidget(self.info_label)


def choose_tree_to_similarities_clicked(self):
    minimum_matching = 8
    # minium matching from 1 to 9
    # minium matching znajduje poprawnie
    matches = compare_tree(self.trees.currentText(),
                           self.trees2.currentText(), minimum_matching)
    output = ""
    for p, o in matches:
        output += f"Found matching between {p} and {o} \n"
    self.info_label.setText(output)


def merge_trees_clicked(self):
    # TODO Można dodać mergowanie tych drzew
    pass
