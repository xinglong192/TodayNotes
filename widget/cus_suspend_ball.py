import sys

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QPaintEvent, QPainter, QColor, QPen, QPainterPath, QBrush, QMouseEvent, \
    QGuiApplication, QContextMenuEvent, QAction, QCursor, QEnterEvent
from PySide6.QtWidgets import QWidget, QApplication, QMenu, QStyle

from modules.cus_msg_bus import CusMsgBus


class CusSuspendBall(QWidget):
    """ 桌面悬浮球窗体 """

    def __init__(self):
        super().__init__()

        self.showOnce = False
        self.setWindowTitle('今日记事')
        self.sx = 43  # 圆心定位x
        self.sy = 43  # 圆心定位y
        self.scr = 0.5  # 缩放比例 scale.x=scale.y 等比缩放
        self.isLeave = False  # 是否失去鼠标位置，用于检查是否呼出右键菜单
        self.ballRMen()  # 创建右键菜单
        self.isLPress = False  # 是否点击过左键
        self.isMoving = False  # 是否点击左键 后移动过鼠标
        self.overAdd = False  # 鼠标是否在新增按钮上
        self.overPoints = False  # 鼠标是否在查看按钮上
        self.isOverSide = False  # 是否贴边
        self.rc = 25  # 方块边长
        self.sds = 5  # 贴边检测距离
        self.setFixedSize(int(130 * self.scr), int(86 * self.scr))  # 重置窗体大小
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setMouseTracking(True)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.scale(self.scr, self.scr)
        painter.setRenderHint(QPainter.Antialiasing, True)
        if self.isOverSide and not self.showOnce:  # 吸边图形
            cpx = int(self.rc * self.scr)
            if self.x() < cpx - self.width():
                self.move(cpx - self.width(), self.y())
            cpy = int(self.rc * self.scr)
            if self.y() < cpy - self.height():
                self.move(self.x(), cpy - self.height())
            self.drawSideShape(painter)
            return
        if self.isOverSide:
            screen = QGuiApplication.primaryScreen().availableGeometry()
            x = max(self.x(), int(-18 * self.scr))
            y = max(self.y(), int(-20 * self.scr))
            if x > screen.width() - self.width():  # 因为不规则图形改变可能脱离鼠标范围，所以减少部分移动
                x = screen.width() - self.width() + 15 * self.scr
            if y > screen.height() - self.height():
                y = screen.height() - self.height() + 20 * self.scr
            self.move(x, y)
        # painter.drawRect(55, 55, 155, 90)
        # start 绘制多边形
        lshape1 = QPainterPath()
        cr = 40  # 左圆半径
        sx = self.sx  # 圆心x
        sy = self.sy  # 圆心y

        sp = QPointF(sx - cr, sy)
        # 左下半圆
        lshape1.moveTo(sp)  # 移动画笔至圆上
        rf1 = QRectF(sx - cr, sy - cr, cr << 1, cr << 1)
        cag = 48  # 角度
        lshape1.arcTo(rf1, 180, 90 + cag)
        # 绘制向右直线
        lle = 30
        lshape1.lineTo(lshape1.currentPosition().x() + lle, lshape1.currentPosition().y())
        # 绘制逆时针180的右半圆
        rr2 = lshape1.currentPosition().y() - sy
        rf2 = QRectF(lshape1.currentPosition().x() - rr2, lshape1.currentPosition().y() - rr2 * 2, rr2 * 2, rr2 * 2)
        lshape1.arcTo(rf2, 270, 180)
        # 绘制向左的直线
        lshape1.lineTo(lshape1.currentPosition().x() - lle, lshape1.currentPosition().y())
        # 绘制左部上半圆
        lshape1.arcTo(rf1, 90 - cag, 90 + cag)
        lshape1.closeSubpath()
        # end 绘制多边形

        painter.setPen(QPen(QColor(14, 98, 81, 150), 2))
        painter.setBrush(QBrush(Qt.darkCyan))
        painter.drawPath(lshape1)

        qppoint = QPen(QColor(215, 215, 215), 5)

        if self.overPoints:
            qppoint = QPen(QColor(240, 250, 255), 8)
        qppoint.setCapStyle(Qt.RoundCap)
        painter.setPen(qppoint)
        p = QPointF(sx, sy)
        painter.drawPoint(p.x() + 46, p.y() + 1)
        painter.drawPoint(p.x() + 56, p.y() + 1)
        painter.drawPoint(p.x() + 66, p.y() + 1)

        qpAdd = QPen(QColor(215, 215, 215), 3)

        if self.overAdd:
            qpAdd = QPen(QColor(240, 250, 255), 5)
        qpAdd.setCapStyle(Qt.RoundCap)
        painter.setPen(qpAdd)
        painter.drawLine(p.x() - 20, p.y(), p.x() + 20, p.y())
        painter.drawLine(p.x(), p.y() - 20, p.x(), p.y() + 20)

    def drawSideShape(self, painter: QPainter):
        """ 悬浮球 贴屏幕边时 图形 """
        painter.setPen(QPen(QColor(120, 60, 0, 190), 3))
        painter.setBrush(QBrush(QColor(148, 74, 0)))
        screen = QGuiApplication.primaryScreen().availableGeometry()
        vx = 0  # 0 无/ 1 左边界 / 2 右边界
        vy = 0  # 0 无/ 1 上边界 / 2 下边界
        cpos = self.pos()
        ccx = cpos.x()
        ccy = cpos.y()
        if ccx <= self.sds:
            vx = 1
        elif ccx >= screen.width() - self.sds - self.width():
            vx = 2
        if ccy <= self.sds:
            vy = 1
        elif ccy >= screen.height() - self.sds - self.height():
            vy = 2
        rx = self.width() // 2
        ry = self.height() // 2
        rc = self.rc
        rcs = 1.2  # 只右一个方块时膨胀倍数
        secr = True
        vsec = 0  # 0 向下/1 向右  绘制第二方块
        match (vx, vy):
            case (1, 0):
                rx = abs(0 - ccx) if ccx <= 0 else 0
            case (2, 0):
                px = screen.width() - ccx - rc * self.scr
                rx = 0 if px < 0 else px
            case (0, 1):
                ry = abs(0 - ccy) if ccy <= 0 else 0
                vsec = 1
            case (0, 2):
                py = screen.height() - ccy - rc * self.scr
                ry = 0 if py < 0 else py
                vsec = 1
            case (1, 1):
                rc = int(rc * rcs)
                rx = abs(0 - ccx) if ccx <= 0 else 0
                ry = abs(0 - ccy) if ccy <= 0 else 0
                secr = False
            case (2, 1):
                rc = int(rc * rcs)
                px = screen.width() - ccx - rc * self.scr
                rx = 0 if px < 0 else px
                ry = abs(0 - ccy) if ccy <= 0 else 0
                secr = False
            case (1, 2):
                rc = int(rc * rcs)
                rx = abs(0 - ccx) if ccx <= 0 else 0
                py = screen.height() - ccy - rc * self.scr
                ry = 0 if py < 0 else py
                secr = False
            case (2, 2):
                rc = int(rc * rcs)
                px = screen.width() - ccx - rc * self.scr
                rx = 0 if px < 0 else px
                py = screen.height() - ccy - rc * self.scr
                ry = 0 if py < 0 else py
                secr = False
        rx //= self.scr
        ry //= self.scr

        if secr:
            ccd = 0
            if vsec == 0:
                ccd = rc // 1.5  # 因为窗体高度不够，向上移动半个rc
            painter.drawRect(rx, ry - ccd, rc, rc)
            painter.drawRect(rx + (rc if vsec else 0), ry + (0 if vsec else rc) - ccd, rc, rc)
        else:
            painter.drawRect(rx, ry, rc, rc)

    def leaveEvent(self, event) -> None:
        self.isLeave = True
        self.isLPress = False
        self.isMoving = False
        if self.isOverSide and self.showOnce:
            self.update()
        self.showOnce = False

    def enterEvent(self, event: QEnterEvent) -> None:
        self.isLPress = False
        self.isLeave = False
        self.isMoving = False
        if self.isOverSide and not self.isLPress:
            self.showOnce = True
            self.update()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        """ 拖动窗口 """
        self.showOnce = False
        self.isLeave = False
        if e.button() == Qt.LeftButton:
            self.start_point = e.globalPosition().toPoint() - self.pos()
            self.isLPress = True

    def mouseMoveEvent(self, e: QMouseEvent):

        self.isLeave = False
        screen = QGuiApplication.primaryScreen().availableGeometry()
        cpos = self.pos()
        mpos = e.position()
        # 鼠标是否在左加号
        if 23 * self.scr <= mpos.x() <= 63 * self.scr and 23 * self.scr <= mpos.y() <= 63 * self.scr:
            if not self.overAdd:
                self.overAdd = True
                self.update()
        elif self.overAdd:
            self.overAdd = False
            self.update()
        # 鼠标是否在右[...]
        if 86 * self.scr <= mpos.x() <= 112 * self.scr and 33 * self.scr <= mpos.y() <= 53 * self.scr:
            if not self.overPoints:
                self.overPoints = True
                self.update()
        elif self.overPoints:
            self.overPoints = False
            self.update()
        rep = e.globalPosition().toPoint()
        rc = +self.rc * self.scr
        if self.isLPress:
            self.isMoving = True
            relpos = rep - self.start_point
            # XXX 超出范围不移动
            if screen.x() - self.width() + rc > QCursor.pos().x():
                QCursor.setPos(screen.x() - self.width() + rc, QCursor.pos().y())
            elif QCursor.pos().x() > screen.width() - rc:
                QCursor.setPos(screen.width() - rc - 1, QCursor.pos().y())
            if screen.y() - self.height() + rc > QCursor.pos().y():
                QCursor.setPos(QCursor.pos().x(), screen.y() - self.height() + rc + 1)
            if QCursor.pos().y() > screen.height() - rc:
                QCursor.setPos(QCursor.pos().x(), screen.height() - rc)
            self.move(relpos)

            if cpos.x() < self.sds or cpos.x() > screen.width() - self.width() - self.sds \
                    or cpos.y() < self.sds - 3 or cpos.y() > screen.height() - self.height() - self.sds:
                self.isOverSide = True
                self.update()

            elif self.isOverSide:
                self.isOverSide = False
                self.update()


    def mouseReleaseEvent(self, e: QMouseEvent):
        if self.isLPress and not self.isLeave:
            if self.isMoving:
                self.isMoving = False
            else:
                if self.overAdd:
                    self.addNote()
                elif self.overPoints:
                    self.openNoteList()
        self.isLPress = False
        self.isLeave = False
        self.isMoving = False

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        ball_menu = self.ballMenu
        ball_menu.exec(QCursor.pos())

    def ballRMen(self):
        ball_menu = QMenu(self)
        closeAction = QAction(self.style().standardIcon(QStyle.SP_TitleBarCloseButton), '关闭悬浮球')
        closeAction.setParent(ball_menu)
        closeAction.triggered.connect(self.quitSBall)

        quitAction = QAction(self.style().standardIcon(QStyle.SP_BrowserStop), '退出程序')
        quitAction.setParent(ball_menu)
        quitAction.triggered.connect(self.quitApp)

        addAction = QAction(self.style().standardIcon(QStyle.SP_FileIcon), '新增笔记')
        addAction.setParent(ball_menu)
        addAction.triggered.connect(self.addNote)

        listAction = QAction(self.style().standardIcon(QStyle.SP_FileDialogContentsView), '查看列表')
        listAction.setParent(ball_menu)
        listAction.triggered.connect(self.openNoteList)

        ball_menu.addAction(addAction)
        ball_menu.addAction(listAction)
        ball_menu.addAction(closeAction)
        ball_menu.addAction(quitAction)
        self.ballMenu = ball_menu

    def addNote(self):
        CusMsgBus.send('openEditor')

    def openNoteList(self):
        CusMsgBus.send('showView')

    def quitSBall(self):
        self.close()
        CusMsgBus.send('closeSball')

    def quitApp(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CusSuspendBall()
    window.show()
    sys.exit(app.exec())
