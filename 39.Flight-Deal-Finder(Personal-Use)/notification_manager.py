from twilio.rest import Client


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self, message):
        self.message_to_send = message

    def sms(self):
        account_sid = '****'
        auth_token = '****'
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=self.message_to_send,
            from_='****',
            to='my_num'
        )
        return message.status
