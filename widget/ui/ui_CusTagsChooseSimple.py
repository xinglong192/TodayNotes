# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusTagsChooseSimple.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_CusTagList(object):
    def setupUi(self, CusTagList):
        if not CusTagList.objectName():
            CusTagList.setObjectName(u"CusTagList")
        CusTagList.resize(107, 156)
        self.gridLayout = QGridLayout(CusTagList)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bFrame = QFrame(CusTagList)
        self.bFrame.setObjectName(u"bFrame")
        self.bFrame.setStyleSheet(u"#bFrame{\n"
"background-color: rgba(221, 221, 221, 180);\n"
"border:2px inset rgba(175, 175, 175, 180);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.bFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnAddNew = QPushButton(self.bFrame)
        self.btnAddNew.setObjectName(u"btnAddNew")
        self.btnAddNew.setMinimumSize(QSize(0, 20))
        self.btnAddNew.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.btnAddNew)

        self.label = QLabel(self.bFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lvCus = QListWidget(self.bFrame)
        self.lvCus.setObjectName(u"lvCus")
        self.lvCus.setStyleSheet(u"#lvCus::item{\n"
"	border:1px solid rgba(40, 81, 121,0.5);\n"
"	margin:1px;\n"
"}\n"
"#lvCus::item:hover{\n"
"	border:1px solid rgba(40, 81, 160,0.3);\n"
"	background-color: rgba(179, 213, 255, 100);\n"
"	margin:1px;\n"
"}\n"
"#lvCus::item:selected:active{\n"
"	border:1px inset rgba(126, 199, 255, 100);\n"
"	\n"
"	color: rgba(0, 0, 0, 150);\n"
"	background-color: rgba(125, 170, 165, 100);\n"
"	margin:1px;\n"
"}\n"
"#lvCus QScrollBar{\n"
"	width:2px;\n"
"    border: none;\n"
"    background-color: rgba(85, 170, 127,0.6);\n"
"}")
        self.lvCus.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lvCus.setDefaultDropAction(Qt.IgnoreAction)

        self.verticalLayout.addWidget(self.lvCus)


        self.gridLayout.addWidget(self.bFrame, 0, 0, 1, 1)


        self.retranslateUi(CusTagList)

        QMetaObject.connectSlotsByName(CusTagList)
    # setupUi

    def retranslateUi(self, CusTagList):
        CusTagList.setWindowTitle(QCoreApplication.translate("CusTagList", u"\u6807\u7b7e\u9009\u62e9", None))
        self.btnAddNew.setText(QCoreApplication.translate("CusTagList", u"+ \u65b0\u589e\u6807\u7b7e", None))
        self.label.setText(QCoreApplication.translate("CusTagList", u"\u5e38\u7528\u6807\u7b7e", None))
    # retranslateUi

