from aiogram import types


inline_keyboard = types.InlineKeyboardMarkup()
for gender in ('der', 'die', 'das'):
    inline_keyboard.add(types.InlineKeyboardButton(
        gender.title(), callback_data=gender))
