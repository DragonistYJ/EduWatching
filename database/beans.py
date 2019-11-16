class Classroom:
    def __init__(self, info):
        self.classroom_id = info[0]
        self.campus = info[1]
        self.building = info[2]
        self.floor = info[3]

    def __str__(self):
        return 'classroom_id: {0}; campus: {1}; building: {2}; floor: {3}'.format(self.classroom_id, self.campus,
                                                                                  self.building, self.floor)


class Teacher:
    def __init__(self, info):
        self.teacher_id = info[0]
        self.name = info[1]
        self.department = info[2]

    def __str__(self):
        return 'teacher_id: {0}; name: {1}; department: {2}'.format(self.teacher_id, self.name, self.department)


class Course:
    def __init__(self, info):
        self.course_id = info[0]
        self.name = info[1]
        self.classroom_id = info[2]
        self.teacher_id = info[3]
        self.student_number = info[4]
        self.weekday = info[5]
        self.begin_time = info[6]
        self.end_time = info[7]

    def __str__(self):
        return 'course_id: {0}; name: {1}; classroom_id: {2}; teacher_id: {3}; student_number: {4}; ' \
               'weekday: {5}; begin_time: {6}; end_time: {7}'.format(self.course_id, self.name, self.classroom_id,
                                                                     self.teacher_id, self.student_number, self.weekday,
                                                                     self.begin_time, self.end_time)


class ClassBrief:
    # 在监控列表页中显示的一个教室方格
    # 显示简略信息
    def __init__(self, classroom: Classroom, teacher: Teacher, course: Course):
        self.classroom = classroom
        self.teacher = teacher
        self.course = course
        self.present_student_number = 0
        self.isAbnormal = False
        self.isShow = True

    def __str__(self):
        return 'classroom: {0}\nteacher: {1}\ncourse: {2}\npresent student number: {3}\n'.format(self.classroom,
                                                                                                 self.teacher,
                                                                                                 self.course,
                                                                                                 self.present_student_number)


class SummaryRecord:
    def __init__(self, summary_record_id, course_id, date, student_score, teacher_score, student_video_path,
                 teacher_video_path):
        self.summary_record_id = summary_record_id
        self.course_id = course_id
        self.date = date
        self.student_score = student_score
        self.teacher_score = teacher_score
        self.student_video_path = student_video_path
        self.teacher_video_path = teacher_video_path


class AbnormalRecord:
    def __init__(self, abnormal_record_id, summary_record_id, type, description, time_point, data_path):
        self.abnormal_record_id = abnormal_record_id
        self.summary_record_id = summary_record_id
        self.type = type
        self.description = description
        self.time_point = time_point
        self.data_path = data_path
