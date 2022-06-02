# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusNoteEdit.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QListView,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_CusNoteEdit(object):
    def setupUi(self, CusNoteEdit):
        if not CusNoteEdit.objectName():
            CusNoteEdit.setObjectName(u"CusNoteEdit")
        CusNoteEdit.resize(200, 300)
        self.gridLayout = QGridLayout(CusNoteEdit)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(CusNoteEdit)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.editOptBar = QFrame(self.verticalFrame)
        self.editOptBar.setObjectName(u"editOptBar")
        self.editOptBar.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.editOptBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnReturn = QPushButton(self.editOptBar)
        self.btnReturn.setObjectName(u"btnReturn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReturn.sizePolicy().hasHeightForWidth())
        self.btnReturn.setSizePolicy(sizePolicy)
        self.btnReturn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btnReturn)

        self.btnCommit = QPushButton(self.editOptBar)
        self.btnCommit.setObjectName(u"btnCommit")
        sizePolicy.setHeightForWidth(self.btnCommit.sizePolicy().hasHeightForWidth())
        self.btnCommit.setSizePolicy(sizePolicy)
        self.btnCommit.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btnCommit)

        self.btnDelNote = QPushButton(self.editOptBar)
        self.btnDelNote.setObjectName(u"btnDelNote")
        sizePolicy.setHeightForWidth(self.btnDelNote.sizePolicy().hasHeightForWidth())
        self.btnDelNote.setSizePolicy(sizePolicy)
        self.btnDelNote.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.btnDelNote.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnDelNote)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.dateTimeEdit = QDateTimeEdit(self.editOptBar)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setMaximumSize(QSize(100, 16777215))
        self.dateTimeEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.dateTimeEdit.setMaximumDate(QDate(9999, 12, 31))
        self.dateTimeEdit.setMinimumDate(QDate(2000, 1, 1))
        self.dateTimeEdit.setCalendarPopup(False)

        self.horizontalLayout_2.addWidget(self.dateTimeEdit)


        self.verticalLayout.addWidget(self.editOptBar)

        self.frame_edit = QFrame(self.verticalFrame)
        self.frame_edit.setObjectName(u"frame_edit")
        self.verticalLayout_3 = QVBoxLayout(self.frame_edit)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.frame_edit)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMouseTracking(False)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.frame_edit)

        self.frame_tags = QFrame(self.verticalFrame)
        self.frame_tags.setObjectName(u"frame_tags")
        self.frame_tags.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.frame_tags)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 0, 0, 0)
        self.label = QLabel(self.frame_tags)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(35, 16777215))
        self.label.setMargin(1)

        self.horizontalLayout.addWidget(self.label)

        self.hboxTags = QHBoxLayout()
        self.hboxTags.setSpacing(0)
        self.hboxTags.setObjectName(u"hboxTags")
        self.listWidgeTags = QListWidget(self.frame_tags)
        self.listWidgeTags.setObjectName(u"listWidgeTags")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listWidgeTags.sizePolicy().hasHeightForWidth())
        self.listWidgeTags.setSizePolicy(sizePolicy3)
        self.listWidgeTags.setStyleSheet(u"QListWidget  QScrollBar{\n"
"	height:5px;\n"
"    border: none;\n"
"    background-color: rgba(85, 170, 127,0.6);\n"
"}\n"
"")
        self.listWidgeTags.setFrameShape(QFrame.StyledPanel)
        self.listWidgeTags.setFrameShadow(QFrame.Sunken)
        self.listWidgeTags.setMidLineWidth(0)
        self.listWidgeTags.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidgeTags.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidgeTags.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidgeTags.setProperty("showDropIndicator", True)
        self.listWidgeTags.setDragEnabled(True)
        self.listWidgeTags.setDragDropOverwriteMode(True)
        self.listWidgeTags.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidgeTags.setDefaultDropAction(Qt.TargetMoveAction)
        self.listWidgeTags.setAlternatingRowColors(False)
        self.listWidgeTags.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidgeTags.setMovement(QListView.Free)
        self.listWidgeTags.setFlow(QListView.LeftToRight)
        self.listWidgeTags.setResizeMode(QListView.Fixed)
        self.listWidgeTags.setSpacing(1)
        self.listWidgeTags.setSortingEnabled(False)

        self.hboxTags.addWidget(self.listWidgeTags)


        self.horizontalLayout.addLayout(self.hboxTags)

        self.btnAddTag = QPushButton(self.frame_tags)
        self.btnAddTag.setObjectName(u"btnAddTag")
        sizePolicy2.setHeightForWidth(self.btnAddTag.sizePolicy().hasHeightForWidth())
        self.btnAddTag.setSizePolicy(sizePolicy2)
        self.btnAddTag.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.btnAddTag)


        self.verticalLayout.addWidget(self.frame_tags)


        self.gridLayout.addWidget(self.verticalFrame, 0, 0, 1, 1)


        self.retranslateUi(CusNoteEdit)

        QMetaObject.connectSlotsByName(CusNoteEdit)
    # setupUi

    def retranslateUi(self, CusNoteEdit):
        CusNoteEdit.setWindowTitle(QCoreApplication.translate("CusNoteEdit", u"NoteEdit", None))
#if QT_CONFIG(tooltip)
        self.btnReturn.setToolTip(QCoreApplication.translate("CusNoteEdit", u"\u8fd4\u56de", None))
#endif // QT_CONFIG(tooltip)
        self.btnReturn.setText(QCoreApplication.translate("CusNoteEdit", u"\u2190", None))
#if QT_CONFIG(tooltip)
        self.btnCommit.setToolTip(QCoreApplication.translate("CusNoteEdit", u"\u5b8c\u6210\u7f16\u8f91", None))
#endif // QT_CONFIG(tooltip)
        self.btnCommit.setText(QCoreApplication.translate("CusNoteEdit", u"\u221a", None))
#if QT_CONFIG(tooltip)
        self.btnDelNote.setToolTip(QCoreApplication.translate("CusNoteEdit", u"\u5220\u9664\u6b64\u7b14\u8bb0", None))
#endif // QT_CONFIG(tooltip)
        self.btnDelNote.setText(QCoreApplication.translate("CusNoteEdit", u"-", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("CusNoteEdit", u"MM/dd HH:mm", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("CusNoteEdit", u"\u8bf7\u8f93\u5165\u7b14\u8bb0\u5185\u5bb9", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("CusNoteEdit", u"<html><head/><body><p>\u62d6\u52a8\u6807\u7b7e\u8c03\u6574\u987a\u5e8f</p><p>\u53f3\u952e\u5220\u9664</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("CusNoteEdit", u"\u6807\u7b7e :", None))
#if QT_CONFIG(tooltip)
        self.btnAddTag.setToolTip(QCoreApplication.translate("CusNoteEdit", u"\u6dfb\u52a0\u6807\u7b7e", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddTag.setText(QCoreApplication.translate("CusNoteEdit", u"+", None))
    # retranslateUi

