import sys
import time
import smtplib
import sendmail
import alarm
import MySQLdb
import Adafruit_DHT

#db = MySQLdb.connect("172.25.11.100","eu","P@ssw0rd","temperature" )
#cursor = db.cursor()
info = 0
heat = 31

while 1:
#	tempfile = open ("/sys/bus/w1/devices/28-0000070533e7/w1_slave")
#	thetext = tempfile.read()
#	tempfile.close()
#	tempdata = thetext.split("\n")[1].split(" ")[9]
#	temperature = float(tempdata[2:])
#	temperature = temperature / 1000

	humidity, temperature = Adafruit_DHT.read_retry(11, 17)
	
	if (temperature >= heat and info == 0):
        	print "OverHeat Worring!",temperature,"seeding massage"
		print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
#		sendmail.temperature(temperature)
		alarm.temperature(temperature)
		info=1
	elif (temperature >= heat and info < 10):
		print "OverHeat Worring!",temperature,"info=",info
		print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
		info = info+1
	elif (temperature >= heat and info == 10):
	        print "OverHeat Worring!",temperature,"seeding massage"
		print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
#                sendmail.temperature(temperature)
                alarm.temperature(temperature)
                info=1
	elif (temperature < heat and info > 0):
		print "Back to normal"
		print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
		alarm.temperature(temperature)
		info=0
	else:
		print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)

	time.sleep(10)


