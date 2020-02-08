import time
import serial

data = serial.Serial(
	port=dev/ttyS0
	baudrate=9600
	parity=serial.PARITY_NONE
	stopbyte=serial.SOTPBBITS_ONE
	bytesize=serial.EIGHTBIT)

while 1:
	x = data.read(12)
