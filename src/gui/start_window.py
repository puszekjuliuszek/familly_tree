from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QVBoxLayout
from os import listdir, system
from shutil import copyfile
from csv import reader

from src.gui.tree_window import TreeWindow
from src.gui.start_window_ui import StartWindowUi
from src.gui.tree_window_graph_ui import TreeWindowGraphUi
from src.io_functions.read_data import read_data
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = StartWindowUi()
        self.ui.setupUi(self)
        self.ui.add_tree_bt.clicked.connect(self.add_tree_clicked)
        self.ui.open_tree_bt.clicked.connect(self.open_tree_clicked)

    def add_tree_clicked(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "../../resources/Tree_files", "JSON Files (*.json)")
        if fname:
            self.add_tree_to_saved_trees(fname[0])
            self.make_copy_of_a_tree(fname[0])
            self.ui.add_saved_trees()
        else:
            # TODO wywala apke jak nie wybierzesz niczego tylko zamkniesz okno
            pass

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

    def open_tree_clicked(self):
        if self.ui.tree_to_open is not None:
            main_person = read_data(self.ui.tree_to_open, 4)
            # # id 6 to babcia, id 4 mama, id 1 ja, 3grzegorz
            # self.tree_window = TreeWindow(main_person, self.ui.tree_to_open.split(".")[0])
            # self.tree_window.show()

            graph_ui = TreeWindowGraphUi()
            canvas = graph_ui.setup_ui(main_person)
            self.widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(canvas)
            self.widget.setLayout(layout)
            self.widget.show()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    window()
