# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusNoteList.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QAbstractSpinBox, QCheckBox, QDateTimeEdit,
                               QFrame, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QListWidget, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CusNoteList(object):
    def setupUi(self, CusNoteList):
        if not CusNoteList.objectName():
            CusNoteList.setObjectName(u"CusNoteList")
        CusNoteList.resize(437, 300)
        self.gridLayout_2 = QGridLayout(CusNoteList)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalFrame = QFrame(CusNoteList)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 30))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.dateTimeEdit = QDateTimeEdit(self.horizontalFrame)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setStyleSheet(u"/** \u65e5\u671f\u663e\u793a\u677f **/\n"
"#qt_calendar_calendarview::item:hover {\n"
"	color:rgba(70, 141, 211,0.7);\n"
"	background: rgb(239, 239, 239);\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calendar_calendarview::item {\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calendar_calendarview::item:focus {\n"
"	color: white;\n"
"	background-color: rgba(70, 141, 211,0.7);\n"
"}\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"	outline:none;\n"
"	color:black;\n"
"	background: white;\n"
"\n"
"}\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"	color: rgb(179, 179, 179) ; \n"
"}\n"
"/* \u5bfc\u822a\u680f  \u53ca \u5bfc\u822a\u680f\u4e2d\u6309\u94ae\u8bbe\u7f6e*/\n"
"\n"
"#qt_calendar_navigationbar {\n"
"	color: rgb(148, 148, 148);\n"
"    background: white;\n"
"}\n"
"QToolButton{\n"
"	color: rgb(81, 81, 81);\n"
"    background: white;\n"
"	qproperty-icon: none;\n"
"\n"
"}\n"
"#qt_calendar_prevmonth{/*\u4e0a\u4e00\u6708*/\n"
"	qproperty-text:'<';\n"
"	font:15px;\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calenda"
                        "r_prevmonth:hover{/*\u4e0a\u4e00\u6708*/\n"
"	color:rgba(70, 141, 211,0.7);\n"
"}\n"
"#qt_calendar_nextmonth{/*\u4e0b\u4e00\u6708*/\n"
"	qproperty-text:'>';\n"
"	font:15px;\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calendar_nextmonth:hover{\n"
"	color:rgba(70, 141, 211,0.7);\n"
"}\n"
"/***************************************************/\n"
"")
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.dateTimeEdit.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateTimeEdit)

        self.dateIntervalWidget = QWidget(self.horizontalFrame)
        self.dateIntervalWidget.setObjectName(u"dateIntervalWidget")
        self.dateIntervalFrame = QHBoxLayout(self.dateIntervalWidget)
        self.dateIntervalFrame.setSpacing(0)
        self.dateIntervalFrame.setObjectName(u"dateIntervalFrame")
        self.dateIntervalFrame.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.dateIntervalWidget)
        self.label.setObjectName(u"label")

        self.dateIntervalFrame.addWidget(self.label)

        self.dateTimeStart = QDateTimeEdit(self.dateIntervalWidget)
        self.dateTimeStart.setObjectName(u"dateTimeStart")
        sizePolicy.setHeightForWidth(self.dateTimeStart.sizePolicy().hasHeightForWidth())
        self.dateTimeStart.setSizePolicy(sizePolicy)
        self.dateTimeStart.setStyleSheet(u"/** \u65e5\u671f\u663e\u793a\u677f **/\n"
"#qt_calendar_calendarview::item:hover {\n"
"	color:rgba(70, 141, 211,0.7);\n"
"	background: rgb(239, 239, 239);\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calendar_calendarview::item {\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calendar_calendarview::item:focus {\n"
"	color: white;\n"
"	background-color: rgba(70, 141, 211,0.7);\n"
"}\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"	outline:none;\n"
"	color:black;\n"
"	background: white;\n"
"\n"
"}\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"	color: rgb(179, 179, 179) ; \n"
"}\n"
"/* \u5bfc\u822a\u680f  \u53ca \u5bfc\u822a\u680f\u4e2d\u6309\u94ae\u8bbe\u7f6e*/\n"
"\n"
"#qt_calendar_navigationbar {\n"
"	color: rgb(148, 148, 148);\n"
"    background: white;\n"
"}\n"
"QToolButton{\n"
"	color: rgb(81, 81, 81);\n"
"    background: white;\n"
"	qproperty-icon: none;\n"
"\n"
"}\n"
"#qt_calendar_prevmonth{/*\u4e0a\u4e00\u6708*/\n"
"	qproperty-text:'<';\n"
"	font:15px;\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calenda"
                        "r_prevmonth:hover{/*\u4e0a\u4e00\u6708*/\n"
"	color:rgba(70, 141, 211,0.7);\n"
"}\n"
"#qt_calendar_nextmonth{/*\u4e0b\u4e00\u6708*/\n"
"	qproperty-text:'>';\n"
"	font:15px;\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calendar_nextmonth:hover{\n"
"	color:rgba(70, 141, 211,0.7);\n"
"}\n"
"/***************************************************/\n"
"")
        self.dateTimeStart.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.dateTimeStart.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateTimeStart.setCalendarPopup(True)

        self.dateIntervalFrame.addWidget(self.dateTimeStart)

        self.horizontalSpacer_7 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.dateIntervalFrame.addItem(self.horizontalSpacer_7)

        self.label_2 = QLabel(self.dateIntervalWidget)
        self.label_2.setObjectName(u"label_2")

        self.dateIntervalFrame.addWidget(self.label_2)

        self.dateTimeEnd = QDateTimeEdit(self.dateIntervalWidget)
        self.dateTimeEnd.setObjectName(u"dateTimeEnd")
        sizePolicy.setHeightForWidth(self.dateTimeEnd.sizePolicy().hasHeightForWidth())
        self.dateTimeEnd.setSizePolicy(sizePolicy)
        self.dateTimeEnd.setStyleSheet(u"/** \u65e5\u671f\u663e\u793a\u677f **/\n"
"#qt_calendar_calendarview::item:hover {\n"
"	color:rgba(70, 141, 211,0.7);\n"
"	background: rgb(239, 239, 239);\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calendar_calendarview::item {\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calendar_calendarview::item:focus {\n"
"	color: white;\n"
"	background-color: rgba(70, 141, 211,0.7);\n"
"}\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"	outline:none;\n"
"	color:black;\n"
"	background: white;\n"
"\n"
"}\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"	color: rgb(179, 179, 179) ; \n"
"}\n"
"/* \u5bfc\u822a\u680f  \u53ca \u5bfc\u822a\u680f\u4e2d\u6309\u94ae\u8bbe\u7f6e*/\n"
"\n"
"#qt_calendar_navigationbar {\n"
"	color: rgb(148, 148, 148);\n"
"    background: white;\n"
"}\n"
"QToolButton{\n"
"	color: rgb(81, 81, 81);\n"
"    background: white;\n"
"	qproperty-icon: none;\n"
"\n"
"}\n"
"#qt_calendar_prevmonth{/*\u4e0a\u4e00\u6708*/\n"
"	qproperty-text:'<';\n"
"	font:15px;\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calenda"
                        "r_prevmonth:hover{/*\u4e0a\u4e00\u6708*/\n"
"	color:rgba(70, 141, 211,0.7);\n"
"}\n"
"#qt_calendar_nextmonth{/*\u4e0b\u4e00\u6708*/\n"
"	qproperty-text:'>';\n"
"	font:15px;\n"
"	border-radius: 10px;\n"
"}\n"
"#qt_calendar_nextmonth:hover{\n"
"	color:rgba(70, 141, 211,0.7);\n"
"}\n"
"/***************************************************/\n"
"")
        self.dateTimeEnd.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.dateTimeEnd.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateTimeEnd.setCalendarPopup(True)

        self.dateIntervalFrame.addWidget(self.dateTimeEnd)


        self.horizontalLayout_4.addWidget(self.dateIntervalWidget)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_5 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.checkBoxDateUse = QCheckBox(self.horizontalFrame)
        self.checkBoxDateUse.setObjectName(u"checkBoxDateUse")
        self.checkBoxDateUse.setMaximumSize(QSize(20, 22))
        self.checkBoxDateUse.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxDateUse)

        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, -1, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.leQueryInput = QLineEdit(CusNoteList)
        self.leQueryInput.setObjectName(u"leQueryInput")

        self.horizontalLayout_2.addWidget(self.leQueryInput)

        self.btnQuery = QPushButton(CusNoteList)
        self.btnQuery.setObjectName(u"btnQuery")
        self.btnQuery.setMaximumSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btnQuery)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.listWidget = QListWidget(CusNoteList)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QListWidget  QScrollBar{\n"
"	width:8px;\n"
"    border: none;\n"
"     background-color: rgba(40, 81, 121,0.2);\n"
"}")
        self.listWidget.setSpacing(5)

        self.verticalLayout_2.addWidget(self.listWidget)

        self.verticalSpacer_4 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.labelStatus = QLabel(CusNoteList)
        self.labelStatus.setObjectName(u"labelStatus")
        sizePolicy.setHeightForWidth(self.labelStatus.sizePolicy().hasHeightForWidth())
        self.labelStatus.setSizePolicy(sizePolicy)
        self.labelStatus.setMaximumSize(QSize(16777215, 15))
        font = QFont()
        font.setPointSize(8)
        self.labelStatus.setFont(font)
        self.labelStatus.setStyleSheet(u"color:rgb(199, 199, 199)")
        self.labelStatus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelStatus.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_2.addWidget(self.labelStatus)

        self.verticalSpacer = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.labelTitle = QLabel(CusNoteList)
        self.labelTitle.setObjectName(u"labelTitle")
        font1 = QFont()
        font1.setPointSize(15)
        self.labelTitle.setFont(font1)

        self.horizontalLayout_3.addWidget(self.labelTitle)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.btnRecovery = QPushButton(CusNoteList)
        self.btnRecovery.setObjectName(u"btnRecovery")
        self.btnRecovery.setEnabled(True)
        self.btnRecovery.setMinimumSize(QSize(23, 23))
        self.btnRecovery.setMaximumSize(QSize(23, 23))
        self.btnRecovery.setStyleSheet(u"")
        self.btnRecovery.setIconSize(QSize(10, 10))

        self.horizontalLayout_3.addWidget(self.btnRecovery)

        self.btnMax = QPushButton(CusNoteList)
        self.btnMax.setObjectName(u"btnMax")
        self.btnMax.setMaximumSize(QSize(23, 23))
        font2 = QFont()
        font2.setPointSize(10)
        self.btnMax.setFont(font2)
        self.btnMax.setStyleSheet(u"")
        self.btnMax.setIconSize(QSize(10, 10))

        self.horizontalLayout_3.addWidget(self.btnMax)

        self.btnClose = QPushButton(CusNoteList)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy1)
        self.btnClose.setMinimumSize(QSize(23, 23))
        self.btnClose.setMaximumSize(QSize(23, 23))
        font3 = QFont()
        font3.setPointSize(12)
        self.btnClose.setFont(font3)
        self.btnClose.setStyleSheet(u"#btnClose{\n"
"	padding-bottom:2px\n"
"}\n"
"#btnClose:hover{\n"
"	color:white;\n"
"	border-radius: 2px;\n"
"	background-color: rgba(223, 0, 0,0.8);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btnClose)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(CusNoteList)
        self.btnClose.clicked.connect(CusNoteList.close)
        self.btnMax.clicked.connect(CusNoteList.showMaximized)
        self.btnRecovery.clicked.connect(CusNoteList.showNormal)
        self.btnRecovery.clicked.connect(self.btnMax.show)
        self.btnMax.clicked.connect(self.btnRecovery.show)
        self.btnMax.clicked.connect(self.btnMax.hide)
        self.btnRecovery.clicked.connect(self.btnRecovery.hide)

        QMetaObject.connectSlotsByName(CusNoteList)
    # setupUi

    def retranslateUi(self, CusNoteList):
        CusNoteList.setWindowTitle(QCoreApplication.translate("CusNoteList", u"\u7b14\u8bb0\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.dateTimeEdit.setToolTip(QCoreApplication.translate("CusNoteList", u"\u53f3\u952e\u53ef\u5207\u6362\u6a21\u5f0f\u65f6\u95f4", None))
#endif // QT_CONFIG(tooltip)
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("CusNoteList", u"yyyy/MM/dd", None))
        self.label.setText(QCoreApplication.translate("CusNoteList", u"\u59cb:", None))
#if QT_CONFIG(tooltip)
        self.dateTimeStart.setToolTip(QCoreApplication.translate("CusNoteList", u"\u8d77\u59cb\u67e5\u8be2\u65f6\u95f4(\u5305\u542b)", None))
#endif // QT_CONFIG(tooltip)
        self.dateTimeStart.setDisplayFormat(QCoreApplication.translate("CusNoteList", u"yyyy/MM/dd", None))
        self.label_2.setText(QCoreApplication.translate("CusNoteList", u"\u6b62:", None))
#if QT_CONFIG(tooltip)
        self.dateTimeEnd.setToolTip(QCoreApplication.translate("CusNoteList", u"\u7ec8\u6b62\u67e5\u8be2\u65f6\u95f4(\u5305\u542b)", None))
#endif // QT_CONFIG(tooltip)
        self.dateTimeEnd.setDisplayFormat(QCoreApplication.translate("CusNoteList", u"yyyy/MM/dd", None))
#if QT_CONFIG(tooltip)
        self.checkBoxDateUse.setToolTip(QCoreApplication.translate("CusNoteList", u"\u4f7f\u7528\u65e5\u671f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBoxDateUse.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.checkBoxDateUse.setText("")
#if QT_CONFIG(tooltip)
        self.leQueryInput.setToolTip(QCoreApplication.translate("CusNoteList", u"<html><head/><body><p>- \u76f4\u63a5\u8f93\u5165 \u6a21\u7cca\u67e5\u8be2\u7b14\u8bb0\u5185\u5bb9</p><p>- \u5728\u6807\u7b7e\u91cc\u8f93\u5165SQL\u683c\u5f0f\u6587\u672c(\u76ee\u524d\u6709\u4e24\u79cd\u6807\u7b7e: @note , @tag)\uff0c\u4e24\u4e2a\u6807\u7b7e\u4e4b\u95f4\u53ef\u4ee5\u7528 and/or \u8fde\u63a5</p><p>@note:[ \u7b5b\u7b14\u8bb0\u6761\u4ef6 ] content \u6587\u672c\u5185\u5bb9 / indate \u65e5\u671f\u65f6\u95f4</p><p>AND | OR </p><p>@tag:[ \u7b5b\u9009\u6807\u7b7e\u6761\u4ef6 ]</p><p>=\u4f8b:</p><p><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">- @note:[content='</span><span style=\" font-family:'\u5b8b\u4f53','monospace'; font-size:9.8pt; color:#808080;\">\u73a9\u6e38\u620f</span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">']</span></p><p><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">- @note:[(content='</span><span style=\" font-family:'\u5b8b\u4f53','monospace'; font-"
                        "size:9.8pt; color:#808080;\">\u4e0a\u5348\u5728\u5b66\u4f5c\u4e1a</span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">' and indate like '2022-05-05%') or (content like '%</span><span style=\" font-family:'\u5b8b\u4f53','monospace'; font-size:9.8pt; color:#808080;\">\u65b0\u95fb\u8054\u64ad\u7ed3\u675f%</span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">' and and indate='2022-05-06 19:30:00')]</span></p><p><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">- @tag:[text='</span><span style=\" font-family:'\u5b8b\u4f53','monospace'; font-size:9.8pt; color:#808080;\">\u65e5\u5e38</span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">']</span></p><p><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">- @tag:[(text='</span><span style=\" font-family:'\u5b8b\u4f53','monospace'; font-size:9.8pt; color:#808080"
                        ";\">\u65e5\u5e38</span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">' and sort=1) or (text='</span><span style=\" font-family:'\u5b8b\u4f53','monospace'; font-size:9.8pt; color:#808080;\">\u5b66\u4e60</span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">' and sort=3)]</span></p><p><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#808080;\">- @note:[content='\u5c0f\u660e'] OR @tag:[text='\u65e5\u5e38']</span></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leQueryInput.setPlaceholderText(QCoreApplication.translate("CusNoteList", u"\u641c\u7d22", None))
#if QT_CONFIG(tooltip)
        self.btnQuery.setToolTip(QCoreApplication.translate("CusNoteList", u"\u641c\u7d22", None))
#endif // QT_CONFIG(tooltip)
        self.btnQuery.setText(QCoreApplication.translate("CusNoteList", u"O", None))
#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.labelStatus.setText(QCoreApplication.translate("CusNoteList", u"\u5171 0 \u6761", None))
        self.labelTitle.setText(QCoreApplication.translate("CusNoteList", u"\u7b14\u8bb0\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.btnRecovery.setToolTip(QCoreApplication.translate("CusNoteList", u"\u6062\u590d", None))
#endif // QT_CONFIG(tooltip)
        self.btnRecovery.setText("")
#if QT_CONFIG(tooltip)
        self.btnMax.setToolTip(QCoreApplication.translate("CusNoteList", u"\u6700\u5927\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.btnMax.setText("")
#if QT_CONFIG(tooltip)
        self.btnClose.setToolTip(QCoreApplication.translate("CusNoteList", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.btnClose.setText(QCoreApplication.translate("CusNoteList", u"x", None))
    # retranslateUi

