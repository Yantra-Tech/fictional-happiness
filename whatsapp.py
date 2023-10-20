from typing import Any

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from os import environ
from dotenv import load_dotenv

load_dotenv()

account_sid = environ.get("TWILIO_ACCOUNT_SID")
auth_token = environ.get("TWILIO_AUTH_TOKEN")

if not (account_sid and auth_token):
    KeyError("Twilio ccount SID and Auth token not set")

_twilio_client = Client(account_sid, auth_token)

class WhatsappMessage:
    def __init__(self, src, body, dest):
        self.create(src, body, dest)
        self.api_response = None
    
    def create(self, src, body, dest):
        self.from_  = src
        self.body   = body
        self.to     = dest
        return self
    
    def getMessage(self) -> str:
        return self.body
    
    def updateMessage(self, body:str):
        self.body = body
        return self

    def send(self):
        self.api_response = _twilio_client.messages.create(
            from_   = self.from_,
            body    = self.body,
            to      = self.to
        )
        return self.api_response
    
    def respond(self):
        response = MessagingResponse()
        response.message(
            from_ = self.from_,
            body  = self.body,
            to    = self.to
        )
        return str(response)
        

if __name__ == "__main__" :
    wm = WhatsappMessage(
        src = "whatsapp:+14155238886",
        body = "Test Successfull",
        dest = "whatsapp:+917798044008"
    )
    for msg in _twilio_client.messages.list():
        print("-"*50)
        print(msg.from_)
        print(msg.body)
        print(msg.to)
