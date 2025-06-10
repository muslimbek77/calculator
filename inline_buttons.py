from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

buttons = "D()x789/456-123+C0.="
calc_btn = InlineKeyboardBuilder()
for i in buttons:
    calc_btn.add(InlineKeyboardButton(text=i,callback_data=i))
calc_btn.adjust(4)
