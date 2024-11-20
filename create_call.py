import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

print("account_sid ===", account_sid)
print("auth_token ===", auth_token)

call = client.calls.create(
    from_="+17577201485",
    to="+919582218845",
    url="https://caller-ai.loophole.site/incoming-call",
)
