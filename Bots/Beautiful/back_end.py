from aiogram import Dispatcher, types
from Bots.Beautiful.back_buttons import inline_kb1, inline_kb2, inline_kb3, inline_kb4, inline_kb5, inline_kb6, ReplyKeyboardRemove

async def handler_start(message: types.Message):
    await message.answer('Ну что ж, начнём!\nЧего же ты хочешь?...', reply_markup=inline_kb1)


async def handler_hello(message: types.Message):
    await message.answer('Hello there')


async def handler_btn_food(callback: types.CallbackQuery):
    await callback.message.edit_text('Выбирай.', reply_markup=inline_kb2)


async def handler_btn_drink(callback: types.CallbackQuery):
    await callback.message.edit_text('Выбирай!', reply_markup=inline_kb3)


async def handler_btn_back(callback: types.CallbackQuery):
    await callback.message.edit_text('Чего же ты хочешь?', reply_markup=inline_kb1)


async def handler_btn_drink_hot(callback: types.CallbackQuery):
    await callback.message.edit_text('Выбирай!', reply_markup=inline_kb4)


async def handler_btn_drink_cold(callback: types.CallbackQuery):
    await callback.message.edit_text('Выбирай!', reply_markup=inline_kb5)


async def handler_btn_drink_alk(callback: types.CallbackQuery):
    await callback.message.edit_text('Выбирай!', reply_markup=inline_kb6)

async def handler_btn_back2(callback: types.CallbackQuery):
    await callback.message.edit_text('Чего же ты хочешь?', reply_markup=inline_kb3)

async def handler_echo(message: types.Message):
    await message.answer(message.text)

async def cancler(message: types.Message):
    await message.answer('deleted', reply_markup=ReplyKeyboardRemove())


def register_handler_menu(dp: Dispatcher):
    dp.register_message_handler(handler_start, commands='start')
    dp.register_message_handler(handler_hello, commands='hi')
    dp.register_message_handler(handler_echo, text='echo')
    dp.register_callback_query_handler(handler_btn_food, lambda c: c.data == 'button_food')
    dp.register_callback_query_handler(handler_btn_drink, lambda c: c.data == 'button_drink')
    dp.register_callback_query_handler(handler_btn_back, lambda c: c.data == 'button_f_back')
    dp.register_callback_query_handler(handler_btn_drink_hot, lambda c: c.data == 'button_drink_hot')
    dp.register_callback_query_handler(handler_btn_drink_cold, lambda c: c.data == 'button_drink_cold')
    dp.register_callback_query_handler(handler_btn_drink_alk, lambda c: c.data == 'button_drink_alk')
    dp.register_callback_query_handler(handler_btn_back2, lambda c: c.data == 'button_f_back2')
    dp.register_message_handler(cancler, commands='del')

