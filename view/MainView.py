from PyQt5.QtCore import Qt, QEvent, pyqtSignal, QPoint, QSize, QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QPushButton

from threads.Sql import get_class_briefs
from threads.ClassBrief import ClassBriefThread
from util.GenerateHTML import HTMLFactory
from util.Interact import *
from util.Variable import update_class_table_lock
from view.RealTimeView import View_RealTime
from view.ReplayView import View_Replay
from view.ui.MainWindow_ui import Ui_MainWindow
from util.WatchMethods import *


class View_Main(QMainWindow, Ui_MainWindow):
    classroom_briefs = []
    class_brief_threads = []
    view_real_time = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 四个页面的切换
        self.widget_building.clicked.connect(self.change_page_class)
        self.widget_status.clicked.connect(self.change_page_status)
        self.widget_abnormal.clicked.connect(self.change_page_abnormal)
        self.widget_record.clicked.connect(self.change_page_record)

        # 从数据库读取教室信息
        get_class_briefs(self.classroom_briefs)
        # 多线程完成教室初始化显示
        threads = []
        for brief in self.classroom_briefs:
            threads.append(threading.Thread(target=init_thumbnail, args=(brief,)))
        for thread in threads:
            thread.start()
            thread.join()

        # 注册教室列表
        self.class_web = QWebEngineView(self.page_class)
        self.class_channel = QWebChannel(self.class_web.page())
        self.class_obj = ClassObj()

        # 注册按教学楼分类的标题组件
        self.building_title_web = QWebEngineView(self.page_class)
        self.building_title_web.setMaximumHeight(90)
        self.building_title_web.setMinimumHeight(90)
        self.building_title_channel = QWebChannel(self.building_title_web.page())
        self.building_title_obj = BuildingTitleObj()

        # 注册按状态分类的标题栏组件
        self.state_title_web = QWebEngineView(self.page_class)
        self.state_title_web.setMinimumHeight(65)
        self.state_title_web.setMaximumHeight(65)
        self.state_title_channel = QWebChannel(self.state_title_web.page())
        self.state_title_obj = StateTitleObj()

        self.setup_class_page()

        # 注册上课回看列表需要的组件
        self.record_list_page = QWebEngineView(self.page_reocrd)
        self.record_list_channel = QWebChannel(self.record_list_page.page())
        self.record_list_obj = RecordListObj()
        self.setup_record_table()

    def setup_class_page(self):
        # 初始化按教学楼搜索标题栏
        self.building_title_obj.sig_confirm_clicked.connect(self.sift_by_building)
        self.building_title_channel.registerObject('building_title_obj', self.building_title_obj)
        self.building_title_web.page().setWebChannel(self.building_title_channel)
        self.building_title_web.load(QUrl.fromLocalFile(os.path.abspath('view/html/TitleBuilding.html')))

        # 初始化按状态搜索标题栏
        self.state_title_channel.registerObject('state_title_obj', self.state_title_obj)
        self.state_title_web.page().setWebChannel(self.state_title_channel)
        self.state_title_web.load(QUrl.fromLocalFile(os.path.abspath('view/html/TitleState.html')))
        self.state_title_web.hide()

        # 初始化教室页面
        self.class_obj.sig_class_item_clicked.connect(self.open_real_time)
        self.class_channel.registerObject('class_obj', self.class_obj)
        self.class_web.page().setWebChannel(self.class_channel)
        self.class_web.load(QUrl.fromLocalFile(os.path.abspath('view/html/ClassTable.html')))
        self.class_web.loadFinished.connect(self.refresh_page)

        self.verticalLayout_7.addWidget(self.building_title_web)
        self.verticalLayout_7.addWidget(self.state_title_web)
        self.verticalLayout_7.addWidget(self.class_web)
        # 统计学生人数线程对象生成
        for brief in self.classroom_briefs:
            self.class_brief_threads.append(ClassBriefThread(brief, self.class_web.page()))
        for thread in self.class_brief_threads:
            thread.start()

    def refresh_page(self):
        # 刷新教室列表的显示
        init_table = ''
        for brief in self.classroom_briefs:
            if brief.isShow:
                init_table += HTMLFactory.get_instance().class_brief_box_first(brief)
        self.class_web.page().runJavaScript("setupTable('{0}')".format(init_table))

    def open_real_time(self, class_brief_id):
        for brief in self.classroom_briefs:
            if brief.classroom.classroom_id == class_brief_id:
                print(">>>>>>>>>>>>>>>>>>>>>> classroom {0} begin to be monitored".format(class_brief_id))
                for thread in self.class_brief_threads:
                    thread.pause()
                time.sleep(2)
                self.view_real_time = View_RealTime(brief)
                self.view_real_time.sig_on_closed.connect(self.resume)
                self.view_real_time.showMaximized()
                break

    def sift_by_building(self, campus, building, floor):
        # 按照教学楼显示
        # 根据校区、教学楼、教室号来进行筛选
        for brief in self.classroom_briefs:
            if (campus in brief.classroom.campus) and (building in brief.classroom.building) and (
                    floor in brief.classroom.floor):
                if not brief.isShow:
                    self.add_box(brief)
                    brief.isShow = True
            elif brief.isShow:
                self.remove_box(brief)
                brief.isShow = False

    # 初始化上课回看列表
    def setup_record_table(self):
        self.record_list_obj.sig_record_list_item_clicked.connect(self.open_replay)
        self.record_list_channel.registerObject('record_list_obj', self.record_list_obj)
        self.record_list_page.page().setWebChannel(self.record_list_channel)
        self.verticalLayout_10.addWidget(self.record_list_page)
        self.record_list_page.load(QUrl.fromLocalFile(os.path.abspath('view/html/Record.html')))

    def open_replay(self, item_id):
        self.view_replay = View_Replay()
        self.view_replay.showMaximized()

    def change_page_class(self):
        for thread in self.class_brief_threads:
            thread.resume()
        self.stackedWidget.setCurrentIndex(0)
        self.building_title_web.show()
        self.state_title_web.hide()

        for brief in self.classroom_briefs:
            if not brief.isShow:
                self.add_box(brief)
                brief.isShow = True

    def change_page_status(self):
        for thread in self.class_brief_threads:
            thread.resume()
        self.stackedWidget.setCurrentIndex(0)
        self.building_title_web.hide()
        self.state_title_web.show()

        for brief in self.classroom_briefs:
            if not brief.isShow:
                self.add_box(brief)
                brief.isShow = True

    def change_page_abnormal(self):
        for thread in self.class_brief_threads:
            thread.resume()
        self.stackedWidget.setCurrentIndex(0)
        self.building_title_web.hide()
        self.state_title_web.hide()

        for brief in self.classroom_briefs:
            if brief.isAbnormal:
                if not brief.isShow:
                    self.add_box(brief)
                brief.isShow = True
            else:
                if brief.isShow:
                    self.remove_box(brief)
                brief.isShow = False

    def add_box(self, brief):
        box = HTMLFactory.get_instance().class_brief_box_first(brief)
        update_class_table_lock.acquire()
        self.class_web.page().runJavaScript("addBox('{0}')".format(box))
        update_class_table_lock.release()

    def remove_box(self, brief):
        update_class_table_lock.acquire()
        self.class_web.page().runJavaScript("removeBox('class_{}')".format(brief.classroom.classroom_id))
        update_class_table_lock.release()

    def change_page_record(self):
        self.stackedWidget.setCurrentIndex(1)
        for thread in self.class_brief_threads:
            thread.pause()

    # 关闭实时监控页之后调用
    def resume(self):
        for thread in self.class_brief_threads:
            thread.resume()
