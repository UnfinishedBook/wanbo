# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setObjectName("tab")
        self.tabQuery = QtWidgets.QWidget()
        self.tabQuery.setObjectName("tabQuery")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabQuery)
        self.horizontalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.trQuery = QtWidgets.QTreeWidget(self.tabQuery)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trQuery.sizePolicy().hasHeightForWidth())
        self.trQuery.setSizePolicy(sizePolicy)
        self.trQuery.setMinimumSize(QtCore.QSize(50, 0))
        self.trQuery.setObjectName("trQuery")
        self.trQuery.headerItem().setText(0, "1")
        self.horizontalLayout_3.addWidget(self.trQuery)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.tabQuery)
        self.label_10.setMinimumSize(QtCore.QSize(0, 25))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.edtFilter = QtWidgets.QLineEdit(self.tabQuery)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtFilter.sizePolicy().hasHeightForWidth())
        self.edtFilter.setSizePolicy(sizePolicy)
        self.edtFilter.setMinimumSize(QtCore.QSize(200, 25))
        self.edtFilter.setObjectName("edtFilter")
        self.horizontalLayout_2.addWidget(self.edtFilter)
        self.btnRefresh = QtWidgets.QPushButton(self.tabQuery)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRefresh.sizePolicy().hasHeightForWidth())
        self.btnRefresh.setSizePolicy(sizePolicy)
        self.btnRefresh.setMinimumSize(QtCore.QSize(0, 25))
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout_2.addWidget(self.btnRefresh)
        self.btnAdd = QtWidgets.QPushButton(self.tabQuery)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setMinimumSize(QtCore.QSize(0, 25))
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_2.addWidget(self.btnAdd)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.twQuery = QtWidgets.QTableWidget(self.tabQuery)
        self.twQuery.setObjectName("twQuery")
        self.twQuery.setColumnCount(0)
        self.twQuery.setRowCount(0)
        self.verticalLayout_2.addWidget(self.twQuery)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.tab.addTab(self.tabQuery, "")
        self.tabStats = QtWidgets.QWidget()
        self.tabStats.setObjectName("tabStats")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabStats)
        self.horizontalLayout_4.setContentsMargins(16, 16, 16, 16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.trStats = QtWidgets.QTreeWidget(self.tabStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trStats.sizePolicy().hasHeightForWidth())
        self.trStats.setSizePolicy(sizePolicy)
        self.trStats.setMinimumSize(QtCore.QSize(50, 0))
        self.trStats.setObjectName("trStats")
        self.trStats.headerItem().setText(0, "1")
        self.horizontalLayout_4.addWidget(self.trStats)
        self.twStats = QtWidgets.QTableWidget(self.tabStats)
        self.twStats.setObjectName("twStats")
        self.twStats.setColumnCount(0)
        self.twStats.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.twStats)
        self.tab.addTab(self.tabStats, "")
        self.tabJob = QtWidgets.QWidget()
        self.tabJob.setObjectName("tabJob")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabJob)
        self.verticalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.tabJob)
        self.label_12.setMinimumSize(QtCore.QSize(0, 25))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.edtFilterJob = QtWidgets.QLineEdit(self.tabJob)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtFilterJob.sizePolicy().hasHeightForWidth())
        self.edtFilterJob.setSizePolicy(sizePolicy)
        self.edtFilterJob.setMinimumSize(QtCore.QSize(200, 25))
        self.edtFilterJob.setObjectName("edtFilterJob")
        self.horizontalLayout.addWidget(self.edtFilterJob)
        self.btnJobRefresh = QtWidgets.QPushButton(self.tabJob)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnJobRefresh.sizePolicy().hasHeightForWidth())
        self.btnJobRefresh.setSizePolicy(sizePolicy)
        self.btnJobRefresh.setMinimumSize(QtCore.QSize(0, 25))
        self.btnJobRefresh.setObjectName("btnJobRefresh")
        self.horizontalLayout.addWidget(self.btnJobRefresh)
        self.btnJobClose = QtWidgets.QPushButton(self.tabJob)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnJobClose.sizePolicy().hasHeightForWidth())
        self.btnJobClose.setSizePolicy(sizePolicy)
        self.btnJobClose.setMinimumSize(QtCore.QSize(0, 25))
        self.btnJobClose.setObjectName("btnJobClose")
        self.horizontalLayout.addWidget(self.btnJobClose)
        spacerItem1 = QtWidgets.QSpacerItem(747, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.twJob = QtWidgets.QTableWidget(self.tabJob)
        self.twJob.setObjectName("twJob")
        self.twJob.setColumnCount(0)
        self.twJob.setRowCount(0)
        self.verticalLayout_3.addWidget(self.twJob)
        self.tab.addTab(self.tabJob, "")
        self.tabLoad = QtWidgets.QWidget()
        self.tabLoad.setObjectName("tabLoad")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabLoad)
        self.verticalLayout_5.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnBrowse = QtWidgets.QPushButton(self.tabLoad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowse.sizePolicy().hasHeightForWidth())
        self.btnBrowse.setSizePolicy(sizePolicy)
        self.btnBrowse.setMinimumSize(QtCore.QSize(0, 25))
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout_5.addWidget(self.btnBrowse)
        self.edtFile = QtWidgets.QLineEdit(self.tabLoad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtFile.sizePolicy().hasHeightForWidth())
        self.edtFile.setSizePolicy(sizePolicy)
        self.edtFile.setMinimumSize(QtCore.QSize(500, 25))
        self.edtFile.setObjectName("edtFile")
        self.horizontalLayout_5.addWidget(self.edtFile)
        self.btnImport = QtWidgets.QPushButton(self.tabLoad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnImport.sizePolicy().hasHeightForWidth())
        self.btnImport.setSizePolicy(sizePolicy)
        self.btnImport.setMinimumSize(QtCore.QSize(0, 25))
        self.btnImport.setObjectName("btnImport")
        self.horizontalLayout_5.addWidget(self.btnImport)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cb1 = QtWidgets.QCheckBox(self.tabLoad)
        self.cb1.setMinimumSize(QtCore.QSize(0, 25))
        self.cb1.setObjectName("cb1")
        self.verticalLayout_4.addWidget(self.cb1)
        self.cb2 = QtWidgets.QCheckBox(self.tabLoad)
        self.cb2.setMinimumSize(QtCore.QSize(0, 25))
        self.cb2.setObjectName("cb2")
        self.verticalLayout_4.addWidget(self.cb2)
        self.cb3 = QtWidgets.QCheckBox(self.tabLoad)
        self.cb3.setMinimumSize(QtCore.QSize(0, 25))
        self.cb3.setObjectName("cb3")
        self.verticalLayout_4.addWidget(self.cb3)
        self.cb4 = QtWidgets.QCheckBox(self.tabLoad)
        self.cb4.setMinimumSize(QtCore.QSize(0, 25))
        self.cb4.setObjectName("cb4")
        self.verticalLayout_4.addWidget(self.cb4)
        self.cb5 = QtWidgets.QCheckBox(self.tabLoad)
        self.cb5.setMinimumSize(QtCore.QSize(0, 25))
        self.cb5.setObjectName("cb5")
        self.verticalLayout_4.addWidget(self.cb5)
        self.cb6 = QtWidgets.QCheckBox(self.tabLoad)
        self.cb6.setMinimumSize(QtCore.QSize(0, 25))
        self.cb6.setObjectName("cb6")
        self.verticalLayout_4.addWidget(self.cb6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.txtLoadMsg = QtWidgets.QTextEdit(self.tabLoad)
        self.txtLoadMsg.setObjectName("txtLoadMsg")
        self.horizontalLayout_6.addWidget(self.txtLoadMsg)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.tab.addTab(self.tabLoad, "")
        self.verticalLayout.addWidget(self.tab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actLoad = QtWidgets.QAction(MainWindow)
        self.actLoad.setObjectName("actLoad")

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "财务管理系统"))
        self.label_10.setText(_translate("MainWindow", "筛选"))
        self.btnRefresh.setText(_translate("MainWindow", "刷新"))
        self.btnAdd.setText(_translate("MainWindow", "新增"))
        self.tab.setTabText(self.tab.indexOf(self.tabQuery), _translate("MainWindow", "数据管理"))
        self.tab.setTabText(self.tab.indexOf(self.tabStats), _translate("MainWindow", "统计汇总"))
        self.label_12.setText(_translate("MainWindow", "筛选"))
        self.btnJobRefresh.setText(_translate("MainWindow", "刷新"))
        self.btnJobClose.setText(_translate("MainWindow", "关闭"))
        self.tab.setTabText(self.tab.indexOf(self.tabJob), _translate("MainWindow", "操作"))
        self.btnBrowse.setText(_translate("MainWindow", "浏览"))
        self.btnImport.setText(_translate("MainWindow", "确认导入"))
        self.cb1.setText(_translate("MainWindow", "现金账户1明细账"))
        self.cb2.setText(_translate("MainWindow", "现金账户2明细账"))
        self.cb3.setText(_translate("MainWindow", "银行明细账"))
        self.cb4.setText(_translate("MainWindow", "应收账款汇总表"))
        self.cb5.setText(_translate("MainWindow", "合同明细"))
        self.cb6.setText(_translate("MainWindow", "开票明细表"))
        self.tab.setTabText(self.tab.indexOf(self.tabLoad), _translate("MainWindow", "导入"))
        self.actLoad.setText(_translate("MainWindow", "导入"))

