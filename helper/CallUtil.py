import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)


#This function will be in charge literally getting the caller client so we can modify the call from any spot
#idk how read the docs,
#https://www.twilio.com/docs/voice/api/call-resource#update-a-call-resource
#https://www.twilio.com/docs/voice/quickstart/python
#https://www.twilio.com/docs/voice/tutorials/how-to-make-outbound-phone-calls/python
#https://www.twilio.com/docs/voice/tutorials/how-to-modify-calls-in-progress/python
#https://www.twilio.com/docs/voice/tutorials/how-to-respond-to-incoming-phone-calls/python
#
#Christian you might have to keep track of the active call SID's inorder to implement this properly
#Logan you will call this function to be able to do TTS
#https://www.twilio.com/docs/voice/quickstart/python
#Cool :)

def get_caller_client(phone_number):
    pass #should return a call object maybe something like:
# call = client.calls('CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX').update(twiml='<Response><Say>Ahoy there</Say></Response>')
#so return the client.calls(sid)
#make sure you void the sid after the call ends
