from twilio.rest import Client
from config import account_sid, auth_token


def send_sms(to_number, parking_spot, floor):

    spot = parking_spot.split(",")
    
    client = Client(account_sid, auth_token)
    from_number = '+19497102366'
    message = f'Your car is parked at row {spot[0]} and column {spot[1]} on floor {floor}'
    message = client.messages.create(
        body=message,
        from_=from_number,
        to="+91 " + to_number
    )

    print("Message sent successfully!")