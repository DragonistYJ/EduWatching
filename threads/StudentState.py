import base64
import os
import threading
import time
from io import BytesIO

from PIL import Image, ImageDraw
from PyQt5.QtCore import QThread, pyqtSignal

# 对教室内的所有学生进行状态的检测
# 首先检测数学生，然后进行分类
# 红色 玩手机
# 黄色 睡觉
# 蓝色 站立
from PyQt5.QtWebEngineWidgets import QWebEngineView

from model.Classification.classification import Classification
from model.Detection.detection import Detection
from util.Variable import *
from util.functions import get_time_format


class StudentStateThread(QThread):
    __flag = threading.Event()

    def __init__(self, class_id, web_page):
        super().__init__()
        self.class_id = class_id
        self.web_page = web_page

    def run(self) -> None:
        self.__flag.set()
        while self.__flag.isSet():
            now_time = time.time()

            img_path = 'classroom/{0}/detect.jpg'.format(self.class_id)
            command = "ffmpeg -ss {0} -i classroom/{1}/{2}.mp4 -vframes 1 -y {3}".format(
                get_time_format(int(time.time() - system_seconds)), self.class_id, self.class_id, img_path)
            print(">>>>>>>>>>>>>>>>>> Student State", command)
            os.system(command)
            usr_gpu_lock.acquire()
            boxes = Detection.get_instance().get_boxes(img_path)
            usr_gpu_lock.release()
            classroom_image = Image.open(img_path)
            draw = ImageDraw.Draw(classroom_image)

            normal_num = 0
            phone_num = 0
            sleep_num = 0
            stand_num = 0
            for box in boxes:
                image = classroom_image.crop((box[0], box[1], box[2], box[3]))
                usr_gpu_lock.acquire()
                category = Classification.get_instance().infer(image)
                usr_gpu_lock.release()
                if category == 'phone':
                    draw.rectangle((box[0], box[1], box[2], box[3]), outline='red')
                    draw.rectangle((box[0] - 1, box[1] - 1, box[2] - 1, box[3] - 1), outline='red')
                    phone_num += 1
                elif category == 'sleep':
                    draw.rectangle((box[0], box[1], box[2], box[3]), outline='yellow')
                    draw.rectangle((box[0] - 1, box[1] - 1, box[2] - 1, box[3] - 1), outline='yellow')
                    sleep_num += 1
                elif category == 'stand':
                    draw.rectangle((box[0], box[1], box[2], box[3]), outline='blue')
                    draw.rectangle((box[0] - 1, box[1] - 1, box[2] - 1, box[3] - 1), outline='blue')
                    stand_num += 1
                else:
                    normal_num += 1

            image = classroom_image.resize((640, 360), Image.ANTIALIAS)
            buffer = BytesIO()
            image.save(buffer, 'jpeg')
            base64code = base64.b64encode(buffer.getvalue()).decode()

            update_real_time_lock.acquire()
            self.web_page.runJavaScript(
                "updateStudentChart({0},{1},{2},{3})".format(normal_num, phone_num, sleep_num, stand_num))
            self.web_page.runJavaScript("updateStudentPic('{0}')".format(base64code))
            update_real_time_lock.release()

            use_time = time.time() - now_time
            if use_time < 2:
                self.sleep(int(2 - use_time))

    def stop(self):
        self.__flag.clear()
