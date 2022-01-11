import serial
import time
port = 'COM4'
baudrate = 9600
timeout = 1
# with serial.Serial(port) as ser:
#     x = ser.read()
#     s = ser.read(10)
ser = serial.Serial(port)
x = 0
i = 0
print(x)
while i<1024:
    x = ser.read(100)
    print(x)
    i=i+1
    time.sleep(1)

print(x)