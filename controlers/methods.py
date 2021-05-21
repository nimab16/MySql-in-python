# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:30:00 2021

@author: Nima
"""

from mysql.connector import Error
from src.dao.agencydao import AgencyDao
from src.model.agency import Agency
from src.dao.customerdao import CustomerDao
from src.model.customer import Customer
from src.dao.accountdao import AccountDao
from src.model.account import Account
from src.dao.loandao import LoanDao
from src.model.loan import Loan
from src.dao.userdao import UserDao
from src.model.user import User

class Methods:
    
    def select_login(userName, password):
        result = -1
        userConf = User(0, userName , password)
        userDao = UserDao()
        adminNum = userDao.login(userConf)
        if adminNum != []:
            
            result = adminNum[0][0]
        
        # resylt = Methods.dao_name(dataBaseNumber).login(idNumber) # select by id
        return result
        
    
    def slect_all(dataBaseNumber, offset=0, limit=0):
        
        data = []
        if offset == 0 and limit == 0:
            
            for agency in Methods.dao_name(dataBaseNumber).findAll(): # select all
                # print('agency find all:')
                # print(agency)
                data.append(agency)
                
        else:
            
            for agency in Methods.dao_name(dataBaseNumber).limitSelect(limit, offset): # select all
                # print('agency find all:')
                # print(agency)
                data.append(agency)
            
        return data
    
    
    def show_column_name(dataBaseNumber):
        
        # result = Methods.dao_name(dataBaseNumber).show_column()
        # print(result)
        data = []
        for agency in Methods.dao_name(dataBaseNumber).show_column(): # select all
            agency[0]
            data.append(agency[0])
            
        return data
        
    def slect_last_row(dataBaseNumber):
        
        result = []
        result = Methods.dao_name(dataBaseNumber).findLastItem() # select by id
        return result 
    
    def find_by_id(dataBaseNumber, idNumber, name=''):
        
        result = []
        if idNumber != '' :

            result = Methods.dao_name(dataBaseNumber).findById(idNumber) # select by id
        elif  name != '' :
            result = Methods.dao_name(dataBaseNumber).findByName(name) # select by id
            
        return result
    
    def insert(dataBaseNumber, objrctClass):
        
        daoName = Methods.dao_name(dataBaseNumber)
        daoName.save(objrctClass)
        return 'data inserted succefully'
    
    def update(dataBaseNumber, objrctClass):
        
        daoName = Methods.dao_name(dataBaseNumber)
        daoName.update(objrctClass)
        return 'data updated succefully'
    
    def delete(dataBaseNumber, objrctClass):
        
        daoName = Methods.dao_name(dataBaseNumber)
        daoName.remove(objrctClass)
        return 'User is deleted'
    
    def dropTable(dataBaseNumber):
        
        daoName = Methods.dao_name(dataBaseNumber)
        tableName = ''
        
        if dataBaseNumber == 1:
            tableName = 'agency'
        
        elif dataBaseNumber == 2:
            tableName = 'customer'
             
        elif dataBaseNumber == 3:
            tableName = 'account'
            
        elif dataBaseNumber == 4:
            tableName = 'loan'
            
        elif dataBaseNumber == 5:
            tableName = 'user'
             
        daoName.dropTable(tableName)
        return 'table ' + tableName + ' is empty'
    
    def dao_name(dataBaseNumber):
        daoName = object
        if  dataBaseNumber == 1:
            agencyDao = AgencyDao()
            daoName = agencyDao
            
        elif dataBaseNumber == 2:
            customerDao = CustomerDao()
            daoName = customerDao
            
            
        elif dataBaseNumber == 3:
            
             accountDao = AccountDao()
             daoName = accountDao
             
        elif dataBaseNumber == 4:
            loanDao = LoanDao()
            daoName = loanDao
            
        elif dataBaseNumber == 5:
            userDao = UserDao()
            daoName = userDao
            
        
            
            
        return daoName   
            
            