import MySQLdb
db = MySQLdb.connect("172.25.11.100","eu","P@ssw0rd","temperature" )
cursor = db.cursor()
temp=13.239
sql= "INSERT INTO temperature.temp (temp_log, time_date) VALUES ('%s', NOW());"%(temp)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
db.close()
