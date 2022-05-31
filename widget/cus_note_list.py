import datetime

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QListWidgetItem, QStyle

from modules.cus_msg_bus import CusMsgBus
from modules.cus_qwidget import CusQWidget
from modules.db_manager import DBManager
from widget.cus_record_label import CusRecordLabel
from widget.ui.ui_CusNoteList import Ui_CusNoteList

FORMAT_DATE_STR = 'yyyy-MM-dd'


class CusNoteList(CusQWidget, Ui_CusNoteList):
    """ 笔记查询窗口 """

    def __init__(self, parent=None):

        self.sdt = datetime.datetime.now()
        self.edt = datetime.datetime.now()
        self.usedate = True
        self.queryText = ''

        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        # 设置最大化和复原的图标
        self.btnRecovery.setIcon(self.style().standardIcon(QStyle.SP_TitleBarNormalButton))
        self.btnMax.setIcon(self.style().standardIcon(QStyle.SP_TitleBarMaxButton))
        # 隐藏窗口复原按钮
        self.btnRecovery.hide()
        # 设置时间选择器
        self.dateTimeEdit.setDateTime(datetime.datetime.now())
        self.dateTimeStart.setDateTime(datetime.datetime.now())
        self.dateTimeEnd.setDateTime(datetime.datetime.now())
        self.dateIntervalWidget.hide()
        self.dateTimeEdit.contextMenuEvent = self.dateRightClickedMenu
        self.dateIntervalWidget.contextMenuEvent = self.dateRightClickedMenu
        self.dateTimeStart.contextMenuEvent = self.dateRightClickedMenu
        self.dateTimeEnd.contextMenuEvent = self.dateRightClickedMenu

        self.loadNoteList()
        self.listWidget.setFocus()
        CusMsgBus.append('loadNoteList', self)

    def dateRightClickedMenu(self, e):
        if self.dateTimeEdit.isHidden():
            self.dateTimeEdit.show()
            self.dateIntervalWidget.hide()
            self.sdt = self.dateTimeEdit.date().toString(FORMAT_DATE_STR)
            self.edt = self.dateTimeEdit.date().toString(FORMAT_DATE_STR)
        else:
            self.dateTimeEdit.hide()
            self.dateIntervalWidget.show()
            self.sdt = self.dateTimeStart.date().toString(FORMAT_DATE_STR)
            self.edt = self.dateTimeEnd.date().toString(FORMAT_DATE_STR)
        self.loadNoteList()

    @Slot()
    def on_checkBoxDateUse_stateChanged(self):
        if self.checkBoxDateUse.checkState() == Qt.CheckState.Unchecked:
            self.dateTimeEdit.setDisabled(True)
            self.usedate = False
        else:
            self.dateTimeEdit.setDisabled(False)
            self.usedate = True
        self.loadNoteList()

    @Slot()
    def on_leQueryInput_textChanged(self):
        self.queryText = self.leQueryInput.text()
        self.loadNoteList()

    @Slot()
    def on_dateTimeEdit_dateTimeChanged(self):
        self.sdt = self.dateTimeEdit.date().toString(FORMAT_DATE_STR)
        self.edt = self.dateTimeEdit.date().toString(FORMAT_DATE_STR)
        self.loadNoteList()

    @Slot()
    def on_dateTimeStart_dateTimeChanged(self):
        self.sdt = self.dateTimeStart.date().toString(FORMAT_DATE_STR)
        self.loadNoteList()

    @Slot()
    def on_dateTimeEnd_dateTimeChanged(self):
        self.edt = self.dateTimeEnd.date().toString(FORMAT_DATE_STR)
        self.loadNoteList()

    @Slot()
    def on_btnQuery_clicked(self):
        self.loadNoteList()

    def loadNoteList(self):
        """ 根据条件 查询笔记 """

        condition = {'conQuery': self.queryText, 'usedate': self.usedate, 'indate': (self.sdt, self.edt)}
        res = DBManager.queryForNotesList(condition)
        self.labelStatus.setText(f'共 {len(res)} 条')
        self.__addNote(res)

    def __addNote(self, notes: list):
        self.listWidget.clear()
        for note in notes:
            rlabel = CusRecordLabel(note[0], True, self)
            rlabel.rcon = note[1]
            rlabel.rtime = note[2]
            newItem = QListWidgetItem(self.listWidget)
            newItem.setSizeHint(rlabel.sizeHint())
            self.listWidget.addItem(newItem)
            self.listWidget.setItemWidget(newItem, rlabel)

    def closeEvent(self, event) -> None:
        CusMsgBus.quit('loadNoteList', self)
        self.dateTimeEdit.contextMenuEvent = None
        self.dateIntervalWidget.contextMenuEvent = None
        self.dateTimeStart.contextMenuEvent = None
        self.dateTimeEnd.contextMenuEvent = None
        super(CusNoteList, self).closeEvent(event)
