from _csv import reader
from functools import partial

from PyQt6 import QtCore, QtGui, QtWidgets

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
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 80, 151, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 0, 441, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 130, 151, 171))
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

        self.add_saved_trees()

        self.add_tree_bt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_tree_bt.setGeometry(QtCore.QRect(493, 270, 96, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.add_tree_bt.setFont(font)
        self.add_tree_bt.setObjectName("add_tree_bt")

        self.open_tree_bt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.open_tree_bt.setGeometry(QtCore.QRect(485, 240, 104, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.open_tree_bt.setFont(font)
        self.open_tree_bt.setAutoDefault(False)
        self.open_tree_bt.setObjectName("open_tree_bt")
        MainWindow.setCentralWidget(self.centralwidget)

        #TODO
        # self.setStyleSheet("""
        #     #horizontalLayoutWidget {
        #         background-color: "green";
        #         color: "white";
        #     }""")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MENADŻER\nDRZEW\nGENELOGICZNYCH"))
        self.label_2.setText(_translate("MainWindow", "Przeglądaj zapisane drzewa"))
        self.add_tree_bt.setText(_translate("MainWindow", "Dodaj drzewo"))
        self.open_tree_bt.setText(_translate("MainWindow", "Otwórz drzewo"))

    def add_saved_trees(self):
        for i in reversed(range(self.verticalLayout_4.count())):
            self.verticalLayout_4.itemAt(i).widget().setParent(None)
        tree_names = []
        with open("../../resources/saved_trees.csv", "r") as file:
            csvreader = reader(file)
            for row in csvreader:
                tree_names.append(row[1].strip())
        for tree_name in tree_names:
            self.add_saved_tree(tree_name)

    def add_saved_tree(self, tree_name):
        bt_name = "radioButton_" + tree_name
        setattr(self, bt_name, QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_4))
        attr = getattr(self, bt_name)
        attr.setObjectName(bt_name)
        self.verticalLayout_4.addWidget(attr)
        attr.setText(QtCore.QCoreApplication.translate("MainWindow", tree_name))
        attr.clicked.connect(partial(self.radio_bt_clicked,tree_name))

    def radio_bt_clicked(self,attr):
        self.tree_to_open = attr
