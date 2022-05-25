import easymodbus.modbusClient

from EasyModbusPy.easymodbus.modbusClient import *

modbus_client = easymodbus.modbusClient.ModbusClient('192.168.0.60',502)
modbus_client.unitidentifier =2
modbus_client.connect()
print("modbus is connected")

#The first argument is the starting address, the second argument is the quantity.
#coils = modbus_client.read_coils(0, 10)	
#Read coils 1 to 10 from server 
discrete_inputs = modbus_client.read_discreteinputs(0, 10)	
#Read discrete inputs 1 to 20 from server 
input_registers = modbus_client.read_inputregisters(0, 10)
#Read input registers 1 to 10 from server 
holding_registers = modbus_client.read_holdingregisters(0, 10)	
#Read holding registers 1 to 10 from server

#for i in range (10):
#    print("Value of discrete_inputs #"+str(i)+":"+str(discrete_inputs[i]))
for i in range (10):
    print("Value of input_registers #"+str(i)+":"+str(input_registers[i]))
for i in range (5):
    print("Value of holding_registers #"+str(i)+":"+str(holding_registers[i]))
    
coil_value = True
#The first argument is the address, the second argument is the value.

modbus_client.write_single_register(0, 111)	
modbus_client.write_single_coil(0, coil_value)

modbus_client.write_multiple_coils(0, [True]*10)
modbus_client.write_multiple_registers(2, convert_float_to_two_registers(3.14159265358976312))

modbus_client.close()
print("modbus is closed")


