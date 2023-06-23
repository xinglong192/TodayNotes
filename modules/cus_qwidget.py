from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QGuiApplication, QContextMenuEvent, QAction, QCursor
from PySide6.QtWidgets import QWidget, QMenu, QStyle


class CusQWidget(QWidget):
    """ 实现窗口拖动"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ismoving = False
        self.start_point = 0

    def mousePressEvent(self, e: QMouseEvent) -> None:
        """ 拖动窗口 """
        if e.button() == Qt.LeftButton:
            self.start_point = e.globalPosition().toPoint() - self.pos()
            if self.start_point.y() > 30:
                return
            self.ismoving = True
        e.accept()

    def mouseMoveEvent(self, e: QMouseEvent):
        if self.ismoving:
            relpos = e.globalPosition().toPoint() - self.start_point
            self.move(relpos)
        e.accept()

    def mouseReleaseEvent(self, e: QMouseEvent):

        self.ismoving = False
        e.accept()

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        """ 用于顶部栏 右键菜单"""
        print('-==-=-=-=--=-=menu')
        menu = QMenu(self)
        menu.setObjectName("topRightMenu")
        windowAction = QAction(
            self.style().standardIcon(QStyle.SP_TitleBarShadeButton), "置顶窗口")
        if self.windowFlags() & Qt.WindowStaysOnTopHint:
            windowAction.setIcon(self.style().standardIcon(QStyle.SP_TitleBarCloseButton))
            windowAction.setText('取消置顶')
        windowAction.setObjectName('windowAction')
        windowAction.setParent(menu)
        windowAction.triggered.connect(self.changeWindowTopStatus)
        menu.addAction(windowAction)
        menu.exec(QCursor.pos())

    def changeWindowTopStatus(self):
        if self.windowFlags() & Qt.WindowStaysOnTopHint:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, False)
        else:
            self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.show()
