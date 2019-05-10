from opcua import Client
from opcua import ua
import time
import csv
import os.path
from Config import *
import datetime


def write_csv(row, header):
    data_file = "opcData.csv"
    file_exists = os.path.isfile(data_file)
    with open(data_file, 'a') as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)



if __name__ == "__main__":



    client = Client("opc.tcp://admin:admin@"+str(HMI_IP)+":48010/")
     
    try:
        client.connect()
        nodes = []

        nodes = [client.get_node("ns=2;s=Tags."+ tag) for tag in Node_Tags]
       
        header = [node.get_browse_name().to_string() for node in nodes]

        while True:
            dataRow = [node.get_value for node in nodes]
            write_csv(dataRow,header)
            time.sleep(1)

    finally:
        client.disconnect()
