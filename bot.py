import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from data.config import BOT_TOKEN
from inline_buttons import calc_btn

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Salom, {full_name}, \nMen oddiy kalkulyatorman")
    await message.answer("0",reply_markup=calc_btn.as_markup())

@dp.callback_query()
async def calc_query(callback: types.CallbackQuery):
    text = callback.message.text
    data = callback.data
    if data.isdigit():
        if callback.message.text == "0":
            text = data
        else:
            text +=data
    if data == "D":
        if len(callback.message.text)== 1:
            text = "0"
        else:
            text = text[:-1]
    if data =="C":
        text = "0"
    if data in "+x/-":
        if not text[-1].isdigit():
            await callback.answer("Notog'ri amal bajardingiz!!!")
        else:
            text += data
    if data == "=":
        
        text = str(eval(text.replace("x","*")))

    try:
        await callback.message.edit_text(text=text,reply_markup=calc_btn.as_markup())
    except:
        pass
    
    # await callback.answer(text=text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
