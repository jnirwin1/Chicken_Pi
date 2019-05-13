from mysql.connector import MySQLConnection, Error
from dbconfig import read_db_config
from datetime import datetime, timedelta
from opcua import Client
from opcua import ua
from Config import *


def insert_time(time):
    query = ("INSERT INTO plc_time(time) "
             "VALUES(%s)")
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, time.strftime('%Y-%m-%d %H:%M:%S'))

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    client = Client("opc.tcp://admin:admin@"+str(HMI_IP)+":48010/")
     
    try:
        client.connect()

        nodes = [client.get_node("ns=2;s=Tags."+ tag) for tag in Node_Tags]
       

        while True:
            dataRow = [node.get_value() for node in nodes]
            time = datetime.fromtimestamp(dataRow[0])
            insert_time(time)
            print(time)
            time.sleep(1)

    finally:
        client.disconnect()
