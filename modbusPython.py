from EasyModbusPy.easymodbus.modbusClient import *
import time
import schedule
import random

modbus_client =ModbusClient('192.168.0.39',502)
modbus_client.parity=Parity.even
modbus_client.unitidentifier =1
modbus_client.baudrate=9600
modbus_client.stopbits=Stopbits.one
modbus_client.connect()
print("modbus is connected")

def writeCoil(index):
    coils = modbus_client.read_coils(0, 10)	
    if index >=10:
        index= index-10
    if coils[index] ==False:
        modbus_client.write_single_coil(index, True)
    else:
        modbus_client.write_single_coil(index, False)
    index=index+1    

def writeRegister(index):
    holding_register = modbus_client.read_holdingregisters(0,10)
    if index >= 10:
        index=index-10
    if holding_register[index] != None:
        modbus_client.write_single_register(index, random.randint(0,32767))

def read():
    print(modbus_client.read_coils(0,10))
    print(modbus_client.read_holdingregisters(0,10))
    

for i in range(10):
    schedule.every(1).seconds.do(writeCoil,i)
    schedule.every(1).seconds.do(writeRegister,i)

schedule.every(10).seconds.do(read)

while True:
    schedule.run_pending()
    time.sleep(1)
    
modbus_client.close()
