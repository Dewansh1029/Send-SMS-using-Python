#How to Send SMS Text Messages with Python:
#Code:

#import the Twilio client from the dependency
from twilio.rest import Client

#Enter your Twilio Account SID and Auth Token
client = Client("<Account Sid>", "<Auth Token>")

message = client.messages.create(
		 body="<Text, eg. Hi, this is Dipanshi>",
 		from_="<Twilio number>", 
		to="<Your registered phone number on Twilio>"
	)

print(message.sid)