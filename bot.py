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
    await message.answer(f"Salom, {full_name}, \nMen oddiy kalkulyatorman",reply_markup=calc_btn.as_markup())

@dp.callback_query()
async def calc_query(callback: types.CallbackQuery):
    text = f"{callback.data} bosildi!"
    await callback.answer(text=text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
