from enum import Enum

from PySide6.QtWidgets import QMessageBox, QCheckBox


class VDialogType(Enum):
    Error = -1
    Default = 0
    Warning = 1
    Question = 2
    Choose = 3
    OTHER = 9


class VDialog:

    @staticmethod
    def doSomething(type: VDialogType = VDialogType.Default, *args: any) -> any:
        """ 提示用户 """
        # TODO 添加具体提示方式
        #print('vd-dosomthing:', args)
        match type:
            case VDialogType.Question:
                mb = QMessageBox.question(args[0], args[1], args[2])
                if mb == QMessageBox.StandardButton.No:
                    return False
                return True
            case VDialogType.Error:
                QMessageBox.critical(None, '错误', args[0])
            case VDialogType.Warning:
                QMessageBox.warning(None, '提示', args[0])
            case VDialogType.Choose:
                mb = QMessageBox()
                mb.setIcon(QMessageBox.Question)
                mb.setWindowTitle(args[0])
                mb.setText(args[1])
                cb = QCheckBox(args[2], mb)
                mb.setCheckBox(cb)

                cancel = mb.addButton('取消', QMessageBox.RejectRole)
                yb = mb.addButton(args[3], QMessageBox.YesRole)
                nb = mb.addButton(args[4], QMessageBox.NoRole)
                mb.setDefaultButton(nb)

                mb.exec()
                if mb.clickedButton() == yb:
                    return 1, cb.isChecked()
                if mb.clickedButton() == nb:
                    return 0, cb.isChecked()
                else:
                    return -1, False
        return None
