import json
from _csv import reader
from collections import deque
from functools import partial
from os import listdir
from shutil import copyfile
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QLineEdit, QMainWindow
from src.definitions.definitions import *
from src.definitions.ui_css import START_WINDOW_SHOW_SAVED_TREES_CSS, START_WINDOW_PREPARE_BACKGROUND_CSS, \
    START_WINDOW_FIND_PERSON_CSS, START_WINDOW_EDIT_PERSON_CLICKED
from src.gui.multi_combobox import CheckableComboBox
from src.gui.person_window import PersonWindow
from src.gui.tree_window_graph_ui import TreeWindowGraphUi
from src.io_functions.json_to_list import json_to_list
from src.io_functions.read_data import read_data
from src.io_functions.read_people import read_people_to_list


# TODO obsługa niedziałających drzew, tzn takich o niepełnej strukturze, że brakuje pól w jsonie czy coś
# TODO przejść na show zamiast ponownego tworzenia atrybutów
class StartWindowUi(object):
    def __init__(self):
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
        self.e6 = None
        self.e5 = None
        self.e4 = None
        self.is_dead = None
        self.e3 = None
        self.e2 = None
        self.e1 = None
        self.widget = None
        self.open_tree_bt = None
        self.add_tree_bt = None
        self.edit_person = None
        self.find_person = None
        self.add_person = None
        self.show_saved_trees = None
        self.verticalLayout_7 = None
        self.verticalLayoutWidget_7 = None
        self.verticalLayout_6 = None
        self.verticalLayoutWidget_6 = None
        self.verticalLayout_4 = None
        self.verticalLayoutWidget_4 = None
        self.verticalLayout_3 = None
        self.verticalLayoutWidget_3 = None
        self.verticalLayoutWidget_3 = None
        self.horizontalLayout = None
        self.horizontalLayoutWidget = None
        self.verticalLayout_2 = None
        self.man_list = []
        self.woman_list = []
        self.death_reasons = []
        self.death_reasons_dicts = []
        self.places = []
        self.places_dicts = []
        self.illnesses = []
        self.illnesses_dicts = []
        self.people_list = []
        self.professions = []
        self.professions_dicts = []
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

        self.show_saved_trees = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.show_saved_trees.setFont(font)
        self.show_saved_trees.setAutoDefault(False)
        self.show_saved_trees.setObjectName("show_saved_trees")
        self.verticalLayout_2.addWidget(self.show_saved_trees)
        self.show_saved_trees.clicked.connect(self.show_saved_trees_clicked)

        self.add_person = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.add_person.setFont(font)
        self.add_person.setAutoDefault(False)
        self.add_person.setObjectName("add_person")
        self.verticalLayout_2.addWidget(self.add_person)
        self.add_person.clicked.connect(self.add_person_clicked)

        self.find_person = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.find_person.setFont(font)
        self.find_person.setAutoDefault(False)
        self.find_person.setObjectName("find_person")
        self.verticalLayout_2.addWidget(self.find_person)
        self.find_person.clicked.connect(self.find_person_clicked)

        self.edit_person = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.edit_person.setFont(font)
        self.edit_person.setAutoDefault(False)
        self.edit_person.setObjectName("edit_person")
        self.verticalLayout_2.addWidget(self.edit_person)
        self.edit_person.clicked.connect(self.edit_person_clicked)

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

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 1 - dodawanie drzewa z pliku $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def add_saved_trees(self) -> None:
        """ Dodawanie już zapisanych drzew do odpowiedniej komórki"""
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        tree_names = []
        with open(ROOT_DIR + "\\resources\\saved_trees.csv", "r") as file:
            csvreader = reader(file)
            for row in csvreader:
                tree_names.append(row[1].strip())
        for tree_name in tree_names:
            self.add_saved_tree(tree_name)

    def add_saved_tree(self, tree_name: str) -> None:
        """ Dodawanie pojedynczego drzewa i tworzenie mu atrybutu w klasie"""
        bt_name = "radioButton_" + tree_name
        # TODO sprawdzanie czy już takiego atrybutu nie ma, bo jak jest to bez sensu duplikować
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
            main_person = read_data(self.tree_to_open, 6)
            # id 6 to babcia, id 4 mama, id 1 ja, 3grzegorz
            # TODO wywalić te dwie linijki, albo dołożyć wybór printowania drzewa
            # self.tree_window = TreeWindow(main_person, self.tree_to_open.split(".")[0])
            # self.tree_window.show()

            graph_ui = TreeWindowGraphUi()
            canvas = graph_ui.setup_ui(main_person)
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
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_7.count())):
            self.verticalLayout_7.itemAt(i).widget().setParent(None)

        self.MainWindow.setStyleSheet(START_WINDOW_PREPARE_BACKGROUND_CSS)
        self.tree_to_open = None
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, WIN_WIDTH - X2, WIN_HEIGHT - Y1)
        self.add_saved_trees()

        self.verticalLayoutWidget_6.setGeometry(X1, Y1, X2 - X1, WIN_HEIGHT - Y1)
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
        self.e5 = QtWidgets.QComboBox()
        self.e5.clear()
        self.e5.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e5)

        mother_lbl = QtWidgets.QLabel()
        mother_lbl.setText("matka:")
        self.verticalLayout_6.addWidget(mother_lbl)
        self.e6 = QtWidgets.QComboBox()
        self.e6.clear()
        self.e6.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e6)

        partners_lbl = QtWidgets.QLabel()
        partners_lbl.setText("partnerzy:")
        self.verticalLayout_6.addWidget(partners_lbl)
        self.e8 = CheckableComboBox()
        self.e8.clear()
        self.e8.setPlaceholderText("wybierz partnerów")
        self.verticalLayout_6.addWidget(self.e8)

        gender_lbl = QtWidgets.QLabel()
        gender_lbl.setText("płeć:")
        self.verticalLayout_6.addWidget(gender_lbl)
        self.e9 = QtWidgets.QComboBox()
        self.e9.setPlaceholderText("wybierz płeć")
        self.e9.addItem("Mężczyzna")
        self.e9.addItem("Kobieta")
        self.verticalLayout_6.addWidget(self.e9)

        death_reason_lbl = QtWidgets.QLabel()
        death_reason_lbl.setText("przyczyna śmierci:")
        self.verticalLayout_6.addWidget(death_reason_lbl)
        self.e10 = QtWidgets.QComboBox()
        self.e10.clear()
        self.e10.setPlaceholderText("wybierz przyczynę śmierci")
        self.verticalLayout_6.addWidget(self.e10)

        birth_place_lbl = QtWidgets.QLabel()
        birth_place_lbl.setText("miejsce urodzenia:")
        self.verticalLayout_6.addWidget(birth_place_lbl)
        self.e11 = QtWidgets.QComboBox()
        self.e11.clear()
        self.e11.setPlaceholderText("wybierz miejsce urodzenia")
        self.verticalLayout_6.addWidget(self.e11)

        professions_lbl = QtWidgets.QLabel()
        professions_lbl.setText("zawody:")
        self.verticalLayout_6.addWidget(professions_lbl)
        self.e12 = CheckableComboBox()
        self.e12.clear()
        self.e12.setPlaceholderText("wybierz partnerów")
        self.verticalLayout_6.addWidget(self.e12)

        illnesses_lbl = QtWidgets.QLabel()
        illnesses_lbl.setText("choroby:")
        self.verticalLayout_6.addWidget(illnesses_lbl)
        self.e13 = CheckableComboBox()
        self.e13.clear()
        self.e13.setPlaceholderText("wybierz partnerów")
        self.verticalLayout_6.addWidget(self.e13)

        residences_lbl = QtWidgets.QLabel()
        residences_lbl.setText("miejsca zamieszkania:")
        self.verticalLayout_6.addWidget(residences_lbl)
        self.e14 = CheckableComboBox()
        self.e14.clear()
        self.e14.setPlaceholderText("wybierz partnerów")
        self.verticalLayout_6.addWidget(self.e14)

    def is_dead_clicked(self) -> None:
        if self.is_dead.isChecked():
            self.e4.setDisabled(True)
        else:
            self.e4.setDisabled(False)

    def import_data_from_tree(self) -> None:
        self.update_dicts()
        self.put_people_to_combobox()

    def put_people_to_combobox(self) -> None:
        # ojcowie
        self.e5.clear()
        if len(self.man_list) > 0:
            self.e5.setPlaceholderText("wybierz osobę")
        for person in self.man_list:
            self.e5.addItem(person[0])

        # matki
        self.e6.clear()
        if len(self.woman_list) > 0:
            self.e6.setPlaceholderText("wybierz osobę")
        for person in self.woman_list:
            self.e6.addItem(person[0])

        # partnerzy
        self.e8.clear()
        if len(self.people_list) > 0:
            self.e8.setPlaceholderText("wybierz osobę")
        for person in self.people_list:
            self.e8.addItem(person[0])

        # przyczyna śmierci
        self.e10.addItems(self.death_reasons)

        # miejsce urodzenia
        self.e11.addItems(self.places)

        # robota
        self.e12.addItems(self.professions)

        # choroby
        self.e13.addItems(self.illnesses)

        # miejsca zamieszkania
        self.e14.addItems(self.places)

    def update_dicts(self) -> None:
        file_path = ROOT_DIR + "\\resources\\information\\" + self.tree_to_open.split(".")[0]
        if self.tree_to_open is not None:
            self.people_list = read_people_to_list(self.tree_to_open)
            for person in self.people_list:
                if person[2] == "W":
                    self.woman_list.append(person)
                else:
                    self.man_list.append(person)
        self.places_dicts = json_to_list(file_path + "\\cities.json")
        self.places = [place.get('name') for place in self.places_dicts]
        self.death_reasons_dicts = json_to_list(file_path + "\\death_reasons.json")
        self.death_reasons = [death.get('name') for death in self.death_reasons_dicts]
        self.illnesses_dicts = json_to_list(file_path + "\\illnesses.json")
        self.illnesses = [illness.get('name') for illness in self.illnesses_dicts]
        self.professions_dicts = json_to_list(file_path + "\\professions.json")
        self.professions = [profession.get('name') for profession in self.professions_dicts]

# $$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 2 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def add_person_clicked(self) -> None:
        self.prepare_background()
        add_person_bt = QtWidgets.QPushButton(parent=self.central_widget)
        add_person_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        add_person_bt.setFont(font)
        add_person_bt.setObjectName("add_person_bt")
        self.verticalLayout_6.addWidget(add_person_bt)
        add_person_bt.clicked.connect(self.enter_person)

        choose_tree_bt = QtWidgets.QPushButton(parent=self.central_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        choose_tree_bt.setFont(font)
        choose_tree_bt.setObjectName("add_person_bt")
        choose_tree_bt.setText("do tego drzewa dodaj")
        self.verticalLayout_4.addWidget(choose_tree_bt)
        choose_tree_bt.clicked.connect(self.import_data_from_tree)

        add_person_bt.setText("Dodaj tę osobę")

    def enter_person(self) -> None:
        """ Dopisywanie nowej osoby do pliku drzewa """
        # TODO czy to nie jest redundancja kodu?
        # father
        father_id = 0
        for man in self.man_list:
            if self.e5.currentText() == man[0]:
                father_id = man[1]

        # mother
        mother_id = 0
        for woman in self.woman_list:
            if self.e6.currentText() == woman[0]:
                mother_id = woman[1]

        # TODO birth date dopisywanie do pliku
        # death date
        if self.is_dead.isChecked():
            death_date = None
        else:
            death_date = self.e4.text()

        file_path = ROOT_DIR + "\\resources\\Tree_files\\" + self.tree_to_open

        # TODO partners
        # TODO gender
        # TODO death reason
        # TODO birth place
        # TODO profession
        # TODO illnesses
        # TODO residences

        with open(file_path, "r+") as f:
            file_data = json.load(f)

        new_id = 1
        file_data.sort(key=lambda x: x["person_id"])
        for person_data in file_data:
            if person_data["person_id"] > new_id:
                new_id = person_data["person_id"]
                new_id += 1

        person_data_dictionary = {'person_id': new_id, 'father_id': father_id, 'mother_id': mother_id,
                                  'first_name': self.e1.text(),
                                  'last_name': self.e2.text(), 'birth_date': self.e3.text(), 'death_date': death_date,
                                  'partners_id': [],
                                  'gender': 1, 'death_reason': None, 'birth_place': 1, 'profession': 1, 'illnesses': [],
                                  'residences': [1, 2]}

        file_data.append(person_data_dictionary)

        with open(file_path, "w+") as f:
            json.dump(file_data, f)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 3 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def find_person_clicked(self) -> None:
        self.prepare_background()
        self.MainWindow.setStyleSheet(START_WINDOW_FIND_PERSON_CSS)

        add_person_bt = QtWidgets.QPushButton(parent=self.central_widget)
        add_person_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        add_person_bt.setFont(font)
        add_person_bt.setObjectName("find_person_bt")
        self.verticalLayout_6.addWidget(add_person_bt)
        add_person_bt.clicked.connect(self.find_person_in_tree)
        add_person_bt.setText("szukaj taką osobę")

        choose_tree_bt = QtWidgets.QPushButton(parent=self.central_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        choose_tree_bt.setFont(font)
        choose_tree_bt.setObjectName("choose_tree_bt")
        choose_tree_bt.setText("w tym drzewie szukaj")
        self.verticalLayout_4.addWidget(choose_tree_bt)
        choose_tree_bt.clicked.connect(self.import_data_from_tree)

    def find_person_in_tree(self) -> None:
        main_person = read_data(self.tree_to_open, 1)
        output_list = []
        que = deque()
        que.append(main_person)
        visited = set()
        while len(que) > 0:
            person_tmp = que.pop()
            if person_tmp.person_id not in visited:
                if person_tmp.father is not None:
                    que.append(main_person.father)
                if person_tmp.mother is not None:
                    que.append(main_person.mother)
                for child in person_tmp.children:
                    que.append(child)
                for partner in person_tmp.partners:
                    que.append(partner)
                # TODO poprawić szukanie ludzi
                if person_tmp.first_name == self.e1.text():
                    output_list.append(person_tmp)
                visited.add(person_tmp.person_id)

        for person in output_list:
            # TODO niech się doda tyle atrybutów ile jest ludzi bo nie wiem czy to tak będzie działać
            self.window = PersonWindow(person, self.tree_to_open)
            self.window.show()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Przycisk 4 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def edit_person_clicked(self) -> None:
        self.prepare_background()
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, WIN_WIDTH - X2, Y3 - Y1)
        self.verticalLayoutWidget_7.setGeometry(X2, Y3, WIN_WIDTH - X2, WIN_HEIGHT - Y3)
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
        self.choose_tree_bt.setText("w tym drzewie wybierz osobe")
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
        father_id = self.person_to_edit.father.person_id
        for man in self.man_list:
            if self.e5.currentText() == man[0]:
                father_id = man[1]
        mother_id = self.person_to_edit.mother.person_id
        for woman in self.woman_list:
            if self.e6.currentText() == woman[0]:
                mother_id = woman[1]
        if self.is_dead.isChecked():
            death_date = None
        else:
            death_date = self.e4.text()

        file_path = ROOT_DIR + "\\resources\\Tree_files\\" + self.tree_to_open

        with open(file_path, "r+") as f:
            file_data = json.load(f)

        id_to_remove = None
        for i in range(len(file_data)):
            if file_data[i]['person_id'] == self.id_to_edit:
                id_to_remove = i
        if id_to_remove is not None:
            file_data.pop(id_to_remove)
        birth_date_list = self.e3.text().split(".")
        birth_date_list.reverse()
        birth_date = "-".join(birth_date_list)
        dict = {'person_id': self.id_to_edit, 'father_id': father_id, 'mother_id': mother_id,
                'first_name': self.e1.text(),
                'last_name': self.e2.text(), 'birth_date': birth_date, 'death_date': death_date, 'partners_id': []}

        file_data.append(dict)

        with open(file_path, "w+") as f:
            json.dump(file_data, f)

    def import_people_from_tree_to_edit(self) -> None:
        self.update_dicts()
        self.e7.setPlaceholderText("wybierz osobę")
        self.e7.setDisabled(False)
        self.choose_person_to_edit.setDisabled(False)
        for person in self.people_list:
            self.e7.addItem(person[0])

    def choose_person_to_edit_clicked(self) -> None:
        self.put_people_to_combobox()
        self.id_to_edit = 0
        # TODO zrobić z people_list set
        for person in self.people_list:
            if person[0] == self.e7.currentText():
                self.id_to_edit = person[1]
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
        else:
            self.e4.setDisabled(False)
        self.e5.setDisabled(False)
        self.e5.setPlaceholderText(f"{self.person_to_edit.father.first_name} {self.person_to_edit.father.last_name}")
        self.e6.setDisabled(False)
        self.e6.setPlaceholderText(f"{self.person_to_edit.mother.first_name} {self.person_to_edit.mother.last_name}")
        self.e8.setDisabled(False)
        self.e8.setPlaceholderText(str(self.person_to_edit.gender))
        self.e9.setDisabled(False)
        # TODO ustawić, żeby było już kliknięte w multi Comboboxach
        # self.e9.setPlaceholderText()
        self.e10.setDisabled(False)
        self.e10.setPlaceholderText(self.person_to_edit.birth_place)
        # TODO jak osoba żyje to nic nie wpisywać
        # TODO chyba nadal to wpisywanie nie działa
        self.e11.setDisabled(False)
        self.e11.setPlaceholderText(self.person_to_edit.death_reason)
        self.e12.setDisabled(False)
        # self.e12.setPlaceholderText()
        self.e13.setDisabled(False)
        # self.e13.setPlaceholderText()
        self.e14.setDisabled(False)
        # self.e14.setPlaceholderText()
        self.edit_person_bt.setDisabled(False)
