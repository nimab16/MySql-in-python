# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:09:41 2021

@author: Nima
"""
from ..config.myconnection import MyConnection
from ..model.user import User
# from .dao import Dao

class UserDao:
    __db = None
    def __init__(self):
        self.__db = MyConnection()
        
    def findAll(self):
        return self.__db.query('SELECT * FROM user', None).fetchall()
        self.__db.close()
        
    def save (self, user: User) -> User:
        
        sql = 'INSERT INTO user (login, password, admin) VALUES("{}", "{}", {});'.format(user.login,user.password, user.admin)
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    
        # pass
    def findById(self, t: int) -> User:
        query = 'SELECT * FROM user WHERE Id = {}'.format(str(t))
        print(query)
        cr =self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    
    def findByName(self, name: str):
        query = 'SELECT * FROM user WHERE login = "{}"'.format(name)
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    
    def login(self, user: User) -> User:
        cr = ''
        query = 'SELECT admin FROM user WHERE login = "{}" and password = "{}"'.format(str(user.login), str(user.password))
        print(query)
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
        # pass
    def update(self, user: User) -> User:
        sql = 'UPDATE user SET password = "{}", admin = {} , login = "{}" WHERE Id = {} '.format(user.password,user.admin, user.login, user.Id)
        print(sql)
        self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        
        return
    
    def remove(self, t: User) -> None:
        sql = 'DELETE FROM user WHERE Id = "{}"'.format(str(t.Id))
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    
    def dropTable(self,tableName: str):
        sql = 'TRUNCATE TABLE {}'.format(tableName)
        cr = self.__db.query( sql, None)
        self.__db.close()
        return cr
    
    def selectByOrder(self):
        sql = 'SELECT * FROM user ORDER BY login'
        cr = self.__db.query( sql, None).fetchall()
        self.__db.close()
        return cr
    
    def limitSelect(self, limit:int, offset:int):
        sql = 'SELECT * FROM user LIMIT {} OFFSET {}'.format(limit,offset)
        cr = self.__db.query( sql, None).fetchall()
        self.__db.close()
        return cr
        
    def show_column(self):
        
        query = 'SHOW COLUMNS FROM user'
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
        
        
    
