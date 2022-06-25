from aiogram import types
from aiogram.dispatcher import FSMContext

from .app import dp, bot
from .states import GameStates
from .data_fetcher import get_next_word
from . import keyboards


@dp.message_handler(commands=['train_all'], state='*')
async def train_all(message: types.Message, state: FSMContext) -> None:
    await GameStates.all_words.set()
    res = await get_next_word(0)
    if not res:
        await GameStates.start.set()
        await message.answer('All is done!')
        return
    async with state.proxy() as data:
        data['step'] = 1
        data['pk'] = 1
        data['answer'] = res.get('gender')
        data['word'] = res.get('word')
        await message.answer(f'{data["step"]}. Das wort ist {data["word"]}', reply_markup=keyboards.inline_keyboard)


@dp.callback_query_handler(lambda c: c.data in ['der', 'die', 'das'], state=GameStates.all_words)
async def button_click_callback_all(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await callback_query.answer()
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data.get('answer'):
            await bot.send_message(callback_query.from_user.id, 'Ya\n')
            res = await get_next_word(data.get('pk'))
            if res:
                data['step'] += 1
                data['answer'] = res.get('gender')
                data['word'] = res.get('word')
                data['pk'] = res.get('pk')
                await bot.send_message(
                    callback_query.from_user.id,
                    f'{data["step"]}. Das wort ist {data["word"]}',
                    reply_markup=keyboards.inline_keyboard
                )
            else:
                await bot.send_message(callback_query.from_user.id, 'The game is over!')
                await GameStates.start.set()
        else:
            await bot.send_message(callback_query.from_user.id,
                                   'Nein\n',
                                   reply_markup=keyboards.inline_keyboard)
