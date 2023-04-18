from _csv import reader
from functools import partial
from os import listdir
from shutil import copyfile
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import  QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QLineEdit
from src.definitions.definitions import ROOT_DIR
from src.gui.not_used.tree_window import TreeWindow
from src.gui.tree_window_graph_ui import TreeWindowGraphUi
from src.io_functions.read_data import read_data


class StartWindowUi(object):
    def setupUi(self, MainWindow):
        self.tree_to_open = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 344)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 151, 80))
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
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 80, 151, 50))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 0, 441, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 130, 151, 200))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(149, 79, 441, 221))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        MainWindow.setCentralWidget(self.centralwidget)


        self.show_saved_trees = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.show_saved_trees.setGeometry(QtCore.QRect(0,0,40,40))
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
        self.add_person.clicked.connect(partial(self.add_person_clicked,MainWindow))

        # self.verticalLayoutWidget_3.setStyleSheet("""background-color: rgb(43, 84, 126)""")

        # TODO
        # self.setStyleSheet("""
        #     #verticalLayoutWidget_5 {
        #         background-color: "green";
        #         color: "white";
        #     }""")
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
        with open(ROOT_DIR+ "\\resources\\saved_trees.csv", "r") as file:
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
        attr.clicked.connect(partial(self.radio_bt_clicked,tree_name))

    def radio_bt_clicked(self,attr):
        self.tree_to_open = attr

    def show_saved_trees_clicked(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.add_saved_trees()

        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 151, 80))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 60, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        # self.verticalLayoutWidget_5.setStyleSheet("""background-color: rgb(43, 84, 126)""")
        self.verticalLayout_3.addWidget(self.verticalLayoutWidget_5)

        self.add_tree_bt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_tree_bt.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_tree_bt.setFont(font)
        self.add_tree_bt.setObjectName("add_tree_bt")
        self.verticalLayout_5.addWidget(self.add_tree_bt)

        self.open_tree_bt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.open_tree_bt.setGeometry(QtCore.QRect(485, 240, 104, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.open_tree_bt.setFont(font)
        self.open_tree_bt.setAutoDefault(False)
        self.open_tree_bt.setObjectName("open_tree_bt")
        self.verticalLayout_5.addWidget(self.open_tree_bt)

        self.add_tree_bt.setText("Dodaj drzewo")
        self.open_tree_bt.setText("Otwórz drzewo")

        self.add_tree_bt.clicked.connect(self.add_tree_clicked)
        self.open_tree_bt.clicked.connect(self.open_tree_clicked)


    def clicked_tmp(self):
        print("klinkieto")


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

    def add_person_clicked(self,MainWindow):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)

        # self.choose_tree_window = ChooseTreeWindow()
        # self.choose_tree_window.show()
        name_lbl = QtWidgets.QLabel()
        name_lbl.setText("imię:")
        self.verticalLayout_4.addWidget(name_lbl)
        e1 = QLineEdit()
        e1.setFont(QFont("Arial", 12))
        self.verticalLayout_4.addWidget(e1)


        surname_lbl = QtWidgets.QLabel()
        surname_lbl.setText("nazwisko:")
        self.verticalLayout_4.addWidget(surname_lbl)
        e4 = QLineEdit()
        # e4.textChanged.connect(self.textchanged)
        self.verticalLayout_4.addWidget(e4)


        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 151, 80))
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
        self.verticalLayout_5.addWidget(add_person_bt)
        add_person_bt.clicked.connect(partial(self.enter_person,e1, e4))

        add_person_bt.setText("Dodaj tę osobę")

    def textchanged(self, text):
        print("Changed: " + text)

    def enter_person(self, e1, e4):
        print(f"{e1.text()} {e4.text()}")
