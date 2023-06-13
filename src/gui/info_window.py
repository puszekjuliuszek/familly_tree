from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout


class InfoWindow(QWidget):
    def __init__(self, people_list, place):
        super(InfoWindow, self).__init__()
        self.people_list = people_list
        self.place = place
        self.birth_counter = 0
        self.death_counter = 0
        self.men_counter = 0
        self.women_counter = 0

        self.scrollArea = QtWidgets.QScrollArea(parent=self)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.vbox = QVBoxLayout()
        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)

        self.run_analysis()
        self.setup_ui(self)
        self.setStyleSheet("""QWidget {
                                background-color: rgba(27,29,35,255);
                                color: "white";
                             }""")

    def run_analysis(self):
        for person in self.people_list:
            if person.death_date is None:
                self.birth_counter += 1
            else:
                self.death_counter += 1
            if person.gender == 1:
                self.men_counter += 1
            else:
                self.women_counter += 1

    def setup_ui(self, form):
        form.setObjectName("form")
        form.resize(496, 454)
        height_tmp = 0

        self.scrollArea.setGeometry(QtCore.QRect(-1, -1, 501, 461))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 700))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.label.setGeometry(QtCore.QRect(10, height_tmp, 420, 20))
        self.label.setObjectName("label")
        self.label.setMargin(10)
        self.vbox.addWidget(self.label)

        self.label_2.setGeometry(QtCore.QRect(10, height_tmp + 40, 420, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setMargin(10)
        self.vbox.addWidget(self.label_2)

        self.label_3.setGeometry(QtCore.QRect(10, height_tmp + 80, 420, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setMargin(10)
        self.vbox.addWidget(self.label_3)

        self.translate_ui(form)
        self.scrollAreaWidgetContents.setLayout(self.vbox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QtCore.QMetaObject.connectSlotsByName(form)

    def translate_ui(self, form):
        # TODO można dorobić więcej informacji
        form.setWindowTitle("Analiza drzewa")
        self.label.setText(f"Żyje {self.birth_counter} osób, nie żyje "
                           f"{self.death_counter} osób")
        self.label_2.setText(f"Najwięcej ludzi mieszkało i mieszka wmieście "
                             f"{self.place}")
        self.label_3.setText(f"Kobiet jest: {self.women_counter} a mężczyzn: "
                             f"{self.men_counter}")
