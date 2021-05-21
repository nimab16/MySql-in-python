# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:09:41 2021

@author: Nima
"""
from ..config.myconnection import MyConnection
from ..model.agency import Agency


class AgencyDao:
    __db = None
    def __init__(self):
        self.__db = MyConnection()
        
    def findAll(self):
        return self.__db.query('SELECT * FROM Agency', None).fetchall()
        self.__db.close()
        
    def save (self, agency: Agency) -> Agency:
        
        sql = 'INSERT INTO Agency (Num_Agency, Name, City, Active ) VALUES({},"{}", "{}", "{}");'.format(agency.Num_Agency, agency.Name, agency.City, agency.Active )
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    
        # pass
    def findById(self, num_Agency: int) -> Agency:
        query = 'SELECT * FROM Agency WHERE Num_Agency = {}'.format(str(num_Agency))
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    
    def findByName(self, name_agency: str) -> Agency:
        query = 'SELECT * FROM Agency WHERE NAme = "{}"'.format(name_agency)
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
    
    def findLastItem(self) -> Agency:
        query = 'SELECT * FROM Agency ORDER BY Num_Agency DESC LIMIT 1'
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
        # pass
    def update(self, agency: Agency) -> Agency:
        sql = 'UPDATE Agency SET Name = "{}", City = "{}", Active = "{}" WHERE Num_Agency = "{}" '.format(agency.Name,agency.City, agency.Active, agency.Num_Agency)
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        print(cr)
        return
    
    def remove(self, agency: Agency) -> None:
        sql = 'DELETE FROM Agency WHERE Num_Agency = "{}"'.format(str(agency.Num_Agency))
        cr = self.__db.query( sql, None)
        self.__db.commit()
        self.__db.close()
        return cr
    
    def show_column(self):
        
        query = 'SHOW COLUMNS FROM agency'
        cr = self.__db.query(query, None).fetchall()
        self.__db.close()
        
        return cr
        
    
    def dropTable(self,tableName: str):
        sql = 'TRUNCATE TABLE {}'.format(tableName)
        cr = self.__db.query( sql, None)
        self.__db.close()
        return cr
    
    # def selectByOrder(self):
    #     sql = 'SELECT * FROM Agency ORDER BY login'
    #     cr = self.__db.query( sql, None).fetchall()
    #     self.__db.close()
    #     return cr
    
    def limitSelect(self, limit:int, offset:int):
        sql = 'SELECT * FROM Agency LIMIT {} OFFSET {}'.format(limit,offset)
        cr = self.__db.query( sql, None).fetchall()
        self.__db.close()
        return cr
        
        
        
    
