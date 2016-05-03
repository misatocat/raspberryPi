# -*- coding:utf-8 -*-

import smtplib

def temperature(temp):
	

	fromaddr = 'yu63824@gmail.com'
	toaddrs = ['yu63824@e-united.com.tw','misatocat@gmail.com']
	msg = """From: EUMIS <yu63824@gmail.com>
	To:<yu63824@e-united.com.tw>
	Subject: Temperature Warning from e-united 

	IDC Temperature Warning: OVERHEAT
	Temperature: %d Digree
	Sensor: 1
	Location: E-united IDC 


	"""%(temp)

	username = 'yu63824'
	password = 'P0cAhont@s'

	server = smtplib.SMTP ('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()


