# -*- coding: utf-8 -*-

# Do things the hard way for a long time
#   then learn efficiencies


# version for 16:9 ratio

# from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3



class Ui_toolhouse(object):

### methods for handling errors, queries, displays
    
    # prints error message inside table 
    def error_msg(self, e):
        err_string = (str(e.__class__) + '{0}'.format(e))
        print (err_string)
        self.clear_table()
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderItem(0,
            QtWidgets.QTableWidgetItem(
                str('Error ->')
            )
        )
        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0,0,
            QtWidgets.QTableWidgetItem(
                err_string
            )
        )

    # cleans input to be int; if cannot be int, throw error
    def clean_id(self, input):

        try:
            i = int(input)
            return i
        except ValueError as e:
            self.error_msg(e)

    # makes connection to database
    def database_connect(self):    
        self.connection = sqlite3.connect('toolhouse.db')

    # gets table headings from the connection exeuction, resulting in cursor
    def set_table_headings(self, cursor):
        column_names = []
        try:
            column_names = [names[0] for names in cursor.description]
        except (TypeError, UnboundLocalError,AttributeError) as e:
            self.error_msg(e)
        self.tableWidget.setColumnCount(len(column_names))
        i = 0
        for name in column_names:
            self.tableWidget.setHorizontalHeaderItem(
                i,
                QtWidgets.QTableWidgetItem(
                    str(name)
                )
            )
            i+=1

    # displays the results of the query
    def table_update(self, cursor):
        self.clear_table()
        self.set_table_headings(cursor)
        try:
            # puts whatever the query was into the table widget
            for row_number, row_data in enumerate(cursor):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(
                        row_number,
                        column_number,
                        QtWidgets.QTableWidgetItem(
                            str(data)
                        )
                    )
        except Exception as e:
            self.error_msg(e)

    # clears the table's contents
    def clear_table(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(7)

    # take in a string, and do some via other method, and update table
    def query(self, string):
        self.table_update(self.simple_query(string))

    # take in string, try the query
    def simple_query(self,s):
        string = ''''''.join(s) # to ensure single, double, or tickbacks can be used
        try:
            cursor = self.connection.execute(string)
            return cursor
        except (sqlite3.OperationalError, sqlite3.IntegrityError, sqlite3.Warning) as e:
            self.error_msg(e)

    # case where pid in 3rd tab is populated
    def product_populate(self, product):


        # needed to change the supplier combobox display
        self.supp_index = self.supp_list.index(str(product[4]))

        # place product tuple values into appropriate fields
        self.lineEdit_5.setText(str(product[0]))
        self.lineEdit_2.setText(str(product[1]))
        self.doubleSpinBox.setValue(float(product[2]))
        self.plainTextEdit_2.setPlainText(str(product[3]))
        self.comboBox_3.setCurrentIndex(self.supp_index)

    # pulls product details and returns list from tab_4
    def pull_prod_details(self):
        product = []

        product.append(str(self.lineEdit_5.text()))
        product.append(str(self.lineEdit_2.text()))
        product.append(str(self.doubleSpinBox.value()))
        product.append(str(self.plainTextEdit_2.toPlainText()))
        product.append(str(self.comboBox_3.currentText()))

        return product


### These methods are the ones that in general have the SQL statements in them

    # deletes product of given pid
    def delete_pid(self):
        pid = self.lineEdit_5.text()
        query = 'DELETE from PRODUCT where product_id = %s' % str(pid)
        self.simple_query(query)
        self.get_all_products()

    # inserts new product tuple
    def new_pid(self):
        product = self.pull_prod_details()

        query ='''
    INSERT INTO product (
                        product_id,
                        product_name,
                        product_price,
                        product_desc,
                        product_supplier_id
                    )
                    VALUES (
                        '{0[0]}',
                        '{0[1]}',
                        '{0[2]}',
                        '{0[3]}',
                        '{0[4]}'
                    );
            '''.format(product)
        self.simple_query(query)
        self.get_all_products()

    # updates selected tuple
    def update_pid(self):

        product = self.pull_prod_details()

        query = '''
    UPDATE product
   SET product_name = '{0[1]}',
       product_price = '{0[2]}',
       product_desc = '{0[3]}',
       product_supplier_id = '{0[4]}'
    WHERE product_id = '{0[0]}';
        '''.format(product)
        self.simple_query(query)
        self.get_all_products()

    # accept product ID from linedit box
    def accept_pid(self):
        pid = self.lineEdit_5.text()
        query = 'SELECT * from product where product_id = %s' % str(pid)

        # does a simple query, and fetches the first row; returns tuple
        product = None
        try:
            product = self.simple_query(query).fetchone()
        except AttributeError as e:
            self.error_msg(e)

        if product == None:
            pass
        else:
            self.product_populate(product)

    # retrieve order details by ID
    def get_order(self):
        orderID = self.lineEdit.text()

        # asserting integer
        orderID = self.clean_id(orderID)
        self.query(
        '''
        SELECT co.order_id as OrderID, c.customer_name as CustomerName , p.product_name as ProductName, oc.order_quantity as OrderQuantity, p.product_price * oc.order_quantity AS Price
        FROM order_content AS oc, customer AS c, product AS p, customer_order AS co 
        WHERE
        (
            CO.order_id= oc.corder_id
            AND
            Co.cust_id = c.customer_id
            AND
            Oc.product_id = p.product_id
            AND
            co.order_id = %s
        )
        ''' % str(orderID)
        ) # very vulnerable to SQL injection

    # retrieve all the products
    def get_all_products(self):
        self.query('SELECT * FROM PRODUCT')

    # retreive all orders
    def get_all_orders(self):
        self.query('SELECT * FROM CUSTOMER_ORDER')

    # retrieve store information, based on two combobox fields
    def get_store_info(self):
        store_name = self.comboBox.currentText()
        request = self.comboBox_2.currentText()
        if request == 'Inventory':
            self.query(
                '''
                SELECT store.store_name, product.product_name, inventory.amount
                FROM store, product, inventory
                WHERE 
                (
                    inventory.store_id = store.store_id
                    AND
                    inventory.product_id = product.product_id
                    AND
                    store.store_name = '%s'
                )
                ''' % str(store_name)
            )
        else:
            self.query(
            '''
            SELECT store.store_name, store.store_phone, store.store_email, address.building_number, address.street, address.apartment, address.city, address.state,address.country,address.zip FROM store
                join address on store.store_address_id = address.address_id
                where store.store_name = '%s'
            ''' % str(store_name)
            )

    # places all store names in tab 1
    def place_store_names(self):
        storenames = self.connection.execute(
            '''
            SELECT store_name FROM store
            '''
        )
        for s in storenames:
            self.comboBox.addItem(str(s[0]))

    # places suppplier id in tab 4
    def place_supplier_id (self):
        supp_id = self.connection.execute(
            '''
            SELECT supplier_id from supplier
            '''
        )
        self.supp_list =[]
        for s in supp_id:
            self.comboBox_3.addItem(str(s[0]))
            self.supp_list.append(str(s[0]))

        ## supp list verification print
        # print (self.supp_list)

    # let's try a generalized query
    def general_query(self):
        user_query = self.plainTextEdit.toPlainText()
        ## extremely vulerable to sql injection
        self.query(user_query)

# UI stuff
    def setupUi(self, toolhouse):
        # establish database connection
        self.database_connect()
        # create base window
        toolhouse.setObjectName("toolhouse")
        toolhouse.resize(650, 700)
        self.tabWidget = QtWidgets.QTabWidget(toolhouse)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 361))
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
        self.comboBox.setGeometry(QtCore.QRect(160, 50, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        ##  store names in dropdown
        self.place_store_names()

        ## create label to go in front of dropdown box
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 50, 141, 31))
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
        self.label_5.setGeometry(QtCore.QRect(10, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        ## create second combo box 
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 110, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")

        ## create placeholders to add options later
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        ## create submit button
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(450,220, 181, 71))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.get_store_info)

        # new tab for order details
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        ## create button to get all orders
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 240, 191, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get_all_orders)

        ## create line edit to take in order ID
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Paste OrderID; then ->")

        ##### and so on and so forth. mostly following documentation
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 571, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        # submit button
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 70, 150, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.get_order)


        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        
        # create get all products button
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 270, 131, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.get_all_products)

        # insert tuple button
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 130, 161, 46))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.new_pid)

        # update tuple button
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_8.setGeometry(QtCore.QRect(360, 170, 161, 46))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.update_pid)

        # delete tuple button :o
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(360, 210, 161, 46))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.delete_pid)

        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(0, 90, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(0, 130, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 90, 251, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(120, 180, 181, 81))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(0, 170, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")


        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox.setGeometry(QtCore.QRect(100, 130, 79, 31))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setPrefix('$')

        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 50, 231, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText('Paste ProdID; then ->')


        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(0, 50, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_5.setGeometry(QtCore.QRect(0, 0, 521, 48))
        self.textBrowser_5.setObjectName("textBrowser_5")

        # combobox for supplier
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(420, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName('comboBox_3')
        self.place_supplier_id()

        # create button to accept product ID
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(360, 50, 150, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.accept_pid)
        
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(360, 90, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_9)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 10, 541, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")

        # create submit button for generalized query
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 190, 231, 111))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.general_query)
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_9)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 190, 331, 121))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_9, "")

        # create table
        self.tableWidget = QtWidgets.QTableWidget(toolhouse)
        self.tableWidget.setGeometry(QtCore.QRect(0, 370, 641,191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clear_table()
        self.tableWidget.setObjectName("tableWidget")

        # create clear table button
        self.pushButton_3 = QtWidgets.QPushButton(toolhouse)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 570, 221, 46))
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
        self.comboBox_2.setItemText(0, _translate("toolhouse", "Inventory"))
        self.comboBox_2.setItemText(1, _translate("toolhouse", "Store Details"))
        self.pushButton_11.setText(_translate("toolhouse", "Get Store Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("toolhouse", "Single Store Lookup"))
        self.pushButton.setText(_translate("toolhouse", "Get All Orders"))
        self.label_3.setText(_translate("toolhouse", "Order ID:"))
        self.textBrowser.setHtml(_translate("toolhouse", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Copy an Order ID from the order list and enter it into the box to get details on order content, price, and name</span></p></body></html>"))
        self.pushButton_6.setText(_translate("toolhouse", "Get Order"))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Here you can edit the total product storage of the whole Toolhouse system. You can look up all the individual product ID\'s and edit their corrosponding fields. When inserting product, enter new unique ID.</span></p></body></html>"))
        self.pushButton_10.setText(_translate("toolhouse", "Get Product"))
        self.label_15.setText(_translate("toolhouse", "Supplier:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("toolhouse", "Inventory Edit"))
        self.textBrowser_2.setHtml(_translate("toolhouse", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Enter your perfect SQL Query, and get tables (or cause injection attacks) Please, use semicolons;</span></p></body></html>"))
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

