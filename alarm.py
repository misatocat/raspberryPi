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

	slack.api_token = 'xoxp-9915537828-9970349523-9971225204-53ffa6'
	slack.chat.post_message('#random', msg, username='System')
