from opcua import Client
from opcua import ua
import time
import csv
import os.path
from Config import *


def write_csv(data):
    csv_header = ['Temperature', 'Pressure', 'Wave', 'Time']
    data_file = "opcData.csv"
    file_exists = os.path.isfile(data_file)
    with open(data_file, 'a') as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            writer.writerow(csv_header)
        writer.writerow(data)



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




""" while True:
    Temp = client.get_node("ns=2; i=3")
    Press = client.get_node("ns=2; i=4")
    Time = client.get_node("ns=2; i=5")
    Wave = client.get_node("ns=2; i=6")

    Temperature = Temp.get_value()
    Pressure = Press.get_value()
    currTime = Time.get_value()
    waveFunc = Decimal(Wave.get_value())

    print("The temperature is: ", Temperature)
    print("The pressure is: ", Pressure)
    print("The time is: ", currTime)
    print("The wave is: ", waveFunc)

    dataRow = [Temperature, Pressure, round(waveFunc, 4), currTime]
    write_csv(dataRow)

    time.sleep(1) """
