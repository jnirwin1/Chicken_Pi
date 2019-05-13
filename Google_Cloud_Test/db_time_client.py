from mysql.connector import MySQLConnection, Error
from python_dbconfig import read_db_config
from datetime import datetime, timedelta
from opcua import Client
from opcua import ua
from Config import *


if __name__ == '__main__':

    query = ("INSERT INTO plc_time2(time) "
             "VALUES(%s)")

    client = Client("opc.tcp://admin:admin@"+str(HMI_IP)+":48010/")
     
    try:

        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        client.connect()

        cursor = conn.cursor()

        nodes = [client.get_node("ns=2;s=Tags."+ tag) for tag in Node_Tags]
       

        while True:
            dataRow = [node.get_value() for node in nodes]
            time = datetime.fromtimestamp(dataRow[0])
            cursor.execute(query, time)
            print(time)
            conn.commit()
            time.sleep(1)

    finally:
        client.disconnect()
        cursor.close()
        conn.close()
