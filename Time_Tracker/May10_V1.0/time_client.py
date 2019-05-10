from opcua import Client
from opcua import ua
import time
import csv
import os.path
from Config import *


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
        client.load_type_definitions()
        time_node = client.get_node("ns=2;s=Tags."+PLC_DT)


        while True:
            print(time_node.get_description())
            print(time_node.get_browse_name())
            print(time_node.get_value())
            time.sleep(1)


    finally:
        client.disconnect()
