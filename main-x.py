from fasthtml.common import *
import asyncio
from telegram import Bot

app,rt = fast_app()

def send_tg():
    TOKEN = '1277140711:AAFTH-NW9MYpwLhu0XaPXkIYFJDMbmcU890' # t.me/mkttalk_bot
    # TOKEN = '1138682560:AAEO3lbONccPVTBPRbKjz5UPHicPoosYHyU' # t.me/ledenbot
    CHAT_ID = '1321049338'
    TEXT_MESSAGE = 'Hello Python!'

    async def main():
        bot = Bot(token=TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=TEXT_MESSAGE)

    asyncio.run(main())


@rt('/telegram')
def get():
    send_tg()
    return Titled(Div(P('SMS Sent!')), A("Link", href="/"))

@rt('/change')
def get():
    return Titled(Div(P('Changed!!!')), A("Link", href="/"))

@rt('/')
def get():
    return Titled(Div(P('Hello World!'), hx_get="/telegram"))

serve()