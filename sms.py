from twilio.rest import Client

account_sid = "AC297a986e7fdea96187649a957d26784c"
auth_token = "935a761077c79e09d5bba7492057df33"
client = Client(account_sid, auth_token)
client.messages.create(from_= "970592513063", body="This is a test message for a program that is working on it" \
                                                   "Khaled Abu Nadi",
                                                   to="0592117971")
