# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

class sendmail:
    def __init__(self):
        self.mail_host="smtp.gmail.com"
        self.mail_user="yu63824@gmail.com"
        self.mail_passwd="P0cAhont@s"
        self.postfix="gmail.com"
        self.mailto="yu63824@e-united.com.tw,misatocat@gmail.com"
    def send(self,subject,content):
        gmailuser=self.mail_user+"@"+self.postfix
        msg=MIMEText(content)                  
        msg['Subject']=subject                    
        msg['From']= "我"
        msg['To']=self.mailto
        smtp=smtplib.SMTP('smtp.gmail.com',587)         
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(self.mail_user,self.mail_passwd)
        smtp.sendmail(gmailuser,self.mailto,msg.as_string())
        smtp.close()
        print "寄信成功"

spam_block = sendmail()
spam_block.send("這是測試信","成功之內文")

