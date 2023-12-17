import imaplib
import email
import pickle

import re
import asyncio
import sys
import logging

from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types , Router

from tgbot.gmail_user import user, password , token
from services import gmail_parse
from database.data_base import async_main

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(user, password)

bots = Bot(token=token , parse_mode='HTML')


async def main():
    await async_main()
    # Объект бота
    bot = bots
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)


async def scheduler():
    while True :
        await gmail_parse.check_email(bots)
        # await asyncio.sleep(1)



if __name__ == '__main__':
    try :
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        loop = asyncio.get_event_loop()
        task = loop.create_task(scheduler())
        loop.run_until_complete(task)
        asyncio.run(main())

    except KeyboardInterrupt :
        print('Exit')
    
