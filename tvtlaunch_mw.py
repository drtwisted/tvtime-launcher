# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tvtlaunch_mw.ui'
#
# Created: Sun Apr 19 15:16:16 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_tvtimelaunch(object):
    def setupUi(self, tvtimelaunch):
        tvtimelaunch.setObjectName(_fromUtf8("tvtimelaunch"))
        tvtimelaunch.resize(373, 422)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("tvtime"))
        tvtimelaunch.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(tvtimelaunch)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 130, 372, 288))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setMargin(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cmbDevice = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cmbDevice.setObjectName(_fromUtf8("cmbDevice"))
        self.horizontalLayout_2.addWidget(self.cmbDevice)
        self.btnRefresh = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRefresh.sizePolicy().hasHeightForWidth())
        self.btnRefresh.setSizePolicy(sizePolicy)
        self.btnRefresh.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("reload"))
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setObjectName(_fromUtf8("btnRefresh"))
        self.horizontalLayout_2.addWidget(self.btnRefresh)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.cmbRegion = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cmbRegion.setObjectName(_fromUtf8("cmbRegion"))
        self.verticalLayout.addWidget(self.cmbRegion)
        self.gbAspect = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.gbAspect.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbAspect.sizePolicy().hasHeightForWidth())
        self.gbAspect.setSizePolicy(sizePolicy)
        self.gbAspect.setMinimumSize(QtCore.QSize(0, 36))
        self.gbAspect.setMaximumSize(QtCore.QSize(16777215, 48))
        self.gbAspect.setObjectName(_fromUtf8("gbAspect"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.gbAspect)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-10, 20, 299, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(10, 5, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.chkAspect = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.chkAspect.setObjectName(_fromUtf8("chkAspect"))
        self.horizontalLayout_3.addWidget(self.chkAspect)
        self.lbAspect = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbAspect.setFont(font)
        self.lbAspect.setObjectName(_fromUtf8("lbAspect"))
        self.horizontalLayout_3.addWidget(self.lbAspect)
        self.verticalLayout.addWidget(self.gbAspect)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnLaunch = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnLaunch.setObjectName(_fromUtf8("btnLaunch"))
        self.horizontalLayout.addWidget(self.btnLaunch)
        self.btnKill = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnKill.setEnabled(False)
        self.btnKill.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnKill.setObjectName(_fromUtf8("btnKill"))
        self.horizontalLayout.addWidget(self.btnKill)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setMaximumSize(QtCore.QSize(24, 16777215))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("multimedia"))
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.chbMagic = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.chbMagic.setMaximumSize(QtCore.QSize(60, 16777215))
        self.chbMagic.setObjectName(_fromUtf8("chbMagic"))
        self.horizontalLayout_4.addWidget(self.chbMagic)
        self.btnListen = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnListen.setMaximumSize(QtCore.QSize(112, 16777215))
        self.btnListen.setObjectName(_fromUtf8("btnListen"))
        self.horizontalLayout_4.addWidget(self.btnListen)
        self.btnReloadUsbtv = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnReloadUsbtv.setMaximumSize(QtCore.QSize(140, 16777215))
        self.btnReloadUsbtv.setObjectName(_fromUtf8("btnReloadUsbtv"))
        self.horizontalLayout_4.addWidget(self.btnReloadUsbtv)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 331, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 10, 101, 101))
        self.pushButton_2.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("tvtime"))
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(96, 96))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        tvtimelaunch.setCentralWidget(self.centralwidget)

        self.retranslateUi(tvtimelaunch)
        QtCore.QMetaObject.connectSlotsByName(tvtimelaunch)

    def retranslateUi(self, tvtimelaunch):
        tvtimelaunch.setWindowTitle(_translate("tvtimelaunch", "TVTime Launcher", None))
        self.label.setText(_translate("tvtimelaunch", "Device:", None))
        self.label_2.setText(_translate("tvtimelaunch", "Region:", None))
        self.gbAspect.setTitle(_translate("tvtimelaunch", "Aspect ratio:", None))
        self.chkAspect.setText(_translate("tvtimelaunch", "Wide screen", None))
        self.lbAspect.setText(_translate("tvtimelaunch", "4:3", None))
        self.btnLaunch.setText(_translate("tvtimelaunch", "Launch", None))
        self.btnKill.setText(_translate("tvtimelaunch", "Kill", None))
        self.chbMagic.setText(_translate("tvtimelaunch", "Magic", None))
        self.btnListen.setText(_translate("tvtimelaunch", "Enable", None))
        self.btnReloadUsbtv.setText(_translate("tvtimelaunch", "Reload Usbtv Module", None))
        self.label_3.setText(_translate("tvtimelaunch", "TVTime", None))
        self.label_4.setText(_translate("tvtimelaunch", "Launcher", None))
