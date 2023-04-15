from collections import deque
from PyQt6 import QtCore, QtGui, QtWidgets

from src.definitions.definitions import *
import math


import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


class TreeWindowUi(object):
    def setup_ui(self, MainWindow, person):

        self.MainWindow = MainWindow
        print(type(MainWindow))
        self.paint_cords = []
        MainWindow.setObjectName("MainWindow")

        level, level_down = self.count_people(person)  # ilosc potomków do góry, ilośc potomków w doł
        tree_height = level - level_down + 1  # wykosoc drzewa
        already_add = set()  # tablica visited
        print(level, "level", level_down, "level_down")

        width = pow(2, level - 1) * COUPLE_WIDTH + (pow(2, level - 1) - 1) * REGULAR_GAP + MARGIN_CORRECT
        height = 2 * MY_MARGIN + (tree_height + 1) * PERSON_HEIGHT + tree_height * 2 * HEIGHT_GAP

        MainWindow.resize(width, height)
        queue = deque()
        queue.append((person, 0, width, 1, "R"))
        already_add.add(person)
        while len(queue) > 0:

            person_tmp, low_border, high_border, level_tmp, gender = queue.pop()
            width_tmp = high_border - low_border

            X = int(low_border + (width_tmp) / 2 - PERSON_WIDTH / 2)
            Y = int(height - MARGIN_CORRECT - MY_MARGIN - (level_tmp - 1) * (PERSON_HEIGHT + 2 * HEIGHT_GAP))

            self.add_person_button(person_tmp, X, Y)
            self.add_paint_cords(gender, X, Y, low_border, high_border)

            if person_tmp.mother is not None:
                if person_tmp.mother not in already_add:
                    already_add.add(person_tmp.mother)
                    if level_tmp == level:
                        queue.append((person_tmp.mother, low_border, low_border + (width_tmp - COUPLE_GAP) / 2,
                                      level_tmp + 1, "GM"))
                    else:
                        queue.append((person_tmp.mother, low_border, low_border + (width_tmp - REGULAR_GAP) / 2,
                                      level_tmp + 1, "M"))
            if person_tmp.father is not None:
                if person_tmp.father not in already_add:
                    already_add.add(person_tmp.father)
                    if level_tmp == level:
                        queue.append((person_tmp.father, high_border - (width_tmp - COUPLE_GAP) / 2, high_border,
                                      level_tmp + 1, "GF"))
                    else:
                        queue.append((person_tmp.father, high_border - (width_tmp - REGULAR_GAP) / 2, high_border,
                                      level_tmp + 1, "F"))

            # TODO dodowanie parternów i dzieci do quque
            for person_partner in person_tmp.partners:
                if person_partner not in already_add:
                    already_add.add(person_partner)
                    queue.append((person_partner,low_border+width_tmp,high_border,level_tmp,"M"))

            for person_child in person_tmp.children:
                if person_child not in already_add:
                    already_add.add(person_child)
                    queue.append((person_child,low_border,high_border,level_tmp-1,"M"))

    def on_node_click(event):
        node_text = event.artist.get_text()
        node_num = str(node_text)
        print(f"Kliknięto węzeł {node_num}")


    def count_people(self, person) -> (int, int):
        # poprawiony count_people, zwraca ilosc pokoleń, pozimów, nie wiem jak to nazwać
        queue = deque()
        level_max = 0
        level_min = math.inf
        level = dif = 0
        already_add = set()
        queue.append((person, level))
        while len(queue) > 0:
            person_tmp, level_tmp = queue.pop()
            level_max = max(level_max, level_tmp)
            level_min = min(level_min, level_tmp)
            dif = max(dif, (level_max - level_min + 1))
            if person_tmp.mother is not None:
                if person_tmp.mother not in already_add:
                    already_add.add(person_tmp.mother)
                    queue.append((person_tmp.mother, level_tmp + 1))
            if person_tmp.father is not None:
                if person_tmp.father not in already_add:
                    already_add.add(person_tmp.father)
                    queue.append((person_tmp.father, level_tmp + 1))
            for person_partner in person_tmp.partners:
                if person_partner not in already_add:
                    already_add.add(person_partner)
                    queue.append((person_partner, level_tmp))
            for person_child in person_tmp.children:
                if person_child not in already_add:
                    already_add.add(person_child)
                    queue.append((person_child, level_tmp - 1))

        return level_max, level_min

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
            self.paint_cords.append(
                (int(X + PERSON_WIDTH / 2), Y, int(X + PERSON_WIDTH / 2), int(Y - 2 * HEIGHT_GAP - PERSON_HEIGHT / 2)))

            self.paint_cords.append((X + PERSON_WIDTH, int(Y + PERSON_HEIGHT / 2), int(high_border + REGULAR_GAP / 2),
                                     int(Y + PERSON_HEIGHT / 2)))
        elif gender == "F":
            self.paint_cords.append(
                (int(X + PERSON_WIDTH / 2), Y, int(X + PERSON_WIDTH / 2), int(Y - 2 * HEIGHT_GAP - PERSON_HEIGHT / 2)))
            self.paint_cords.append(
                (X, int(Y + PERSON_HEIGHT / 2), int(low_border - REGULAR_GAP / 2), int(Y + PERSON_HEIGHT / 2)))
        elif gender == "GM":
            self.paint_cords.append((X + PERSON_WIDTH, int(Y + PERSON_HEIGHT / 2), int(high_border + COUPLE_GAP / 2),
                                     int(Y + PERSON_HEIGHT / 2)))
        else:
            self.paint_cords.append(
                (X, int(Y + PERSON_HEIGHT / 2), int(low_border - COUPLE_GAP / 2), int(Y + PERSON_HEIGHT / 2)))

    def set_window_name(self, tree_name):
        self.MainWindow.setWindowTitle("drzewo " + tree_name)
