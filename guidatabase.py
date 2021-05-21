# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:34:10 2021

@author: Nima
"""

import os, sys, math, pdb

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QWidget
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import numpy as np
from numpy import *
from mysql.connector import Error
from src.model.agency import Agency
from src.model.customer import Customer
from src.model.account import Account
from src.model.loan import Loan
from src.model.user import User
from controlers.methods import Methods
from controlers.setlevelvisibility import SetLevelVisibility


from gui import Ui_MainWindow
import controlers.customdialog as customdialog
import xlsxwriter

textComDatabase = textComMethod =''
numberComDatbase = numberComMethod = levele_search = 0
userName = password = ''

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.showMaximized()

########################################################################
        self.ui.btn_process.clicked.connect(self.process_button)
        self.ui.cm_database.currentIndexChanged.connect(self.combo_database)
        self.ui.tabWidget.currentChanged.connect(self.show_contain_tab)
        self.ui.btn_login.clicked.connect(self.login_process)
        self.ui.btn_logout.clicked.connect(self.logOut)
        self.ui.btn_save_excel.clicked.connect(self.save_click)
        # self.show_group(0)
        # self.show_insert_gp(0)
#######################################################################
    def selectall(self,idNum = 1):
        resultToShow = Methods.slect_all(numberComDatbase)
        return resultToShow
    
    
    
    def logOut(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        
    def login_process(self):
        global userName, password , levele_search
        
        userName = self.ui.et_user_name.text()
        password = self.ui.et_password.text()
        levele_search = Methods.select_login(userName, password)
        
        if levele_search != -1:
            self.ui.lable_login_name.setText('Welcome ' + str(userName))
            SetLevelVisibility.setVisibility(self, levele_search )
            
        else:
            self.ui.lb_result_login.setText('Incorrect userName or Password')
            
                
        print(levele_search)
        
   
            
            
    def process_button(self):
        print('process_button')
        global resultToShow, textComDatabase,dataSelect, colmn_name
        numberComMethod = self.ui.tabWidget.currentIndex()
        
        # select all
        if numberComMethod == 0:
            # self.ui.txt_result.setText(textComDatabase + '-----------')
            colmn_name = Methods.show_column_name(numberComDatbase)
            dataSelect = Methods.slect_all(numberComDatbase, int(self.ui.spinBox_offset.text()), int(self.ui.spinBox_limit.text()))
            self.set_table_value(dataSelect, colmn_name, self.ui.table_seelctall)
            # for data in resultToShow:
                
            #     self.set_text_browser_selectall(str(data))
        # insert
        elif numberComMethod == 2:
            
            self.ui.txt_result_insert.setText(textComDatabase + ' ------------------')
            re = self.create_object_for_insert(numberComDatbase)
            resultToShow = Methods.insert(numberComDatbase, re )
            self.set_text_browser_insert(str(resultToShow))
            result = self.selectall()
            for data in result:
                
                self.set_text_browser_insert(str(data))
            
        # find by id 
        elif numberComMethod == 1:
            # self.ui.txt_findbyid.setText(textComDatabase + ' ------------------')
            # self.set_text_browser_findbyid('')
            colmn_name = Methods.show_column_name(numberComDatbase)
            idR = self.ui.et_find_by_id.text()
            name = self.ui.et_find_name.text()
            resultToShow = Methods.find_by_id(numberComDatbase, idR , name)
            self.set_table_value(resultToShow, colmn_name, self.ui.table_findbyid)
            # print(idR)
        
        # update
        elif numberComMethod == 3:
            
            self.alert_update('Update', 'Do you want to update this data?')

            
        # delete
        elif numberComMethod == 4:
            
            self.alert_delete('Delete', 'Do you want to delete this data?')
           
            
    def combo_database(self):
        print('combo_database')
        global textComDatabase, numberComDatbase, numberComMethod
        textComDatabase = self.ui.cm_database.currentText()
        numberComDatbase = self.ui.cm_database.findText(textComDatabase, QtCore.Qt.MatchFixedString)
        self.show_contain_tab()
        # if numberComMethod ==4:
        #     self.show_insert_gp(numberComDatbase)
            
    def combo_method(self):
        print('combo_method')
        global textComMethod, numberComMethod
        textComMethod = self.ui.cm_method.currentText()
        numberComMethod = self.ui.cm_method.findText(textComMethod, QtCore.Qt.MatchFixedString)
        # self.show_group(numberComMethod)
        
    def show_contain_tab(self):
        global numberComDatbase, numberComMethod
        numberComMethod = self.ui.tabWidget.currentIndex()
        print(numberComMethod)
        self.ui.btn_save_excel.setText('Save as Excel')
        if numberComMethod == 0:
            print(numberComMethod)
        elif numberComMethod == 1:
             SetLevelVisibility.set_visible_findbyid(self, numberComDatbase)
        
        elif numberComMethod == 2:
            # self.show_insert_gp()
            SetLevelVisibility.show_insert_gp(self, numberComDatbase)
        
        elif numberComMethod == 3:
            # self.show_update_gp()
            SetLevelVisibility.show_update_gp(self, numberComDatbase)
            
        elif numberComMethod == 4:
            # self.show_delete_gp()
            SetLevelVisibility.show_delete_gp(self, numberComDatbase)
            
    
  
    def create_object_for_insert(self, numberDatabase):
        
        try:
            resultObj = object
            if numberDatabase == 1:
                name = self.ui.et_ag_name.text()
                city = self.ui.et_ag_city.text()
                active = self.ui.et_ag_active.text()
                resultObj = Agency(0,name,city, active)
                
            elif numberDatabase == 2:
                name = self.ui.et_customer_name.text()
                city = self.ui.et_customer_city.text()
                resultObj = Customer(0, name, city)
            
            elif numberDatabase == 3:
                numAgency = int(self.ui.et_account_num_agency.text())
                customer = int(self.ui.et_account_num_customer.text())
                balance = float(self.ui.et_account_account.text())
                resultObj = Account(0, int(numAgency) ,int(customer), float(balance))
                  
            elif numberDatabase == 4:
                numAgency = int(self.ui.et_loan_num_agency.text())
                customer = int(self.ui.et_loan_num_customer.text())
                amount = float(self.ui.et_loan_amount.text())
                resultObj = Loan(0, int(numAgency) ,int(customer), float(amount))
                
            elif numberDatabase == 4:
                numAgency = int(self.ui.et_loan_num_agency.text())
                customer = int(self.ui.et_loan_num_customer.text())
                amount = float(self.ui.et_loan_amount.text())
                resultObj = Loan(0, int(numAgency) ,int(customer), float(amount))
                
            elif numberDatabase == 5:
                login = str(self.ui.et_user_login.text())
                password = str(self.ui.et_user_pass.text())
                admin = int(self.ui.et_user_admin.text())
                resultObj = User(0, login , password, admin)
                
            return resultObj
        
        except :
            resultObj = ''
            return resultObj
    
    def create_object_for_update(self):
        global numberComDatbase
        resultObj = object
        if numberComDatbase == 1:
            
            num_agency = int(self.ui.et_update_agency.text())
            resultToShow = Methods.find_by_id(numberComDatbase, num_agency )
            name = self.ui.et_update_agency_name.text()
            if name == '':
                name =  resultToShow[0][1]
            
            city = self.ui.et_update_agency_city.text()
            if city == '':
                city =  resultToShow[0][2]
            active = self.ui.et_update_agency_active.text()
            if active == '':
                active =  resultToShow[0][3]
            resultObj = Agency(num_agency, name ,city, active)
            
        elif numberComDatbase == 2:
            num_customer= int(self.ui.et_update_customer.text())
            resultToShow = Methods.find_by_id(numberComDatbase, num_customer )
            name = self.ui.et_update_customer_name.text()
            if name == '':
                name =  resultToShow[0][1]
            city = self.ui.et_update_customer_city.text()
            if city == '':
                city =  resultToShow[0][2]
            resultObj = Customer(num_customer, name ,city)
            
        
        elif numberComDatbase == 3:
            
            num_account= int(self.ui.et_update_account.text())
            resultToShow = Methods.find_by_id(numberComDatbase, num_account )
            
            numAgency = self.ui.et_update_account_agency.text()
            if numAgency == '':
                numAgency =  resultToShow[0][1]
            numAgency = int(numAgency)
            
            customer = self.ui.et_update_account_customer.text()
            if customer == '':
                customer =  resultToShow[0][2]
            customer = int(customer)    
            
            balance = self.ui.et_update_account_balanc.text()
            if balance == '':
                balance =  resultToShow[0][3]
            balance = float(balance)
            
            resultObj = Account(num_account, numAgency,customer, balance)
              
        elif numberComDatbase == 4:
            num_loan= int(self.ui.et_update_loan.text())
            resultToShow = Methods.find_by_id(numberComDatbase, num_loan )
            
            numAgency = self.ui.et_update_loan_agency.text()
            if numAgency == '':
                numAgency =  resultToShow[0][1]
            numAgency = int(numAgency)
            
            customer = self.ui.et_update_loan_customer.text()
            if customer == '':
                customer =  resultToShow[0][2]
            customer = int(customer)    
            
            amount = self.ui.et_update_loan_amount.text()
            if amount == '':
                amount =  resultToShow[0][3]
            amount = float(amount)
                
            resultObj = Loan(num_loan, numAgency ,customer, amount)
            
        elif numberComDatbase == 5:
            Id= int(self.ui.et_update_user_Id.text())
            resultToShow = Methods.find_by_id(numberComDatbase, Id )
            
            login = str(self.ui.et_update_user_login.text())
            if login == '':
                login =  resultToShow[0][1]
            login = str(login)
            
            password = self.ui.et_update_user_pass.text()
            if password == '':
                password =  resultToShow[0][2]
            password = str(password)
            
            admin = self.ui.et_update_user_admin.text()
            if admin == '':
                admin =  resultToShow[0][3]
            admin = int(admin)    
            
                
            resultObj = User(Id ,login, password ,admin)
            
        return resultObj
    
    def create_object_for_delete(self):
        global numberComDatbase
        resultObj = object
        if numberComDatbase == 1:
            num = int(self.ui.et_delete_agancy.text())
            resultObj = Agency(num)
            
        elif numberComDatbase == 2:
            num = int(self.ui.et_delete_customer.text())
            resultObj = Customer(num)
        
        elif numberComDatbase == 3:
            num = int(self.ui.et_delete_active.text())
            resultObj = Account(num)
              
        elif numberComDatbase == 4:
            num = int(self.ui.et_delete_loan.text())
            resultObj = Loan(num)
            
        elif numberComDatbase == 5:
            num = int(self.ui.et_delete_user.text())
            resultObj = User(num)
            
        return resultObj  
    
    def set_table_value(self,data, coulmn_name, table_name):
            
            row = len(data) + 1
            column = len(coulmn_name)
            table_name.setRowCount(row)
            table_name.setColumnCount(column)
            # self.ui.table_seelctall.verticalHeader.setVisible(False)
            
            for j in range (0,len(coulmn_name)):
                
                table_name.setItem(0,j, QTableWidgetItem(coulmn_name[j]))
            
            
            for i in range(0, len(data)):
                
                for k in range(0, len(coulmn_name)):
                    
                    table_name.setItem(i+1,k, QTableWidgetItem( str(data[i][k])))
                   
            
           
    def set_text_browser(self,text):
            self.ui.txt_result.append(text)
            
    def set_text_browser_findbyid(self,text):
            self.ui.txt_findbyid.append(text)
            
    def set_text_browser_insert(self,text):
            self.ui.txt_result_insert.append(text)
            
    def set_text_browser_update(self,text):
            self.ui.txt_update.append(text)
            
    def set_text_browser_delete(self,text):
            self.ui.txt_delete.append(text)
    
    ## save as a excel file ####
    def save_click(self):
        
        global numberComMethod, dataSelect, colmn_name
        if numberComMethod == 0:
           self.save_excel(dataSelect, colmn_name) 
        
        elif numberComMethod == 4:
            self.alert_drop_table('Drop table', 'Do you want to empty this table? (Data can not be restored)')
        else:
            self.alert_save_excel('Save', 'Please go to tab SelectAll')
            
    def save_excel(self, data, column_name):
        try:
            
            tableName = self.ui.cm_database.currentText()
            result = []
            result.append(column_name)
            for da in data:
                result.append(da)
            print(result)
            
            new_list = result
            # open dialog for save 
            filename = self.saveFileDialog(tableName)
            # name = QFileDialog.getSaveFileName(self, 'Save File')
            # file = open(name,'w')
            # text = self.textEdit.toPlainText()
            # file.write(text)
            # file.close()
            if filename != '':
            
                fileOut = filename
                with xlsxwriter.Workbook(fileOut) as workbook:
                    worksheet = workbook.add_worksheet()
        
                    for row_num, data in enumerate(new_list):
                        worksheet.write_row(row_num, 0, data)
                        
                # self.alert_save_excel('Save', 'Data saved succefully')
                
        except :
            self.alert_save_excel('Save', 'Error')
            print('result')
            
    def saveFileDialog(self, tablename):
        fileName =''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save as Excel","{}.xlsx".format(tablename),"All Files (*);;Text Files (*.xls)", options=options)
        return fileName
        
    ##### alert ###########
    def alert_delete(self, tiltle, textMessage):
        print("click")
        customdialog.textCustom = textMessage
        customdialog.titleCustom = tiltle
        dlg = customdialog.CustomDialog()  # If you pass self, the dialog will be centered over the main window as before.
        if dlg.exec_():
            
            self.ui.txt_delete.setText(textComDatabase + ' ------------------')
            re = self.create_object_for_delete()
            resultToShow = Methods.delete(numberComDatbase, re )
            self.set_text_browser_delete(str(resultToShow))
            result = self.selectall()
            for data in result:
                
                self.set_text_browser_delete(str(data))
            print("Success!")
        else:
            print("Cancel!")  
            
    def alert_update(self, tiltle, textMessage):
        print("click")
        customdialog.textCustom = textMessage
        customdialog.titleCustom = tiltle
        dlg = customdialog.CustomDialog()  # If you pass self, the dialog will be centered over the main window as before.
        if dlg.exec_():
            self.ui.txt_update.setText(textComDatabase + ' ------------------')
            re = self.create_object_for_update()
            resultToShow = Methods.update(numberComDatbase, re )
            self.set_text_browser_update(str(resultToShow))
            result = self.selectall()
            # for data in result:
                
            self.set_text_browser_update(str(result))
            print("Success!")
        else:
            print("Cancel!")  
            
    def alert_save_excel(self, tiltle, textMessage):
        customdialog.textCustom = textMessage
        customdialog.titleCustom = tiltle
        dlg = customdialog.Alert_CustomDialog()  # If you pass self, the dialog will be centered over the main window as before.
        if dlg.exec_():
           
            print("Success!")
        # else:
        #     print("Cancel!")  
            
    def alert_drop_table(self, tiltle, textMessage):
        print("click")
        customdialog.textCustom = textMessage
        customdialog.titleCustom = tiltle
        dlg = customdialog.CustomDialog()  # If you pass self, the dialog will be centered over the main window as before.
        if dlg.exec_():
            
            self.ui.txt_delete.setText(textComDatabase + ' ------------------')
            
            resultToShow = Methods.dropTable(numberComDatbase)
            self.set_text_browser_delete(str(resultToShow))
            result = self.selectall()
            for data in result:
                
                self.set_text_browser_delete(str(data))
            print("Success!")
        else:
            print("Cancel!")  
########################################################################

    # def closeEvent(self,event):
    #     QApplication.quit()
        
def myExitHandler():
        print('Exit')
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(myExitHandler)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
