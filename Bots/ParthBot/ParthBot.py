from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from Bots.config import TOKEN

from parth_backend import random_news

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def random_news(msg: types.Message):
    for i in random_news:
        await msg.answer(i)
    await msg.answer(f'')