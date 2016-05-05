import sys
import time
import MySQLdb
import Adafruit_DHT

db = MySQLdb.connect("172.25.11.100","eu","passowrd","temperature" )
cursor = db.cursor()
while 1:
	humidity, temperature = Adafruit_DHT.read_retry(11, 17)
	sql= "INSERT INTO temperature.sensor01_Humidity (humi_log, time_date) VALUES ('%s', NOW());"%(humidity)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()

	print "Humidity=",humidity,"%"
	time.sleep(3600)


