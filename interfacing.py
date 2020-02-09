import time
import serial
import mysql.connector as mysql

db=mysql.conection(
	host=''
	user=''
	passwd=''
	database='')

corsor=db.corsor()

class timer:
	__init__(self)
		t=300
		while t!=0:
			time.sleep(1)
			t=t-1
			return t

class id_pull:
	__init__(self)
		data = serial.Serial(
			port=dev/ttyS0
			baudrate=9600
			parity=serial.PARITY_NONE
			stopbyte=serial.SOTPBBITS_ONE
			bytesize=serial.EIGHTBIT)

		while 1:
			x = data.read(12)
			if x.isnumeric == true:
				#timer_initialize
				timer()
				#sql_code
				corsor.execute('')
			elif x.isalnum == true && timer()!=0:
				#sql_code
				corsor.execute('')
