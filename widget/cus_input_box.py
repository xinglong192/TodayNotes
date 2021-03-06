from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QDialog

from widget.ui.ui_CusInputBox import Ui_CusInputBox


class CusInputBox(QDialog, Ui_CusInputBox):
    __cur_box = None

    def __init__(self, tf=False, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ismoving = False
        self.setupUi(self)
        self.labeText.hide()
        if not tf:
            self.setWindowFlags(Qt.CustomizeWindowHint)
        self.res = ()

    @Slot()
    def on_btnConfirm_clicked(self):
        self.res = (self.lineInput.text(), True)
        self.accept()

    @Slot()
    def on_btnCancel_clicked(self):
        self.res = ('', False)
        self.reject()

    @staticmethod
    def getText(title=None, pht='请输入', parent=None, defVal=None, tipText=None):
        CusInputBox.__cur_box = CusInputBox(title, parent)
        if title:
            CusInputBox.__cur_box.setWindowTitle(title)
        if pht:
            CusInputBox.__cur_box.lineInput.setPlaceholderText(pht)
        if defVal:
            CusInputBox.__cur_box.lineInput.setText(defVal)
        if tipText:
            CusInputBox.__cur_box.labeText.setText(tipText)
            CusInputBox.__cur_box.labeText.show()
        CusInputBox.__cur_box.exec()
        r = CusInputBox.__cur_box.res
        CusInputBox.__cur_box = None
        return r

    def mousePressEvent(self, e: QMouseEvent) -> None:
        """ 拖动窗口 """
        if e.button() == Qt.LeftButton:
            self.start_point = e.globalPosition().toPoint() - self.pos()
            # if self.start_point.y() > 30:
            #     return
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
