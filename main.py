# importing all required libraries
import argparse
import asyncio

from telethon import TelegramClient

# getting all the required parameters
parser = argparse.ArgumentParser(description='Telegram Message Sender')
parser.add_argument('-i', '--api_id', help='Telegram API ID', required=True)
parser.add_argument('-s', '--api_hash', help='Telegram API Hash', required=True)
parser.add_argument('-m', '--message', help='Message to send', required=True)
parser.add_argument('-p', '--phone', help='Phone number', required=True)
parser.add_argument('-u', '--username', help='Telegram username', required=True)
parser.add_argument('-c', '--username_target', help='Telegram username target', required=True)
parser.add_argument('-f', '--sending_file', help='File to send', required=True)

args = parser.parse_args()

api_id = args.api_id
api_hash = args.api_hash
message = args.message
phone = args.phone

# creating a telegram session and assigningA
your_username = args.username

# username of the target
username_target = args.username_target
# sending message using username
sending_file = args.sending_file

if api_id is None or api_hash is None or message is None or phone is None or your_username is None or username_target is None or sending_file is None:
    print('You need to pass your API ID, API Hash, Message, Phone, Username, Username Target and Sending File')
    print('Usage: python main.py --api_id 12345 --api_hash 0123456789abcdef0123456789abcdef \
    --message "Hello World" --phone "+123456789" --username "username" --username_target \
    "username_target" --sending_file "sending_file"')


async def telegram_async():
    async with TelegramClient(your_username, api_id, api_hash) as client:

        # connecting and building the session
        await client.connect()

        # ensuring you're authorized
        if not await client.is_user_authorized():
            # sending code request
            await client.send_code_request(phone)

            # signing in the client
            await client.sign_in(phone, input('Enter the code: '))

        try:
            # sending message using telegram client
            await client.send_file(username_target, sending_file, caption=message)
        except Exception as e:
            # error handling
            print(e)

        # disconnecting the telegram session
        await client.disconnect()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(telegram_async())


if __name__ == '__main__':
    main()
