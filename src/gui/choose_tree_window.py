from PyQt6.QtWidgets import QWidget

from resources.start_window import Ui_MainWindow


class ChooseTreeWindow(QWidget):
    def __init__(self):
        super(ChooseTreeWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
