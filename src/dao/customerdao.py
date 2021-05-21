# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:09:41 2021

@author: Nima
"""
from ..config.myconnection import MyConnection
from ..model.customer import Customer


class CustomerDao:
    __db = None
    def __init__(self):
        self.__db = MyConnection()
        
    def findAll(self):
        return self.__db.query('SELECT * FROM Customer', None).fetchall()
        self.__db.close()
        
    def save (self, Customer: Customer) -> Customer:
        
        sql = 'INSERT INTO Customer (Num_Customer, Name, City) VALUES({}, "{}", "{}");'.format(Customer.Num_Customer, Customer.Name, Customer.City)
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    
    def findById(self, t: int) -> Customer:
        query = 'SELECT * FROM Customer WHERE Num_Customer = {}'.format(str(t))
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    
    def findByName(self, name: str):
        query = 'SELECT * FROM Customer WHERE Name = "{}"'.format(name)
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    #     # pass
    def update(self, customer: Customer) -> Customer:
        sql = 'UPDATE Customer SET Name = "{}", City = "{}" WHERE Num_Customer = "{}" '.format(customer.Name, customer.City, customer.Num_Customer )
        self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        
        return
    
    def remove(self, t: Customer) -> None:
        sql = 'DELETE FROM Customer WHERE Num_Customer = "{}"'.format(str(t.Num_Customer))
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    def show_column(self):
        
        query = 'SHOW COLUMNS FROM customer'
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    
    def dropTable(self,tableName: str):
        sql = 'TRUNCATE TABLE {}'.format(tableName)
        print(sql)
        cr = self.__db.query( sql, None)
        self.__db.close()
        return cr
    
    # def selectByOrder(self):
    #     sql = 'SELECT * FROM Customer ORDER BY login'
    #     cr = self.__db.query( sql, None).fetchall()
    #     self.__db.close()
    #     return cr
    
    def limitSelect(self, limit:int, offset:int):
        sql = 'SELECT * FROM Customer LIMIT {} OFFSET {}'.format(limit,offset)
        cr = self.__db.query( sql, None).fetchall()
        self.__db.close()
        return cr
        
        
        
    
