# importing all required libraries
import asyncio

from telethon import TelegramClient

api_id = input('Enter your API ID: ')
api_hash = input('Enter your API Hash: ')
message = input('Enter your message: ')
phone = input('Enter your phone number: ')

# creating a telegram session and assigningA
your_username = input("Enter your Telegram username: ")


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
            # username of the target
            username_target = input('Enter the username of the person you want to send message to: ')
            # sending message using username
            sending_file = input('Enter the location of the file you want to send: ')

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
