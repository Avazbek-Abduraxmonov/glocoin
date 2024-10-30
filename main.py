from aiogram import Dispatcher, Bot, F
from asyncio import run
from function import *
from config import *
from admin import * 
from aiogram.filters.command import Command

dp = Dispatcher()


async def startAdminAnswer(bot: Bot):
    await bot.send_message(chat_id=5667762268, text="Bot ishlamoqda")
    

async def shutdownAdminAnswer(bot: Bot):
    await bot.send_message(chat_id=5667762268, text="Bot tugadi")
    
async def start():
    dp.startup.register(startAdminAnswer)
    dp.shutdown.register(shutdownAdminAnswer)
    dp.message.register(startAnswer, Command('start'))
    dp.message.register(adminPanel, Command('panel'))
    dp.callback_query.register(statistika_callback, F.data == 'status')
    dp.callback_query.register(baza_callback, F.data== 'baza')
    dp.callback_query.register(xabar_callback, F.data == 'rek')
    dp.message.register(input_answer)
    bot = Bot(token="7368791035:AAG0ZnHiy4Vq-IXcedVB50RGCrrLOv6fWYs")
    await dp.start_polling(bot, polling_timeout=1)
    
run(start())