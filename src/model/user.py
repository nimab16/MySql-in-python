# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:43:52 2021

@author: Nima
"""

class User:
    def __init__ (self, Id: int = 0, login: str = '', password: str = '', admin: int = 0):
        self._id = Id 
        self._login = login
        self._password = password
        self._admin = admin
    @property 
    def Id(self) -> int:
        return self._id
    
    @Id.setter
    def Id(self, Id) -> None: 
        if Id > 0:
            self._id = Id 
        else:
            self._id = 0
    
    @property
    def login (self) -> str:
        return self._login
    
    @login.setter
    def login(self, login) -> None:
        self._login = login
        
    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password (self,password) -> None:
        self._password = password
        
    @property
    def admin(self) -> int:
        
        return self._admin
    
    @admin.setter
    def admin (self,admin) -> None:
        self._admin = admin
        
    @password.deleter
    def password(self) -> None:
        del self._password
        
    def __str__(self)-> str:
        return str(self._id) + ' ' + self._login + ' ' + self._password
        
        
        
