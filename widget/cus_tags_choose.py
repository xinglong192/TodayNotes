from PySide6.QtCore import Qt, QEvent, Slot
from PySide6.QtGui import QAction, QCursor, QEnterEvent
from PySide6.QtWidgets import QWidget, QListWidgetItem, QMenu, QStyle

from modules.db_manager import DBManager
from modules.vdialog import VDialogType, VDialog
from widget.cus_input_box import CusInputBox
from widget.ui.ui_CusTagsChooseSimple import Ui_CusTagList


class CusTagsChoose(QWidget, Ui_CusTagList):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.viewshow = False
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.move(self.parent().width() - self.width() - 10, self.parent().height() - self.height() - 10)
        self.__loadCusTagList()
        self.lvCus.contextMenuEvent = self.lvContextMenu

    def __loadCusTagList(self):
        res = DBManager.queryUseTags()
        for t in res:
            newItem = QListWidgetItem(self.lvCus)
            newItem.tid = t[0]
            newItem.setText(t[1])
            self.lvCus.addItem(newItem)

    def lvContextMenu(self, event) -> None:
        self.viewshow = True
        menu = QMenu(self)

        menu.setObjectName("rightRecMenu")

        delTagAc = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton), '删除')
        delTagAc.setObjectName('delTagAc')
        delTagAc.setParent(menu)

        def CloseAfer(func):
            def handle(*args, **kwargs):
                func(*args, **kwargs)
                self.close()

            return handle

        @CloseAfer
        def delTag():
            st = self.lvCus.selectedItems()[0]
            res = VDialog.doSomething(VDialogType.Question, None, '确认', '确定从所有记录中删除此标签？')
            if not res:
                return
            DBManager.delTag(st.tid)
            self.parent().delTag(st.tid,False)

        delTagAc.triggered.connect(delTag)

        renameTagAc = QAction(self.style().standardIcon(QStyle.SP_CommandLink), '重命名')
        renameTagAc.setObjectName('renameTagAc')
        renameTagAc.setParent(menu)

        @CloseAfer
        def renameTag():
            st = self.lvCus.selectedItems()[0]
            text = CusInputBox.getText('重命名标签', '标签名', self, st.text(),'提示:所有记录中的此标签都将重命名!')
            if not text or not text[1] or not text[0]:
                return
            tagText = text[0].strip()
            if not tagText:
                VDialog.doSomething(VDialogType.Warning, '标签名不能为空或只有空格')
                return
            DBManager.renameTag(st.tid, tagText)
            self.parent().loadTags()

        renameTagAc.triggered.connect(renameTag)

        menu.addAction(renameTagAc)
        menu.addAction(delTagAc)
        menu.exec(QCursor.pos())

    def toAddTag(self, tid: int | str, text: str):
        self.parent().addTag([{'tid': tid, 'text': text}])
        self.close()

    @Slot()
    def on_lvCus_itemClicked(self):
        st = self.lvCus.selectedItems()[0]
        self.toAddTag(st.tid, st.text())

    @Slot()
    def on_btnAddNew_clicked(self):
        self.parent().add_new_tag()

    def leaveEvent(self, event: QEvent) -> None:
        if self.viewshow:
            return
        self.close()

    def enterEvent(self, event: QEnterEvent) -> None:
        self.viewshow = False

    def closeEvent(self, event) -> None:
        self.lvCus.contextMenuEvent = None
