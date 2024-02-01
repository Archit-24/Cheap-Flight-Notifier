from twilio.rest import Client

TWILIO_SID = "AC78e16fc76248370cb83073dd56d0da6b"
TWILIO_AUTH_TOKEN = "59a6417b4ee241c7ddc4e17b51c33643"
TWILIO_VIRTUAL_NUMBER = "+14848512765"
TWILIO_VERIFIED_NUMBER = "+919560890859"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
