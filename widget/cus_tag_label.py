from PySide6.QtGui import QContextMenuEvent, QAction, QCursor, Qt
from PySide6.QtWidgets import QMenu, QStyle, QWidget

from modules.cus_msg_bus import CusMsgBus
from modules.vdialog import VDialog, VDialogType
from widget.ui.ui_CusTagLabel2 import Ui_CusTagLabel


class CusTagLabel(QWidget, Ui_CusTagLabel):

    def __init__(self, tid=0, tsort=0, text=''):
        super().__init__()
        self.isMoving = None
        self.setupUi(self)
        self.tid = tid
        self.tsort = tsort
        self.tttext = text
        self.labelTagText.setText(text)
        self.labelTagText.setToolTip(text)
        self.setAttribute(Qt.WA_DeleteOnClose)
        # self.btnDelTag.setToolTip('移除:' + text)
        # self.btnDelTag.hide()

    # @Slot()
    # def on_btnDelTag_clicked(self):
    #     res = VDialog.doSomething(VDialogType.Question, None, '确认', '确定删除此标签？')
    #     if res:
    #         CusMsgBus.send('delTag', self)

    # def leaveEvent(self, event: QEvent) -> None:
    #     self.labelTagText.setFixedWidth(self.reWidth)
    #     event.accept()
    #
    # def enterEvent(self, event: QEnterEvent) -> None:
    #     self.reWidth = self.labelTagText.width()
    #     self.labelTagText.setFixedWidth(self.reWidth * 1.5)
    #     event.accept()

    # def mousePressEvent(self, event: QMouseEvent) -> None:
    #     if event.button() == Qt.LeftButton:
    #         res = VDialog.doSomething(VDialogType.Question, None, '确认', '确定删除此标签？')
    #         if res:
    #             CusMsgBus.send('delTag', self)

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu(self)
        menu.setObjectName("rightMenu")
        delAction = QAction(self.style().standardIcon(QStyle.SP_DialogCloseButton), '删除')
        delAction.setObjectName('delAction')
        delAction.setParent(menu)
        delAction.triggered.connect(self.delTag)
        menu.addAction(delAction)
        menu.exec(QCursor.pos())

    def delTag(self):
        res = VDialog.doSomething(VDialogType.Question, None, '确认', '确定删除此标签？')
        if res:
            CusMsgBus.send('delTag', self.tid)
