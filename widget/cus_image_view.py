from PySide6.QtCore import QRect, QPoint, QSize
from PySide6.QtGui import QImage, QPixmap, QWheelEvent, QMouseEvent, QPainter, QPaintEvent, Qt
from PySide6.QtWidgets import QMainWindow

from widget.ui.ui_CusImageView import Ui_CusImageView


class CusImageView(QMainWindow, Ui_CusImageView):
    """ 图片预览窗口 """

    def __init__(self, parent=None, title='预览'):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.imgWidth = 0  # 当前图片宽度
        self.imgHeight = 0  # 当前图片高度
        self.imgpos = QPoint(0, 0)  # 当前图片左上角点
        self.imgData = None  # 当前图片QImage
        self.scaleVal = 1  # 缩放倍数

        self.setupUi(self)
        self.setWindowTitle(title)
        self.LabImage.wheelEvent = self.imgWheelEvent
        self.LabImage.paintEvent = self.imgLabelPaint
        self.LabImage.mousePressEvent = self.areamousePress
        self.LabImage.mouseReleaseEvent = self.areamouseRelease
        self.LabImage.mouseMoveEvent = self.areaMoveEvent

    def resizeEvent(self, event) -> None:
        if event.oldSize().width() > 1:
            self.reSizeImage(
                min(event.size().width() / event.oldSize().width(), event.size().height() / event.oldSize().height()),
                QPoint(0, 0))
        super(CusImageView, self).resizeEvent(event)

    def setLabelImage(self, image: QImage, suffix='png'):
        self.imgData = image
        w = self.width()
        h = self.height()
        c = max(image.width() / w, image.height() / h)
        self.scaleVal = 1 / c
        self.imgWidth, self.imgHeight = image.width() * self.scaleVal, image.height() * self.scaleVal
        self.imgpos.setX((w - self.imgWidth) / 2)
        self.imgpos.setY((h - self.imgHeight) / 2)
        self.LabImage.update()

    def areamousePress(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.LabImage.setCursor(Qt.ClosedHandCursor)
            self.start_point = event.globalPosition().toPoint() - self.LabImage.pos()

    def areamouseRelease(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.LabImage.setCursor(Qt.OpenHandCursor)

    def areaMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton:
            relpos = event.globalPosition().toPoint() - self.start_point
            oldPos = QPoint(self.imgpos)
            if self.imgWidth > self.width():
                x = min(0, self.imgpos.x() + relpos.x())
                self.imgpos.setX(max(x, self.width() - self.imgWidth) if x else self.imgpos.x())
            if self.imgHeight > self.height():
                y = min(0, self.imgpos.y() + relpos.y())
                self.imgpos.setY(max(y, self.height() - self.imgHeight) if y else self.imgpos.y())

            self.start_point = event.globalPosition().toPoint()
            if oldPos != self.imgpos:
                self.LabImage.update()

    def imgLabelPaint(self, event: QPaintEvent) -> None:
        # 重写label的paint事件
        painter = QPainter(self.LabImage)
        painter.setRenderHint(QPainter.Antialiasing, True)
        pp = QPixmap.fromImage(self.imgData)
        pp = pp.scaled(self.imgWidth, self.imgHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        painter.drawPixmap(QRect(self.imgpos, QSize(self.imgWidth, self.imgHeight)), pp)

    def imgWheelEvent(self, event: QWheelEvent):
        """ 滚轮缩放事件 """
        f = 1.1 if event.angleDelta().y() > 0 else 1 / 1.1
        self.reSizeImage(f, event.position())
        event.accept()

    def reSizeImage(self, f, point: QPoint):
        oldSclVal = self.scaleVal
        self.scaleVal *= f
        if self.scaleVal > 6:
            self.scaleVal = 6
        self.imgWidth, self.imgHeight = self.imgData.width() * self.scaleVal, self.imgData.height() * self.scaleVal

        # 图片大小不能小于窗口大小
        if self.imgWidth < self.width() and self.imgHeight < self.height():
            c = max(self.imgData.width() / self.width(), self.imgData.height() / self.height())
            self.scaleVal = 1 / c
            self.imgWidth, self.imgHeight = self.imgData.width() * self.scaleVal, self.imgData.height() * self.scaleVal

        if self.imgWidth < self.width():  # 小于窗口大小，居中
            self.imgpos.setX((self.width() - self.imgWidth) / 2)
        else:
            # 定位鼠标
            dx = (self.imgpos.x() - point.x()) * ((self.scaleVal / oldSclVal) - 1)
            self.imgpos.setX(self.imgpos.x() + dx)
            if self.imgpos.x() > 0:
                self.imgpos.setX(0)
            elif self.imgpos.x() < self.width() - self.imgWidth:
                self.imgpos.setX(max(self.imgpos.x(), self.width() - self.imgWidth))

        if self.imgHeight < self.height():
            self.imgpos.setY((self.height() - self.imgHeight) / 2)
        else:
            dy = (self.imgpos.y() - point.y()) * ((self.scaleVal / oldSclVal) - 1)
            self.imgpos.setY(self.imgpos.y() + dy)
            if self.imgpos.y() > 0:
                self.imgpos.setY(0)
            elif self.imgpos.y() < self.height() - self.imgHeight:
                self.imgpos.setY(max(self.imgpos.y(), self.height() - self.imgHeight))

        # if oldSclVal != self.scaleVal:
        self.LabImage.update()

    def closeEvent(self, event) -> None:
        self.LabImage.wheelEvent = None
        self.LabImage.paintEvent = None
        self.LabImage.mousePressEvent = None
        self.LabImage.mouseReleaseEvent = None
        self.LabImage.mouseMoveEvent = None
        super(CusImageView, self).closeEvent(event)
