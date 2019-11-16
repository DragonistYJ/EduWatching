import os

from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, pyqtSignal
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow

from database.beans import ClassBrief
from threads.Speech import SpeechWordThread
from threads.StudentState import StudentStateThread
from threads.TeacherVideo import TeacherVideoThread
from util.Interact import RealTimeObj
from util.functions import img_format_base64
from view.ui.RealTime_ui import Ui_RealTime


class View_RealTime(QMainWindow, Ui_RealTime):
    sig_on_closed = pyqtSignal()

    def __init__(self, brief: ClassBrief):
        super().__init__()
        self.setupUi(self)

        self.brief = brief
        self.real_time_web = QWebEngineView(self.centralwidget)
        self.verticalLayout.addWidget(self.real_time_web)
        self.real_time_channel = QWebChannel(self.real_time_web.page())
        self.real_time_obj = RealTimeObj()
        self.real_time_channel.registerObject('real_time_obj', self.real_time_obj)
        self.real_time_web.page().setWebChannel(self.real_time_channel)
        self.real_time_web.load(QUrl.fromLocalFile(os.path.abspath('view/html/RealTime.html')))
        self.real_time_web.loadFinished.connect(self.init_view)

        self.student_state_thread = StudentStateThread(self.brief.classroom.classroom_id, self.real_time_web.page())
        self.student_state_thread.start()
        self.teacher_video_thread = TeacherVideoThread(self.brief.classroom.classroom_id, self.real_time_web.page())
        self.teacher_video_thread.start()
        self.speech_word_thread = SpeechWordThread(self.brief.classroom.classroom_id, self.real_time_web.page())
        self.speech_word_thread.start()

    def init_view(self):
        class_id = self.brief.classroom.classroom_id
        student_pic = img_format_base64(os.path.abspath('classroom/' + class_id + '/detect.jpg'), 640, 360)
        teacher_pic = img_format_base64(os.path.abspath('classroom/' + class_id + '/teacher.jpg'), 640, 360)
        self.real_time_web.page().runJavaScript("initView('{0}','{1}')".format(student_pic, teacher_pic))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.student_state_thread.stop()
        self.teacher_video_thread.stop()
        self.speech_word_thread.stop()
        self.sig_on_closed.emit()
