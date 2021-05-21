# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:09:41 2021

@author: Nima
"""
from ..config.myconnection import MyConnection
from ..model.loan import Loan


class LoanDao:
    __db = None
    def __init__(self):
        self.__db = MyConnection()
        
    def findAll(self):
        return self.__db.query('SELECT * FROM Loan', None).fetchall()
        self.__db.close()
        
    def save (self, loan: Loan) -> Loan:
        
        sql = 'INSERT INTO Loan (Num_Loan, Num_Agency, Num_Customer, Amount ) VALUES({}, {}, {}, {});'.format(loan.Num_Loan, loan.Num_Agency, loan.Num_Customer, loan.Amount )
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    
    #     # pass
    def findById(self, t: int) -> Loan:
        query = 'SELECT * FROM Loan WHERE Num_Loan = {}'.format(str(t))
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    #     # pass
    def update(self, loan: Loan) -> Loan:
        sql = 'UPDATE Loan SET Num_Agency = {}, Num_Customer = {}, Amount = {} WHERE Num_Loan = {} '.format(loan.Num_Agency , loan.Num_Customer ,loan.Amount, loan.Num_Loan )
        self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        
        return
    
    def remove(self, t: Loan) -> None:
        sql = 'DELETE FROM Loan WHERE Num_Loan = "{}"'.format(str(t.Num_Loan))
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    def show_column(self):
        
        query = 'SHOW COLUMNS FROM loan'
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    
    def dropTable(self,tableName: str):
        sql = 'TRUNCATE TABLE {}'.format(tableName)
        cr = self.__db.query( sql, None)
        self.__db.close()
        return cr
    
    # def selectByOrder(self):
    #     sql = 'SELECT * FROM Loan ORDER BY login'
    #     cr = self.__db.query( sql, None).fetchall()
    #     self.__db.close()
    #     return cr
    
    def limitSelect(self, limit:int, offset:int):
        sql = 'SELECT * FROM Loan LIMIT {} OFFSET {}'.format(limit,offset)
        cr = self.__db.query( sql, None).fetchall()
        self.__db.close()
        return cr
        
        
        
    
