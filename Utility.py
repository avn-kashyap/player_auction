import Exceptions
import mysql.connector

def getconnection():
    try:
        connection = mysql.connector.connect(user='*****',password='*****'
                                      ,host='******',database='*****')
    except Exception:
        raise Exceptions.DaoExceptions("Connection to the database failed!!!!!!")
    else:
        return connection

