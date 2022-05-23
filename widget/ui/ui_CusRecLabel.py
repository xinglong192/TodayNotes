# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusRecLabel.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QVBoxLayout)

class Ui_frameRecLabel(object):
    def setupUi(self, frameRecLabel):
        if not frameRecLabel.objectName():
            frameRecLabel.setObjectName(u"frameRecLabel")
        frameRecLabel.resize(102, 38)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frameRecLabel.sizePolicy().hasHeightForWidth())
        frameRecLabel.setSizePolicy(sizePolicy)
        frameRecLabel.setMaximumSize(QSize(16777215, 70))
        frameRecLabel.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(frameRecLabel)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.framew = QFrame(frameRecLabel)
        self.framew.setObjectName(u"framew")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.framew.sizePolicy().hasHeightForWidth())
        self.framew.setSizePolicy(sizePolicy1)
        self.framew.setMaximumSize(QSize(16777215, 16777215))
        self.framew.setMouseTracking(True)
        self.framew.setStyleSheet(u"#framew{\n"
"border:2px inset gray;\n"
"border-left-color: rgba(40, 81, 121,0.5);\n"
"}\n"
"#framew:hover{\n"
" border:2px outset rgb(198, 229, 220);\n"
" border-left-color:rgb(73, 120, 100);\n"
"}")
        self.framew.setFrameShape(QFrame.StyledPanel)
        self.framew.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.framew)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameTime = QFrame(self.framew)
        self.frameTime.setObjectName(u"frameTime")
        sizePolicy.setHeightForWidth(self.frameTime.sizePolicy().hasHeightForWidth())
        self.frameTime.setSizePolicy(sizePolicy)
        self.frameTime.setMouseTracking(True)
        self.frameTime.setFrameShape(QFrame.StyledPanel)
        self.frameTime.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameTime)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTime = QLabel(self.frameTime)
        self.labelTime.setObjectName(u"labelTime")
        sizePolicy.setHeightForWidth(self.labelTime.sizePolicy().hasHeightForWidth())
        self.labelTime.setSizePolicy(sizePolicy)
        self.labelTime.setMouseTracking(False)
        self.labelTime.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.labelTime)

        self.btnDelRec = QPushButton(self.frameTime)
        self.btnDelRec.setObjectName(u"btnDelRec")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnDelRec.sizePolicy().hasHeightForWidth())
        self.btnDelRec.setSizePolicy(sizePolicy2)
        self.btnDelRec.setMinimumSize(QSize(15, 15))
        self.btnDelRec.setMaximumSize(QSize(15, 15))
        font = QFont()
        font.setPointSize(8)
        self.btnDelRec.setFont(font)
        self.btnDelRec.setMouseTracking(False)
        self.btnDelRec.setStyleSheet(u"padding:0px")
        self.btnDelRec.setIconSize(QSize(5, 5))

        self.horizontalLayout.addWidget(self.btnDelRec)


        self.verticalLayout_2.addWidget(self.frameTime)

        self.frameCon = QFrame(self.framew)
        self.frameCon.setObjectName(u"frameCon")
        self.frameCon.setMouseTracking(False)
        self.frameCon.setStyleSheet(u"")
        self.frameCon.setFrameShape(QFrame.StyledPanel)
        self.frameCon.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameCon)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelContent = QLabel(self.frameCon)
        self.labelContent.setObjectName(u"labelContent")
        sizePolicy.setHeightForWidth(self.labelContent.sizePolicy().hasHeightForWidth())
        self.labelContent.setSizePolicy(sizePolicy)
        self.labelContent.setMouseTracking(False)
        self.labelContent.setStyleSheet(u"")
        self.labelContent.setScaledContents(True)
        self.labelContent.setWordWrap(False)

        self.verticalLayout.addWidget(self.labelContent)


        self.verticalLayout_2.addWidget(self.frameCon)


        self.verticalLayout_3.addWidget(self.framew)


        self.retranslateUi(frameRecLabel)

        QMetaObject.connectSlotsByName(frameRecLabel)
    # setupUi

    def retranslateUi(self, frameRecLabel):
        frameRecLabel.setWindowTitle(QCoreApplication.translate("frameRecLabel", u"RecLabel", None))
        self.labelTime.setText("")
#if QT_CONFIG(tooltip)
        self.btnDelRec.setToolTip(QCoreApplication.translate("frameRecLabel", u"\u5220\u9664", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnDelRec.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btnDelRec.setText(QCoreApplication.translate("frameRecLabel", u"x", None))
        self.labelContent.setText("")
    # retranslateUi

