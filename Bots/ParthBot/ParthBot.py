from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from Bots.config import TOKEN
from parth_backend import random_news
from parth_backend import scroll
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_news(message: types.Message):
    news = random_news()
    await message.answer(f'{news[1]}\n{news[0]}\n{news[3]}', reply_markup=scroll)


@dp.callback_query_handler(lambda c: c.data == 'button_next_scr')
async def procces_next_news(callback_query: types.CallbackQuery):
    news = random_news()
    await bot.edit_message_text(f'{news[0]}\n{news[3]}',
                                message_id=callback_query.message.message_id,
                                chat_id=callback_query.message.chat.id,
                                reply_markup=scroll)


@dp.callback_query_handler(lambda c: c.data == 'button_prev_scr')
async def proccess_previous_news(callback_query: types.CallbackQuery):
    news = random_news()
    await bot.edit_message_media(news[1])

if __name__ == '__main__':
    executor.start_polling(dp)