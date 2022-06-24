# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusTagsChoose.ui'
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
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QToolBox,
    QVBoxLayout, QWidget)

class Ui_CusTagList(object):
    def setupUi(self, CusTagList):
        if not CusTagList.objectName():
            CusTagList.setObjectName(u"CusTagList")
        CusTagList.resize(120, 170)
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
        self.verticalSpacer = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnAddNew = QPushButton(self.bFrame)
        self.btnAddNew.setObjectName(u"btnAddNew")
        self.btnAddNew.setMinimumSize(QSize(0, 20))
        self.btnAddNew.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.btnAddNew)

        self.verticalSpacer_4 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolBox = QToolBox(self.bFrame)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBoxButton{\n"
"	min-height:18px;\n"
"}")
        self.cpage = QWidget()
        self.cpage.setObjectName(u"cpage")
        self.cpage.setGeometry(QRect(0, 0, 114, 95))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpage.sizePolicy().hasHeightForWidth())
        self.cpage.setSizePolicy(sizePolicy)
        self.cpage.setMinimumSize(QSize(0, 0))
        self.cpage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.cpage)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.lvCus = QListWidget(self.cpage)
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

        self.verticalLayout_4.addWidget(self.lvCus)

        self.toolBox.addItem(self.cpage, u"\u5e38\u7528\u6807\u7b7e")
        self.spage = QWidget()
        self.spage.setObjectName(u"spage")
        self.spage.setGeometry(QRect(0, 0, 114, 75))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spage.sizePolicy().hasHeightForWidth())
        self.spage.setSizePolicy(sizePolicy1)
        self.spage.setStyleSheet(u"QPushButton{\n"
"	max-height:15px;\n"
"	padding:0px;\n"
"	margin:0px;\n"
"}\n"
"QLabel{\n"
"border-radius: 7px;\n"
"}\n"
"#hf1 QLabel{\n"
"background-color: rgb(251, 251, 219);\n"
"border:1px solid rgba(255, 255, 127, 160);\n"
"}\n"
"\n"
"#hf2 QLabel{\n"
"background-color: rgb(255, 227, 183);\n"
"border:1px solid rgba(255, 200, 144, 160);\n"
"}\n"
"#hf3 QLabel{\n"
"background-color: rgb(207, 207, 207);\n"
"border:1px solid rgba(170, 170, 170,160);\n"
"}\n"
"#hf4 QLabel{\n"
"background-color: rgb(94, 193, 143);\n"
"border:1px solid rgba(75, 175, 125, 160);\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.spage)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 1, 2, 0)
        self.hf1 = QFrame(self.spage)
        self.hf1.setObjectName(u"hf1")
        self.hl1 = QHBoxLayout(self.hf1)
        self.hl1.setSpacing(0)
        self.hl1.setObjectName(u"hl1")
        self.hl1.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.hf1)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(15, 15))
        self.label.setMaximumSize(QSize(15, 15))

        self.hl1.addWidget(self.label)

        self.btnTD = QPushButton(self.hf1)
        self.btnTD.setObjectName(u"btnTD")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnTD.sizePolicy().hasHeightForWidth())
        self.btnTD.setSizePolicy(sizePolicy3)
        self.btnTD.setStyleSheet(u"")

        self.hl1.addWidget(self.btnTD)


        self.verticalLayout_5.addWidget(self.hf1)

        self.hf2 = QFrame(self.spage)
        self.hf2.setObjectName(u"hf2")
        self.hl2 = QHBoxLayout(self.hf2)
        self.hl2.setSpacing(0)
        self.hl2.setObjectName(u"hl2")
        self.hl2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.hf2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(15, 15))
        self.label_2.setMaximumSize(QSize(15, 15))

        self.hl2.addWidget(self.label_2)

        self.btnTDS = QPushButton(self.hf2)
        self.btnTDS.setObjectName(u"btnTDS")
        sizePolicy3.setHeightForWidth(self.btnTDS.sizePolicy().hasHeightForWidth())
        self.btnTDS.setSizePolicy(sizePolicy3)
        self.btnTDS.setStyleSheet(u"")

        self.hl2.addWidget(self.btnTDS)


        self.verticalLayout_5.addWidget(self.hf2)

        self.hf3 = QFrame(self.spage)
        self.hf3.setObjectName(u"hf3")
        self.hl3 = QHBoxLayout(self.hf3)
        self.hl3.setSpacing(0)
        self.hl3.setObjectName(u"hl3")
        self.hl3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.hf3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(15, 15))
        self.label_3.setMaximumSize(QSize(15, 15))

        self.hl3.addWidget(self.label_3)

        self.btnCancel = QPushButton(self.hf3)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy3.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy3)
        self.btnCancel.setStyleSheet(u"")

        self.hl3.addWidget(self.btnCancel)


        self.verticalLayout_5.addWidget(self.hf3)

        self.hf4 = QFrame(self.spage)
        self.hf4.setObjectName(u"hf4")
        self.hl4 = QHBoxLayout(self.hf4)
        self.hl4.setSpacing(0)
        self.hl4.setObjectName(u"hl4")
        self.hl4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.hf4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(15, 15))
        self.label_4.setMaximumSize(QSize(15, 15))

        self.hl4.addWidget(self.label_4)

        self.btnDone = QPushButton(self.hf4)
        self.btnDone.setObjectName(u"btnDone")
        sizePolicy3.setHeightForWidth(self.btnDone.sizePolicy().hasHeightForWidth())
        self.btnDone.setSizePolicy(sizePolicy3)
        self.btnDone.setStyleSheet(u"")

        self.hl4.addWidget(self.btnDone)


        self.verticalLayout_5.addWidget(self.hf4)

        self.toolBox.addItem(self.spage, u"\u7279\u6b8a\u6807\u7b7e")

        self.verticalLayout_2.addWidget(self.toolBox)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addWidget(self.bFrame, 0, 0, 1, 1)


        self.retranslateUi(CusTagList)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(1)


        QMetaObject.connectSlotsByName(CusTagList)
    # setupUi

    def retranslateUi(self, CusTagList):
        CusTagList.setWindowTitle(QCoreApplication.translate("CusTagList", u"\u6807\u7b7e\u5217\u8868", None))
        self.btnAddNew.setText(QCoreApplication.translate("CusTagList", u"+ \u65b0\u589e\u6807\u7b7e", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.cpage), QCoreApplication.translate("CusTagList", u"\u5e38\u7528\u6807\u7b7e", None))
        self.label.setText("")
        self.btnTD.setText(QCoreApplication.translate("CusTagList", u"\u5f85\u529e", None))
        self.label_2.setText("")
        self.btnTDS.setText(QCoreApplication.translate("CusTagList", u"\u5f85\u529eS", None))
        self.label_3.setText("")
        self.btnCancel.setText(QCoreApplication.translate("CusTagList", u"\u53d6\u6d88", None))
        self.label_4.setText("")
        self.btnDone.setText(QCoreApplication.translate("CusTagList", u"\u5b8c\u6210", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.spage), QCoreApplication.translate("CusTagList", u"\u7279\u6b8a\u6807\u7b7e", None))
    # retranslateUi

