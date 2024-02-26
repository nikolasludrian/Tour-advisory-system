from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QPushButton


class QtBoxFuncListWidget1(QListWidget):
    def __init__(self):
        super(QtBoxFuncListWidget1, self).__init__()
        self.setFixedSize(100, 200)
        self.add_btns()

    def add_btns(self):
        for _ in range(4):
            item = QListWidgetItem()
            item.setSizeHint(QSize(80, 30))
            self.addItem(item)

            btn = QPushButton()
            btn.setText("button")
            self.setItemWidget(item, btn)
