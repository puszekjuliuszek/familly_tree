import json
from _csv import reader
from collections import deque
from functools import partial
from os import listdir
from shutil import copyfile
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QLineEdit, QMainWindow

from src.Funtcions.find_family_relation import find_family_relation
from src.Funtcions.uodate_partners import update_partners
from src.definitions.definitions import *
from src.definitions.ui_css import *
from src.gui.multi_combobox import CheckableComboBox
from src.gui.person_window import PersonWindow
from src.gui.tree_window_graph_ui import TreeWindowGraphUi
from src.io_functions.json_to_list import json_to_dict
from src.io_functions.read_data import read_data
from src.io_functions.read_people import read_people_to_dict


def pyqt_date_to_json_date(date: str) -> str:
    date_list = date.split(".")
    date_list.reverse()
    return "-".join(date_list)


# TODO obsługa niedziałających drzew, tzn takich o niepełnej strukturze, że brakuje pól w jsonie czy coś
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
        self.trees_list = []
        self.person_to_edit = None
        self.id_to_edit = None
        self.choose_person_to_edit = None
        self.e7 = None
        self.choose_tree_bt = None
        self.edit_person_bt = None
        self.e14 = None
        self.e13 = None
        self.e12 = None
        self.e11 = None
        self.e10 = None
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
        self.MainWindow = None
        self.tree_to_open = None
        self.central_widget = None
        self.verticalLayoutWidget = None
        self.verticalLayout = None
        self.label = None
        self.verticalLayoutWidget_2 = None

    def setup_ui(self, main_window: QMainWindow) -> None:
        self.MainWindow = main_window
        main_window.setObjectName("MainWindow")
        main_window.resize(WIN_WIDTH, WIN_HEIGHT)
        self.central_widget = QtWidgets.QWidget(parent=main_window)
        self.central_widget.setObjectName("central_widget")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.central_widget)
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

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.central_widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, Y1, X1, Y2 - Y1))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.central_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(X1, 0, WIN_WIDTH - X1, Y1))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.error_label)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.central_widget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, Y2, X1, WIN_HEIGHT - Y2))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.central_widget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(X1, Y1, WIN_WIDTH - X1, WIN_HEIGHT - Y1))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # self.scrollArea_6 = QtWidgets.QScrollArea()
        # TODO scroll
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.central_widget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(X1, Y1, 0, 0))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        # self.scrollArea_6.setWidget(self.verticalLayoutWidget_6)

        self.verticalLayoutWidget_7 = QtWidgets.QWidget(parent=self.central_widget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(X2, WIN_HEIGHT, 0, 0))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN)
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
        self.add_person.clicked.connect(self.add_person_clicked)

        self.find_person.setAutoDefault(False)
        self.find_person.setObjectName("find_person")
        self.verticalLayout_2.addWidget(self.find_person)
        self.find_person.clicked.connect(self.find_person_clicked)

        self.edit_person.setAutoDefault(False)
        self.edit_person.setObjectName("edit_person")
        self.verticalLayout_2.addWidget(self.edit_person)
        self.edit_person.clicked.connect(self.edit_person_clicked)

        self.add_tree.setAutoDefault(False)
        self.add_tree.setObjectName("add_tree")
        self.verticalLayout_2.addWidget(self.add_tree)
        self.add_tree.clicked.connect(self.add_tree_main_clicked)

        self.add_city.setAutoDefault(False)
        self.add_city.setObjectName("add_city")
        self.verticalLayout_2.addWidget(self.add_city)
        self.add_city.clicked.connect(self.add_city_clicked)

        self.add_death_reason.setAutoDefault(False)
        self.add_death_reason.setObjectName("add_death_reason")
        self.verticalLayout_2.addWidget(self.add_death_reason)
        self.add_death_reason.clicked.connect(self.add_death_reason_clicked)

        self.add_illness.setAutoDefault(False)
        self.add_illness.setObjectName("add_illness")
        self.verticalLayout_2.addWidget(self.add_illness)
        self.add_illness.clicked.connect(self.add_illness_clicked)

        self.add_profession.setAutoDefault(False)
        self.add_profession.setObjectName("add_profession")
        self.verticalLayout_2.addWidget(self.add_profession)
        self.add_profession.clicked.connect(self.add_profession_clicked)

        self.find_relation.setAutoDefault(False)
        self.find_relation.setObjectName("find_relation")
        self.verticalLayout_2.addWidget(self.find_relation)
        self.find_relation.clicked.connect(self.find_relation_clicked)
        self.find_similarities.setAutoDefault(False)
        self.find_similarities.setObjectName("find_similarities")
        self.verticalLayout_2.addWidget(self.find_similarities)
        self.find_similarities.clicked.connect(self.find_similarities_clicked)

        self.analise_tree.setAutoDefault(False)
        self.analise_tree.setObjectName("analise_tree")
        self.verticalLayout_2.addWidget(self.analise_tree)
        self.analise_tree.clicked.connect(self.analise_tree_clicked)

        self.translate_ui(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_ui(self, main_window: QMainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Menadżer drzew genealogicznych"))
        self.label.setText(_translate("MainWindow", "MENADŻER\nDRZEW\nGENEALOGICZNYCH"))
        self.show_saved_trees.setText(_translate("MainWindow", "Przeglądaj zapisane drzewa"))
        self.add_person.setText(_translate("MainWindow", "Dodaj osobę"))
        self.find_person.setText(_translate("MainWindow", "Znajdź osobę"))
        self.edit_person.setText(_translate("MainWindow", "Edytuj osobę"))
        self.add_tree.setText(_translate("MainWindow", "Dodaj drzewo"))
        self.add_city.setText(_translate("MainWindow", "Dodaj miasto"))
        self.add_death_reason.setText(_translate("MainWindow", "Dodaj powód śmierci"))
        self.add_illness.setText(_translate("MainWindow", "Dodaj chorobę"))
        self.add_profession.setText(_translate("MainWindow", "Dodaj zawód"))
        self.find_relation.setText(_translate("MainWindow", "Znajdź pokrewieństwo"))
        self.find_similarities.setText(_translate("MainWindow", "Znajdź podobieństwa"))
        self.analise_tree.setText(_translate("MainWindow", "Analizuj drzewo"))

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 1 - dodawanie drzewa z pliku $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def add_saved_trees(self) -> None:
        """ Dodawanie już zapisanych drzew do odpowiedniej komórki"""
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.load_saved_trees()
        for tree_name in self.trees_list:
            self.add_saved_tree(tree_name)

    def add_saved_tree(self, tree_name: str) -> None:
        """ Dodawanie pojedynczego drzewa i tworzenie mu atrybutu w klasie"""
        bt_name = "radioButton_" + tree_name
        # TODO sprawdzanie czy już takiego atrybutu nie ma, bo jak jest to bez sensu duplikować, a po co wgl ten atrybut
        setattr(self, bt_name, QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_4))
        attr = getattr(self, bt_name)
        attr.setObjectName(bt_name)
        self.verticalLayout_4.addWidget(attr)
        attr.setText(QtCore.QCoreApplication.translate("MainWindow", tree_name))
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
        self.verticalLayoutWidget_4.setGeometry(X1, Y1, WIN_WIDTH - X1, WIN_HEIGHT - Y1)
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

    @staticmethod
    def add_tree_to_saved_trees(path: str) -> None:
        tree_name = path.split("/")[-1]
        relative_path = "../../resources/Tree_files/" + tree_name
        tree_names = []
        with open("../../resources/saved_trees.csv", "r") as file:
            csvreader = reader(file)
            for row in csvreader:
                tree_names.append(row[1].strip())
        if tree_name not in tree_names:
            with open("../../resources/saved_trees.csv", "a") as file:
                file.write(relative_path + "," + tree_name + "\n")
        else:
            # TODO może info, że drzewo jest już zapisane?
            pass

    @staticmethod
    def make_copy_of_a_tree(path: str) -> None:
        filenames = listdir('/'.join(path.split("/")[0:-1]))
        tree_name = path.split("/")[-1]
        if tree_name not in filenames:
            copyfile(path, "../../resources/Tree_files/" + tree_name)

    def add_tree_clicked(self) -> None:
        file_name = QFileDialog.getOpenFileName(None, "Open File", "../../resources/Tree_files", "JSON Files (*.json)")
        if file_name:
            self.add_tree_to_saved_trees(file_name[0])
            self.make_copy_of_a_tree(file_name[0])
            self.add_saved_trees()
        else:
            # TODO wywala apke jak nie wybierzesz niczego tylko zamkniesz okno
            pass

    def open_tree_clicked(self):
        if self.tree_to_open is not None:
            main_person,peron_list = read_data(self.tree_to_open, 6, flag=True)
            # id 6 to babcia, id 4 mama, id 1 ja, 3grzegorz
            # TODO wywalić te dwie linijki, albo dołożyć wybór printowania drzewa
            # self.tree_window = TreeWindow(main_person, self.tree_to_open.split(".")[0])
            # self.tree_window.show()

            graph_ui = TreeWindowGraphUi()
            canvas = graph_ui.setup_ui(main_person,peron_list)
            canvas.figure.canvas.mpl_connect('pick_event', self.on_node_click)
            self.widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(canvas)
            self.widget.setLayout(layout)
            self.widget.show()

    @staticmethod
    def on_node_click(event):
        node_text = event.artist.get_text()
        node_num = str(node_text)
        print(f"Kliknięto węzeł {node_num}")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$ do przycisków 2, 3, 4 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def prepare_background(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_7.count())):
            self.verticalLayout_7.itemAt(i).widget().setParent(None)
        self.error_label.setText(" ")

        self.MainWindow.setStyleSheet(START_WINDOW_PREPARE_BACKGROUND_CSS)
        self.tree_to_open = None
        self.add_saved_trees()
        self.verticalLayoutWidget_4.setGeometry(X1, Y1, X2 - X1, WIN_HEIGHT - Y1)
        self.verticalLayoutWidget_6.setGeometry(X2, Y1, WIN_WIDTH - X2, WIN_HEIGHT - Y1)
        self.verticalLayoutWidget_7.setGeometry(X2, Y3, 0, 0)
        name_lbl = QtWidgets.QLabel()
        name_lbl.setText("imię:")
        name_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(name_lbl)
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
        self.is_dead.clicked.connect(self.is_dead_clicked)
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
        self.e10 = QtWidgets.QComboBox()
        self.e10.clear()
        self.e10.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e10)

        birth_place_lbl = QtWidgets.QLabel()
        birth_place_lbl.setText("miejsce urodzenia:")
        self.verticalLayout_6.addWidget(birth_place_lbl)
        self.e11 = QtWidgets.QComboBox()
        self.e11.clear()
        self.e11.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e11)

        professions_lbl = QtWidgets.QLabel()
        professions_lbl.setText("zawody:")
        self.verticalLayout_6.addWidget(professions_lbl)
        self.e12 = CheckableComboBox()
        self.e12.clear()
        self.verticalLayout_6.addWidget(self.e12)

        illnesses_lbl = QtWidgets.QLabel()
        illnesses_lbl.setText("choroby:")
        self.verticalLayout_6.addWidget(illnesses_lbl)
        self.e13 = CheckableComboBox()
        self.e13.clear()
        self.verticalLayout_6.addWidget(self.e13)

        residences_lbl = QtWidgets.QLabel()
        residences_lbl.setText("miejsca zamieszkania:")
        self.verticalLayout_6.addWidget(residences_lbl)
        self.e14 = CheckableComboBox()
        self.e14.clear()
        self.verticalLayout_6.addWidget(self.e14)

        self.e1.setDisabled(True)
        self.e2.setDisabled(True)
        self.e3.setDisabled(True)
        self.e4.setDisabled(True)
        self.e5.setDisabled(True)
        self.e6.setDisabled(True)
        self.e8.setDisabled(True)
        self.e9.setDisabled(True)
        self.e10.setDisabled(True)
        self.e11.setDisabled(True)
        self.e12.setDisabled(True)
        self.e13.setDisabled(True)
        self.e14.setDisabled(True)
        self.is_dead.setDisabled(True)

    def is_dead_clicked(self) -> None:
        if self.is_dead.isChecked():
            self.e4.setDisabled(True)
            self.e10.setDisabled(True)
        else:
            self.e4.setDisabled(False)
            self.e10.setDisabled(False)

    def unable_inputs(self):
        self.e1.setDisabled(False)
        self.e2.setDisabled(False)
        self.e3.setDisabled(False)
        self.is_dead.setDisabled(False)
        self.e4.setDisabled(False)
        self.e5.setDisabled(False)
        self.e6.setDisabled(False)
        self.e8.setDisabled(False)
        self.e9.setDisabled(False)
        self.e10.setDisabled(False)
        self.e11.setDisabled(False)
        self.e12.setDisabled(False)
        self.e13.setDisabled(False)
        self.e14.setDisabled(False)

    def import_data_from_tree(self) -> None:
        self.unable_inputs()
        self.update_dicts()
        self.put_people_to_combobox()

    def put_people_to_combobox(self) -> None:
        self.e5.setPlaceholderText(" ")
        self.e6.setPlaceholderText(" ")
        self.e9.setPlaceholderText(" ")
        self.e10.setPlaceholderText(" ")
        self.e11.setPlaceholderText(" ")
        self.add_items_to_inputs()
        self.set_multiombobox_placeholder_texts()

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
        file_path = ROOT_DIR + "\\resources\\information\\" + self.tree_to_open.split(".")[0]
        if self.tree_to_open is not None:
            self.people_dict = read_people_to_dict(self.tree_to_open)
            self.woman_list = [person for person in self.people_dict.keys() if person.split(" ")[0][-1] == "a"]
            self.man_list = [person for person in self.people_dict.keys() if person.split(" ")[0][-1] != "a"]
        self.places_dicts = json_to_dict(file_path + "\\cities.json")
        self.places = [place for place in self.places_dicts.keys()]
        self.death_reasons_dicts = json_to_dict(file_path + "\\death_reasons.json")
        self.death_reasons = [death for death in self.death_reasons_dicts.keys()]
        self.illnesses_dicts = dict(json_to_dict(file_path + "\\illnesses.json"))
        self.illnesses = [illness for illness in self.illnesses_dicts.keys()]
        self.professions_dicts = json_to_dict(file_path + "\\professions.json")
        self.professions = [profession for profession in self.professions_dicts.keys()]

    def set_multiombobox_placeholder_texts(self):
        self.e8.setPlaceholderText(" ")
        self.e12.setPlaceholderText(" ")
        self.e13.setPlaceholderText(" ")
        self.e14.setPlaceholderText(" ")

    def read_inputs(self):
        # father
        self.person_to_edit_father_id = 0
        if self.e5.currentText() != '':
            self.person_to_edit_father_id = self.people_dict.get(self.e5.currentText())
        elif self.e5.placeholderText() != ' ':
            self.person_to_edit_father_id = self.people_dict.get(self.e5.placeholderText())

        # mother
        self.person_to_edit_mother_id = 0
        if self.e6.currentText() != '':
            self.person_to_edit_mother_id = self.people_dict.get(self.e6.currentText())
        elif self.e6.placeholderText() != ' ':
            self.person_to_edit_mother_id = self.people_dict.get(self.e6.placeholderText())

        # birthdate
        self.person_to_edit_birth_date = pyqt_date_to_json_date(self.e3.text())

        # death date
        if self.is_dead.isChecked():
            self.person_to_edit_death_date = None
            self.person_to_edit_death_reason = None
        else:
            self.person_to_edit_death_date = pyqt_date_to_json_date(self.e4.text())
            self.person_to_edit_death_reason = None
            if self.e10.currentText() != '':
                self.person_to_edit_death_reason = self.death_reasons_dicts.get(self.e10.currentText())
            elif self.e10.placeholderText() != ' ':
                self.person_to_edit_death_reason = self.death_reasons_dicts.get(self.e10.placeholderText())

        # partners
        self.person_to_edit_partners = []
        for partner in self.e8.currentText().split(", "):
            self.person_to_edit_partners.append(self.people_dict.get(partner))

        # gender
        if self.e9.currentText() == "Kobieta" or self.e9.placeholderText() == "Kobieta":
            self.person_to_edit_gender = 0
        else:
            self.person_to_edit_gender = 1

        # birthplace
        self.person_to_edit_birth_place = None
        if self.e11.currentText() != '':
            self.person_to_edit_birth_place = self.places_dicts.get(self.e11.currentText())
        elif self.e11.placeholderText() != ' ':
            self.person_to_edit_birth_place = self.places_dicts.get(self.e11.placeholderText())

        # professions
        self.person_to_edit_professions = []
        for profession in self.e12.currentText().split(", "):
            self.person_to_edit_professions.append(self.professions_dicts.get(profession))

        # illnesses
        self.person_to_edit_illnesses = []
        for illness in self.e13.currentText().split(", "):
            self.person_to_edit_illnesses.append(self.illnesses_dicts.get(illness))

        # residences
        self.person_to_edit_residences = []
        for residence in self.e14.currentText().split(", "):
            self.person_to_edit_residences.append(self.places_dicts.get(residence))

        if len(self.person_to_edit_professions) == 1 and self.person_to_edit_professions[0] is None:
            self.person_to_edit_professions = []
        if len(self.person_to_edit_illnesses) == 1 and self.person_to_edit_illnesses[0] is None:
            self.person_to_edit_illnesses = []
        if len(self.person_to_edit_residences) == 1 and self.person_to_edit_residences[0] is None:
            self.person_to_edit_residences = []
        if len(self.person_to_edit_partners) == 1 and self.person_to_edit_partners[0] is None:
            self.person_to_edit_partners = []

    # $$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 2 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def add_person_clicked(self) -> None:
        self.prepare_background()
        self.add_person_bt = QtWidgets.QPushButton(parent=self.central_widget)
        self.add_person_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_person_bt.setFont(font)
        self.add_person_bt.setObjectName("add_person_bt")
        self.verticalLayout_6.addWidget(self.add_person_bt)
        self.add_person_bt.clicked.connect(self.enter_person)
        self.add_person_bt.setDisabled(True)

        choose_tree_bt = QtWidgets.QPushButton(parent=self.central_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        choose_tree_bt.setFont(font)
        choose_tree_bt.setObjectName("add_person_bt")
        choose_tree_bt.setText("do tego drzewa dodaj")
        self.verticalLayout_4.addWidget(choose_tree_bt)
        choose_tree_bt.clicked.connect(self._choose_tree_bt_clicked)

        self.add_person_bt.setText("Dodaj tę osobę")

    def _choose_tree_bt_clicked(self):
        self.import_data_from_tree()
        self.add_person_bt.setDisabled(False)

    """ Dopisywanie nowej osoby do pliku drzewa """

    def enter_person(self) -> None:
        # TODO czy to nie jest redundancja kodu?
        # TODO czy jak nie wszystkie dane są wprowadzone to coś z tym robimy? może już zrobiliśmy?
        file_path = ROOT_DIR + "\\resources\\Tree_files\\" + self.tree_to_open
        self.read_inputs()
        with open(file_path, "r+") as f:
            file_data = json.load(f)

        new_id = 0
        # file_data.sort(key=lambda x: x["person_id"])
        for person_data in file_data:
            new_id = max(new_id, person_data['person_id'])
        new_id += 1
        update_partners(new_id, self.person_to_edit_partners, file_data)
        person_data_dictionary = {'person_id': new_id, 'father_id': self.person_to_edit_father_id,
                                  'mother_id': self.person_to_edit_mother_id, 'first_name': self.e1.text(),
                                  'last_name': self.e2.text(), 'birth_date': self.person_to_edit_birth_date,
                                  'death_date': self.person_to_edit_death_date,
                                  'partners_id': self.person_to_edit_partners, 'gender': self.person_to_edit_gender,
                                  'death_reason': self.person_to_edit_death_reason,
                                  'birth_place': self.person_to_edit_birth_place,
                                  'profession': self.person_to_edit_professions,
                                  'illnesses': self.person_to_edit_illnesses,
                                  'residences': self.person_to_edit_residences}

        file_data.append(person_data_dictionary)
        with open(file_path, "w+") as f:
            json.dump(file_data, f)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 3 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def find_person_clicked(self) -> None:
        self.prepare_background()
        self.MainWindow.setStyleSheet(START_WINDOW_FIND_PERSON_CSS)

        self.find_person_bt = QtWidgets.QPushButton(parent=self.central_widget)
        self.find_person_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.find_person_bt.setFont(font)
        self.find_person_bt.setObjectName("find_person_bt")
        self.verticalLayout_6.addWidget(self.find_person_bt)
        self.find_person_bt.clicked.connect(self.find_person_in_tree)
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
        choose_tree_bt.clicked.connect(self._choose_tree_bt_to_find_in)

    def _choose_tree_bt_to_find_in(self):
        self.find_person_bt.setDisabled(False)
        self.import_data_from_tree()

    def find_person_in_tree(self) -> None:
        main_person = read_data(self.tree_to_open, 1, flag=True)
        output_list = []
        que = deque()
        que.append(main_person)
        visited = set()
        while len(que) > 0:
            person_tmp = que.pop()
            if person_tmp.father is not None:
                if person_tmp.father.person_id not in visited:
                    que.append(person_tmp.father)
            if person_tmp.mother is not None:
                if person_tmp.mother.person_id not in visited:
                    que.append(person_tmp.mother)
            for child in person_tmp.children:
                if child.person_id not in visited:
                    que.append(child)
            for partner in person_tmp.partners:
                if partner.person_id not in visited:
                    que.append(partner)

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
            if person_tmp.gender == (1 if self.e9.currentText() == "Mężczyzna" else 0):
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
            if self.e5.currentText() != '' and str(person.father) != self.e5.currentText():
                is_ok = False
            if self.e6.currentText() != '' and str(person.mother) == self.e6.currentText():
                is_ok = False
            # TODO sprawdzanie po partnerach
            if self.e9.currentText() != '' and person.gender != (1 if self.e9.currentText() == "Mężczyzna" else 0):
                is_ok = False
            if self.e10.currentText() != '' and person.birth_place != self.e10.currentText():
                is_ok = False
            if self.e11.currentText() != '' and person.death_reason != self.e11.currentText():
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

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 4 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def edit_person_clicked(self) -> None:
        self.prepare_background()
        self.verticalLayoutWidget_4.setGeometry(X1, Y1, X2 - X1, Y3 - Y1)
        self.verticalLayoutWidget_7.setGeometry(X1, Y3, X2 - X1, WIN_HEIGHT - Y3)
        self.MainWindow.setStyleSheet(START_WINDOW_EDIT_PERSON_CLICKED)

        self.edit_person_bt = QtWidgets.QPushButton(parent=self.central_widget)
        self.edit_person_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.edit_person_bt.setFont(font)
        self.edit_person_bt.setObjectName("edit_person_bt")
        self.verticalLayout_6.addWidget(self.edit_person_bt)
        self.edit_person_bt.clicked.connect(self.edit_person_data)
        self.edit_person_bt.setText("na takie zmień dane tej osoby")

        self.choose_tree_bt = QtWidgets.QPushButton(parent=self.central_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.choose_tree_bt.setFont(font)
        self.choose_tree_bt.setObjectName("choose_tree_bt")
        self.choose_tree_bt.setText("w tym drzewie wybierz \n osobę")
        self.verticalLayout_4.addWidget(self.choose_tree_bt)
        self.choose_tree_bt.clicked.connect(self.import_people_from_tree_to_edit)

        self.choose_person_to_edit = QtWidgets.QPushButton(parent=self.central_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.choose_person_to_edit.setFont(font)
        self.choose_person_to_edit.setObjectName("choose_person_to_edit")
        self.choose_person_to_edit.setText("tę osobę edytuj")
        self.choose_person_to_edit.clicked.connect(self.choose_person_to_edit_clicked)

        person_lbl = QtWidgets.QLabel()
        person_lbl.setText("wybierz osobę do edycji:")
        self.verticalLayout_7.addWidget(person_lbl)
        self.e7 = QtWidgets.QComboBox()
        self.e7.setFont(QFont("Arial", 11))
        self.verticalLayout_7.addWidget(self.e7)
        self.verticalLayout_7.addWidget(self.choose_person_to_edit)

        # TODO redundancja ?
        self.e1.setDisabled(True)
        self.e2.setDisabled(True)
        self.e3.setDisabled(True)
        self.e4.setDisabled(True)
        self.e5.setDisabled(True)
        self.e6.setDisabled(True)
        self.e7.setDisabled(True)
        self.e8.setDisabled(True)
        self.e9.setDisabled(True)
        self.e10.setDisabled(True)
        self.e11.setDisabled(True)
        self.e12.setDisabled(True)
        self.e13.setDisabled(True)
        self.e14.setDisabled(True)
        self.is_dead.setDisabled(True)
        self.choose_person_to_edit.setDisabled(True)
        self.edit_person_bt.setDisabled(True)

    def edit_person_data(self) -> None:
        # TODO tu mamy redundancje kodu, trzeba coś z tym zrobić, powtarza się to w jakieś tam metodzie wyżej
        file_path = ROOT_DIR + "\\resources\\Tree_files\\" + self.tree_to_open
        with open(file_path, "r+") as f:
            file_data = json.load(f)
        id_to_remove = None
        for i in range(len(file_data)):
            if file_data[i]['person_id'] == self.id_to_edit:
                id_to_remove = i
        if id_to_remove is not None:
            file_data.pop(id_to_remove)

        self.read_inputs()
        update_partners(self.id_to_edit, self.person_to_edit_partners, file_data)
        person_data_dictionary = {'person_id': self.id_to_edit, 'father_id': self.person_to_edit_father_id,
                                  'mother_id': self.person_to_edit_mother_id, 'first_name': self.e1.text(),
                                  'last_name': self.e2.text(), 'birth_date': self.person_to_edit_birth_date,
                                  'death_date': self.person_to_edit_death_date,
                                  'partners_id': self.person_to_edit_partners, 'gender': self.person_to_edit_gender,
                                  'death_reason': self.person_to_edit_death_reason,
                                  'birth_place': self.person_to_edit_birth_place,
                                  'profession': self.person_to_edit_professions,
                                  'illnesses': self.person_to_edit_illnesses,
                                  'residences': self.person_to_edit_residences}

        file_data.append(person_data_dictionary)
        with open(file_path, "w+") as f:
            json.dump(file_data, f)

    def import_people_from_tree_to_edit(self) -> None:
        self.update_dicts()
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
        self.e3.setDate(QtCore.QDate(int(birth_date[2]), int(birth_date[1]), int(birth_date[0])))
        self.is_dead.setDisabled(False)
        if self.person_to_edit.death_date is None:
            self.is_dead.setChecked(True)
            self.e10.setPlaceholderText(" ")
        else:
            self.e4.setDisabled(False)
            self.e10.setPlaceholderText(self.person_to_edit.death_reason)
        self.e5.setDisabled(False)
        if self.person_to_edit.father is not None:
            self.e5.setPlaceholderText(
                f"{self.person_to_edit.father.first_name} {self.person_to_edit.father.last_name}")
        else:
            self.e5.setPlaceholderText(" ")
        self.e6.setDisabled(False)
        if self.person_to_edit.mother is not None:
            self.e6.setPlaceholderText(
                f"{self.person_to_edit.mother.first_name} {self.person_to_edit.mother.last_name}")
        else:
            self.e6.setPlaceholderText(" ")
        self.e9.setDisabled(False)
        self.e9.setPlaceholderText("Mężczyzna" if self.person_to_edit.gender == 1 else "Kobieta")
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
        self.add_items_to_inputs()
        self.e8.set_items([str(person) for person in self.person_to_edit.partners])
        self.e12.set_items(self.person_to_edit.profession)
        self.e13.set_items(self.person_to_edit.illnesses)
        self.e14.set_items(self.person_to_edit.residences)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 5 - tworzenie nowego drzewa $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def add_tree_main_clicked(self):
        # TODO redundancja
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        self.error_label.setText(" ")
        self.MainWindow.setStyleSheet(START_WINDOW_ADD_TREE_CSS)
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, NEW_PARAMETER_WINDOW_HEIGHT)
        self.verticalLayoutWidget_7.setGeometry(X1, Y1 + NEW_PARAMETER_WINDOW_HEIGHT, WIN_WIDTH - X1,
                                                Y4 - NEW_PARAMETER_WINDOW_HEIGHT - Y1)

        self.error_label = QtWidgets.QLabel()
        self.error_label.setFont(QFont("Arial", 15))
        self.error_label.setObjectName("error_lbl")
        self.verticalLayout_6.addWidget(self.error_label)

        name_lbl = QtWidgets.QLabel()
        name_lbl.setText("podaj nazwę drzewa:")
        name_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(name_lbl)

        self.e1 = QLineEdit(self.verticalLayoutWidget_6)
        self.e1.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e1)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_tree_main_bt.setFont(font)
        self.add_tree_main_bt.setAutoDefault(False)
        self.add_tree_main_bt.setObjectName("add_tree_main")
        self.add_tree_main_bt.clicked.connect(self.make_new_tree)
        self.verticalLayout_6.addWidget(self.add_tree_main_bt)
        self.add_tree_main_bt.setText("Utwórz drzewo o takiej nazwie")

    def make_new_tree(self):
        self.load_saved_trees()
        if self.e1.text() in self.trees_list:
            self.error_label.setText("Drzewo o takiej nazwie już istnieje, wybierz inną nazwę")
        else:
            with open(ROOT_DIR + "\\resources\\Tree_files\\" + self.e1.text() + ".json", "w") as file:
                json.dump([], file)
            os.mkdir(ROOT_DIR + "\\resources\\information\\" + self.e1.text())
            with open(ROOT_DIR + "\\resources\\information\\" + self.e1.text() + "\\death_reasons.json", "w") as file:
                json.dump([], file)
            with open(ROOT_DIR + "\\resources\\information\\" + self.e1.text() + "\\illnesses.json", "w") as file:
                json.dump([], file)
            with open(ROOT_DIR + "\\resources\\information\\" + self.e1.text() + "\\professions.json", "w") as file:
                json.dump([], file)
            with open(ROOT_DIR + "\\resources\\information\\" + self.e1.text() + "\\cities.json", "w") as file:
                json.dump([], file)
            self.add_tree_to_saved_trees("../../resources/Tree_files/" + self.e1.text() + ".json")
            self.error_label.setText(f"Udało się dodać drzewo {self.e1.text()}")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przyciski 6,7,8,9 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def append_parameter_to_file(self, file_path):
        parameter = self.e1.text()
        # TODO niedodawalne jak nie wybierzesz drzewa
        file_path = ROOT_DIR + "\\resources\\information\\" + self.trees.currentText().split(".")[0] + file_path
        parameters = json_to_dict(file_path)
        if parameters.get(parameter) is not None:
            self.error_label.setText("dodawanie nie powiodło się, taka nazwa już istnieje")
        else:
            with open(file_path, "r+") as f:
                file_data = json.load(f)
            if len(parameters.values()) > 0:
                dictionary = {'id': max(parameters.values()) + 1, 'name': parameter}
            else:
                dictionary = {'id': 1, 'name': parameter}
            file_data.append(dictionary)
            with open(file_path, "w+") as f:
                json.dump(file_data, f)

            self.error_label.setText("dodawanie powiodło się")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 6 - dodawanie miasta $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def add_city_clicked(self):
        # TODO redundancja
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        self.error_label.setText(" ")
        self.MainWindow.setStyleSheet(START_WINDOW_ADD_CITY_CSS)
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, NEW_PARAMETER_WINDOW_HEIGHT)
        self.verticalLayoutWidget_7.setGeometry(X1, Y1 + NEW_PARAMETER_WINDOW_HEIGHT, WIN_WIDTH - X1,
                                                Y4 - NEW_PARAMETER_WINDOW_HEIGHT - Y1)
        self.error_label = QtWidgets.QLabel()
        self.error_label.setFont(QFont("Arial", 15))
        self.error_label.setObjectName("error_lbl")
        self.verticalLayout_6.addWidget(self.error_label)

        tree_lbl = QtWidgets.QLabel()
        tree_lbl.setText("wybierz drzewo do którego dodajemy miasto:")
        tree_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(tree_lbl)

        self.load_saved_trees()
        self.trees = QtWidgets.QComboBox()
        self.trees.setPlaceholderText("wybierz drzewo")
        self.trees.addItems(self.trees_list)
        self.verticalLayout_6.addWidget(self.trees)

        name_lbl = QtWidgets.QLabel()
        name_lbl.setText("podaj nazwę miasta:")
        name_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(name_lbl)

        self.e1 = QLineEdit(self.verticalLayoutWidget_6)
        self.e1.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e1)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_city_main_bt.setFont(font)
        self.add_city_main_bt.setAutoDefault(False)
        self.add_city_main_bt.clicked.connect(partial(self.append_parameter_to_file, "\\cities.json"))
        self.verticalLayout_6.addWidget(self.add_city_main_bt)
        self.add_city_main_bt.setText("Dodaj miasto o takiej nazwie")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 7 - dodawanie powodu śmierci $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def add_death_reason_clicked(self):
        # TODO redundancja
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_7.count())):
            self.verticalLayout_7.itemAt(i).widget().setParent(None)
        self.MainWindow.setStyleSheet(START_WINDOW_ADD_DEATH_REASON_CSS)
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, NEW_PARAMETER_WINDOW_HEIGHT)
        self.verticalLayoutWidget_7.setGeometry(X1, Y1 + NEW_PARAMETER_WINDOW_HEIGHT, WIN_WIDTH - X1,
                                                Y4 - NEW_PARAMETER_WINDOW_HEIGHT - Y1)
        self.error_label = QtWidgets.QLabel()
        self.error_label.setFont(QFont("Arial", 15))
        self.error_label.setObjectName("error_lbl")
        self.verticalLayout_6.addWidget(self.error_label)

        tree_lbl = QtWidgets.QLabel()
        tree_lbl.setText("wybierz drzewo do którego dodajemy powód śmierci:")
        tree_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(tree_lbl)

        self.load_saved_trees()
        self.trees = QtWidgets.QComboBox()
        self.trees.setPlaceholderText("wybierz drzewo")
        self.trees.addItems(self.trees_list)
        self.verticalLayout_6.addWidget(self.trees)

        name_lbl = QtWidgets.QLabel()
        name_lbl.setText("podaj nazwę powodu śmierci:")
        name_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(name_lbl)

        self.e1 = QLineEdit(self.verticalLayoutWidget_6)
        self.e1.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e1)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_death_reason_main_bt.setFont(font)
        self.add_death_reason_main_bt.setAutoDefault(False)
        self.add_death_reason_main_bt.clicked.connect(partial(self.append_parameter_to_file, "\\death_reasons.json"))
        self.verticalLayout_6.addWidget(self.add_death_reason_main_bt)
        self.add_death_reason_main_bt.setText("Dodaj powód śmierci o powyższej nazwie")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 8 - dodawanie choroby $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def add_illness_clicked(self):
        # TODO redundancja
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        self.error_label.setText(" ")
        self.MainWindow.setStyleSheet(START_WINDOW_ADD_ILLNESS_CSS)
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, NEW_PARAMETER_WINDOW_HEIGHT)
        self.verticalLayoutWidget_7.setGeometry(X1, Y1 + NEW_PARAMETER_WINDOW_HEIGHT, WIN_WIDTH - X1,
                                                Y4 - NEW_PARAMETER_WINDOW_HEIGHT - Y1)
        self.error_label = QtWidgets.QLabel()
        self.error_label.setFont(QFont("Arial", 15))
        self.error_label.setObjectName("error_lbl")
        self.verticalLayout_6.addWidget(self.error_label)

        tree_lbl = QtWidgets.QLabel()
        tree_lbl.setText("wybierz drzewo do którego dodajemy chorobę:")
        tree_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(tree_lbl)

        self.load_saved_trees()
        self.trees = QtWidgets.QComboBox()
        self.trees.setPlaceholderText("wybierz drzewo")
        self.trees.addItems(self.trees_list)
        self.verticalLayout_6.addWidget(self.trees)

        name_lbl = QtWidgets.QLabel()
        name_lbl.setText("podaj nazwę choroby:")
        name_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(name_lbl)

        self.e1 = QLineEdit(self.verticalLayoutWidget_6)
        self.e1.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e1)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_illness_main_bt.setFont(font)
        self.add_illness_main_bt.setAutoDefault(False)
        self.add_illness_main_bt.clicked.connect(partial(self.append_parameter_to_file, "\\illnesses.json"))
        self.verticalLayout_6.addWidget(self.add_illness_main_bt)
        self.add_illness_main_bt.setText("Dodaj chorobę o takiej nazwie")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 9 - dodawanie zawodu $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def add_profession_clicked(self):
        # TODO redundancja
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        self.error_label.setText(" ")
        self.MainWindow.setStyleSheet(START_WINDOW_ADD_PROFESSION_CSS)
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, NEW_PARAMETER_WINDOW_HEIGHT)
        self.verticalLayoutWidget_7.setGeometry(X1, Y1 + NEW_PARAMETER_WINDOW_HEIGHT, WIN_WIDTH - X1,
                                                Y4 - NEW_PARAMETER_WINDOW_HEIGHT - Y1)
        self.error_label = QtWidgets.QLabel()
        self.error_label.setFont(QFont("Arial", 15))
        self.error_label.setObjectName("error_lbl")
        self.verticalLayout_6.addWidget(self.error_label)

        tree_lbl = QtWidgets.QLabel()
        tree_lbl.setText("wybierz drzewo do którego dodajemy zawód:")
        tree_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(tree_lbl)

        self.load_saved_trees()
        self.trees = QtWidgets.QComboBox()
        self.trees.setPlaceholderText("wybierz drzewo")
        self.trees.addItems(self.trees_list)
        self.verticalLayout_6.addWidget(self.trees)

        name_lbl = QtWidgets.QLabel()
        name_lbl.setText("podaj nazwę zawodu:")
        name_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(name_lbl)

        self.e1 = QLineEdit(self.verticalLayoutWidget_6)
        self.e1.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e1)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_profession_main_bt.setFont(font)
        self.add_profession_main_bt.setAutoDefault(False)
        self.add_profession_main_bt.clicked.connect(partial(self.append_parameter_to_file, "\\professions.json"))
        self.verticalLayout_6.addWidget(self.add_profession_main_bt)
        self.add_profession_main_bt.setText("Dodaj zawód o takiej nazwie")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 10 - znajdowanie relacji $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def find_relation_clicked(self):
        # TODO redundancja
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        self.error_label.setText(" ")
        self.MainWindow.setStyleSheet(START_WINDOW_FIND_RELATION_CSS)
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, Y4)
        # self.verticalLayoutWidget_7.setGeometry(X1, Y1 + NEW_PARAMETER_WINDOW_HEIGHT, WIN_WIDTH - X1,
        #                                         Y4 - NEW_PARAMETER_WINDOW_HEIGHT - Y1)

        tree_lbl = QtWidgets.QLabel()
        tree_lbl.setText("wybierz drzewo do którego dodajemy zawód:")
        tree_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(tree_lbl)

        self.load_saved_trees()
        self.trees = QtWidgets.QComboBox()
        self.trees.setPlaceholderText("wybierz drzewo")
        self.trees.addItems(self.trees_list)
        self.verticalLayout_6.addWidget(self.trees)

        self.choose_tree_to_find = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.choose_tree_to_find.setFont(font)
        self.choose_tree_to_find.setAutoDefault(False)
        self.choose_tree_to_find.clicked.connect(self.chose_tree_to_find_relation_clicked)
        self.verticalLayout_6.addWidget(self.choose_tree_to_find)
        self.choose_tree_to_find.setText("W tym drzewie określ relację")

        name_lbl = QtWidgets.QLabel()
        name_lbl.setText("wybierz pierwszą osobę:")
        name_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(name_lbl)

        self.e5.clear()
        self.verticalLayout_6.addWidget(self.e5)

        name2_lbl = QtWidgets.QLabel()
        name2_lbl.setText("wybierz drugą osobę:")
        name2_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(name2_lbl)

        self.e6.clear()
        self.verticalLayout_6.addWidget(self.e6)

        self.find_relation_inside = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.find_relation_inside.setFont(font)
        self.find_relation_inside.setAutoDefault(False)
        self.find_relation_inside.clicked.connect(self.find_relation_inside_clicked)
        self.verticalLayout_6.addWidget(self.find_relation_inside)
        self.find_relation_inside.setText("Określ relację")

        self.error_label = QtWidgets.QLabel()
        self.error_label.setFont(QFont("Arial", 15))
        self.error_label.setObjectName("error_lbl")
        self.verticalLayout_6.addWidget(self.error_label)

    def find_relation_inside_clicked(self):
        first_person = self.e5.currentText()
        second_person = self.e6.currentText()
        first_id = self.people_dict.get(first_person)
        second_id = self.people_dict.get(second_person)
        text_to_show = find_family_relation(first_id, second_id, self.tree_to_open)
        self.error_label.setText(text_to_show)

    def chose_tree_to_find_relation_clicked(self):
        self.tree_to_open = self.trees.currentText()
        self.update_dicts()
        self.e6.addItems(self.people_dict.keys())
        self.e5.addItems(self.people_dict.keys())

    def load_saved_trees(self):
        self.trees_list = []
        with open(ROOT_DIR + "\\resources\\saved_trees.csv", "r") as file:
            csvreader = reader(file)
            for row in csvreader:
                self.trees_list.append(row[1].strip())


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 11 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def find_similarities_clicked(self):
        # TODO redundancja
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.error_label.setText(" ")
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_7.count())):
            self.verticalLayout_7.itemAt(i).widget().setParent(None)
        self.MainWindow.setStyleSheet(START_WINDOW_FIND_SIMILARITIES_CSS)
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, Y4)
        # self.verticalLayoutWidget_7.setGeometry(X1, Y1 + NEW_PARAMETER_WINDOW_HEIGHT, WIN_WIDTH - X1,
        #                                         Y4 - NEW_PARAMETER_WINDOW_HEIGHT - Y1)

        tree_lbl = QtWidgets.QLabel()
        tree_lbl.setText("wybierz pierwsze drzewo do znalezienia podobieństw:")
        tree_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(tree_lbl)

        self.load_saved_trees()
        self.trees = QtWidgets.QComboBox()
        self.trees.setPlaceholderText("wybierz drzewo")
        self.trees.addItems(self.trees_list)
        self.verticalLayout_6.addWidget(self.trees)

        tree_lbl2 = QtWidgets.QLabel()
        tree_lbl2.setText("wybierz drugie drzewo do znalezienia podobieństw:")
        tree_lbl2.setObjectName("lbl2")
        self.verticalLayout_6.addWidget(tree_lbl2)

        self.load_saved_trees()
        self.trees2 = QtWidgets.QComboBox()
        self.trees2.setPlaceholderText("wybierz drzewo")
        self.trees2.addItems(self.trees_list)
        self.verticalLayout_6.addWidget(self.trees2)

        self.choose_tree_to_similarities = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.choose_tree_to_similarities.setFont(font)
        self.choose_tree_to_similarities.setAutoDefault(False)
        self.choose_tree_to_similarities.clicked.connect(self.choose_tree_to_similarities_clicked)
        self.verticalLayout_6.addWidget(self.choose_tree_to_similarities)
        self.choose_tree_to_similarities.setText("W tym drzewie znajdź podobieństwa")

        self.error_label = QtWidgets.QLabel()
        self.error_label.setFont(QFont("Arial", 15))
        self.error_label.setObjectName("error_lbl")
        self.verticalLayout_6.addWidget(self.error_label)

    def choose_tree_to_similarities_clicked(self):
        tree_first_path = ROOT_DIR+"\\resources\\Tree_files\\"+self.trees.currentText()
        tree_second_path = ROOT_DIR + "\\resources\\Tree_files\\" + self.trees2.currentText()
        # if funkcja_do_szukania_podobieństwa(tree_first_path, tree_second_path):
        #     self.error_label.setText("udało się znaleźć podobieństwa")
        #      # TODO czy robimy mergowanie tych drzew?
        #     self.merge_trees = QtWidgets.QPushButton()
        #     self.merge_trees.setAutoDefault(False)
        #     self.merge_trees.clicked.connect(self.merge_trees_clicked)
        #     self.verticalLayout_6.addWidget(self.merge_trees)
        #     self.choose_tree_to_similarities.setText("Połącz te drzewa")
        # else:
        #     self.error_label.setText("nie udało się znaleźć podobieństwa")
        # pass

    def merge_trees_clicked(self):
        # TODO do wywalenie jak nie mergujemy tych drzew
        pass

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 12 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def analise_tree_clicked(self):
        # TODO redundancja
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.error_label.setText(" ")
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_7.count())):
            self.verticalLayout_7.itemAt(i).widget().setParent(None)
        self.MainWindow.setStyleSheet(START_WINDOW_ANALISE_TREE_CSS)
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, Y4)
        # self.verticalLayoutWidget_7.setGeometry(X1, Y1 + NEW_PARAMETER_WINDOW_HEIGHT, WIN_WIDTH - X1,
        #                                         Y4 - NEW_PARAMETER_WINDOW_HEIGHT - Y1)

        tree_lbl = QtWidgets.QLabel()
        tree_lbl.setText("wybierz drzewo do przeanalizowania:")
        tree_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(tree_lbl)

        self.load_saved_trees()
        self.trees = QtWidgets.QComboBox()
        self.trees.setPlaceholderText("wybierz drzewo")
        self.trees.addItems(self.trees_list)
        self.verticalLayout_6.addWidget(self.trees)

        self.choose_tree_to_analise = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.choose_tree_to_analise.setFont(font)
        self.choose_tree_to_analise.setAutoDefault(False)
        self.choose_tree_to_analise.clicked.connect(self.choose_tree_to_analise_clicked)
        self.verticalLayout_6.addWidget(self.choose_tree_to_analise)
        self.choose_tree_to_analise.setText("W to drzewo analizuj")

        self.error_label = QtWidgets.QLabel()
        self.error_label.setFont(QFont("Arial", 15))
        self.error_label.setObjectName("error_lbl")
        self.verticalLayout_6.addWidget(self.error_label)

    def choose_tree_to_analise_clicked(self):
        tree_path = ROOT_DIR + "\\resources\\Tree_files\\" + self.trees.currentText()