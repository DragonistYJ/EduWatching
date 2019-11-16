# 将秒数转换为xx:xx:xx格式的时间
import base64
from io import BytesIO

from PIL import Image


def get_time_format(seconds):
    s = seconds % 60
    s = str(s) if s >= 10 else '0' + str(s)
    h = seconds // 3600
    h = str(h) if h >= 10 else '0' + str(h)
    m = (seconds // 60) % 60
    m = str(m) if m >= 10 else '0' + str(m)
    return "{0}:{1}:{2}".format(h, m, s)


# 将音频转换为base64格式
def to_base64(wav_path):
    with open(wav_path, 'rb') as fileObj:
        base64_data = fileObj.read()
        data = base64.b64encode(base64_data)
    return data.decode()


# 将图片转换成指定大小的base64格式
def img_format_base64(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.ANTIALIAS)
    buffer = BytesIO()
    img.save(buffer, 'jpeg')
    return base64.b64encode(buffer.getvalue()).decode()
