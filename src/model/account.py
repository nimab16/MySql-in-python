# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:49:36 2021

@author: Nima
"""

class Account:
    def __init__ (self, Num_Account: int = 0, Num_Agency: int = 0 , Num_Customer: int = 0 , Balance: float = 0):
        self._Num_Account = Num_Account 
        self._Num_Agency = Num_Agency
        self._Num_Customer = Num_Customer
        self._Balance = Balance
        
    @property 
    def Num_Account(self) -> int:
        return self._Num_Account
    
    @Num_Account.setter
    def Num_Account(self, Num_Account) -> None: 
        if Num_Account > 0:
            self._Num_Account = Num_Account 
        else:
            self._Num_Account = 0
    
    @property
    def Num_Agency (self) -> int:
        return self._Num_Agency
    
    @Num_Agency.setter
    def Name(self, Num_Agency) -> None:
        self._Num_Agency = Num_Agency
        
    @property
    def Num_Customer (self) -> int:
        return self._Num_Customer
    
    @Num_Customer.setter
    def Num_Customer(self, Num_Customer) -> None:
        self._Num_Customer = Num_Customer
        
        
    @property
    def Balance (self) -> float:
        return self._Balance
    
    @Balance.setter
    def Balance(self, Balance) -> None:
        self._Balance = Balance   
        
        
        
   