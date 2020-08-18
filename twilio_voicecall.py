from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC1ecf923e2827eee7e486bcfff776f7e2'
auth_token = '077eef2e83d4eb07b5e81eb0d1ef4a88'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+919677758721',
                        from_='+12056351684'
                    )

print(call.sid)