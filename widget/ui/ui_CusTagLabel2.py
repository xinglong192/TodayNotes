# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusTagLabel2.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel,
                               QSizePolicy)

class Ui_CusTagLabel(object):
    def setupUi(self, CusTagLabel):
        if not CusTagLabel.objectName():
            CusTagLabel.setObjectName(u"CusTagLabel")
        CusTagLabel.resize(322, 300)
        CusTagLabel.setMouseTracking(False)
        CusTagLabel.setStyleSheet(u"#rightMenu{\n"
"padding:0px;\n"
"height:20px;\n"
"width:60px;\n"
"}\n"
"#rightMenu::item{\n"
"font:10px;\n"
"height:17px;\n"
"width:58px;\n"
"padding-top:0px;\n"
"padding-bottom:1px;\n"
"margin:1px;\n"
"background-color: rgba(214, 214, 214,0.7);\n"
"}\n"
"#rightMenu::item:selected{\n"
"	color:white;\n"
"	background-color: rgba(63, 127, 190,0.5);\n"
"}")
        self.gridLayout_2 = QGridLayout(CusTagLabel)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridFrame = QFrame(CusTagLabel)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setMouseTracking(True)
        self.gridFrame.setStyleSheet(u"#gridFrame:hover{\n"
"	border:1px outset rgba(210, 228, 255,0.5);\n"
"	border-left:1px solid rgb(85, 170, 127);\n"
"}	")
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.gridFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(5, 3))
        self.frame.setMaximumSize(QSize(5, 3))
        self.frame.setMouseTracking(False)
        self.frame.setFrameShape(QFrame.VLine)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(2)

        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.labelTagText = QLabel(self.gridFrame)
        self.labelTagText.setObjectName(u"labelTagText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelTagText.sizePolicy().hasHeightForWidth())
        self.labelTagText.setSizePolicy(sizePolicy1)
        self.labelTagText.setMouseTracking(False)
        self.labelTagText.setStyleSheet(u"")
        self.labelTagText.setMargin(0)

        self.gridLayout.addWidget(self.labelTagText, 0, 1, 5, 1)


        self.gridLayout_2.addWidget(self.gridFrame, 0, 1, 1, 1)


        self.retranslateUi(CusTagLabel)

        QMetaObject.connectSlotsByName(CusTagLabel)
    # setupUi

    def retranslateUi(self, CusTagLabel):
        CusTagLabel.setWindowTitle(QCoreApplication.translate("CusTagLabel", u"\u6807\u7b7e", None))
        self.labelTagText.setText(QCoreApplication.translate("CusTagLabel", u"TextLabel", None))
    # retranslateUi

