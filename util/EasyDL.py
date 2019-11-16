import base64
import json

import requests


def test_speech_speed(base64code):
    request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/speechSpeed'
    params = json.dumps({'sound': base64code, 'top_num': 2})
    access_token = EasyDL.get_instance().access_token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        EasyDL.get_instance().speed = int(response.json()['results'][0]['name'])
    else:
        EasyDL.get_instance().speed = 0


def test_speech_emotion(base64code):
    request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/emotion'
    params = json.dumps({'sound': base64code, 'top_num': 2})
    access_token = EasyDL.get_instance().access_token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    emotion_dict = {
        "nervous": 60,
        "happy": 100,
        "proud": 80,
        "surprise": 70,
        "sorrow": 50,
        "but": 60,
        "angry": 40,
        "peaceful": 70,
        "passionate": 80,
        "humorous": 90,
        "exciting": 75,
        "affectionate": 60
    }
    if response:
        emotion = response.json()['results'][0]['name']
        EasyDL.get_instance().emotion = emotion_dict[emotion]
    else:
        EasyDL.get_instance().emotion = 0


class EasyDL:
    instance = None
    access_token = None
    speed = None
    emotion = None

    def __init__(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=fVP9VGjFeUMNEf8dhyLyuiN7&client_secret=BG349KHUIt7Ddu1cNKGuY3B32p07OKaC'
        response = requests.get(host)
        self.access_token = response.json()['access_token']

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = EasyDL()
        return cls.instance
