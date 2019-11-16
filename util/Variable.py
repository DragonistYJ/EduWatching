import threading
import time
import pymysql

system_seconds = time.time()

lock = threading.Lock()
update_class_table_lock = threading.Lock()
usr_gpu_lock = threading.Lock()
update_real_time_lock = threading.Lock()

access_token = None

connection = None
try:
    connection = pymysql.connect(host='rm-bp16979l63az3x58ato.mysql.rds.aliyuncs.com', port=3306, user='paddle',
                                 password='Paddle2019', db='edu_watching')
except Exception as e:
    print("can't connect to db")
