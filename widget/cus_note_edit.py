import datetime
import os
import re
import uuid

from PySide6.QtCore import Slot, QMimeData, QBuffer, QByteArray, QIODevice, QUrl, QPoint
from PySide6.QtGui import QDropEvent, QImage, QImageReader, QTextDocument, QAction, QCursor, Qt, \
    QMouseEvent, QDesktopServices, QTextCursor, QKeyEvent
from PySide6.QtWidgets import QListWidgetItem, QFileDialog

from modules.cus_msg_bus import CusMsgBus
from modules.cus_qwidget import CusQWidget
from modules.db_manager import DBManager, FORMAT_TIME_STR
from modules.setting import temp_path_images, use_cus_view
from modules.vdialog import VDialogType, VDialog
from widget.cus_image_view import CusImageView
from widget.cus_input_box import CusInputBox
from widget.cus_tag_label import CusTagLabel
from widget.cus_tags_choose import CusTagsChoose
from widget.ui.ui_CusNoteEdit import Ui_CusNoteEdit


class CusNoteEdit(CusQWidget, Ui_CusNoteEdit):
    """ 笔记编辑窗口 """

    def __init__(self, rid, parent=None):
        super().__init__(parent)
        self.ctrlPress = False
        self.editMovePos = QPoint(0, 0)
        self.mouseOnImgMove = False
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.images = {}
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
        self.textEdit.insertFromMimeData = self.insertFromMimeData(self.textEdit.insertFromMimeData)
        self.textEdit.canInsertFromMimeData = self.canInsertFromMimeData(self.textEdit.canInsertFromMimeData)
        self.textEdit.contextMenuEvent = self.textEditContextMenu
        self.textEdit.mouseReleaseEvent = self.textEditMouseRelease(self.textEdit.mouseReleaseEvent)
        self.textEdit.mouseMoveEvent = self.textEditMouseMove(self.textEdit.mouseMoveEvent)
        self.textEdit.mousePressEvent = self.textEditMousePress(self.textEdit.mousePressEvent)

        self.textEdit.setFocus()

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

            # 尝试查询图片等附件
            files = DBManager.getFileByRid(rid)
            if files:
                for fd in files:
                    img = QImage()
                    img.loadFromData(fd[2], fd[3])
                    self.loadImages(img, QUrl(fd[0]), fd[3])

            if res.get('content'):
                ht = res['content']
                self.textEdit.setHtml(ht)

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
            newItem = QListWidgetItem()
            newItem.tid = tag['tid']
            newItem.tsort = idx
            newItem.setSizeHint(cusTag.sizeHint())
            self.listWidgeTags.addItem(newItem)
            self.listWidgeTags.setItemWidget(newItem, cusTag)

    def addTag(self, tag: list):
        self.tags.extend([t['tid'] for t in tag])
        self.loadTags()
        self.modifyStatus('tags', self.tags != self.rtags)

    def delTag(self, item: CusTagLabel):
        if item.tid in self.tags:
            self.tags.remove(item.tid)
        self.listWidgeTags.takeItem(item.tsort)
        item.close()
        item.deleteLater()
        self.tagIndexesMoved()
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
        self.con = self.textEdit.toHtml()
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
        con = self.textEdit.toHtml()
        data = {'content': con, 'indate': dt, 'tags': self.tags}
        # 从self.images里删除被移除的图片
        imgs = re.findall(r'<img src="([^"]*)" />', con)
        difimgids = self.images.keys() - set(imgs)
        for ids in difimgids:
            self.images.pop(ids, None)
        if self.rid:
            DBManager.modifyNote(self.rid, data)
            self.saveImagesToDB()
            self.updateData()
        else:
            tmprid = DBManager.addNote(data)
            self.saveImagesToDB(tmprid)
            self.rid = tmprid

    @Slot()
    def on_btnDelNote_clicked(self):
        res = VDialog.doSomething(VDialogType.Question, None, '确认', '确定删除此记录？')
        if not res:
            return
        DBManager.delNote(self.rid)
        DBManager.delFileByRid(self.rid)
        self.on_btnReturn_clicked()

    @Slot()
    def on_btnReturn_clicked(self):
        self.close()
        CusMsgBus.send('load_rec_list')
        CusMsgBus.send('loadNoteList')
        CusMsgBus.send('closeEditor', self.rid)

    @Slot()
    def on_btnAddTag_clicked(self):
        # self.add_new_tag()
        a = CusTagsChoose(self)
        a.show()

    def add_new_tag(self):
        text = CusInputBox.getText('创建标签', '标签名', self)

        if not text or not text[1] or not text[0]:
            return
        tagText = text[0].strip()
        if not tagText:
            VDialog.doSomething(VDialogType.Warning, '标签名不能为空或只有空格')
            return
        # 创建标签并入库
        tid = DBManager.addTag(tagText)
        self.addTag([{'tid': tid, 'text': tagText}])

    @Slot()
    def on_textEdit_textChanged(self):
        con = self.textEdit.toHtml()
        # 找出新插入的图片添加链接
        recon = self.addImgsHref(con)
        if recon != con:
            self.textEdit.setHtml(recon)
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

    def addImgsHref(self, con):
        diffImgs = set(re.findall(r'<img src="([^"]*)" />', con)) - set(
            re.findall(r'<a href=[^>]*><img src="([^"]*)" /></a>', con))
        for iid in diffImgs:
            con = re.sub(f'(<img src="{iid}" />)', f' <a href="{iid}">\\1</a> ', con)
        return con

    def textEditContextMenu(self, e):
        menu = self.textEdit.createStandardContextMenu()
        saveImage = QAction('save image to')
        saveImage.setObjectName('saveImage')
        saveImage.setParent(menu)
        saveImage.triggered.connect(self.editSaveAsImage)
        saveImage.setDisabled(True)
        sf = self.textEdit.textCursor().hasSelection()
        if sf:
            md = self.textEdit.createMimeDataFromSelection()
            rr = re.findall('<img src="([^"]*)"[^>]* />', md.html())
            if rr:
                saveImage.setDisabled(False)
        menu.addAction(saveImage)
        menu.exec(QCursor.pos())

    def editSaveAsImage(self):
        md = self.textEdit.createMimeDataFromSelection()
        mr = re.findall('<img src="([^"]*)"[^>]* />', md.html())
        if not mr:
            VDialog.doSomething(VDialogType.Error, '发成错误:未获取到图片信息')
            return
        dir = QFileDialog.getExistingDirectory(self, "选择存储路径", './')
        if not dir:
            return
        for mid in mr:
            bitup = self.images.get(mid, None)
            if bitup is None:
                VDialog.doSomething(VDialogType.Warning, f'图片数据丢失，请重试！id={mid}')
                continue
            try:
                with open(dir + f'/image{mid}.{bitup[1].lower()}', 'wb') as imgfile:
                    imgfile.write(bitup[0].data())
            except Exception as e:
                VDialog.doSomething(VDialogType.Error, f'图片数据保存失败，请重试！\n{e}')

    """    ↓↓↓↓----- 编辑器图片插入相关函数  -------↓↓↓↓↓↓   """

    def canInsertFromMimeData(self, func):
        """判断数据是否能够插入"""

        def inner(source: QMimeData):
            return source.hasImage() or source.hasUrls() or func(source)

        return inner

    def insertFromMimeData(self, func):
        """ 粘贴数据 """

        def inner(source: QMimeData):
            if source.hasImage():
                image = source.imageData()
                imgid = self.getImageId()
                self.loadImages(image, QUrl(imgid))
                self.createImageData(QUrl(imgid))
            elif source.hasUrls():
                for url in source.urls():
                    path = url.toLocalFile()
                    if not path:
                        # 说明可能不是本地文件，而是新创建的链接
                        func(source)
                        continue
                    suffix = path[path.rfind('.') + 1:]
                    if suffix in QImageReader.supportedImageFormats():
                        image = QImage(path)
                        imgid = self.getImageId()
                        self.loadImages(image, QUrl(imgid), suffix)
                        self.createImageData(QUrl(imgid))
                    else:
                        # 尝试已文本形式加入
                        try:
                            with open(path, 'r', encoding='utf8') as f:
                                self.textEdit.textCursor().insertText(f.read())
                        except Exception as e:
                            VDialog.doSomething(VDialogType.Error, f'发生错误:{e}')
            elif source.hasFormat('application/x-qt-windows-mime;value="Titled Hyperlink Format"') and (
                    "http:" in source.text() or "https:" in source.text()):
                """ 如果是包含标题的超链接，尝试重新拼接标题，加入链接地址"""
                ss = re.sub(
                    r'<!--StartFragment--><a href="([^"]*)"([^>]*)>(.*)</a><!--EndFragment-->',
                    r'<!--StartFragment--><a href="\1"\2>[\3](\1)</a><!--EndFragment-->',
                    source.html())
                scc = QMimeData()
                scc.setHtml(ss)
                scc.setText(source.text())
                func(scc)
            else:
                func(source)

        return inner

    def getImageId(self):
        return re.sub('-', '', str(uuid.uuid1()))

    def createImageData(self, url):
        """ 插入资源时请先确保 document已加载数据"""
        cursor = self.textEdit.textCursor()
        cursor.insertImage(url.toString())

    def loadImages(self, image: QImage, url, end="PNG"):
        """ 加载资源数据 """
        self.saveImages(image, url.toString(), end)
        image = image.scaled(30, 30, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.textEdit.document().addResource(QTextDocument.ImageResource, url, image)

    def saveImages(self, image: QImage, imgid: str, end="PNG"):
        ba = QByteArray()
        buffer = QBuffer(ba)
        buffer.open(QIODevice.WriteOnly)
        image.save(buffer, end)
        self.images[imgid] = (ba, end)

    def saveImagesToDB(self, rid=0):
        """ 保存图片信息并清空对象中的图片临时数据 """
        if self.images:
            if not rid:
                rid = self.rid
            DBManager.saveFile([[imgid, rid, self.images[imgid][0], self.images[imgid][1]] for imgid in self.images])
        # self.images.clear()

    """ ↑↑↑↑↑ images funcs end ↑↑↑↑↑↑ """

    def textEditMousePress(self, func):
        def inner(e: QMouseEvent):
            if e.button() == Qt.LeftButton:
                self.editMovePos = e.pos()
            func(e)

        return inner

    def textEditMouseMove(self, func):
        def inner(e: QMouseEvent):
            if not self.mouseOnImgMove and e.buttons() == Qt.LeftButton:
                if not (abs(e.pos().x() - self.editMovePos.x()) < 3 and abs(e.pos().y() - self.editMovePos.y()) < 3):
                    self.mouseOnImgMove = True
            func(e)

        return inner

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Control:
            self.ctrlPress = True
        super(CusNoteEdit, self).keyPressEvent(event)

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Control:
            self.ctrlPress = False
        super(CusNoteEdit, self).keyReleaseEvent(event)

    def textEditMouseRelease(self, func):
        def inner(e: QMouseEvent):
            if e.button() == Qt.RightButton:
                self.mouseOnImgMove = False
                url = self.textEdit.anchorAt(e.pos())
                if url and url in self.images:
                    if not self.textEdit.textCursor().hasSelection():
                        cursor = self.textEdit.cursorForPosition(e.pos())
                        cursor.select(QTextCursor.WordUnderCursor)
                        self.textEdit.setTextCursor(cursor)

                func(e)
                return
            if e.button() != Qt.LeftButton:
                self.mouseOnImgMove = False
                func(e)
                return
            if self.mouseOnImgMove:
                self.mouseOnImgMove = False
                func(e)
                return
            url = self.textEdit.anchorAt(e.pos())
            if url:
                if url in self.images:
                    if use_cus_view == '0':
                        tmpFilePath = os.path.abspath(temp_path_images + f'/temp{url}.{self.images[url][1]}')
                        with open(tmpFilePath, 'wb') as imgFile:
                            imgFile.write(self.images[url][0].data())

                        QDesktopServices.openUrl(QUrl("file:///" + tmpFilePath, QUrl.TolerantMode))
                    else:
                        img = QImage()
                        img.loadFromData(self.images[url][0], self.images[url][1])
                        iv = CusImageView(title=f'图片{url}')
                        iv.setLabelImage(img, self.images[url][1])
                        iv.show()
                elif self.ctrlPress and (url.startswith('http://') or url.startswith('https://')):
                    # 按下ctrl键才能打开链接
                    self.ctrlPress = False
                    QDesktopServices.openUrl(QUrl(url))
            func(e)

        return inner

    def closeEvent(self, event) -> None:
        CusMsgBus.quit('delTag', self)
        self.listWidgeTags.dropEvent = None
        self.textEdit.insertFromMimeData = None
        self.textEdit.canInsertFromMimeData = None
        self.textEdit.contextMenuEvent = None
        self.textEdit.mouseReleaseEvent = None
        self.textEdit.mouseMoveEvent = None
        self.textEdit.mousePressEvent = None
        super(CusNoteEdit, self).closeEvent(event)
