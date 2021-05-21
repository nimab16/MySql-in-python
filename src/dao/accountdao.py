# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:09:41 2021

@author: Nima
"""
from ..config.myconnection import MyConnection
from ..model.account import Account


class AccountDao:
    __db = None
    def __init__(self):
        self.__db = MyConnection()
        
    def findAll(self):
        return self.__db.query('SELECT * FROM Account', None).fetchall()
        self.__db.close()
        
    def save (self, account: Account) -> Account:
        
        sql = 'INSERT INTO Account (Num_Account, Num_Agency, Num_Customer, Balance ) VALUES({}, {}, {}, {});'.format(account.Num_Account, account.Num_Agency, account.Num_Customer, account.Balance )
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    
    #     # pass
    def findById(self, t: int) -> Account:
        query = 'SELECT * FROM Account WHERE Num_Account = {}'.format(str(t))
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    
    #     # pass
    def update(self, account: Account) -> Account:
        sql = 'UPDATE Account SET Num_Agency = {}, Num_Customer = {}, Balance = {} WHERE Num_Account = {} '.format(account.Num_Agency , account.Num_Customer, account.Balance, account.Num_Account)
        self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        
        return
    
    def remove(self, t: Account) -> None:
        sql = 'DELETE FROM Account WHERE Num_Account = "{}"'.format(str(t.Num_Account))
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    def show_column(self):
        
        query = 'SHOW COLUMNS FROM account'
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    def dropTable(self,tableName: str):
        sql = 'TRUNCATE TABLE {}'.format(tableName)
        cr = self.__db.query( sql, None)
        self.__db.close()
        return cr
    
    # def selectByOrder(self):
    #     sql = 'SELECT * FROM Account ORDER BY login'
    #     cr = self.__db.query( sql, None).fetchall()
    #     self.__db.close()
    #     return cr
    
    def limitSelect(self, limit:int, offset:int):
        sql = 'SELECT * FROM Account LIMIT {} OFFSET {}'.format(limit,offset)
        cr = self.__db.query( sql, None).fetchall()
        self.__db.close()
        return cr
        
        
        
    
