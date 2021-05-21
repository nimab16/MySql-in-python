# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:59:12 2021

@author: Nima
"""

class Customer:
    def __init__ (self, Num_Customer: int = 0, Name: str = '', City: str = ''):
        self._Num_Customer = Num_Customer 
        self._Name = Name
        self._City = City
        
        
    @property 
    def Num_Customer(self) -> int:
        return self._Num_Customer
    
    @Num_Customer.setter
    def Num_Customer(self, Num_Customer) -> None: 
        if Num_Customer > 0:
            self._Num_Customer = Num_Customer 
        else:
            self._Num_Customer = 0
    
    @property
    def Name (self) -> str:
        return self._Name
    
    @Name.setter
    def Name(self, Name) -> None:
        self._Name = Name
        
    @property
    def City(self) -> str:
        return self._City
    
    @City.setter
    def password (self,City) -> None:
        self._City = City
    
    