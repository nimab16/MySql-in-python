# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:36:44 2021

@author: Nima
"""

import mysql.connector as pymysql 
from mysql.connector import Error
from .config import config 


class MyConnection:
    
    
    __connection = None
    __cursor = None
    
    def __init__(self):
        
     
        __db_config = config['mysql']
        
        self.__connection = pymysql.connect(host=__db_config['host'],
                                            user =__db_config['user'],
                                            password = __db_config['password'],
                                            db = __db_config['db'],
                                            port=__db_config['port'])
        self.__cursor = self. __connection.cursor()
        
    def query(self, query, params ) :
        self.__cursor.execute(query, params)
        return self.__cursor
    def close(self):
        return self.__connection.close()
    def commit(self):
        return self.__connection.commit()

