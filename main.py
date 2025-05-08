from fasthtml.common import *
import asyncio
from telegram import Bot

app,rt = fast_app()

@rt('/change')
def get():
    return Titled(Div(P('Changed!!!')), A("Link", href="/"))

@rt('/')
def get():
    return Titled(Div(P('Hello World!'), hx_get="/change"))

serve()