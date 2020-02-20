# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC1a097cf65e9be1e9f76d3c7c138c3490'
auth_token = 'c4920dbfff913d5a7edcdb6b3028664d'
client = Client(account_sid, auth_token)

message = client.messages.create( 
                              from_='+19383333284',  
                              body='hello. i am a bot speaking',      
                              to='+8801843926937' 
                          )

print(message.sid)
