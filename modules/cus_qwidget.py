from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QGuiApplication
from PySide6.QtWidgets import QWidget


class CusQWidget(QWidget):
    """ 实现窗口拖动"""

    def __init__(self,parent=None):
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
