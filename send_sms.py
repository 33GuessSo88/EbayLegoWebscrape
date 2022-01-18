from twilio.rest import Client


def send_inititate_sms():
    account_sid = 'ACe83bcadf007af63af632a4b90a3d5789'
    auth_token = '5e92f2fc80d8fea11a1ed5d3ede8410f'

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Ebay webscraper script initiating now.",
        from_='+14159039940',
        to='+14035401053'
    )


def send_finished_sms(new_records):
    account_sid = 'ACe83bcadf007af63af632a4b90a3d5789'
    auth_token = '5e92f2fc80d8fea11a1ed5d3ede8410f'

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Ebay webscraper successfully ran with {new_records} new records",
        from_='+14159039940',
        to='+14035401053'
    )

    # print(message.sid)
