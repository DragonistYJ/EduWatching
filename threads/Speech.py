import os
import threading
import time

import jieba
from PyQt5.QtCore import QThread

from model.Emotion.emotion import Emotion
from model.KeyWord.filter import DFAFilter
from util.EasyDL import test_speech_speed, test_speech_emotion, EasyDL
from util.Variable import system_seconds, update_real_time_lock, usr_gpu_lock
from util.baidu import DuAPI
from util.functions import get_time_format, to_base64


class SpeechWordThread(QThread):
    __flag = threading.Event()

    def __init__(self, class_id, web_page):
        super().__init__()
        self.class_id = class_id
        self.web_page = web_page

    def run(self) -> None:
        self.__flag.set()
        while self.__flag.isSet():
            now_time = time.time()

            wav_path = 'classroom/{0}/sound.wav'.format(self.class_id)
            command = 'ffmpeg -ss {0} -t 5 -i classroom/{1}/{2}.mp4 -f wav -ar 16000 -y {3}'.format(
                get_time_format(int(time.time() - system_seconds)), self.class_id, self.class_id, wav_path)
            print(">>>>>>>>>>> Speech Thread ", command)
            os.system(command)

            thread_speed = threading.Thread(target=test_speech_speed, args=(to_base64(wav_path),))
            thread_emotion = threading.Thread(target=test_speech_emotion, args=(to_base64(wav_path),))
            thread_speed.start()
            thread_emotion.start()

            sentence = DuAPI.get_instance().asr(wav_path)
            words = jieba.lcut(sentence)
            show_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
            if not words:
                emotion = '无话'
            else:
                usr_gpu_lock.acquire()
                emotion = Emotion.get_instance().infer(words)
                usr_gpu_lock.release()
            sentence = DFAFilter.get_instance().filter(sentence)

            thread_speed.join()
            thread_emotion.join()
            update_real_time_lock.acquire()
            self.web_page.runJavaScript("addSpeech('{0}','{1}','{2}')".format(show_time, emotion, sentence))
            self.web_page.runJavaScript(
                "updateTeacherChart('{0}',{1},{2})".format(show_time, EasyDL.get_instance().emotion, len(sentence) * 2))
            update_real_time_lock.release()

            use_time = time.time() - now_time
            if use_time < 5:
                self.sleep(int(5 - use_time))

    def stop(self):
        self.__flag.clear()
