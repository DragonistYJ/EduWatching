import os
import threading
import time

# 监控总览下的定时检测
from PyQt5.QtGui import QPixmap

from database.beans import ClassBrief
from model.Detection.detection import Detection
from util.Variable import system_seconds, lock, usr_gpu_lock
from util.functions import get_time_format


def init_thumbnail(class_brief: ClassBrief):
    # 刚开启系统的时候，为了使得界面有图片、数据的显示
    # 需要进行初始化的识别
    # 截取视频的第一帧作为识别的图片以及教师的缩略图
    class_id = class_brief.classroom.classroom_id
    if not os.path.exists('classroom/{0}/thumbnail.jpg'.format(class_id)):
        command = "ffmpeg -ss 00:00:00 -i classroom/{0}/{1}.mp4 -vframes 1 -y classroom/{2}/thumbnail.jpg".format(
            class_id, class_id, class_id)
        os.system(command)
    usr_gpu_lock.acquire()
    num = Detection.get_instance().count_number('classroom/{0}/thumbnail.jpg'.format(class_id))
    print("init classroom {0}; student {1} present".format(class_id, num))
    usr_gpu_lock.release()
    class_brief.present_student_number = num
    if num < class_brief.course.student_number * 0.6:
        class_brief.isAbnormal = True


def count_student_amount(classroom_id, widget1, widget2, widget3):
    pic_path = 'classroom/{0}/thumbnail.jpg'.format(classroom_id)
    command = "ffmpeg -ss {0} -i classroom/{1}/{2}.mp4 -vframes 1 -y {3}".format(
        get_time_format(int(time.time() - system_seconds)),
        classroom_id,
        classroom_id,
        pic_path)
    os.system(command)
    widget1.label_img.setPixmap(QPixmap(pic_path))
    widget2.label_img.setPixmap(QPixmap(pic_path))
    widget3.label_img.setPixmap(QPixmap(pic_path))
    lock.acquire()
    num = str(Detection.get_instance().count_number(pic_path))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> classroom {0}; student {1} present".format(classroom_id, num))
    widget1.label_present_no.setText(num)
    widget2.label_present_no.setText(num)
    widget3.label_present_no.setText(num)
    lock.release()
