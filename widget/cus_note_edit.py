import datetime

from PySide6.QtCore import Slot
from PySide6.QtGui import QDropEvent
from PySide6.QtWidgets import QListWidgetItem

from modules.cus_msg_bus import CusMsgBus
from modules.cus_qwidget import CusQWidget
from modules.db_manager import DBManager, FORMAT_TIME_STR
from modules.vdialog import VDialogType, VDialog
from widget.cus_input_box import CusInputBox
from widget.cus_tag_label import CusTagLabel
from widget.ui.ui_CusNoteEdit import Ui_CusNoteEdit


class CusNoteEdit(CusQWidget, Ui_CusNoteEdit):
    """ 笔记编辑窗口 """

    def __init__(self, rid):
        super().__init__()
        self.con = ''
        self.dt = datetime.datetime.now()
        self.ismodify = set()
        self.rtags = []  # 初始化此窗口时的标签id
        self.tags = []  # 仅 id

        self.setupUi(self)
        self.dateTimeEdit.setDateTime(datetime.datetime.now())
        CusMsgBus.append('delTag', self)
        self.__rid = rid
        self.rid = rid
        self.listWidgeTags.dropEvent = self.overwriteTagDropEvent(self.listWidgeTags.dropEvent)

    @property
    def rid(self):
        return self.__rid

    @rid.setter
    def rid(self, rid):
        """ 设置窗口记录rid 并查库加载内容"""
        if self.rid == 0 and rid:
            CusMsgBus.send('updateEditorId', self.rid, rid)
        self.listWidgeTags.rid = rid

        self.__rid = rid
        if rid:
            self.loadCon(rid)
            self.btnDelNote.show()
        else:
            self.btnDelNote.hide()

        self.updateData()

    def loadCon(self, rid):
        """ 加载内容 """
        res = DBManager.getNoteById(rid)
        if res:
            if res.get('indate'):
                d = datetime.datetime.strptime(res['indate'], FORMAT_TIME_STR)
                self.dateTimeEdit.setDateTime(d)
            else:
                self.dateTimeEdit.setDateTime(datetime.datetime.now())
            if res.get('content'):
                self.textEdit.setText(res['content'])

            # for i in range(self.tagListBox.count() - 1, -1, -1):
            #     child = self.tagListBox.takeAt(i)
            #     child.widget().deleteLater()
            #     del child
            self.tags = [t['tid'] for t in res['tags']]
            self.loadTags()

    def loadTags(self):
        """ 加载标签 """
        self.listWidgeTags.clear()
        tags = DBManager.queryTags(self.tags)
        for idx, tid in enumerate(self.tags):
            if tid not in tags:
                continue
            tag = tags[tid]
            cusTag = CusTagLabel(tag['tid'], idx, tag['text'])
            # self.tagListBox.addWidget(cusTag)
            newItem = QListWidgetItem()
            newItem.tid = tag['tid']
            newItem.tsort = idx
            newItem.setSizeHint(cusTag.sizeHint())
            self.listWidgeTags.addItem(newItem)
            self.listWidgeTags.setItemWidget(newItem, cusTag)

    def addTag(self, tag: list):

        self.tags.extend([t['tid'] for t in tag])
        self.loadTags()

    def delTag(self, item: CusTagLabel):
        if item.tid in self.tags:
            self.tags.remove(item.tid)
        # self.tagListBox.removeWidget(item)
        self.listWidgeTags.takeItem(item.tsort)
        item.close()
        item.deleteLater()
        del item
        self.modifyStatus('tags', self.tags != self.rtags)

    def overwriteTagDropEvent(self, func):
        def inner(e: QDropEvent):
            func(e)
            self.tagIndexesMoved()

        return inner

    def tagIndexesMoved(self):
        tags = [self.listWidgeTags.item(i).tid for i in
                range(self.listWidgeTags.count()) if hasattr(self.listWidgeTags.item(i), 'tid')]
        self.tags = tags
        self.loadTags()
        self.modifyStatus('tags', self.tags != self.rtags)

    def updateData(self):
        self.con = self.textEdit.toPlainText()
        self.dt = self.dateTimeEdit.dateTime().toString('yyyy-MM-dd HH:mm:ss')
        self.rtags = self.tags.copy()
        self.ismodify.clear()
        self.btnCommit.hide()

    def modifyStatus(self, name: str, flag=True):
        if flag:
            self.ismodify.add(name)
        else:
            self.ismodify.discard(name)

        if self.ismodify:
            self.btnCommit.show()
        else:
            self.btnCommit.hide()

    @Slot()
    def on_btnCommit_clicked(self):
        dt = self.dateTimeEdit.dateTime().toString('yyyy-MM-dd HH:mm:ss')
        con = self.textEdit.toPlainText()
        data = {'content': con, 'indate': dt, 'tags': self.tags}
        if self.rid:
            DBManager.modifyNote(self.rid, data)
            self.updateData()
        else:
            self.rid = DBManager.addNote(data)

    @Slot()
    def on_btnDelNote_clicked(self):
        res = VDialog.doSomething(VDialogType.Question, None, '确认', '确定删除此记录？')
        if not res:
            return
        DBManager.delNote(self.rid)
        self.on_btnReturn_clicked()

    @Slot()
    def on_btnReturn_clicked(self):
        self.close()
        CusMsgBus.send('load_rec_list')
        CusMsgBus.send('loadNoteList')
        CusMsgBus.send('closeEditor', self.rid)

    @Slot()
    def on_btnAddTag_clicked(self):

        text = CusInputBox.getText('创建标签', '标签名')

        if not text[1] or not text[0]:
            return
        tagText = text[0].strip()
        if not tagText:
            VDialog.doSomething(VDialogType.Warning,'标签名不能为空或只有空格')
            return
        # 创建标签并入库
        tid = DBManager.addTag(tagText)
        self.addTag([{'tid': tid, 'text': tagText, 'sort': len(self.tags)}])
        self.modifyStatus('tags', self.tags != self.rtags)

    @Slot()
    def on_textEdit_textChanged(self):
        con = self.textEdit.toPlainText()
        if con != self.con:
            self.modifyStatus('textEdit')
        else:
            self.modifyStatus('textEdit', False)

    @Slot()
    def on_dateTimeEdit_dateTimeChanged(self):
        dt = self.dateTimeEdit.dateTime().toString('yyyy-MM-dd HH:mm:ss')
        if dt != self.dt:
            self.modifyStatus('dateTime')
        else:
            self.modifyStatus('dateTime', False)

    def close(self) -> bool:
        CusMsgBus.quit('delTag',self)
        return super(CusNoteEdit, self).close()

