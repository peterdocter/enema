# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\enema\gui\main\form.ui'
#
# Created: Sat Mar 10 17:05:35 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(591, 618)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setMinimumSize(QtCore.QSize(591, 618))
        MainForm.setMaximumSize(QtCore.QSize(1112, 618))
        MainForm.setBaseSize(QtCore.QSize(0, 0))
        MainForm.setWindowTitle(_fromUtf8("Enema"))
        MainForm.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainForm.setDocumentMode(False)
        MainForm.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainForm)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setEnabled(True)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 591, 601))
        self.tabs.setMinimumSize(QtCore.QSize(1, 1))
        self.tabs.setMaximumSize(QtCore.QSize(1000, 1000))
        self.tabs.setDocumentMode(True)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.db_structureTab = QtGui.QWidget()
        self.db_structureTab.setObjectName(_fromUtf8("db_structureTab"))
        self.comboBox = QtGui.QComboBox(self.db_structureTab)
        self.comboBox.setGeometry(QtCore.QRect(520, 10, 61, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.tablesButton = QtGui.QPushButton(self.db_structureTab)
        self.tablesButton.setGeometry(QtCore.QRect(10, 200, 91, 23))
        self.tablesButton.setObjectName(_fromUtf8("tablesButton"))
        self.countButton = QtGui.QPushButton(self.db_structureTab)
        self.countButton.setGeometry(QtCore.QRect(110, 200, 91, 23))
        self.countButton.setObjectName(_fromUtf8("countButton"))
        self.getColumnsButton = QtGui.QPushButton(self.db_structureTab)
        self.getColumnsButton.setGeometry(QtCore.QRect(210, 200, 91, 23))
        self.getColumnsButton.setObjectName(_fromUtf8("getColumnsButton"))
        self.groupBox = QtGui.QGroupBox(self.db_structureTab)
        self.groupBox.setGeometry(QtCore.QRect(410, 200, 171, 301))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioOrdinalPosition = QtGui.QRadioButton(self.groupBox)
        self.radioOrdinalPosition.setGeometry(QtCore.QRect(10, 90, 141, 17))
        self.radioOrdinalPosition.setObjectName(_fromUtf8("radioOrdinalPosition"))
        self.radioNotInArray = QtGui.QRadioButton(self.groupBox)
        self.radioNotInArray.setGeometry(QtCore.QRect(10, 50, 141, 17))
        self.radioNotInArray.setChecked(True)
        self.radioNotInArray.setObjectName(_fromUtf8("radioNotInArray"))
        self.radioNotInSubstring = QtGui.QRadioButton(self.groupBox)
        self.radioNotInSubstring.setGeometry(QtCore.QRect(10, 70, 141, 17))
        self.radioNotInSubstring.setChecked(False)
        self.radioNotInSubstring.setObjectName(_fromUtf8("radioNotInSubstring"))
        self.threadBox = QtGui.QSpinBox(self.groupBox)
        self.threadBox.setGeometry(QtCore.QRect(10, 180, 41, 20))
        self.threadBox.setMinimum(1)
        self.threadBox.setMaximum(100)
        self.threadBox.setProperty("value", 10)
        self.threadBox.setObjectName(_fromUtf8("threadBox"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 131, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineTimeout = QtGui.QLineEdit(self.groupBox)
        self.lineTimeout.setGeometry(QtCore.QRect(60, 180, 41, 20))
        self.lineTimeout.setObjectName(_fromUtf8("lineTimeout"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.lineMS = QtGui.QLineEdit(self.groupBox)
        self.lineMS.setGeometry(QtCore.QRect(110, 140, 21, 20))
        self.lineMS.setMaxLength(1)
        self.lineMS.setObjectName(_fromUtf8("lineMS"))
        self.label_22 = QtGui.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(10, 140, 91, 20))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(10, 110, 101, 20))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.lineMP = QtGui.QLineEdit(self.groupBox)
        self.lineMP.setGeometry(QtCore.QRect(110, 110, 51, 20))
        self.lineMP.setText(_fromUtf8(""))
        self.lineMP.setObjectName(_fromUtf8("lineMP"))
        self.logButton = QtGui.QToolButton(self.groupBox)
        self.logButton.setGeometry(QtCore.QRect(40, 240, 91, 21))
        self.logButton.setObjectName(_fromUtf8("logButton"))
        self.isRndUpper = QtGui.QCheckBox(self.groupBox)
        self.isRndUpper.setGeometry(QtCore.QRect(10, 210, 131, 17))
        self.isRndUpper.setObjectName(_fromUtf8("isRndUpper"))
        self.killButton = QtGui.QToolButton(self.groupBox)
        self.killButton.setGeometry(QtCore.QRect(40, 270, 91, 21))
        self.killButton.setObjectName(_fromUtf8("killButton"))
        self.lineUrl = QtGui.QLineEdit(self.db_structureTab)
        self.lineUrl.setGeometry(QtCore.QRect(40, 10, 471, 20))
        self.lineUrl.setObjectName(_fromUtf8("lineUrl"))
        self.label_4 = QtGui.QLabel(self.db_structureTab)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 31, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(self.db_structureTab)
        self.label.setGeometry(QtCore.QRect(10, 550, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.totalLabel = QtGui.QLabel(self.db_structureTab)
        self.totalLabel.setGeometry(QtCore.QRect(90, 550, 31, 16))
        self.totalLabel.setObjectName(_fromUtf8("totalLabel"))
        self.progressBar = QtGui.QProgressBar(self.db_structureTab)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(130, 550, 451, 16))
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setToolTip(_fromUtf8(""))
        self.progressBar.setStatusTip(_fromUtf8(""))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 83210)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.cleanThreeButton = QtGui.QPushButton(self.db_structureTab)
        self.cleanThreeButton.setGeometry(QtCore.QRect(310, 200, 91, 23))
        self.cleanThreeButton.setObjectName(_fromUtf8("cleanThreeButton"))
        self.listOfTables = QtGui.QListWidget(self.db_structureTab)
        self.listOfTables.setGeometry(QtCore.QRect(10, 230, 191, 311))
        self.listOfTables.setDragEnabled(True)
        self.listOfTables.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.listOfTables.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listOfTables.setObjectName(_fromUtf8("listOfTables"))
        self.treeOfTables = QtGui.QTreeWidget(self.db_structureTab)
        self.treeOfTables.setGeometry(QtCore.QRect(210, 230, 191, 311))
        self.treeOfTables.setAcceptDrops(True)
        self.treeOfTables.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeOfTables.setDragDropOverwriteMode(True)
        self.treeOfTables.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.treeOfTables.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.treeOfTables.setIndentation(20)
        self.treeOfTables.setRootIsDecorated(True)
        self.treeOfTables.setUniformRowHeights(False)
        self.treeOfTables.setItemsExpandable(True)
        self.treeOfTables.setAnimated(True)
        self.treeOfTables.setWordWrap(False)
        self.treeOfTables.setColumnCount(1)
        self.treeOfTables.setObjectName(_fromUtf8("treeOfTables"))
        self.treeOfTables.header().setVisible(False)
        self.treeOfTables.header().setCascadingSectionResizes(False)
        self.treeOfTables.header().setHighlightSections(False)
        self.dbListComboBox = QtGui.QComboBox(self.db_structureTab)
        self.dbListComboBox.setGeometry(QtCore.QRect(410, 520, 131, 21))
        self.dbListComboBox.setObjectName(_fromUtf8("dbListComboBox"))
        self.label_7 = QtGui.QLabel(self.db_structureTab)
        self.label_7.setGeometry(QtCore.QRect(470, 500, 41, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.getBasesButton = QtGui.QToolButton(self.db_structureTab)
        self.getBasesButton.setGeometry(QtCore.QRect(550, 520, 31, 21))
        self.getBasesButton.setObjectName(_fromUtf8("getBasesButton"))
        self.textEdit = QtGui.QTextEdit(self.db_structureTab)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 571, 101))
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_3 = QtGui.QLabel(self.db_structureTab)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 51, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineCookie = QtGui.QLineEdit(self.db_structureTab)
        self.lineCookie.setGeometry(QtCore.QRect(10, 170, 571, 21))
        self.lineCookie.setText(_fromUtf8(""))
        self.lineCookie.setObjectName(_fromUtf8("lineCookie"))
        self.label_15 = QtGui.QLabel(self.db_structureTab)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.tabs.addTab(self.db_structureTab, _fromUtf8(""))
        self.queryTab = QtGui.QWidget()
        self.queryTab.setObjectName(_fromUtf8("queryTab"))
        self.groupBox_3 = QtGui.QGroupBox(self.queryTab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 571, 281))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.queryButton = QtGui.QPushButton(self.groupBox_3)
        self.queryButton.setGeometry(QtCore.QRect(10, 250, 101, 23))
        self.queryButton.setObjectName(_fromUtf8("queryButton"))
        self.queryText = QtGui.QTextEdit(self.groupBox_3)
        self.queryText.setGeometry(QtCore.QRect(10, 20, 551, 111))
        self.queryText.setDocumentTitle(_fromUtf8(""))
        self.queryText.setObjectName(_fromUtf8("queryText"))
        self.queryOutput = QtGui.QTextEdit(self.groupBox_3)
        self.queryOutput.setGeometry(QtCore.QRect(10, 160, 551, 81))
        self.queryOutput.setDocumentTitle(_fromUtf8(""))
        self.queryOutput.setReadOnly(True)
        self.queryOutput.setObjectName(_fromUtf8("queryOutput"))
        self.radioSelect = QtGui.QRadioButton(self.groupBox_3)
        self.radioSelect.setGeometry(QtCore.QRect(10, 140, 91, 17))
        self.radioSelect.setChecked(True)
        self.radioSelect.setObjectName(_fromUtf8("radioSelect"))
        self.radioExec = QtGui.QRadioButton(self.groupBox_3)
        self.radioExec.setGeometry(QtCore.QRect(100, 140, 151, 17))
        self.radioExec.setObjectName(_fromUtf8("radioExec"))
        self.tabs.addTab(self.queryTab, _fromUtf8(""))
        self.dumpTab = QtGui.QWidget()
        self.dumpTab.setObjectName(_fromUtf8("dumpTab"))
        self.label_18 = QtGui.QLabel(self.dumpTab)
        self.label_18.setGeometry(QtCore.QRect(200, 10, 71, 20))
        self.label_18.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.dumpTab)
        self.label_19.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.label_19.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.dumpTab)
        self.label_20.setGeometry(QtCore.QRect(270, 40, 31, 20))
        self.label_20.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.dumpTab)
        self.label_21.setEnabled(True)
        self.label_21.setGeometry(QtCore.QRect(140, 40, 41, 20))
        self.label_21.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineTable = QtGui.QLineEdit(self.dumpTab)
        self.lineTable.setGeometry(QtCore.QRect(50, 10, 141, 20))
        self.lineTable.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineTable.setObjectName(_fromUtf8("lineTable"))
        self.lineTo = QtGui.QLineEdit(self.dumpTab)
        self.lineTo.setGeometry(QtCore.QRect(300, 40, 71, 20))
        self.lineTo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineTo.setObjectName(_fromUtf8("lineTo"))
        self.lineColumns = QtGui.QLineEdit(self.dumpTab)
        self.lineColumns.setGeometry(QtCore.QRect(260, 10, 321, 20))
        self.lineColumns.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineColumns.setObjectName(_fromUtf8("lineColumns"))
        self.lineFrom = QtGui.QLineEdit(self.dumpTab)
        self.lineFrom.setEnabled(True)
        self.lineFrom.setGeometry(QtCore.QRect(180, 40, 71, 20))
        self.lineFrom.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineFrom.setObjectName(_fromUtf8("lineFrom"))
        self.lineKey = QtGui.QLineEdit(self.dumpTab)
        self.lineKey.setGeometry(QtCore.QRect(80, 40, 41, 20))
        self.lineKey.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineKey.setObjectName(_fromUtf8("lineKey"))
        self.label_2 = QtGui.QLabel(self.dumpTab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 51, 20))
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableWidget = QtGui.QTableWidget(self.dumpTab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 571, 451))
        self.tableWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.dmpButton = QtGui.QCommandLinkButton(self.dumpTab)
        self.dmpButton.setGeometry(QtCore.QRect(380, 30, 91, 41))
        self.dmpButton.setObjectName(_fromUtf8("dmpButton"))
        self.progressBarDump = QtGui.QProgressBar(self.dumpTab)
        self.progressBarDump.setEnabled(True)
        self.progressBarDump.setGeometry(QtCore.QRect(10, 550, 571, 16))
        self.progressBarDump.setAcceptDrops(False)
        self.progressBarDump.setToolTip(_fromUtf8(""))
        self.progressBarDump.setStatusTip(_fromUtf8(""))
        self.progressBarDump.setMaximum(0)
        self.progressBarDump.setProperty("value", 0)
        self.progressBarDump.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarDump.setTextVisible(True)
        self.progressBarDump.setOrientation(QtCore.Qt.Horizontal)
        self.progressBarDump.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBarDump.setObjectName(_fromUtf8("progressBarDump"))
        self.label_14 = QtGui.QLabel(self.dumpTab)
        self.label_14.setGeometry(QtCore.QRect(190, 530, 321, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.killDumpButton = QtGui.QToolButton(self.dumpTab)
        self.killDumpButton.setGeometry(QtCore.QRect(490, 40, 91, 21))
        self.killDumpButton.setObjectName(_fromUtf8("killDumpButton"))
        self.tabs.addTab(self.dumpTab, _fromUtf8(""))
        self.logTxtEdit = QtGui.QTextEdit(self.centralwidget)
        self.logTxtEdit.setGeometry(QtCore.QRect(600, 20, 501, 541))
        self.logTxtEdit.setReadOnly(True)
        self.logTxtEdit.setObjectName(_fromUtf8("logTxtEdit"))
        self.clearLogButton = QtGui.QToolButton(self.centralwidget)
        self.clearLogButton.setGeometry(QtCore.QRect(1020, 570, 81, 21))
        self.clearLogButton.setObjectName(_fromUtf8("clearLogButton"))
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSave = QtGui.QMenu(self.menubar)
        self.menuSave.setObjectName(_fromUtf8("menuSave"))
        self.menuLoad = QtGui.QMenu(self.menubar)
        self.menuLoad.setObjectName(_fromUtf8("menuLoad"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuPlugins = QtGui.QMenu(self.menubar)
        self.menuPlugins.setObjectName(_fromUtf8("menuPlugins"))
        self.menuMssql = QtGui.QMenu(self.menuPlugins)
        self.menuMssql.setObjectName(_fromUtf8("menuMssql"))
        MainForm.setMenuBar(self.menubar)
        self.saveTables = QtGui.QAction(MainForm)
        self.saveTables.setObjectName(_fromUtf8("saveTables"))
        self.saveColumns = QtGui.QAction(MainForm)
        self.saveColumns.setObjectName(_fromUtf8("saveColumns"))
        self.actionLoad_tables = QtGui.QAction(MainForm)
        self.actionLoad_tables.setObjectName(_fromUtf8("actionLoad_tables"))
        self.actionLoad_columns = QtGui.QAction(MainForm)
        self.actionLoad_columns.setObjectName(_fromUtf8("actionLoad_columns"))
        self.actionLoad_tables_2 = QtGui.QAction(MainForm)
        self.actionLoad_tables_2.setObjectName(_fromUtf8("actionLoad_tables_2"))
        self.loadTables = QtGui.QAction(MainForm)
        self.loadTables.setObjectName(_fromUtf8("loadTables"))
        self.menuEncoder = QtGui.QAction(MainForm)
        self.menuEncoder.setObjectName(_fromUtf8("menuEncoder"))
        self.menuDump = QtGui.QAction(MainForm)
        self.menuDump.setObjectName(_fromUtf8("menuDump"))
        self.saveBases = QtGui.QAction(MainForm)
        self.saveBases.setObjectName(_fromUtf8("saveBases"))
        self.actionAll = QtGui.QAction(MainForm)
        self.actionAll.setObjectName(_fromUtf8("actionAll"))
        self.loadBases = QtGui.QAction(MainForm)
        self.loadBases.setObjectName(_fromUtf8("loadBases"))
        self.menuAbout = QtGui.QAction(MainForm)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.csvExport = QtGui.QAction(MainForm)
        self.csvExport.setObjectName(_fromUtf8("csvExport"))
        self.save_cmdshell = QtGui.QAction(MainForm)
        self.save_cmdshell.setObjectName(_fromUtf8("save_cmdshell"))
        self.ssSettings = QtGui.QAction(MainForm)
        self.ssSettings.setObjectName(_fromUtf8("ssSettings"))
        self.lsSettings = QtGui.QAction(MainForm)
        self.lsSettings.setObjectName(_fromUtf8("lsSettings"))
        self.lpSettings = QtGui.QAction(MainForm)
        self.lpSettings.setObjectName(_fromUtf8("lpSettings"))
        self.spSettings = QtGui.QAction(MainForm)
        self.spSettings.setObjectName(_fromUtf8("spSettings"))
        self.qEditor = QtGui.QAction(MainForm)
        self.qEditor.setObjectName(_fromUtf8("qEditor"))
        self.actionFtp = QtGui.QAction(MainForm)
        self.actionFtp.setObjectName(_fromUtf8("actionFtp"))
        self.actionAdd_user = QtGui.QAction(MainForm)
        self.actionAdd_user.setObjectName(_fromUtf8("actionAdd_user"))
        self.actionOpenrowset = QtGui.QAction(MainForm)
        self.actionOpenrowset.setObjectName(_fromUtf8("actionOpenrowset"))
        self.actionXp_cmdshell = QtGui.QAction(MainForm)
        self.actionXp_cmdshell.setObjectName(_fromUtf8("actionXp_cmdshell"))
        self.menuSave.addAction(self.saveTables)
        self.menuSave.addAction(self.saveColumns)
        self.menuSave.addAction(self.saveBases)
        self.menuSave.addAction(self.csvExport)
        self.menuSave.addSeparator()
        self.menuSave.addAction(self.ssSettings)
        self.menuLoad.addAction(self.loadTables)
        self.menuLoad.addAction(self.loadBases)
        self.menuLoad.addSeparator()
        self.menuLoad.addAction(self.lsSettings)
        self.menuTools.addAction(self.menuEncoder)
        self.menuTools.addAction(self.qEditor)
        self.menuHelp.addAction(self.menuAbout)
        self.menuMssql.addAction(self.actionFtp)
        self.menuMssql.addAction(self.actionAdd_user)
        self.menuMssql.addAction(self.actionOpenrowset)
        self.menuMssql.addAction(self.actionXp_cmdshell)
        self.menuPlugins.addAction(self.menuMssql.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuLoad.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuPlugins.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainForm)
        self.tabs.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainForm", "GET", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainForm", "POST", None, QtGui.QApplication.UnicodeUTF8))
        self.tablesButton.setText(QtGui.QApplication.translate("MainForm", "Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.countButton.setText(QtGui.QApplication.translate("MainForm", "Count", None, QtGui.QApplication.UnicodeUTF8))
        self.getColumnsButton.setText(QtGui.QApplication.translate("MainForm", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainForm", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.radioOrdinalPosition.setText(QtGui.QApplication.translate("MainForm", "ordinal_position", None, QtGui.QApplication.UnicodeUTF8))
        self.radioNotInArray.setText(QtGui.QApplication.translate("MainForm", "not in(array)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioNotInSubstring.setText(QtGui.QApplication.translate("MainForm", "not in(substring)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainForm", "Threads / Timeout:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineTimeout.setText(QtGui.QApplication.translate("MainForm", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("MainForm", "MSSQL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("MainForm", "MySQL", None, QtGui.QApplication.UnicodeUTF8))
        self.lineMS.setText(QtGui.QApplication.translate("MainForm", "~", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainForm", "Match symbol:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainForm", "Match pattern:", None, QtGui.QApplication.UnicodeUTF8))
        self.logButton.setText(QtGui.QApplication.translate("MainForm", "Show log", None, QtGui.QApplication.UnicodeUTF8))
        self.isRndUpper.setText(QtGui.QApplication.translate("MainForm", "Random UpCase", None, QtGui.QApplication.UnicodeUTF8))
        self.killButton.setText(QtGui.QApplication.translate("MainForm", "Kill task", None, QtGui.QApplication.UnicodeUTF8))
        self.lineUrl.setText(QtGui.QApplication.translate("MainForm", "http://192.168.1.35/Default.aspx?db=mssql&id=1 and 1=[sub];[cmd]--", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainForm", "URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainForm", "Tables total:", None, QtGui.QApplication.UnicodeUTF8))
        self.totalLabel.setText(QtGui.QApplication.translate("MainForm", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("MainForm", "%p%", None, QtGui.QApplication.UnicodeUTF8))
        self.cleanThreeButton.setText(QtGui.QApplication.translate("MainForm", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.treeOfTables.setSortingEnabled(False)
        self.treeOfTables.headerItem().setText(0, QtGui.QApplication.translate("MainForm", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainForm", "db:", None, QtGui.QApplication.UnicodeUTF8))
        self.getBasesButton.setText(QtGui.QApplication.translate("MainForm", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainForm", "Cookies:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainForm", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.db_structureTab), QtGui.QApplication.translate("MainForm", "db structure", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainForm", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.queryButton.setText(QtGui.QApplication.translate("MainForm", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSelect.setText(QtGui.QApplication.translate("MainForm", " SELECT TOP", None, QtGui.QApplication.UnicodeUTF8))
        self.radioExec.setText(QtGui.QApplication.translate("MainForm", "STACKED QURY", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.queryTab), QtGui.QApplication.translate("MainForm", "query", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainForm", "Columns:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainForm", "Primary key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainForm", "To:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainForm", "From:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineTable.setText(QtGui.QApplication.translate("MainForm", "customers", None, QtGui.QApplication.UnicodeUTF8))
        self.lineTo.setText(QtGui.QApplication.translate("MainForm", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.lineColumns.setText(QtGui.QApplication.translate("MainForm", "id;username;password;email", None, QtGui.QApplication.UnicodeUTF8))
        self.lineFrom.setText(QtGui.QApplication.translate("MainForm", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineKey.setText(QtGui.QApplication.translate("MainForm", "id", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainForm", "Table:", None, QtGui.QApplication.UnicodeUTF8))
        self.dmpButton.setText(QtGui.QApplication.translate("MainForm", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBarDump.setFormat(QtGui.QApplication.translate("MainForm", "%p%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#ff0000;\">WARNING: Separate thread pool for each column!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.killDumpButton.setText(QtGui.QApplication.translate("MainForm", "Kill task", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.dumpTab), QtGui.QApplication.translate("MainForm", "dump", None, QtGui.QApplication.UnicodeUTF8))
        self.clearLogButton.setText(QtGui.QApplication.translate("MainForm", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSave.setTitle(QtGui.QApplication.translate("MainForm", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLoad.setTitle(QtGui.QApplication.translate("MainForm", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainForm", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainForm", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlugins.setTitle(QtGui.QApplication.translate("MainForm", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMssql.setTitle(QtGui.QApplication.translate("MainForm", "mssql", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTables.setText(QtGui.QApplication.translate("MainForm", "Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.saveColumns.setText(QtGui.QApplication.translate("MainForm", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_tables.setText(QtGui.QApplication.translate("MainForm", "Load tables", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_columns.setText(QtGui.QApplication.translate("MainForm", "Load columns", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_tables_2.setText(QtGui.QApplication.translate("MainForm", "Load tables", None, QtGui.QApplication.UnicodeUTF8))
        self.loadTables.setText(QtGui.QApplication.translate("MainForm", "Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEncoder.setText(QtGui.QApplication.translate("MainForm", "Encoder", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDump.setText(QtGui.QApplication.translate("MainForm", "Dump", None, QtGui.QApplication.UnicodeUTF8))
        self.saveBases.setText(QtGui.QApplication.translate("MainForm", "Bases", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAll.setText(QtGui.QApplication.translate("MainForm", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.loadBases.setText(QtGui.QApplication.translate("MainForm", "Bases", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setText(QtGui.QApplication.translate("MainForm", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.csvExport.setText(QtGui.QApplication.translate("MainForm", "Dump to csv", None, QtGui.QApplication.UnicodeUTF8))
        self.save_cmdshell.setText(QtGui.QApplication.translate("MainForm", "xp_cmdshell output", None, QtGui.QApplication.UnicodeUTF8))
        self.ssSettings.setText(QtGui.QApplication.translate("MainForm", "Site settings", None, QtGui.QApplication.UnicodeUTF8))
        self.lsSettings.setText(QtGui.QApplication.translate("MainForm", "Site settings", None, QtGui.QApplication.UnicodeUTF8))
        self.lpSettings.setText(QtGui.QApplication.translate("MainForm", "Program settings", None, QtGui.QApplication.UnicodeUTF8))
        self.spSettings.setText(QtGui.QApplication.translate("MainForm", "Program settings", None, QtGui.QApplication.UnicodeUTF8))
        self.qEditor.setText(QtGui.QApplication.translate("MainForm", "Query editor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFtp.setText(QtGui.QApplication.translate("MainForm", "ftp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_user.setText(QtGui.QApplication.translate("MainForm", "add_user", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenrowset.setText(QtGui.QApplication.translate("MainForm", "openrowset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionXp_cmdshell.setText(QtGui.QApplication.translate("MainForm", "xp_cmdshell", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainForm = QtGui.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

