import json
import os
from _csv import reader
import matplotlib.pyplot as plt
from functools import partial
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QLineEdit, \
    QMainWindow

from src.Funtcions.compare_tree import compare_tree
from src.Funtcions.find_family_relation import find_family_relation
from src.Funtcions.uodate_partners import update_partners
from src.definitions.definitions import WIN_WIDTH, WIN_HEIGHT, X1, Y1, \
    REGULAR_MARGIN, Y2, X2, Y3, ROOT_DIR, Y4, \
    NEW_PARAMETER_WINDOW_HEIGHT
from src.definitions.ui_css import START_WINDOW_ANALISE_TREE_CSS, \
    START_WINDOW_FIND_SIMILARITIES_CSS, \
    START_WINDOW_FIND_RELATION_CSS, START_WINDOW_ADD_PROFESSION_CSS, \
    START_WINDOW_ADD_ILLNESS_CSS, \
    START_WINDOW_ADD_DEATH_REASON_CSS, START_WINDOW_ADD_CITY_CSS, \
    START_WINDOW_ADD_TREE_CSS, \
    START_WINDOW_EDIT_PERSON_CLICKED, START_WINDOW_FIND_PERSON_CSS, \
    START_WINDOW_PREPARE_BACKGROUND_CSS, \
    START_WINDOW_SHOW_SAVED_TREES_CSS
from src.gui.info_window import InfoWindow
from src.gui.multi_combobox import CheckableComboBox
from src.gui.person_window import PersonWindow
from src.gui.start_window_methods.layout_10_find_relation import \
    find_relation_clicked, chose_tree_to_find_relation_clicked, \
    find_relation_inside_clicked, load_saved_trees
from src.gui.start_window_methods.layout_11_find_similarities import \
    find_similarities_clicked
from src.gui.start_window_methods.layout_12_analise_tree import \
    analise_tree_clicked
from src.gui.start_window_methods.layout_2 import add_person_clicked
from src.gui.start_window_methods.layout_3_find_person import \
    find_person_clicked
from src.gui.start_window_methods.layout_4_edit_person import \
    edit_person_clicked
from src.gui.start_window_methods.layout_5_new_tree_creation import \
    add_tree_main_clicked
from src.gui.start_window_methods.layout_6_9_add_parameters import \
    add_city_clicked, add_death_reason_clicked, add_illness_clicked, \
    add_profession_clicked, append_parameter_to_file
from src.gui.start_window_methods.start_window_ui_static import on_node_click, \
    add_tree_to_saved_trees, make_copy_of_a_tree
from src.gui.tree_window_graph_ui import TreeWindowGraphUi
from src.io_functions.json_to_list import json_to_dict
from src.io_functions.read_data import read_data
from src.io_functions.read_people import read_people_to_dict


# TODO obsługa niedziałających drzew, tzn takich o niepełnej strukturze, że
#  brakuje pól w jsonie czy coś
# TODO przejść na show zamiast ponownego tworzenia atrybutów
class StartWindowUi(object):
    def __init__(self) -> None:
        self.person_to_edit_partners = None
        self.person_to_edit_death_reason = None
        self.person_to_edit_birth_place = None
        self.person_to_edit_gender = None
        self.person_to_edit_professions = None
        self.person_to_edit_illnesses = None
        self.person_to_edit_residences = None
        self.person_to_edit_birth_date = None
        self.person_to_edit_mother_id = None
        self.person_to_edit_father_id = None
        self.person_to_edit = None
        self.id_to_edit = None
        self.choose_person_to_edit = None
        self.e7 = None
        self.choose_tree_bt = None
        self.edit_person_bt = None
        self.e14 = CheckableComboBox()
        self.e13 = CheckableComboBox()
        self.e12 = CheckableComboBox()
        self.e11 = QtWidgets.QComboBox()
        self.e10 = QtWidgets.QComboBox()
        self.e9 = None
        self.e8 = None
        self.e6 = QtWidgets.QComboBox()
        self.e5 = QtWidgets.QComboBox()
        self.e4 = None
        self.is_dead = None
        self.e3 = None
        self.e2 = None
        self.e1 = None
        self.error_label = QtWidgets.QLabel()
        self.error_label.setObjectName("error_lbl")
        self.widget = None
        self.open_tree_bt = None
        self.add_tree_bt = None
        self.verticalLayout_7 = None
        self.verticalLayoutWidget_7 = None
        self.verticalLayout_6 = None
        self.verticalLayoutWidget_6 = None
        self.verticalLayout_4 = None
        self.verticalLayoutWidget_4 = None
        self.verticalLayout_3 = None
        self.find_similarities = QtWidgets.QPushButton()
        self.analise_tree = QtWidgets.QPushButton()
        self.verticalLayoutWidget_3 = None
        self.verticalLayoutWidget_3 = None
        self.horizontalLayout = None
        self.horizontalLayoutWidget = None
        self.verticalLayout_2 = None
        self.add_tree = QtWidgets.QPushButton()
        self.show_saved_trees = QtWidgets.QPushButton()
        self.add_person = QtWidgets.QPushButton()
        self.find_person = QtWidgets.QPushButton()
        self.edit_person = QtWidgets.QPushButton()
        self.add_tree_main_bt = QtWidgets.QPushButton()
        self.add_city_main_bt = QtWidgets.QPushButton()
        self.add_death_reason_main_bt = QtWidgets.QPushButton()
        self.add_illness_main_bt = QtWidgets.QPushButton()
        self.add_profession_main_bt = QtWidgets.QPushButton()
        self.add_city = QtWidgets.QPushButton()
        self.add_death_reason = QtWidgets.QPushButton()
        self.add_illness = QtWidgets.QPushButton()
        self.add_profession = QtWidgets.QPushButton()
        self.find_relation = QtWidgets.QPushButton()
        self.trees = QtWidgets.QComboBox()
        self.tree_lbl = QtWidgets.QLabel()
        self.choose_tree_to_analise = QtWidgets.QPushButton()
        self.info_label = QtWidgets.QLabel()
        self.trees2 = QtWidgets.QComboBox()
        self.choose_tree_to_similarities = QtWidgets.QPushButton()
        self.choose_tree_to_find = QtWidgets.QPushButton()
        self.name_lbl = QtWidgets.QLabel()
        self.find_relation_inside = QtWidgets.QPushButton()
        self.MainWindow = None
        self.tree_to_open = None
        self.central_widget = None
        self.verticalLayoutWidget = None
        self.verticalLayout = None
        self.label = None
        self.verticalLayoutWidget_2 = None
        self.info_window = None
        self.name2_lbl = QtWidgets.QLabel()
        self.man_list = []
        self.woman_list = []
        self.death_reasons = []
        self.death_reasons_dicts = {}
        self.places = []
        self.places_dicts = {}
        self.illnesses = []
        self.illnesses_dicts = {}
        self.people_dict = {}
        self.professions = []
        self.professions_dicts = {}
        self.trees_list = []

    def setup_ui(self, main_window: QMainWindow) -> None:
        self.MainWindow = main_window
        main_window.setObjectName("MainWindow")
        main_window.resize(WIN_WIDTH, WIN_HEIGHT)
        self.central_widget = QtWidgets.QWidget(parent=main_window)
        self.central_widget.setObjectName("central_widget")

        self.verticalLayoutWidget = QtWidgets.QWidget(
            parent=self.central_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, X1, Y1))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.error_label.setFont(QFont("Arial", 15))

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(
            parent=self.central_widget)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(0, Y1, X1, Y2 - Y1))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayoutWidget = QtWidgets.QWidget(
            parent=self.central_widget)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(X1, 0, WIN_WIDTH - X1, Y1))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.error_label)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(
            parent=self.central_widget)
        self.verticalLayoutWidget_3.setGeometry(
            QtCore.QRect(0, Y2, X1, WIN_HEIGHT - Y2))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(REGULAR_MARGIN,
                                                 REGULAR_MARGIN,
                                                 REGULAR_MARGIN,
                                                 REGULAR_MARGIN)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(
            parent=self.central_widget)
        self.verticalLayoutWidget_4.setGeometry(
            QtCore.QRect(X1, Y1, WIN_WIDTH - X1, WIN_HEIGHT - Y1))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(REGULAR_MARGIN,
                                                 REGULAR_MARGIN,
                                                 REGULAR_MARGIN,
                                                 REGULAR_MARGIN)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # self.scrollArea_6 = QtWidgets.QScrollArea()
        # TODO scroll
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(
            parent=self.central_widget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(X1, Y1, 0, 0))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(REGULAR_MARGIN,
                                                 REGULAR_MARGIN,
                                                 REGULAR_MARGIN,
                                                 REGULAR_MARGIN)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        # self.scrollArea_6.setWidget(self.verticalLayoutWidget_6)

        self.verticalLayoutWidget_7 = QtWidgets.QWidget(
            parent=self.central_widget)
        self.verticalLayoutWidget_7.setGeometry(
            QtCore.QRect(X2, WIN_HEIGHT, 0, 0))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(REGULAR_MARGIN,
                                                 REGULAR_MARGIN,
                                                 REGULAR_MARGIN,
                                                 REGULAR_MARGIN)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        main_window.setCentralWidget(self.central_widget)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.show_saved_trees.setFont(font)
        self.add_person.setFont(font)
        self.find_person.setFont(font)
        self.edit_person.setFont(font)
        self.add_tree.setFont(font)
        self.add_city.setFont(font)
        self.add_death_reason.setFont(font)
        self.add_illness.setFont(font)
        self.add_profession.setFont(font)

        self.show_saved_trees.setAutoDefault(False)
        self.show_saved_trees.setObjectName("show_saved_trees")
        self.verticalLayout_2.addWidget(self.show_saved_trees)
        self.show_saved_trees.clicked.connect(self.show_saved_trees_clicked)

        self.add_person.setAutoDefault(False)
        self.add_person.setObjectName("add_person")
        self.verticalLayout_2.addWidget(self.add_person)
        self.add_person.clicked.connect(partial(add_person_clicked, self))

        self.find_person.setAutoDefault(False)
        self.find_person.setObjectName("find_person")
        self.verticalLayout_2.addWidget(self.find_person)
        self.find_person.clicked.connect(partial(find_person_clicked,self))

        self.edit_person.setAutoDefault(False)
        self.edit_person.setObjectName("edit_person")
        self.verticalLayout_2.addWidget(self.edit_person)
        self.edit_person.clicked.connect(partial(edit_person_clicked, self))

        self.add_tree.setAutoDefault(False)
        self.add_tree.setObjectName("add_tree")
        self.verticalLayout_2.addWidget(self.add_tree)
        self.add_tree.clicked.connect(partial(add_tree_main_clicked,self))

        self.add_city.setAutoDefault(False)
        self.add_city.setObjectName("add_city")
        self.verticalLayout_2.addWidget(self.add_city)
        self.add_city.clicked.connect(partial(add_city_clicked,self))

        self.add_death_reason.setAutoDefault(False)
        self.add_death_reason.setObjectName("add_death_reason")
        self.verticalLayout_2.addWidget(self.add_death_reason)
        self.add_death_reason.clicked.connect(partial(add_death_reason_clicked
                                                      , self))

        self.add_illness.setAutoDefault(False)
        self.add_illness.setObjectName("add_illness")
        self.verticalLayout_2.addWidget(self.add_illness)
        self.add_illness.clicked.connect(partial(add_illness_clicked, self))

        self.add_profession.setAutoDefault(False)
        self.add_profession.setObjectName("add_profession")
        self.verticalLayout_2.addWidget(self.add_profession)
        self.add_profession.clicked.connect(partial(add_profession_clicked, self))

        self.find_relation.setAutoDefault(False)
        self.find_relation.setObjectName("find_relation")
        self.verticalLayout_2.addWidget(self.find_relation)
        self.find_relation.clicked.connect(partial(find_relation_clicked,
                                                   self))
        self.find_similarities.setAutoDefault(False)
        self.find_similarities.setObjectName("find_similarities")
        self.verticalLayout_2.addWidget(self.find_similarities)
        self.find_similarities.clicked.connect(partial(
            find_similarities_clicked, self))

        self.analise_tree.setAutoDefault(False)
        self.analise_tree.setObjectName("analise_tree")
        self.verticalLayout_2.addWidget(self.analise_tree)
        self.analise_tree.clicked.connect(partial(analise_tree_clicked, self))

        self.translate_ui(main_window)

        self.tree_lbl.setObjectName("lbl")
        self.info_label.setObjectName("info_lbl")
        self.name2_lbl.setObjectName("lbl")
        self.choose_tree_to_find.setAutoDefault(False)
        self.choose_tree_to_find.clicked.connect(
            partial(chose_tree_to_find_relation_clicked,self))
        self.choose_tree_to_find.setText("W tym drzewie określ relację")

        self.name_lbl.setObjectName("lbl")
        self.find_relation_inside.clicked.connect(
            partial(find_relation_inside_clicked,self))
        self.add_profession_main_bt.clicked.connect(
            partial(append_parameter_to_file, self, "\\professions.json"))
        self.find_relation_inside.setText("Określ relację")
        self.add_illness_main_bt.clicked.connect(
            partial(append_parameter_to_file, self, "\\illnesses.json"))
        self.add_death_reason_main_bt.clicked.connect(
            partial(append_parameter_to_file, self, "\\death_reasons.json"))

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_ui(self, main_window: QMainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(
            _translate("MainWindow", "Menadżer drzew genealogicznych"))
        self.label.setText(
            _translate("MainWindow", "MENADŻER\nDRZEW\nGENEALOGICZNYCH"))
        self.show_saved_trees.setText(
            _translate("MainWindow", "Przeglądaj zapisane drzewa"))
        self.add_person.setText(_translate("MainWindow", "Dodaj osobę"))
        self.find_person.setText(_translate("MainWindow", "Znajdź osobę"))
        self.edit_person.setText(_translate("MainWindow", "Edytuj osobę"))
        self.add_tree.setText(_translate("MainWindow", "Dodaj drzewo"))
        self.add_city.setText(_translate("MainWindow", "Dodaj miasto"))
        self.add_death_reason.setText(
            _translate("MainWindow", "Dodaj powód śmierci"))
        self.add_illness.setText(_translate("MainWindow", "Dodaj chorobę"))
        self.add_profession.setText(_translate("MainWindow", "Dodaj zawód"))
        self.find_relation.setText(
            _translate("MainWindow", "Znajdź pokrewieństwo"))
        self.find_similarities.setText(
            _translate("MainWindow", "Znajdź podobieństwa"))
        self.analise_tree.setText(_translate("MainWindow", "Analizuj drzewo"))

    def set_error_label_text(self, text: str) -> None:
        """ moja metodka, żeby tekst w error label znikał"""
        self.error_label.setText(text)
        # TODO nie działa xd
        # time.sleep(2)
        # self.error_label.setText(" ")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 1 - dodawanie drzewa z pliku $$$$$
    def add_saved_trees(self) -> None:
        """ Dodawanie już zapisanych drzew do odpowiedniej komórki"""
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        load_saved_trees(self)
        for tree_name in self.trees_list:
            self.add_saved_tree(tree_name)

    def add_saved_tree(self, tree_name: str) -> None:
        """ Dodawanie pojedynczego drzewa i tworzenie mu atrybutu w klasie"""
        bt_name = "radioButton_" + tree_name
        # TODO sprawdzanie czy już takiego atrybutu nie ma, bo jak jest to bez
        #  sensu duplikować, a po co wgl ten atrybut
        setattr(self, bt_name,
                QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_4))
        attr = getattr(self, bt_name)
        attr.setObjectName(bt_name)
        self.verticalLayout_4.addWidget(attr)
        attr.setText(
            QtCore.QCoreApplication.translate("MainWindow", tree_name))
        attr.clicked.connect(partial(self.set_chosen_tree, tree_name))

    def set_chosen_tree(self, attr: str) -> None:
        """ Ustawianie wybranego drzewa jako tego, które chcemy otworzyć"""
        self.tree_to_open = attr

    def show_saved_trees_clicked(self) -> None:
        """ Przeglądaj zapisane drzewa — przycisk główny numer 1"""
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.verticalLayoutWidget_4.setGeometry(X1, Y1, WIN_WIDTH - X1,
                                                WIN_HEIGHT - Y1)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, 0, 0)
        self.verticalLayoutWidget_7.setGeometry(X2, Y3, 0, 0)
        self.add_saved_trees()

        self.MainWindow.setStyleSheet(START_WINDOW_SHOW_SAVED_TREES_CSS)

        self.add_tree_bt = QtWidgets.QPushButton(parent=self.central_widget)
        self.add_tree_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_tree_bt.setFont(font)
        self.add_tree_bt.setObjectName("add_tree_bt")
        self.verticalLayout_4.addWidget(self.add_tree_bt)

        self.open_tree_bt = QtWidgets.QPushButton(parent=self.central_widget)
        self.open_tree_bt.setGeometry(QtCore.QRect(485, 240, 104, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.open_tree_bt.setFont(font)
        self.open_tree_bt.setAutoDefault(False)
        self.open_tree_bt.setObjectName("open_tree_bt")
        self.verticalLayout_4.addWidget(self.open_tree_bt)

        self.add_tree_bt.setText("Dodaj drzewo")
        self.open_tree_bt.setText("Otwórz drzewo")

        self.add_tree_bt.clicked.connect(self.add_tree_clicked)
        self.open_tree_bt.clicked.connect(self.open_tree_clicked)

    def add_tree_clicked(self) -> None:
        file_name = QFileDialog.getOpenFileName(None, "Open File",
                                                "../../resources/Tree_files",
                                                "JSON Files (*.json)")
        if file_name:
            add_tree_to_saved_trees(file_name[0])
            make_copy_of_a_tree(file_name[0])
            self.add_saved_trees()
        else:
            # TODO wywala apke jak nie wybierzesz niczego tylko zamkniesz okno
            pass

    def open_tree_clicked(self):
        if self.tree_to_open is not None:
            main_person, peron_list = read_data(self.tree_to_open, 6,
                                                flag=True)
            # id 6 to babcia, id 4 mama, id 1 ja, 3grzegorz

            graph_ui = TreeWindowGraphUi()
            canvas = graph_ui.setup_ui(main_person, peron_list)
            canvas.figure.canvas.mpl_connect('pick_event', on_node_click)
            self.widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(canvas)
            self.widget.setLayout(layout)
            self.widget.show()

    def clear_ui(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_7.count())):
            self.verticalLayout_7.itemAt(i).widget().setParent(None)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$ do przycisków 2, 3, 4 $$$$$$$$$$$$$$$$$$$$$$$
