from datetime import datetime

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QMouseEvent, QFontMetrics, QResizeEvent, QCursor, QAction
from PySide6.QtWidgets import QWidget, QStyle, QMenu

from modules.cus_msg_bus import CusMsgBus
from modules.db_manager import DBManager, html2text
from modules.vdialog import VDialog, VDialogType
from widget.ui.ui_CusRecLabel import Ui_frameRecLabel


def formatTime(d: str, showDate=False) -> str:
    if showDate:
        return datetime.strptime(d, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    return datetime.strptime(d, '%Y-%m-%d %H:%M:%S').strftime('%H:%M:%S')


class CusRecordLabel(QWidget, Ui_frameRecLabel):

    def __init__(self, rid: int | str, showDate=False, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.__showtime = None
        self.__rtime = None
        self.__rcon = None
        self.__showcon = None
        self.__showDate = showDate
        self.rid = rid
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.__queryTagStatus()

    @property
    def rcon(self):
        return self.__rcon

    @rcon.setter
    def rcon(self, c: str):
        if '<html>' in c:
            c = html2text(c)
        self.__rcon = c
        width = self.size().width() - 1
        fm = QFontMetrics(self.labelContent.font())
        sc = c if '\n' not in c else c[:c.find('\n')]
        self.__showcon = fm.elidedText(sc, Qt.ElideRight, width)
        self.labelContent.setText(self.__showcon)

    @property
    def rtime(self):
        return self.__rtime

    @rtime.setter
    def rtime(self, t):
        self.__rtime = t
        self.__showtime = formatTime(t, self.__showDate)
        self.labelTime.setText(self.__showtime)

    def __queryTagStatus(self):
        """ 根据标签状态 选择样式 """
        res = DBManager.queryTagsByRid(self.rid)
        d = {r['text'] for r in res}
        if '待办' in d:
            self.framew.setProperty('tagStauts', 'todo')
        if '待办S' in d:
            self.framew.setProperty('tagStauts', 'todos')
        if '取消' in d:
            self.framew.setProperty('tagStauts', 'cancel')
        if '完成' in d:
            self.framew.setProperty('tagStauts', 'done')
        self.framew.style().unpolish(self.framew)
        self.framew.style().polish(self.framew)


    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            CusMsgBus.send('openEditor', self.rid)
        e.accept()

    def contextMenuEvent(self, event) -> None:
        menu = QMenu(self)
        menu.setObjectName("rightRecMenu")
        delRecAction = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton), '删除')
        delRecAction.setObjectName('delRecAction')
        delRecAction.setParent(menu)
        delRecAction.triggered.connect(self.on_btnDelRec_clicked)
        menu.addAction(delRecAction)
        menu.exec(QCursor.pos())

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.rcon = self.__rcon
        event.accept()

    @Slot()
    def on_btnDelRec_clicked(self):
        res = VDialog.doSomething(VDialogType.Question, None, '确认', '确定删除此记录？')
        if not res:
            return
        DBManager.delNote(self.rid)
        DBManager.delFileByRid(self.rid)
        CusMsgBus.send('closeEditor', self.rid)
        CusMsgBus.send('load_rec_list')
        CusMsgBus.send('loadNoteList')
        self.close()
