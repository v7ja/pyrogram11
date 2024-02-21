import asyncio
import uvloop

from pyrogram import Client


async def main():
    app = Client("my_account")

    async with app:
        print(await app.get_me())


uvloop.install()
asyncio.run(main())
