# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusInputBox.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem)

class Ui_CusInputBox(object):
    def setupUi(self, CusInputBox):
        if not CusInputBox.objectName():
            CusInputBox.setObjectName(u"CusInputBox")
        CusInputBox.resize(177, 68)
        self.gridLayout_2 = QGridLayout(CusInputBox)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.lineInput = QLineEdit(CusInputBox)
        self.lineInput.setObjectName(u"lineInput")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineInput.sizePolicy().hasHeightForWidth())
        self.lineInput.setSizePolicy(sizePolicy)
        self.lineInput.setMaxLength(64)

        self.horizontalLayout.addWidget(self.lineInput)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnConfirm = QPushButton(CusInputBox)
        self.btnConfirm.setObjectName(u"btnConfirm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnConfirm.sizePolicy().hasHeightForWidth())
        self.btnConfirm.setSizePolicy(sizePolicy1)
        self.btnConfirm.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_2.addWidget(self.btnConfirm)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(CusInputBox)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy1.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy1)
        self.btnCancel.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_2.addWidget(self.btnCancel)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(CusInputBox)

        QMetaObject.connectSlotsByName(CusInputBox)
    # setupUi

    def retranslateUi(self, CusInputBox):
        CusInputBox.setWindowTitle(QCoreApplication.translate("CusInputBox", u"\u8bf7\u8f93\u5165", None))
        self.lineInput.setPlaceholderText(QCoreApplication.translate("CusInputBox", u"\u8bf7\u8f93\u5165", None))
        self.btnConfirm.setText(QCoreApplication.translate("CusInputBox", u"\u786e\u5b9a", None))
        self.btnCancel.setText(QCoreApplication.translate("CusInputBox", u"\u53d6\u6d88", None))
    # retranslateUi

