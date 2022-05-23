# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusRecordView.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import images_rc

class Ui_CusRecordView(object):
    def setupUi(self, CusRecordView):
        if not CusRecordView.objectName():
            CusRecordView.setObjectName(u"CusRecordView")
        CusRecordView.resize(200, 300)
        CusRecordView.setMouseTracking(False)
        CusRecordView.setTabletTracking(False)
        icon = QIcon()
        icon.addFile(u":/resource/images/note.ico", QSize(), QIcon.Normal, QIcon.Off)
        CusRecordView.setWindowIcon(icon)
        self.gridLayout = QGridLayout(CusRecordView)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame = QFrame(CusRecordView)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 0, 0)
        self.btnAddRecord = QPushButton(self.horizontalFrame)
        self.btnAddRecord.setObjectName(u"btnAddRecord")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddRecord.sizePolicy().hasHeightForWidth())
        self.btnAddRecord.setSizePolicy(sizePolicy)
        self.btnAddRecord.setMaximumSize(QSize(30, 30))
        self.btnAddRecord.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setBold(True)
        self.btnAddRecord.setFont(font)
        self.btnAddRecord.setIconSize(QSize(10, 10))

        self.horizontalLayout.addWidget(self.btnAddRecord)

        self.spacerTopBar = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spacerTopBar)

        self.btnOther = QPushButton(self.horizontalFrame)
        self.btnOther.setObjectName(u"btnOther")
        sizePolicy.setHeightForWidth(self.btnOther.sizePolicy().hasHeightForWidth())
        self.btnOther.setSizePolicy(sizePolicy)
        self.btnOther.setMaximumSize(QSize(30, 16777215))
        self.btnOther.setFont(font)
        self.btnOther.setIconSize(QSize(10, 11))

        self.horizontalLayout.addWidget(self.btnOther)

        self.btnExit = QPushButton(self.horizontalFrame)
        self.btnExit.setObjectName(u"btnExit")
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setMaximumSize(QSize(30, 16777215))
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet(u"#btnExit:hover{\n"
"	color:white;\n"
"	background-color: rgba(208, 0, 0,0.8);\n"
"	border-radius:3px;\n"
"}")

        self.horizontalLayout.addWidget(self.btnExit)


        self.gridLayout.addWidget(self.horizontalFrame, 0, 0, 1, 1)

        self.frameRecordList = QFrame(CusRecordView)
        self.frameRecordList.setObjectName(u"frameRecordList")
        self.frameRecordList.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.frameRecordList)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 2, 0, 2)
        self.boxRecList = QVBoxLayout()
        self.boxRecList.setSpacing(10)
        self.boxRecList.setObjectName(u"boxRecList")
        self.recListWidget = QListWidget(self.frameRecordList)
        self.recListWidget.setObjectName(u"recListWidget")
        self.recListWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.recListWidget.setStyleSheet(u"QListWidget  QScrollBar{\n"
"	width:8px;\n"
"    border: none;\n"
"    background-color: rgba(40, 81, 121,0.2);\n"
"}")
        self.recListWidget.setAutoScrollMargin(2)
        self.recListWidget.setProperty("showDropIndicator", False)
        self.recListWidget.setSpacing(6)

        self.boxRecList.addWidget(self.recListWidget)


        self.verticalLayout.addLayout(self.boxRecList)


        self.gridLayout.addWidget(self.frameRecordList, 1, 0, 1, 1)


        self.retranslateUi(CusRecordView)

        QMetaObject.connectSlotsByName(CusRecordView)
    # setupUi

    def retranslateUi(self, CusRecordView):
        CusRecordView.setWindowTitle(QCoreApplication.translate("CusRecordView", u"\u4eca\u65e5\u8bb0\u4e8b", None))
#if QT_CONFIG(tooltip)
        self.btnAddRecord.setToolTip(QCoreApplication.translate("CusRecordView", u"\u6dfb\u52a0\u7b14\u8bb0", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddRecord.setText(QCoreApplication.translate("CusRecordView", u"+", None))
#if QT_CONFIG(tooltip)
        self.btnOther.setToolTip(QCoreApplication.translate("CusRecordView", u"\u67e5\u770b\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.btnOther.setText(QCoreApplication.translate("CusRecordView", u"...", None))
#if QT_CONFIG(tooltip)
        self.btnExit.setToolTip(QCoreApplication.translate("CusRecordView", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.btnExit.setText(QCoreApplication.translate("CusRecordView", u"x", None))
#if QT_CONFIG(tooltip)
        self.recListWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
    # retranslateUi

