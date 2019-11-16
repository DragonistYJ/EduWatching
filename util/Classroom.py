import pymysql


class ClassroomInfo:
    def __init__(self, id):
        self.id = id
        conn = pymysql.connect(host='rm-bp16979l63az3x58ato.mysql.rds.aliyuncs.com',
                               port=3306,
                               user='paddle',
                               password='Paddle2019',
                               db='edu_watching')
        cursor = conn.cursor()
        sql = 'select * from classroom where classroom_id = %s'
        cursor.execute(sql, id)
        one = cursor.fetchone()
        self.campus = '江安校区'
        self.building = '一教A'
        self.floor = 5
        self.number = '一教A'
        self.teacher = '一教A'
        self.project = '一教A'
        self.number_student = str(60)
        self.status = 'on'
        self.isAbnormal = False
