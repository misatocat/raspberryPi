import time
import MySQLdb

db = MySQLdb.connect("172.25.11.100","eu","password","temperature" )
cursor = db.cursor()
while 1:
	tempfile = open ("/sys/bus/w1/devices/28-0000070533e7/w1_slave")
	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split("\n")[1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature / 1000
	sql= "INSERT INTO temperature.sensor01 (temp_log, time_date) VALUES ('%s', NOW());"%(temperature)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()

	print temperature
	time.sleep(600)


