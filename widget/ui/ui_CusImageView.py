# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusImageView.ui'
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
    QLabel, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CusImageView(object):
    def setupUi(self, CusImageView):
        if not CusImageView.objectName():
            CusImageView.setObjectName(u"CusImageView")
        CusImageView.resize(509, 437)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CusImageView.sizePolicy().hasHeightForWidth())
        CusImageView.setSizePolicy(sizePolicy)
        CusImageView.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget = QWidget(CusImageView)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame = QFrame(self.verticalFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy1.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy1)
        self.horizontalFrame.setMinimumSize(QSize(100, 100))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LabImage = QLabel(self.horizontalFrame)
        self.LabImage.setObjectName(u"LabImage")
        sizePolicy1.setHeightForWidth(self.LabImage.sizePolicy().hasHeightForWidth())
        self.LabImage.setSizePolicy(sizePolicy1)
        self.LabImage.setCursor(QCursor(Qt.OpenHandCursor))
        self.LabImage.setMouseTracking(False)
        self.LabImage.setFocusPolicy(Qt.NoFocus)
        self.LabImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.LabImage.setStyleSheet(u"background-color: rgba(80, 80, 80, 200);")
        self.LabImage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.LabImage)


        self.verticalLayout.addWidget(self.horizontalFrame)


        self.gridLayout.addWidget(self.verticalFrame, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        CusImageView.setCentralWidget(self.centralwidget)

        self.retranslateUi(CusImageView)
        CusImageView.destroyed.connect(CusImageView.deleteLater)

        QMetaObject.connectSlotsByName(CusImageView)
    # setupUi

    def retranslateUi(self, CusImageView):
        CusImageView.setWindowTitle(QCoreApplication.translate("CusImageView", u"\u9884\u89c8", None))
        self.LabImage.setText("")
    # retranslateUi

