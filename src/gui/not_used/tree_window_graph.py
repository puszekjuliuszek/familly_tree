import json
import sys
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from src.Classes.person import Person
from src.gui.tree_window_graph_ui import TreeWindowGraphUi
from src.io_functions.read_data import read_data


class TreeWindowGraph:
    def __init__(self, tree_name="Zawislak2.json", id=3):
        # super(TreeWindowGraph, self).__init__()
        P = read_data(tree_name, id)
        self.ui = TreeWindowGraphUi()
        canvas = self.ui.setup_ui(P)

        app = QApplication([])
        self.widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.widget.setLayout(layout)
        self.widget.show()
        app.exec()






def window():

    TreeWindowGraph()


if __name__ == "__main__":
    window()
