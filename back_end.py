from aiogram import Bot, Dispatcher, types
from back_buttons import inline_kb1

async def handler_start(message: types.Message):
    await message.answer('Стандартный текст')


async def handler_hello(message: types.Message):
    await message.answer('Hello there', reply_markup=inline_kb1)


async def handler_btn(callback: types.CallbackQuery):
    await callback.answer('Победа')


async def handler_echo(message: types.Message):
    await message.answer(message.text)


def register_handler_menu(dp: Dispatcher):
    dp.register_message_handler(handler_start, commands='start')
    dp.register_message_handler(handler_hello, commands='hi')
    dp.register_message_handler(handler_echo, text='echo')
    dp.register_message_handler(handler_btn, callback='button_ura')

