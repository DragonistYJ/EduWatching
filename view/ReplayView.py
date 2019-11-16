import os

from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QWidget

from util.Interact import ReplayObj
from view.ui.Replay_ui import Ui_RecordWindow


class View_Replay(QMainWindow, Ui_RecordWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.web = QWebEngineView(self.centralwidget)
        self.verticalLayout.addWidget(self.web)
        self.channel = QWebChannel(self.web.page())
        self.interact_obj = ReplayObj()
        self.channel.registerObject('interact_obj', self.interact_obj)
        self.web.page().setWebChannel(self.channel)
        self.web.load(QUrl.fromLocalFile(os.path.abspath('view/html/Replay.html')))
