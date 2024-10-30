from aiogram.types import Message, CallbackQuery
import function
import config
from keyboards import *
from aiogram.types.input_file import FSInputFile, InputFile
from aiogram import Bot
from aiogram.fsm.context import FSMContext



async def adminPanel(message: Message):
    if message.chat.id == 5667762268:
        await message.answer("Assalomu Aleykum botimizga xush kelibsiz 🎉", reply_markup=panel_builder)
    else: 
        pass
    
async def statistika_callback(callback_data: CallbackQuery):
    with open('users.txt', 'r') as f:
        file_read = f.readlines()
        people_status = len(file_read)
    await callback_data.message.answer(f"Statistika bo'limidasiz\n\n👤 A'zolar: {people_status}")


async def baza_callback(callback_query: CallbackQuery):
    try:
        local = 'users.txt'
        fs_input_file = FSInputFile(local)
        await callback_query.message.answer_document(document=fs_input_file, caption="Ma'lumotlar bazasi")
    except Exception as e:
        print(e)
        
async def xabar_callback(callback_data: CallbackQuery):
    await callback_data.message.answer("❗Yubormoqchi bo'lgan xabaringizni yozing: ")

async def input_answer(message: Message, bot: Bot):
    try:
        text = message.text
        photo = message.photo
        if message.chat.id == 5667762268:
            if photo:
                with open('users.txt', 'r') as f:
                    for lines in f:
                        parts = lines.split('ID: ')
                        if len(parts) > 1:
                            ids = parts[1].split(' Ism:')[0]
                            users_id = int(ids)  # caption ni tekshirib to'g'irlash
                            await bot.send_photo(chat_id=users_id, photo=photo[-1].file_id, caption=message.caption)
            elif text:
                with open('users.txt', 'r') as f:
                    for line in f:
                        parts = line.split('ID: ')
                        if len(parts) > 1:
                            id_str = parts[1].split(' Ism:')[0]
                            user_id = int(id_str)
                            await bot.send_message(chat_id=user_id, text=text)
        else:
            print("Xatolik")
    except Exception as e:
        print(e)