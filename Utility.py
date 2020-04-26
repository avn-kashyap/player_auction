import Exceptions
import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('./config.ini')
def getconnection():
    try:
        connection = mysql.connector.connect(user=config.get('database_server','user'),
                     password=config.get('database_server','password')
                    ,host=config.get('database_server','host'),
                    database=config.get('database_server','database'))
    except mysql.connector.Error as e:
        raise Exceptions.DaoExceptions(e.msg+"\nConnection to the database failed!!!!!!")
    else:
        return connection