import sys
import typing
from PyQt6.QtGui import QStandardItem
from PyQt6.QtCore import QEvent, Qt, QObject
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox


class CheckableComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.closeOnLineEditClick = False

        self.lineEdit().installEventFilter(self)
        self.view().viewport().installEventFilter(self)
        self.model().dataChanged.connect(self.update_line_edit_field)

    def eventFilter(self, widget: QObject, event: QEvent) -> bool:
        if widget == self.lineEdit():
            if event.type() == QEvent.Type.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return super().eventFilter(widget, event)
        if widget == self.view().viewport():
            if event.type() == QEvent.Type.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == Qt.CheckState.Checked:
                    item.setCheckState(Qt.CheckState.Unchecked)
                else:
                    item.setCheckState(Qt.CheckState.Checked)
                return True
            return super().eventFilter(widget, event)

    def hidePopup(self) -> None:
        super().hidePopup()
        self.startTimer(100)

    def addItems(self, items: typing.Iterable[str], item_list: list = None) -> None:
        for index, text in enumerate(items):
            try:
                data = item_list[index]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def addItem(self, text: str, user_data: typing.Any = None) -> None:
        item = QStandardItem()
        item. setText(text)
        if user_data is not None:
            item.setData(user_data)

        item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        self.model().appendRow(item)

    def update_line_edit_field(self):
        text_container = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                text_container.append(self.model().item(i).text())
        text_string = ", ".join(text_container)
        self.lineEdit().setText(text_string)

    def setPlaceholderText(self, placeholder_text: str) -> None:
        self.lineEdit().setText(placeholder_text)

    def currentText(self) -> str:
        return self.lineEdit().text()

    def clear(self) -> None:
        for item in range(self.count()):
            self.removeItem(item)


if __name__ == "__main__":
    class MultiComboBox(QWidget):
        def __init__(self, data):
            super().__init__()
            self.window_width, self.window_height = 1200, 200
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)
            combobox = CheckableComboBox()
            combobox.addItems(data)
            self.layout.addWidget(combobox)

    colors = ["Blue", "Yellow", "Orange", "Green"]
    app = QApplication(sys.argv)
    myApp = MultiComboBox(colors)
    myApp.show()
    sys.exit(app.exec())
