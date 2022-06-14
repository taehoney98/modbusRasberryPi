from django.http import HttpResponse
from django.shortcuts import render
from easyModbusTCP.easymodbus.modbusClient import *
from modbusRasberryPi.models import Digital ,  Analog
import random
# Create your views here.

modbus_client=ModbusClient('192.168.0.39',502) # pAWS외부 ip:3.38.3.27  
modbus_client.parity = Parity.even #짝수 패리티
modbus_client.unitidentifier = 1 #slave id 
modbus_client.baudrate = 9600  #전송속도 보오 레이트
modbus_client.stopbits = Stopbits.one #정지 비트  데이터 송출 종료 알림

modbus_client.connect()

Analog.objects.all().delete()
Digital.objects.all().delete()

coils = modbus_client.read_coils(0, 10)
for i in range(len(coils)):
    Digital.objects.create(id=i,coil_value=coils[i])

holding_registers=modbus_client.read_holdingregisters(0,10)
for i in range (len(holding_registers)):
    Analog.objects.create(id=i,register_value=holding_registers[i])

def index(request):
    coils = modbus_client.read_coils(0, 10)
    holding_registers=modbus_client.read_holdingregisters(0,10)

    
    for i in range(10):
        for index in range(random.randrange(0,10)):
            modbus_client.write_single_coil(index, not coils[index])
            item =Digital.objects.get(id=index)
            item.coil_value = not coils[index]
            item.save()
        
        randNum=random.randint(0,32767)
        if holding_registers[i] != None:
            modbus_client.write_single_register(i,randNum)
            item =Analog.objects.get(id=i)
            item.register_value = randNum
            item.save()

    coils = modbus_client.read_coils(0, 10)
    holding_registers=modbus_client.read_holdingregisters(0,10)
    
    indexCoils = dict(enumerate(coils))
    indexRegisters =dict(enumerate(holding_registers))
    
    context={'coils': indexCoils ,'registers': indexRegisters }
    return HttpResponse('test')
    return render(request,'modbusRasberryPi/list.html',context)