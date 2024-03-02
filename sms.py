from twilio.rest import Client

def send_sms(to_number, parking_spot, floor):
    account_sid = 'AC3dcd7b708b5b975a7d465eed56399e13'
    auth_token = '896214f3639ad3f5ec322973168791f4'

    spot = parking_spot.split(",")
    
    client = Client(account_sid, auth_token)
    from_number = '+19497102366'
    message = f'Your car is parked at row {spot[0]} and column {spot[1]} on floor {floor}'
    message = client.messages.create(
        body=message,
        from_=from_number,
        to="+91" + to_number
    )

    print("Message sent successfully!")