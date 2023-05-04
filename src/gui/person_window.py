import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget

from src.definitions.definitions import ROOT_DIR


class PersonWindow(QWidget):
    def __init__(self, person, tree):
        super(PersonWindow, self).__init__()
        self.person = person
        self.tree = tree
        self.setupUi(self)
        self.setStyleSheet("""QWidget {
                                background-color: rgba(27,29,35,255);
                                color: "white";
                             }""")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(496, 454)
        path = ROOT_DIR + "\\resources\\pictures\\" + self.tree.split(".")[0] + "\\" + str(self.person.person_id)
        photos = os.listdir(path)
        if len(photos) > 0:
            height_tmp = 200
        else:
            height_tmp = 0

        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setGeometry(QtCore.QRect(-1, -1, 501, 461))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 460))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.picture_label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.picture_label.setGeometry(QtCore.QRect(0,0, 500, height_tmp))
        self.picture_label.setObjectName("picture_label")
        if len(photos) > 0:
            pixmap = QPixmap("../../resources/pictures/"+self.tree.split(".")[0]+"/"+str(self.person.person_id)+"/"+photos[0]).scaled(500, height_tmp, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.picture_label.setPixmap(pixmap)
            self.picture_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, height_tmp, 420, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, height_tmp + 40, 420, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(10, height_tmp + 80, 420, 20))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(10, height_tmp + 120, 420, 20))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(10, height_tmp + 160, 420, 20))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(10, height_tmp + 200, 420, 20))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(f"{self.person.first_name} {self.person.last_name}")
        self.label.setText(f"Imię: {self.person.first_name}")
        self.label_2.setText(f"Nazwisko: {self.person.last_name}")
        self.label_3.setText(f"Data urodzenia: {self.person.birth_date}")
        self.label_4.setText(f"Data śmierci: {self.person.death_date}")
        self.label_5.setText(f"Matka: {self.person.mother.first_name} {self.person.mother.last_name}")
        self.label_6.setText(f"Ojciec: {self.person.father.first_name} {self.person.father.last_name}")