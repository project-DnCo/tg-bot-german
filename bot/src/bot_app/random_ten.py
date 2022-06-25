from aiogram import types
from aiogram.dispatcher import FSMContext

from .app import dp, bot
from .states import GameStates
from .data_fetcher import get_random_word
from . import keyboards


@dp.message_handler(commands=['train_ten'], state='*')
async def train_ten(message: types.Message, state: FSMContext) -> None:
    await GameStates.random_ten.set()
    res = await get_random_word()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('gender')
        data['word'] = res.get('word')
        await message.answer(f'{data["step"]} of 10. Das wort ist {data["word"]}', reply_markup=keyboards.inline_keyboard)


@dp.callback_query_handler(lambda c: c.data in ['der', 'die', 'das'], state=GameStates.random_ten)
async def button_click_callback_random(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await callback_query.answer()
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data.get('answer'):
            res = await get_random_word()
            data['step'] += 1
            data['answer'] = res.get('gender')
            data['word'] = res.get('word')
            if data['step'] > 10:
                await bot.send_message(callback_query.from_user.id, 'The game is over!')
                await GameStates.start.set()
            else:
                await bot.send_message(
                    callback_query.from_user.id,
                    'Ya\n' +
                    f'{data["step"]} of 10. Das wort ist {data["word"]}',
                    reply_markup=keyboards.inline_keyboard
                )
        else:
            await bot.send_message(callback_query.from_user.id,
                                   'Nein\n',
                                   reply_markup=keyboards.inline_keyboard)
