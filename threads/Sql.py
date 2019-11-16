import datetime
import os
import time

from database.beans import Classroom, Course, Teacher, ClassBrief
from util.Variable import connection


def get_class_briefs(content):
    if connection is None:
        return
    cursor = connection.cursor()
    cursor.execute('SELECT * from classroom')
    results = cursor.fetchall()
    for result in results:
        classroom = Classroom(result)
        if not os.path.exists(
                'classroom/{0}/{1}.mp4'.format(classroom.classroom_id, classroom.classroom_id)) or not os.path.exists(
            'classroom/{0}/{1}_back.mp4'.format(classroom.classroom_id, classroom.classroom_id)):
            print(classroom.classroom_id, " video not exist")
            continue
        # 临时数据库是根据我校时间来计算的，为了展示效果，采用默认数据段来显示
        # cursor.execute('SELECT * from course WHERE classroom_id = %s AND begin_time <= %s AND end_time>= %s',
        #                [classroom.classroom_id, time.strftime("%H:%M:%S", time.localtime()),
        #                 time.strftime("%H:%M:%S", time.localtime())])
        cursor.execute('SELECT * from course WHERE classroom_id = %s', [classroom.classroom_id])
        course = Course(cursor.fetchone())
        cursor.execute('SELECT * FROM teacher WHERE teacher_id = %s', [course.teacher_id])
        teacher = Teacher(cursor.fetchone())
        class_brief = ClassBrief(classroom, teacher, course)
        content.append(class_brief)
