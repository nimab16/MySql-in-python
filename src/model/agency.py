# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:49:36 2021

@author: Nima
"""

class Agency:
    def __init__ (self, Num_Agency: int = 0, Name: str = '', City: str = '', Active: str = 'Yes'):
        self._Num_Agency = Num_Agency 
        self._Name = Name
        self._City = City
        self._Active = Active
        
    @property 
    def Num_Agency(self) -> int:
        return self._Num_Agency
    
    @Num_Agency.setter
    def Num_Agency(self, Num_Agency) -> None: 
        if Num_Agency > 0:
            self._Num_Agency = Num_Agency 
        else:
            self._Num_Agency = 0
    
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
    def City (self,City) -> None:
        self._City = City
    
    @property
    def Active(self) -> str:
        if self._Active == 'Yes' or self._Active == 'No' :
            
            self._Active = self._Active
            
        else:
            self._Active = 'Yes'
            
        return self._Active
        
    
    @Active.setter
    def Active (self,Active) -> str:
   
        return self._Active
            
        
        