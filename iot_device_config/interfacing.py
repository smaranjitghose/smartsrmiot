import time
import serial
import mysql.connector as mysql

db=mysql.conection(
	host='10.0.2.15'
	user='swat'
	passwd='helloworld'
	database='students')

corsor=db.corsor()

class timer:
	def __init__(self)
		t=300
		while t!=0:
			time.sleep(1)
			t=t-1
			return t

class id_pull:
	def __init__(self)
		device_id=001
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
				time_stamp=time.time()
				input_data=(timestamp,device_id)
				corsor.execute('',input_data)
