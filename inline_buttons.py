buttons = "123x456-789/0.+="
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
calc_btn = InlineKeyboardBuilder()
for i in buttons:
    calc_btn.add(InlineKeyboardButton(text=i,callback_data=i))
calc_btn.adjust(4)
