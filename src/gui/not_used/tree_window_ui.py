from collections import deque
from PyQt6 import QtCore, QtGui, QtWidgets

from src.definitions.definitions import *


class TreeWindowUi(object):
    def setup_ui(self, MainWindow, person):

        self.MainWindow = MainWindow

        self.paint_cords = []
        level = self.count_people(person)
        MainWindow.setObjectName("MainWindow")
        width = pow(2,level-1)*COUPLE_WIDTH+(pow(2,level-1)-1)*REGULAR_GAP +MARGIN_CORRECT
        height = 2*MY_MARGIN+(level+1)*PERSON_HEIGHT+level*2*HEIGHT_GAP
        MainWindow.resize(int(width),int(height))


        queue = deque()
        queue.append((person, 0, width, 1, "R"))
        while len(queue) > 0:
            person_tmp, low_border, high_border, level_tmp, gender = queue.pop()
            width_tmp = high_border - low_border
            X = int(low_border + (width_tmp) / 2 - PERSON_WIDTH / 2)
            Y = int(height - MARGIN_CORRECT - MY_MARGIN - (level_tmp - 1) * (PERSON_HEIGHT + 2 * HEIGHT_GAP))
            self.add_person_button(person_tmp, X, Y)
            self.add_paint_cords(gender, X, Y, low_border, high_border)
            if person_tmp.mother is not None:
                if level_tmp == level:
                    queue.append(
                        (person_tmp.mother, low_border, low_border + (width_tmp - COUPLE_GAP) / 2, level_tmp + 1, "GM"))
                else:
                    queue.append(
                        (person_tmp.mother, low_border, low_border + (width_tmp - REGULAR_GAP) / 2, level_tmp + 1, "M"))
            if person_tmp.father is not None:
                if level_tmp == level:
                    queue.append((person_tmp.father, high_border - (width_tmp - COUPLE_GAP) / 2, high_border, level_tmp + 1,"GF"))
                else:
                    queue.append((person_tmp.father, high_border -(width_tmp-REGULAR_GAP)/2, high_border, level_tmp+1,"F"))
    def on_node_click(event):
        node_text = event.artist.get_text()
        node_num = str(node_text)
        print(f"Kliknięto węzeł {node_num}")


    def count_people(self, person) -> (int, int):
        # poprawiony count_people, zwraca ilosc pokoleń, pozimów, nie wiem jak to nazwać
        queue = deque()
        level = 0
        queue.append((person,level))
        while len(queue) > 0:
            person_tmp, level_tmp = queue.pop()
            level = max(level, level_tmp)
            if person_tmp.mother is not None:
                queue.append((person_tmp.mother, level_tmp + 1))
            if person_tmp.father is not None:
                queue.append((person_tmp.father, level_tmp + 1))
        return level


    def add_person_button(self, person, X, Y):
        bt_name = str(person)
        setattr(self, bt_name, QtWidgets.QPushButton(parent=self.MainWindow))
        bt = getattr(self, bt_name)
        bt.setGeometry(QtCore.QRect(X, Y, PERSON_WIDTH, PERSON_HEIGHT))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        bt.setFont(font)
        bt.setAutoDefault(False)
        bt.setObjectName(bt_name)
        bt.setText(bt_name)

    def add_paint_cords(self, gender, X, Y, low_border, high_border):
        if gender == "R":
            self.paint_cords.append(
                (int(X + PERSON_WIDTH / 2), Y, int(X + PERSON_WIDTH / 2), int(Y - 2 * HEIGHT_GAP - PERSON_HEIGHT / 2)))
        elif gender == "M":
            self.paint_cords.append((int(X+PERSON_WIDTH/2),Y,int(X+PERSON_WIDTH/2),int(Y-2*HEIGHT_GAP-PERSON_HEIGHT/2)))
            self.paint_cords.append((X+PERSON_WIDTH,int(Y+PERSON_HEIGHT/2),int(high_border+REGULAR_GAP/2),int(Y+PERSON_HEIGHT/2)))
        elif gender == "F":
            self.paint_cords.append((int(X+PERSON_WIDTH/2),Y,int(X+PERSON_WIDTH/2),int(Y-2*HEIGHT_GAP-PERSON_HEIGHT/2)))
            self.paint_cords.append((X,int(Y+PERSON_HEIGHT/2),int(low_border-REGULAR_GAP/2),int(Y+PERSON_HEIGHT/2)))
        elif gender == "GM":
            self.paint_cords.append((X + PERSON_WIDTH, int(Y + PERSON_HEIGHT / 2), int(high_border + COUPLE_GAP / 2),
                                     int(Y + PERSON_HEIGHT / 2)))
        else:
            self.paint_cords.append((X,int(Y+PERSON_HEIGHT/2),int(low_border-COUPLE_GAP/2),int(Y+PERSON_HEIGHT/2)))



    def set_window_name(self, tree_name):
        self.MainWindow.setWindowTitle("drzewo " + tree_name)
