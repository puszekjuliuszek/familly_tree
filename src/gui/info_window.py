import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from src.definitions.definitions import ROOT_DIR


class InfoWindow(QWidget):
    def __init__(self, people_list, place):
        super(InfoWindow, self).__init__()
        self.people_list = people_list
        self.place = place
        self.birth_counter = 0
        self.death_counter = 0
        self.run_analisys()
        self.setupUi(self)
        self.setStyleSheet("""QWidget {
                                background-color: rgba(27,29,35,255);
                                color: "white";
                             }""")

    def run_analisys(self):
        for person in self.people_list:
            if person.death_date is None:
                self.birth_counter +=1
            else:
                self.death_counter +=1

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(496, 454)
        # path = ROOT_DIR + "\\resources\\pictures\\" + self.tree.split(".")[0] + "\\" + str(self.person.person_id)
        height_tmp = 0
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setGeometry(QtCore.QRect(-1, -1, 501, 461))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 700))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.vbox = QVBoxLayout()


        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, height_tmp, 420, 20))
        self.label.setObjectName("label")
        self.label.setMargin(10)
        self.vbox.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, height_tmp + 40, 420, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setMargin(10)
        self.vbox.addWidget(self.label_2)
        #
        # self.label_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_3.setGeometry(QtCore.QRect(10, height_tmp + 80, 420, 20))
        # self.label_3.setObjectName("label_3")
        # self.label_3.setMargin(10)
        # self.vbox.addWidget(self.label_3)
        #
        # self.label_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_4.setGeometry(QtCore.QRect(10, height_tmp + 120, 420, 20))
        # self.label_4.setObjectName("label_4")
        # self.label_4.setMargin(10)
        # self.vbox.addWidget(self.label_4)
        #
        # self.label_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_5.setGeometry(QtCore.QRect(10, height_tmp + 160, 420, 20))
        # self.label_5.setObjectName("label_5")
        # self.label_5.setMargin(10)
        # self.vbox.addWidget(self.label_5)
        #
        # self.label_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_6.setGeometry(QtCore.QRect(10, height_tmp + 200, 420, 20))
        # self.label_6.setObjectName("label_6")
        # self.label_6.setMargin(10)
        # self.vbox.addWidget(self.label_6)
        #
        # self.label_7 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_7.setGeometry(QtCore.QRect(10, height_tmp + 240, 420, 20))
        # self.label_7.setObjectName("label_7")
        # self.label_7.setMargin(10)
        # self.vbox.addWidget(self.label_7)
        #
        # self.label_8 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_8.setGeometry(QtCore.QRect(10, height_tmp + 280, 420, 20))
        # self.label_8.setObjectName("label_8")
        # self.label_8.setMargin(10)
        # self.vbox.addWidget(self.label_8)
        #
        # self.label_9 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_9.setGeometry(QtCore.QRect(10, height_tmp + 320, 420, 20))
        # self.label_9.setObjectName("label_9")
        # self.label_9.setMargin(10)
        # self.vbox.addWidget(self.label_9)
        #
        # self.label_10 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_10.setGeometry(QtCore.QRect(10, height_tmp + 360, 420, 20))
        # self.label_10.setObjectName("label_10")
        # self.label_10.setMargin(10)
        # self.vbox.addWidget(self.label_10)
        #
        # self.label_11 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_11.setGeometry(QtCore.QRect(10, height_tmp + 400, 420, 20))
        # self.label_11.setObjectName("label_11")
        # self.label_11.setMargin(10)
        # self.vbox.addWidget(self.label_11)
        #
        # self.label_12 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_12.setGeometry(QtCore.QRect(10, height_tmp + 440, 420, 20))
        # self.label_12.setObjectName("label_12")
        # self.label_12.setMargin(10)
        # self.vbox.addWidget(self.label_12)
        #
        # self.label_13 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        # self.label_13.setGeometry(QtCore.QRect(10, height_tmp + 480, 420, 20))
        # self.label_13.setObjectName("label_13")
        # self.label_13.setMargin(10)
        # self.vbox.addWidget(self.label_13)

        self.retranslateUi(Form)
        self.scrollAreaWidgetContents.setLayout(self.vbox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        # TODO dorobić dobre informacje
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(f"Analiza drzewa")
        self.label.setText(f"Żyje {self.birth_counter} osób, nie żyje {self.death_counter} osób")
        self.label_2.setText(f"Najwięcej ludzi mieszkało i mieszka wmieście {self.place}")
        # self.label_3.setText(f"Data urodzenia: {self.person.birth_date}")
        # if self.person.death_date is None:
        #     death_date = " "
        # else:
        #     death_date = self.person.death_date
        # self.label_4.setText(f"Data śmierci: {death_date}")
        # if self.person.mother is not None:
        #     self.label_5.setText(f"Matka: {self.person.mother.first_name} {self.person.mother.last_name}")
        # if self.person.father is not None:
        #     self.label_6.setText(f"Ojciec: {self.person.father.first_name} {self.person.father.last_name}")
        # partners = ",".join([str(person) for person in self.person.partners])
        # self.label_7.setText(f"Partnerzy: {partners}")
        # if self.person.gender == 1:
        #     gender = "Mężczyzna"
        # else:
        #     gender = "Kobieta"
        # self.label_8.setText(f"Płeć: {gender}")
        # if self.person.death_reason is None:
        #     death_reason = " "
        # else:
        #     death_reason = self.person.death_reason
        # self.label_9.setText(f"Przyczyna śmierci: {death_reason}")
        # if self.person.birth_place is None:
        #     birth_place = " "
        # else:
        #     birth_place = self.person.birth_place
        # self.label_10.setText(f"Miejsce urodzenia: {birth_place}")
        # illnesses = ",".join(self.person.illnesses)
        # self.label_11.setText(f"Choroby: {illnesses}")
        # # TODO zawody źle się wczytują w Personie jak jest tylko jeden zawód
        # professions = ",".join(self.person.profession)
        # self.label_12.setText(f"Zawody: {professions}")
        # residences = ",".join(self.person.residences)
        # self.label_13.setText(f"Miejsca zamieszkania: {residences}")
        pass