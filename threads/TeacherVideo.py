import os
import threading
import time

from PyQt5.QtCore import QThread, pyqtSignal

from util.Variable import system_seconds, update_real_time_lock
from util.functions import get_time_format, img_format_base64


class TeacherVideoThread(QThread):
    __flag = True

    def __init__(self, class_id, web_page):
        super().__init__()
        self.class_id = class_id
        self.web_page = web_page

    def run(self) -> None:
        while self.__flag:
            now_time = time.time()
            video_path = 'classroom/{0}/teacher.jpg'.format(self.class_id)
            command = "ffmpeg -ss {0} -i classroom/{1}/{2}_back.mp4 -vframes 1 -y {3}".format(
                get_time_format(int(time.time() - system_seconds)), self.class_id, self.class_id, video_path)
            print(">>>>>>>>>>>>>> Teacher Video Thread ", command)
            os.system(command)
            base64code = img_format_base64(video_path, 640, 360)

            update_real_time_lock.acquire()
            self.web_page.runJavaScript("updateTeacherPic('{0}')".format(base64code))
            update_real_time_lock.release()

            use_time = time.time() - now_time
            if use_time < 2:
                self.sleep(int(2 - use_time))

    def stop(self):
        self.__flag = False
