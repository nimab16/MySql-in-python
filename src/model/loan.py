# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:49:36 2021

@author: Nima
"""

class Loan:
    def __init__ (self, Num_Loan: int = 0, Num_Agency: int = 0 , Num_Customer: int = 0 , Amount: float = 0.00):
        self._Num_Loan = Num_Loan 
        self._Num_Agency = Num_Agency
        self._Num_Customer = Num_Customer
        self._Amount = Amount
        
    @property 
    def Num_Loan(self) -> int:
        return self._Num_Loan
    
    @Num_Loan.setter
    def Num_Loan(self, Num_Loan) -> None: 
        if Num_Loan > 0:
            self._Num_Loan = Num_Loan 
        else:
            self._Num_Loan = 0
    
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
    def Amount (self) -> int:
        return self._Amount
    
    @Amount.setter
    def Amount(self, Amount) -> None:
        self._Amount = Amount   
        
        
        
   