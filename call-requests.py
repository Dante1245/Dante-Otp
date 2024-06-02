from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'

def make_call(to_number, message):
    client = Client(account_sid, auth_token)

    try:
        call = client.calls.create(
            to=to_number,
            from_=twilio_phone_number,
            twiml=f'<Response><Say>{message}</Say></Response>'
        )
        print(f"Call SID: {call.sid}")
    except Exception as e:
        print(f"Error making call: {str(e)}")

to_number = '+1234567890' 
message = 'Hello, this is a test call from Twilio!' 
make_call(to_number, message)
