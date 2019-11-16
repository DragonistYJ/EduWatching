import os
import sys

import pymysql
from PyQt5.QtWidgets import QApplication

from model.Classification.classification import Classification
from model.Detection.detection import Detection
from view.LogView import View_Log
from view.MainView import View_Main

# 教室人数检测
Detection().get_instance()
# 人物状态分类
Classification().get_instance()


def log2main(log, main):
    username = log.lineEdit_username.text()
    password = log.lineEdit_password.text()
    conn = pymysql.connect(host='rm-bp16979l63az3x58ato.mysql.rds.aliyuncs.com',
                           port=3306,
                           user='paddle',
                           password='Paddle2019',
                           db='edu_watching')
    cursor = conn.cursor()
    sql = 'select * from user where username = %s'
    cursor.execute(sql, [username])
    one = cursor.fetchone()
    if one is None or one[1] != password:
        return

    main.show()
    log.close()


if __name__ == '__main__':
    os.environ['FLAGS_eager_delete_tensor_gb'] = str(0)
    app = QApplication(sys.argv)
    view_log = View_Log()
    # 效果展示需要，直接进入实时监控页面
    # view_log.show()
    view_main = View_Main()
    # view_log.pushButton_login.clicked.connect(lambda: log2main(view_log, view_main))
    view_main.show()
    sys.exit(app.exec_())
