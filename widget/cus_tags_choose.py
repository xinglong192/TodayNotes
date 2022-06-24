from PySide6.QtCore import Qt, QEvent, Slot
from PySide6.QtWidgets import QWidget, QListWidgetItem, QPushButton

from modules.db_manager import DBManager
from widget.ui.ui_CusTagsChoose import Ui_CusTagList


class CusTagsChoose(QWidget, Ui_CusTagList):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.move(self.parent().width() - self.width() - 10, self.parent().height() - self.height() - 10)
        self.__loadSpecialTagList()
        self.__loadCusTagList()


    def __loadSpecialTagList(self):
        res = DBManager.queryTypeTags(1)
        d = {r[1]: r[0] for r in res if r[1] in {'待办', '待办S', '取消', '完成'}}
        for text in ['待办', '待办S', '取消', '完成']:
            if text not in d:
                d[text] = DBManager.addTag(text, 1)
        self.btnTD.tid = d['待办']
        self.btnTDS.tid = d['待办S']
        self.btnCancel.tid = d['取消']
        self.btnDone.tid = d['完成']

    def __loadCusTagList(self):
        res = DBManager.queryUseTags()
        for t in res:
            newItem = QListWidgetItem(self.lvCus)
            newItem.tid = t[0]
            newItem.setText(t[1])
            self.lvCus.addItem(newItem)

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

    @Slot()
    def on_btnTD_clicked(self):
        self.toAddTag(self.btnTD.tid, self.btnTD.text())

    @Slot()
    def on_btnTDS_clicked(self):
        self.toAddTag(self.btnTDS.tid, self.btnTDS.text())

    @Slot()
    def on_btnCancel_clicked(self):
        self.toAddTag(self.btnCancel.tid, self.btnCancel.text())

    @Slot()
    def on_btnDone_clicked(self):
        self.toAddTag(self.btnDone.tid, self.btnDone.text())

    def leaveEvent(self, event: QEvent) -> None:
        self.close()

    def __del__(self):
        print('---ddd--')
