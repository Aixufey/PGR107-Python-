# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 09:03:37 2023

@author: sparrow
"""

import sqlite3
import os

class Connect:
    """
    Required parameter: Database file name, "test.db"
    ---
    RETURN: None
    """
    def __init__(this, dbFile):
        this.dbFile = dbFile
    
    # SQLite API connection
    def createConn(this):
        """
        Creates connection object from specified file
        ---
        RETURN: Connection instance
        """
        conn = None
        try:
            
            if this.dbFile.endswith('.db'):
                conn = sqlite3.connect(this.dbFile)
            else:
                print("\n >>>> Not valid filename '%s' <<<<" % this.dbFile)
                
            if conn is not None:
                
                if this.dbFile in os.listdir(os.getcwd()):
                    print("\n >>>> Connected '%s' <<<<" % this.dbFile)
                else:
                    print("\n >>>> Created '%s' <<<<" % this.dbFile)
                # if os.listdir(os.getcwd())
                #     print("\n >>>> Connected '%s' <<<<" % this.dbFile)
                # else:
                #     print("\n >>>> Created '%s' <<<<" % this.dbFile)
                
                sql = """ CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY, 
                    name TEXT
                    ); 
                """
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                conn.close()
            return conn
        
        except sqlite3.Error as e:
            print(e)
    
        
def lazyInit():
    """ 
    Initialize database and use cursor mechanism to traverse over the records
    Cursor instance enable execution of sql statements
    ---
    :return: None

    """
    db = "Sparrow.db"
    myDb = Connect(db)
    print(myDb)
    if myDb is not None:
        conn = myDb.createConn()
        cursor = conn.cursor()
        
        tablesql = """ CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            name TEXT
            ); 
        """
        cursor.execute(tablesql)
        conn.commit()
    else:
        print('Error')
    conn.close()

if __name__ == '__lazyInit__':
    lazyInit()