from PyQt6.QtWidgets import QApplication, QMainWindow
from src.gui.start_window_ui import StartWindowUi
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = StartWindowUi()
        self.ui.setup_ui(self)

        self.setStyleSheet("""QWidget {
                        background-color: rgba(27,29,35,255);
                        color: "white";
                     }
                     #verticalLayoutWidget_4 {
                            background-color: rgba(44,49,62,255);
                            color: "white";
                        }""")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    window()
