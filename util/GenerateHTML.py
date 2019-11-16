import random

import jieba

from database.beans import ClassBrief
from model.Emotion.emotion import Emotion
from util.functions import img_format_base64


class HTMLFactory:
    instance = None

    def class_brief_box_first(self, class_brief: ClassBrief):
        template = '''
                    <div class="box" id="class_{0}" onclick="class_clicked(this)">
                        <h3>{1}</h3>
                        <img src="data:image/jpeg;base64,{2}" alt=""/>
                        <h4>上课地点：{3}</h4>
                        <h4>教师：{4}</h4>
                        <div class="button">
                            <span><a href="#">应到人数：{5}</a></span>
                            <span><a href="#">实到人数：{6}</a></span>
                        </div>
                    </div>
                    '''
        base64code = img_format_base64('classroom/' + class_brief.classroom.classroom_id + '/thumbnail.jpg', 640,
                                       360)
        template = template.replace('\n', '')
        return template.format(class_brief.classroom.classroom_id, class_brief.course.name, base64code,
                               class_brief.classroom.campus + class_brief.classroom.building + class_brief.classroom.floor,
                               class_brief.teacher.name, class_brief.course.student_number,
                               class_brief.present_student_number)

    def class_brief_box(self, class_brief: ClassBrief):
        template = '''
                    <h3>{0}</h3>
                    <img src="data:image/jpeg;base64,{1}" alt=""/>
                    <h4>上课地点：{2}</h4>
                    <h4>教师：{3}</h4>
                    <div class="button">
                        <span><a href="#">应到人数：{4}</a></span>
                        <span><a href="#">实到人数：{5}</a></span>
                    </div>
                    '''
        base64code = img_format_base64('classroom/' + class_brief.classroom.classroom_id + '/thumbnail.jpg', 640,
                                       360)
        template = template.replace('\n', '')
        return template.format(class_brief.course.name,
                               base64code,
                               class_brief.classroom.campus + class_brief.classroom.building + class_brief.classroom.floor,
                               class_brief.teacher.name, class_brief.course.student_number,
                               class_brief.present_student_number)

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = HTMLFactory()
        return cls.instance
