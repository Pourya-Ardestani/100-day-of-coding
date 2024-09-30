from twilio.rest import Client

# Replace with your account SID and auth token
account_sid = "ACa24eea0b80bca7aa84926c661a3a7210"
auth_token = "dd9ccbaf642291a6be8a2ac534bdba90"

client = Client(account_sid, auth_token)


message = client.messages.create(


    to="+989031828457",
    from_="+12136343225",
    body="Hello from Twilio!"
)

print(message.sid)
