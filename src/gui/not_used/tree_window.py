from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget
from src.gui.not_used.tree_window_ui import TreeWindowUi


class TreeWindow(QWidget):
    def __init__(self, person,tree_name):
        super(TreeWindow, self).__init__()
        self.ui = TreeWindowUi()
        self.ui.setup_ui(self, person)
        self.ui.set_window_name(tree_name)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(168, 34, 3))

        for cord in self.ui.paint_cords:
            x1,y1,x2,y2 = cord
            painter.drawLine(x1,y1,x2,y2)


if __name__ == "__main__":
    pass
