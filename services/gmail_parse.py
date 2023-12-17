from aiogram import Bot
import imaplib
import email
from tgbot.gmail_user import user, password 
import re
import asyncio
from run import mail
from run import scheduler


async def check_email( bot : Bot):
    try :
        mail.list()
        mail.select('inbox')
        result, data = mail.search(None, 'ALL')
        if result == 'OK':
            for num in data[0].split() :
                result,data = mail.fetch(num, "(RFC822)")
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                sender = msg['From']
                subject = msg['Subject']
                body = ""

                if msg.is_multipart() :
                    for part in msg.walk() :
                        if part.get_content_type() == 'text/plain' :
                            body = part.get_payload(decode=True).decode('utf-8')
                else :
                    body = part.get_payload(decode=True).decode('utf-8')
                    match = re.search(r'pick up at(.*)', body, re.IGNORECASE)
                    if match:
                        pick_up_location = match.group(1).strip()


                    await bot.send_message(chat_id='111',text=f'New email : {pick_up_location}')
    except :
        await scheduler()

