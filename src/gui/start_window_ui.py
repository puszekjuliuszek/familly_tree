import json
from _csv import reader
from functools import partial
from os import listdir
from shutil import copyfile
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QLineEdit, QScrollArea
from PyQt6.QtCore import Qt
from src.definitions.definitions import *
from src.gui.not_used.tree_window import TreeWindow
from src.gui.tree_window_graph_ui import TreeWindowGraphUi
from src.io_functions.read_data import read_data
from src.io_functions.read_people import read_people_to_list


class StartWindowUi(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.tree_to_open = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(WIN_WIDTH, WIN_HEIGHT)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
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

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, Y1, X1, Y2 - Y1))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(X1, 0, WIN_WIDTH - X1, Y1))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, Y2, X1, WIN_HEIGHT - Y2))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(X1, Y1, WIN_WIDTH - X1, WIN_HEIGHT - Y1))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN,REGULAR_MARGIN)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(X1, Y1, 0, 0))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN, REGULAR_MARGIN)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        MainWindow.setCentralWidget(self.centralwidget)

        self.show_saved_trees = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.show_saved_trees.setGeometry(QtCore.QRect(0, 0, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.show_saved_trees.setFont(font)
        self.show_saved_trees.setAutoDefault(False)
        self.show_saved_trees.setObjectName("show_saved_trees")
        self.verticalLayout_2.addWidget(self.show_saved_trees)
        self.show_saved_trees.clicked.connect(self.show_saved_trees_clicked)

        self.add_person = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.add_person.setGeometry(QtCore.QRect(0, 0, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.add_person.setFont(font)
        self.add_person.setAutoDefault(False)
        self.add_person.setObjectName("add_person")
        self.verticalLayout_2.addWidget(self.add_person)
        self.add_person.clicked.connect(self.add_person_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menadżer drzew genealogicznych"))
        self.label.setText(_translate("MainWindow", "MENADŻER\nDRZEW\nGENELOGICZNYCH"))
        self.show_saved_trees.setText(_translate("MainWindow", "Przeglądaj zapisane drzewa"))
        self.add_person.setText(_translate("MainWindow", "Dodaj osobę"))

    def add_saved_trees(self):
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        tree_names = []
        with open(ROOT_DIR + "\\resources\\saved_trees.csv", "r") as file:
            csvreader = reader(file)
            for row in csvreader:
                tree_names.append(row[1].strip())
        for tree_name in tree_names:
            self.add_saved_tree(tree_name)

    def add_saved_tree(self, tree_name):
        bt_name = "radioButton_" + tree_name
        # TODO sprawdzanie czy już takiego atrybutu nie ma, bo jak jest to bez sensu duplikować
        setattr(self, bt_name, QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_4))
        attr = getattr(self, bt_name)
        attr.setObjectName(bt_name)
        self.verticalLayout_4.addWidget(attr)
        attr.setText(QtCore.QCoreApplication.translate("MainWindow", tree_name))
        attr.clicked.connect(partial(self.radio_bt_clicked, tree_name))

    def radio_bt_clicked(self, attr):
        self.tree_to_open = attr

    def show_saved_trees_clicked(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.verticalLayoutWidget_4.setGeometry(X1, Y1, WIN_WIDTH - X1, WIN_HEIGHT - Y1)
        self.verticalLayoutWidget_6.setGeometry(X1, Y1, 0, 0)
        self.add_saved_trees()

        self.MainWindow.setStyleSheet("""
                            #show_saved_trees {
                                background-color: rgba(44,49,62,255);
                                color: "white";
                                border: 2px solid white;
                                border-color: rgba(44,49,62,255);
                            }
                            QWidget {
                                background-color: rgba(27,29,35,255);
                                color: "white";
                            }
                            #verticalLayoutWidget_4 {
                            background-color: rgba(44,49,62,255);
                            color: "white";
                        }
                        
                    QLabel {
                        background-color: rgba(44,49,62,255);
                        color: "white";
                     }
                     QRadioButton {
                        background-color: rgba(44,49,62,255);
                        color: "white";
                     }
                     #label{
                     background-color: rgba(27,29,35,255)
                     }""")

        self.add_tree_bt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_tree_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_tree_bt.setFont(font)
        self.add_tree_bt.setObjectName("add_tree_bt")
        self.verticalLayout_4.addWidget(self.add_tree_bt)

        self.open_tree_bt = QtWidgets.QPushButton(parent=self.centralwidget)
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
    def add_tree_to_saved_trees(path):
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
    def make_copy_of_a_tree(path):
        filenames = listdir('/'.join(path.split("/")[0:-1]))
        tree_name = path.split("/")[-1]
        if tree_name not in filenames:
            copyfile(path, "../../resources/Tree_files/" + tree_name)

    def add_tree_clicked(self):
        fname = QFileDialog.getOpenFileName(None, "Open File", "../../resources/Tree_files", "JSON Files (*.json)")
        if fname:
            self.add_tree_to_saved_trees(fname[0])
            self.make_copy_of_a_tree(fname[0])
            self.add_saved_trees()
        else:
            # TODO wywala apke jak nie wybierzesz niczego tylko zamkniesz okno
            pass

    def open_tree_clicked(self):
        if self.tree_to_open is not None:
            main_person = read_data(self.tree_to_open, 1)
            # id 6 to babcia, id 4 mama, id 1 ja, 3grzegorz
            # TODO wywalić te dwie linijki, albo dołożyć wybór printowania drzewa
            self.tree_window = TreeWindow(main_person, self.tree_to_open.split(".")[0])
            self.tree_window.show()

            graph_ui = TreeWindowGraphUi()
            canvas = graph_ui.setup_ui(main_person)
            canvas.figure.canvas.mpl_connect('pick_event', self.on_node_click)
            self.widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(canvas)
            self.widget.setLayout(layout)
            self.widget.show()

    def on_node_click(self, event):
        node_text = event.artist.get_text()
        node_num = str(node_text)
        print(f"Kliknięto węzeł {node_num}")

    def add_person_clicked(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(i).widget().setParent(None)

        self.MainWindow.setStyleSheet("""
                    #add_person {
                        background-color: rgba(44,49,62,255);
                        color: "white";
                        border: 2px solid white;
                        border-color: rgba(44,49,62,255);
                    }
                    QWidget {
                        background-color: rgba(27,29,35,255);
                        color: "white";
                     }
                     #verticalLayoutWidget_4 {
                            background-color: rgba(44,49,62,255);
                            color: "white";
                        }
                        #verticalLayoutWidget_6 {
                            background-color: rgba(44,49,62,255);
                            color: "white";
                        }
                        QWidget {
                            color: white;
                        }
                        QLabel {
                        background-color: rgba(44,49,62,255);
                     }
                     QRadioButton {
                        background-color: rgba(44,49,62,255);
                     }
                     QCheckBox {
                        background-color: rgba(44,49,62,255);
                     }
                     QLineEdit {
                        background-color: rgba(80,90,120,255);
                     }
                     QComboBox {
                        background-color: rgba(80,90,120,255);
                     }
                     QDateEdit {
                        background-color: rgba(80,90,120,255);
                     }
                     #label{
                     background-color: rgba(27,29,35,255)
                     }
                        
                        """)
        self.tree_to_open = None
        self.verticalLayoutWidget_4.setGeometry(X2, Y1, WIN_WIDTH - X2, WIN_HEIGHT - Y1)
        self.add_saved_trees()

        self.verticalLayoutWidget_6.setGeometry(X1, Y1, X2 - X1, WIN_HEIGHT - Y1)

        name_lbl = QtWidgets.QLabel()
        name_lbl.setText("imię:")
        name_lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(name_lbl)
        e1 = QLineEdit(self.verticalLayoutWidget_6)
        e1.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(e1)

        surname_lbl = QtWidgets.QLabel()
        surname_lbl.setText("nazwisko:")
        self.verticalLayout_6.addWidget(surname_lbl)
        e2 = QLineEdit()
        e2.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(e2)

        birth_lbl = QtWidgets.QLabel()
        birth_lbl.setText("data urodzenia:")
        self.verticalLayout_6.addWidget(birth_lbl)
        e3 = QtWidgets.QDateEdit()
        e3.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(e3)

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

        self.man_list = []
        self.woman_list = []
        father_lbl = QtWidgets.QLabel()
        father_lbl.setText("ojciec:")
        self.verticalLayout_6.addWidget(father_lbl)
        self.e5 = QtWidgets.QComboBox()
        self.put_people_to_combobox()
        self.e5.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e5)

        mother_lbl = QtWidgets.QLabel()
        mother_lbl.setText("matka:")
        self.verticalLayout_6.addWidget(mother_lbl)
        self.e6 = QtWidgets.QComboBox()
        self.put_people_to_combobox()
        self.e6.setFont(QFont("Arial", 11))
        self.verticalLayout_6.addWidget(self.e6)

        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, X1, Y1))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 60, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3.addWidget(self.verticalLayoutWidget_5)

        add_person_bt = QtWidgets.QPushButton(parent=self.centralwidget)
        add_person_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        add_person_bt.setFont(font)
        add_person_bt.setObjectName("add_person_bt")
        self.verticalLayout_6.addWidget(add_person_bt)
        add_person_bt.clicked.connect(partial(self.enter_person, e1, e2, e3))

        choose_tree_bt = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        choose_tree_bt.setFont(font)
        choose_tree_bt.setObjectName("add_person_bt")
        choose_tree_bt.setText("do tego drzewa dodaj")
        self.verticalLayout_4.addWidget(choose_tree_bt)
        choose_tree_bt.clicked.connect(self.import_people_from_tree)

        add_person_bt.setText("Dodaj tę osobę")

    def is_dead_clicked(self):
        if self.is_dead.isChecked():
            self.e4.setDisabled(True)
        else:
            self.e4.setDisabled(False)

    def enter_person(self, e1, e2, e3):
        father_id = 0
        for man in self.man_list:
            if self.e5.currentText() == man[0]:
                father_id = man[1]
        mother_id = 0
        for woman in self.woman_list:
            if self.e6.currentText() == woman[0]:
                mother_id = woman[1]
        if self.is_dead.isChecked():
            death_date = None
        else:
            death_date = self.e4.text()

        file_path = ROOT_DIR + "\\resources\\Tree_files\\" + self.tree_to_open
        dict = {'person_id': 11, 'father_id': father_id, 'mother_id': mother_id,
                      'first_name': e1.text(),
                      'last_name': e2.text(), 'birth_date': e3.text(), 'death_date': death_date, 'partners_id': []}

        with open(file_path, "r+") as f:
            file_data = json.load(f)
        file_data.append(dict)
        with open(file_path, "w+") as f:
            json.dump(file_data,f)


        print(f"{e1.text()} {e2.text()} {e3.text()} {death_date} {str(father_id)} {str(mother_id)}")

    def import_people_from_tree(self):
        if self.tree_to_open is not None:
            people_list = read_people_to_list(self.tree_to_open)
            for person in people_list:
                if person[2] == "W":
                    self.woman_list.append(person)
                else:
                    self.man_list.append(person)
        self.put_people_to_combobox()

    def put_people_to_combobox(self):
        if len(self.man_list) > 0:
            self.e5.setPlaceholderText("wybierz osobę")
        if len(self.woman_list) > 0:
            self.e6.setPlaceholderText("wybierz osobę")
        for person in self.man_list:
            self.e5.addItem(person[0])
        for person in self.woman_list:
            self.e6.addItem(person[0])
