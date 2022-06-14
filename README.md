# modbusRasberryPi

라즈베이파이 모델을 이용해 modbus TCP 통신의 동작을 확인한다.

## 라즈베리파이 모델

![1517457252419l0](https://user-images.githubusercontent.com/81626703/171130399-b9eb2083-6f1d-4648-a321-e9992682c751.png)

컴파일 테크놀로지 사의 컴파일 파이 제품군중 [CPi-A070WR](https://www.comfile.co.kr/shop/goods/goods_view.php?goodsno=386&category=014)을 사용해 진행

해당 모델을 ModbusTCP 프로토콜의 Client로 설정, ModbusTCP Server와의 통신을 구현

## modbusClient 프로그램

```

modbus_client=ModbusClient('192.168.0.39',502) #Modbus Server 연결  
modbus_client.parity = Parity.even #짝수 패리티
modbus_client.unitidentifier = 1 #slave id 
modbus_client.baudrate = 9600  #전송속도 보오 레이트
modbus_client.stopbits = Stopbits.one #정지 비트  데이터 송출 종료 알림
modbus_client.connect()

```