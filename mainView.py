import configparser
import os
import sys

from PySide6.QtCore import QCoreApplication, Slot, Qt
from PySide6.QtGui import QIcon, QAction, QCursor
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QStyle, QListWidgetItem

from modules.cus_msg_bus import CusMsgBus
from modules.cus_qwidget import CusQWidget
from modules.db_manager import DBManager
from modules.vdialog import VDialog, VDialogType
from ui_CusRecordView import Ui_CusRecordView
from widget.cus_note_edit import CusNoteEdit
from widget.cus_note_list import CusNoteList
from widget.cus_record_label import CusRecordLabel
from widget.cus_suspend_ball import CusSuspendBall

default_close_flag = '0'  # 关闭按钮的标识(0:无/1:关闭程序/2:最小化到托盘)
default_sball_flag = '0'  # 最小化至托盘后是否显示悬浮球 (0:无-未设置/1:手动显示/2:自动显示)
confFile = 'data/conf.ini'
con = configparser.ConfigParser()


def update_conf(sec: str, opt: str, val: str) -> None:
    """ 更新配置文件中键值 """
    if os.path.exists(confFile) and con.has_section(sec):
        con.read(confFile)
        con.set(sec, opt, val)
        con.write(open(file=confFile, mode='r+', encoding='utf8'))
        return
    con.add_section(sec)
    con.set(sec, opt, val)
    con.write(open(file=confFile, mode='a', encoding='utf8'))


# 读取配置文件
if os.path.exists(confFile):
    con.read(confFile, 'utf-8')
    # 读按钮标识配置
    if con.has_option('base', 'default_close_flag'):
        baseItems = dict(con.items('base'))
        default_close_flag = baseItems.get('default_close_flag', '0')
    else:
        update_conf('base', 'default_close_flag', '0')
    # 读悬浮球标识配置
    if con.has_option('base', 'default_sball_flag'):
        baseItems = dict(con.items('base'))
        default_sball_flag = baseItems.get('default_sball_flag', '0')
    else:
        update_conf('base', 'default_sball_flag', '0')
else:
    if not os.path.exists('data'):
        os.makedirs('data')
    update_conf('base', 'default_close_flag', '0')
    update_conf('base', 'default_sball_flag', '0')


class MainWindow(CusQWidget, Ui_CusRecordView):
    """ 主窗口 -- 今日笔记列表"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.edit_views = {}  # 已打开的编辑窗口
        self.load_rec_list()
        self.regMsgBus()
        self.spdBall = None
        self.setTray()
        self.setRightMenu()
        self.setAttribute(Qt.WA_DeleteOnClose, False)  # 主窗体 不销毁

    def regMsgBus(self):
        CusMsgBus.append('load_rec_list', self)
        CusMsgBus.append('openEditor', self)
        CusMsgBus.append('closeEditor', self)
        CusMsgBus.append('updateEditorId', self)
        CusMsgBus.append('showView', self)
        CusMsgBus.append('closeSball', self)

    def unRegMsgBus(self):
        CusMsgBus.quit('load_rec_list', self)
        CusMsgBus.quit('openEditor', self)
        CusMsgBus.quit('closeEditor', self)
        CusMsgBus.quit('updateEditorId', self)
        CusMsgBus.quit('showView', self)
        CusMsgBus.quit('closeSball', self)

    def showView(self):
        self.showNormal()
        self.activateWindow()
        self.show()

    def setRightMenu(self):
        self.recListWidget.contextMenuEvent = self.viewListMenu

    def viewListMenu(self, event) -> None:
        menu = QMenu(self)
        menu.setObjectName("viewRightMenu")
        reloadAction = QAction(self.style().standardIcon(QStyle.SP_BrowserReload), '刷新')
        reloadAction.setObjectName('reloadAction')
        reloadAction.setParent(menu)
        reloadAction.triggered.connect(self.load_rec_list)
        qa = QAction()
        qa.setSeparator(True)
        addAction = QAction(self.style().standardIcon(QStyle.SP_FileIcon), '新增')
        addAction.setObjectName('addAction')
        addAction.setParent(menu)
        addAction.triggered.connect(self.on_btnAddRecord_clicked)

        menu.addAction(reloadAction)
        menu.addAction(qa)
        menu.addAction(addAction)
        menu.exec(QCursor.pos())

    def setTray(self):
        # 托盘图标

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayRMenu())
        self.trayIcon.setIcon(QIcon(":/resource/images/note.ico"))
        self.trayIcon.setToolTip('今日记事')
        self.trayIcon.activated.connect(self.trayClicked)
        self.trayIcon.show()

    def trayRMenu(self):

        trayMmenu = QMenu(self)

        addAction = QAction(self.style().standardIcon(QStyle.SP_FileIcon), '新增')
        addAction.setParent(trayMmenu)
        addAction.triggered.connect(self.on_btnAddRecord_clicked)

        sBallAction = QAction(self.style().standardIcon(QStyle.SP_DialogYesButton), '打开悬浮球')
        sBallAction.setParent(trayMmenu)
        # sBallAction.triggered.connect(self.showSball)

        quitAction = QAction(self.style().standardIcon(QStyle.SP_BrowserStop), '退出')
        quitAction.setParent(trayMmenu)
        quitAction.triggered.connect(self.quitApp)

        trayMmenu.addAction(addAction)
        trayMmenu.addAction(sBallAction)
        trayMmenu.addAction(quitAction)
        return trayMmenu

    def trayClicked(self, re: QSystemTrayIcon.ActivationReason):
        if re == re.Trigger:  # 点击托盘图标时触发
            self.showView()
        elif re == re.Context:  # 刷新菜单状态
            isbs = not hasattr(self, 'spdBall') or self.spdBall is None or self.spdBall.isHidden()
            if isbs:
                act = self.trayIcon.contextMenu().actions()[1]
                act.setText('打开悬浮球')
                act.setIcon(self.style().standardIcon(QStyle.SP_DialogYesButton))
                act.triggered.disconnect()
                act.triggered.connect(self.showSball)
            else:
                act = self.trayIcon.contextMenu().actions()[1]
                act.setText('关闭悬浮球')
                act.setIcon(self.style().standardIcon(QStyle.SP_DialogNoButton))
                act.triggered.disconnect()
                act.triggered.connect(self.closeSball)

    def load_rec_list(self):
        """加载列表"""
        res = DBManager.getDayNotes()
        self.recListWidget.clear()
        for r in res:
            rlabel = CusRecordLabel(r[0])
            rlabel.rcon = r[1]
            rlabel.rtime = r[2]
            newItem = QListWidgetItem()
            newItem.setSizeHint(rlabel.sizeHint())
            self.recListWidget.addItem(newItem)
            self.recListWidget.setItemWidget(newItem, rlabel)

    def openEditor(self, rid=0):
        """ 打开编辑窗口 并加入列表 如已有打开重新显示"""
        eview = self.edit_views.get(rid, None)
        if eview is None:
            eview = self.edit_views.setdefault(rid, CusNoteEdit(rid))
        eview.hide()
        eview.show()

    def updateEditorId(self, oldRid, newRid):
        """ 编辑窗口更新自己rid时 更新列表中自己主键"""
        self.edit_views.setdefault(newRid, self.edit_views.pop(oldRid, None))

    def closeEditor(self, rid=0):
        eview = self.edit_views.pop(rid, None)
        if eview:
            eview.close()

    @Slot()
    def on_btnAddRecord_clicked(self):
        self.openEditor(0)

    @Slot()
    def on_btnExit_clicked(self):
        global default_close_flag
        res = (-1, 0)
        if default_close_flag == '0':
            res = VDialog.doSomething(VDialogType.Choose, '关闭', "是否关闭程序", "记住我的选择", "退出程序", "最小化至托盘")
            if res[0] == -1:
                return
            if res[1]:
                default_close_flag = '1' if res[0] else '2'
                update_conf('base', 'default_close_flag', default_close_flag)
        if default_close_flag == '1' or (res and res[0] == 1):
            self.quitApp()
        else:
            self.close()
            if default_sball_flag == '2':
                self.showSball()

    @Slot()
    def on_btnOther_clicked(self):
        CusNoteList().show()

    def showSball(self):
        global default_sball_flag
        res = (-1, 0)
        if default_sball_flag == '0' or default_sball_flag == '3':
            res = VDialog.doSomething(VDialogType.Choose, '悬浮球', "是否在最小化至托盘时开启悬浮球", "记住我的选择", "手动开启", "最小化时开启")
            if res[0] == -1:
                return
            if res[1]:
                default_sball_flag = '1' if res[0] else '2'
                update_conf('base', 'default_sball_flag', default_sball_flag)
        if default_sball_flag == '1' or default_sball_flag == '2' or res[0] != -1:
            if not hasattr(self, 'spdBall') or self.spdBall is None :
                self.spdBall = CusSuspendBall()
            self.spdBall.show()

    def closeSball(self):
        self.spdBall.close()
        del self.spdBall

    def quitApp(self):
        QApplication.quit()
        QCoreApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
