# importing all required libraries
from telethon import TelegramClient

# get your api_id, api_hash
api_id = 'some_api_id'
api_hash = 'some_api_hash'
message = 'some_message'

# your phone number
phone = '+123456789'

# creating a telegram session and assigningA
client = TelegramClient('your_username', api_id, api_hash)

# connecting and building the session
client.connect()

# ensuring you're authorized
if not client.is_user_authorized():
    # sending code request
    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('Enter the code: '))

try:
    # sending message using telegram client
    client.send_file('some_username', 'file_location', caption=message)
except Exception as e:
    # error handling
    print(e)

# disconnecting the telegram session
client.disconnect()
