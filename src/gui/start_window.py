from PyQt6.QtWidgets import QApplication, QMainWindow
from src.gui.start_window_ui import StartWindowUi
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
