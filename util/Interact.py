from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class RecordListObj(QObject):
    sig_record_list_item_clicked = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    @pyqtSlot(int)
    def record_list_item_clicked(self, item_id):
        print('record list item {0} clicked'.format(item_id))
        self.sig_record_list_item_clicked.emit(item_id)


class ReplayObj(QObject):
    def __init__(self):
        super().__init__()


class BuildingTitleObj(QObject):
    sig_confirm_clicked = pyqtSignal(str, str, str)

    def __init__(self):
        super().__init__()

    @pyqtSlot(str, str, str)
    def confirm_clicked(self, campus, building, floor):
        self.sig_confirm_clicked.emit(campus, building, floor)


class StateTitleObj(QObject):
    sig_button_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    @pyqtSlot(str)
    def button_clicked(self, button_id):
        self.sig_button_clicked.emit(button_id)


class ClassObj(QObject):
    sig_class_item_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    @pyqtSlot(str)
    def class_item_clicked(self, class_id: str):
        classroom_id = class_id[6:]
        self.sig_class_item_clicked.emit(str(classroom_id))


class RealTimeObj(QObject):
    def __init__(self):
        super().__init__()
