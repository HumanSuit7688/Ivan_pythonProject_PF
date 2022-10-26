from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from Bots.config import TOKEN
from back_end_BTC import crypto_crash, inline_kb_st, inline_kb_ch

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, Выбирай криптовалюту и делай ставку!', reply_markup=inline_kb_ch)

crypto_id = ''
@dp.callback_query_handler(lambda c: c.data == 'button_btc')
async def change_btc(callback_query: types.CallbackQuery):
    crypto_id = 'bitcoin'
    await bot.edit_message_text('Теперь сделайте ставку', message_id=callback_query.message.message_id,
                          chat_id=callback_query.message.chat.id,
                          reply_markup=inline_kb_st)

@dp.callback_query_handler(lambda c: c.data == 'button_eth')
async def change_btc(callback_query: types.CallbackQuery):
    crypto_id = 'ethereum'
    await bot.edit_message_text('Теперь сделайте ставку', message_id=callback_query.message.message_id,
                          chat_id=callback_query.message.chat.id,
                          reply_markup=inline_kb_st)

@dp.callback_query_handler(lambda c: c.data == 'button_bnb')
async def change_btc(callback_query: types.CallbackQuery):
    crypto_id = 'binancecoin'
    await bot.edit_message_text('Теперь сделайте ставку', message_id=callback_query.message.message_id,
                          chat_id=callback_query.message.chat.id,
                          reply_markup=inline_kb_st)


@dp.callback_query_handler(lambda c: c.data == 'button_more')
async def button_more(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(crypto_crash(crypto_id, 'больше'))

@dp.callback_query_handler(lambda c: c.data == 'button_less')
async def button_more(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(crypto_crash(crypto_id, 'меньше'))



if __name__ == '__main__':
    executor.start_polling(dp)