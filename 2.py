import uvloop
from pyrogram import Client

uvloop.install()

app = Client("my_account")


@app.on_message()
async def hello(client, message):
    print(await client.get_me())


app.run()
