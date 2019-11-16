from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow, QApplication

from view.ui.LogWindow_ui import Ui_LogWindow


class View_Log(QMainWindow, Ui_LogWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def test(self):
        print(1)

    # 拖动界面
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
