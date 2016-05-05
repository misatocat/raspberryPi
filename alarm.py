import slack
import slack.chat

def temperature(temp):
	if (temp >= 29):
		msg="""IDC Temperature Alarm: OVERHEAT
		       Temperature: %d Digree
	      	 Sensor: 1
	      	 Location: E-united IDC"""% (temp)
	else:
		msg="back to normal"

	slack.api_token = 'token file'
	slack.chat.post_message('#random', msg, username='System')
