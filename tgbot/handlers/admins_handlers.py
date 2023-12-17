from aiogram import Bot, Router, F
from aiogram.types import Message , CallbackQuery
from aiogram.filters import BaseFilter
from tgbot import configs

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in configs.admin_ids



admin_router = Router()
admin_router.filters()

@admin_router.message(F.text == '/search')
async def search(msg : Message):
    try :
        text = msg.text.split(' ')
        shtat = text[1:]

    
    except :

        await msg.answer(' Похоже вы неправильно ввели запрос\nПример : " /search Texas "')