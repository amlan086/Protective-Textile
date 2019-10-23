from twilio.rest import Client

account_sid = 'ACec8b09987b86f06aebdcd9fe660a5b69' 
auth_token = '2734e7a3f7dbf66ea4cebd651eaf6214' 

myPhone = '+8801521313223' 
TwilioNumber = '+12512548095' 

client = Client(account_sid, auth_token)
client.messages.create(
  to=myPhone,
  from_=TwilioNumber,
  body="I'm in danger. Rescue me")
