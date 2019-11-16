import os
import threading
import time

from PyQt5.QtCore import QThread, pyqtSignal

from database.beans import ClassBrief
from model.Detection.detection import Detection
from util.GenerateHTML import HTMLFactory
from util.Variable import system_seconds, update_class_table_lock, usr_gpu_lock
from util.functions import get_time_format


class ClassBriefThread(QThread):
    # 统计教室内学生人数
    update_signal = pyqtSignal(int)
    __flag = threading.Event()
    __working = threading.Event()

    def __init__(self, class_brief: ClassBrief, page):
        super().__init__()
        self.__class_brief = class_brief
        self.__page = page

    def run(self) -> None:
        self.__flag.set()
        self.__working.set()

        class_id = self.__class_brief.classroom.classroom_id
        while self.__flag.isSet():
            self.__working.wait()
            now_time = time.time()
            img_path = 'classroom/{0}/thumbnail.jpg'.format(class_id)
            command = "ffmpeg -ss {0} -i classroom/{1}/{2}.mp4 -vframes 1 -y {3}".format(
                get_time_format(int(time.time() - system_seconds)), class_id, class_id, img_path)
            print(">>>>>>>>>>>>>>>>>> StudentNum ", command)
            os.system(command)

            usr_gpu_lock.acquire()
            num = Detection.get_instance().count_number(img_path)
            usr_gpu_lock.release()

            self.__class_brief.present_student_number = num
            if num < self.__class_brief.course.student_number * 0.6:
                self.__class_brief.isAbnormal = True
            html = HTMLFactory.get_instance().class_brief_box(self.__class_brief)

            if self.__class_brief.isShow:
                update_class_table_lock.acquire()
                self.__page.runJavaScript("updateBox('class_{0}','{1}')".format(class_id, html))
                update_class_table_lock.release()

            self.sleep(int(10 - (time.time() - now_time)))

    def pause(self):
        self.__working.clear()

    def resume(self):
        self.__working.set()

    def stop(self):
        self.__flag.clear()
