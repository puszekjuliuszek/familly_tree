from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QVBoxLayout
from os import listdir
from shutil import copyfile
from csv import reader

from src.gui.not_used.tree_window import TreeWindow
from src.gui.start_window_ui import StartWindowUi
from src.gui.tree_window_graph_ui import TreeWindowGraphUi
from src.io_functions.read_data import read_data
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = StartWindowUi()
        self.ui.setupUi(self)

        # self.setStyleSheet("""
        #     #verticalLayoutWidget_5 {
        #         background-color: "green";
        #         color: "white";
        #     }""")





def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    window()
