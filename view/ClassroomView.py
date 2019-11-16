import time

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton

from view.ui.ClassroomWidget_ui import Ui_Form_Classroom


class View_Classroom(Ui_Form_Classroom, QPushButton):
    def __init__(self, parent, info, scheduler):
        super().__init__(parent)
        self.start_time = time.time()
        self.setupUi(self)
        self.info = info

        # 显示该教室的位置、教师、课程
        self.label_address.setText(info.building + info.number)
        self.label_teacher.setText(info.teacher)
        self.label_project.setText(info.project)
        self.label_amount_no.setText(info.number_student)
        self.scheduler = scheduler

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.scheduler.pause()
