# -*- coding: utf-8 -*-

# Do things the hard way for a long time
#   then learn efficiencies

# from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as s3



class Ui_toolhouse(object):
    def database_connect(self):
        self.connection = s3.connect('toolhouse.db')

    # query = 'PRAGMA table_info(PRODUCT)'
    ## massively important; get's the table column names

    def clear_table(self):
        self.tableWidget.clear()

    # @pyqtSlot() hey man this thing broke the program
    #   unsure if needed
    def get_all_products(self):
        self.query = 'SELECT * FROM product'
        result = self.connection.execute(self.query)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number,
                    column_number,
                    QtWidgets.QTableWidgetItem(
                        str(data)
                    )
                )
        
        # TODO use PRAGMA table info to get table headings
        self.query
        pass

    def get_store_names(self):
        
        pass


    def setupUi(self, toolhouse):
        # establish database connection
        self.database_connect()

        # create base window
        toolhouse.setObjectName("toolhouse")
        toolhouse.resize(1449, 1189)
        self.tabWidget = QtWidgets.QTabWidget(toolhouse)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1401, 701))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)

        # create tab widget for navigation
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        # for tab 1, create
        ## create combo box, dropdown box
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(290, 400, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        
        ## create label to go in front of dropdown box
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 410, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        ## create label to go on top of window
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 1011, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        ## create label to go in front of other dropdown box
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 470, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        ## create second combo box 
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 460, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")

        ### add code later for store locations
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        ## create submit button
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(770, 400, 271, 111))
        self.pushButton_11.setObjectName("pushButton_11")

        # new tab for order details
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        ## create button to get all orders
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 570, 191, 81))
        self.pushButton.setObjectName("pushButton")

        ## create line edit to take in order ID
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(170, 310, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        ##### and so on and so forth. mostly following documentation
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 310, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1011, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 310, 150, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        
        # create get all products button
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 570, 241, 81))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.get_all_products)

        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(780, 370, 161, 46))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_8.setGeometry(QtCore.QRect(780, 450, 161, 46))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(780, 530, 161, 46))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(10, 300, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 240, 291, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 410, 481, 151))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(10, 370, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox.setGeometry(QtCore.QRect(200, 300, 79, 31))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 190, 231, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(10, 190, 301, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_5.setGeometry(QtCore.QRect(10, 0, 1001, 171))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.spinBox = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox.setGeometry(QtCore.QRect(430, 300, 61, 31))
        self.spinBox.setObjectName("spinBox")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(500, 190, 150, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(310, 300, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_9)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 30, 1011, 151))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 460, 231, 111))
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_9)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 390, 751, 261))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_9, "")
        self.tableWidget = QtWidgets.QTableWidget(toolhouse)
        self.tableWidget.setGeometry(QtCore.QRect(10, 710, 1431, 401))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")

        # create clear table button
        self.pushButton_3 = QtWidgets.QPushButton(toolhouse)
        self.pushButton_3.setGeometry(QtCore.QRect(1210, 1130, 221, 46))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.clear_table)

        self.retranslateUi(toolhouse)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(toolhouse)

    def retranslateUi(self, toolhouse):

        # this sets all the text and HTML spacing of the widgets in the window
        _translate = QtCore.QCoreApplication.translate
        toolhouse.setWindowTitle(_translate("toolhouse", "Dialog"))
        self.label.setText(_translate("toolhouse", "Select Store Name:"))
        self.label_2.setText(_translate("toolhouse", "Please select a store and catagory to see details for that store"))
        self.label_5.setText(_translate("toolhouse", "Select Store Detail:"))
        self.comboBox_2.setItemText(0, _translate("toolhouse", "Contact Info"))
        self.comboBox_2.setItemText(1, _translate("toolhouse", "Inventory"))
        self.comboBox_2.setItemText(2, _translate("toolhouse", "Departments"))
        self.pushButton_11.setText(_translate("toolhouse", "SUBMIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("toolhouse", "Single Store Lookup"))
        self.pushButton.setText(_translate("toolhouse", "Get All Orders"))
        self.label_3.setText(_translate("toolhouse", "Order ID:"))
        self.textBrowser.setHtml(_translate("toolhouse", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Copy an Order ID from the order list and enter it into the box to get more details</span></p></body></html>"))
        self.pushButton_6.setText(_translate("toolhouse", "SUBMIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("toolhouse", "Retrieve Order Details"))
        self.pushButton_5.setText(_translate("toolhouse", "Refresh Products List"))
        self.pushButton_7.setText(_translate("toolhouse", "Insert New"))
        self.pushButton_8.setText(_translate("toolhouse", "Update Existing"))
        self.pushButton_9.setText(_translate("toolhouse", "Delete Existing"))
        self.label_4.setText(_translate("toolhouse", "Product Name:"))
        self.label_12.setText(_translate("toolhouse", "Product Price:"))
        self.label_13.setText(_translate("toolhouse", "Product Description:"))
        self.label_14.setText(_translate("toolhouse", "Selected Product ID: "))
        self.textBrowser_5.setHtml(_translate("toolhouse", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Here you can edit the total product storage of the whole Toolhouse system. You can look up all the individual product ID\'s and edit their corrosponding fields. To enter new product, simply leave the product ID field blank.</span></p></body></html>"))
        self.pushButton_10.setText(_translate("toolhouse", "SUBMIT"))
        self.label_15.setText(_translate("toolhouse", "Quantity:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("toolhouse", "Inventory Edit"))
        self.textBrowser_2.setHtml(_translate("toolhouse", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Enter your perfect SQL Query, and get tables (or cause injection attacks)</span></p></body></html>"))
        self.pushButton_2.setText(_translate("toolhouse", "SUBMIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("toolhouse", "Advanced Lookup"))
        self.pushButton_3.setText(_translate("toolhouse", "Clear table"))


if __name__ == "__main__":
    # python main execution
    import sys

    # create application window
    app = QtWidgets.QApplication(sys.argv)

    # set application window of type dialog 
    toolhouse = QtWidgets.QDialog()

    # creat instance of ui
    ui = Ui_toolhouse()

    # call setupUI
    ui.setupUi(toolhouse)

    # show the UI in the window
    toolhouse.show()

    # execute the application, then async exit the window when finished
    sys.exit(app.exec_())

