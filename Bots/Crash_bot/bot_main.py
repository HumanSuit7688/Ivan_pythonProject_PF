import asyncio
from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from Bots.config import TOKEN
from back_end_BTC import crypto_crash, inline_kb_st, inline_kb_ch
from pycoingecko import CoinGeckoAPI
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
cg = CoinGeckoAPI()
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, Выбирай криптовалюту и делай ставку!', reply_markup=inline_kb_ch)
price = 0
crypto_id = ''
@dp.callback_query_handler(lambda c: c.data == 'button_btc')
async def change_btc(callback_query: types.CallbackQuery):
    global crypto_id
    global price
    crypto_id = 'bitcoin'
    crypto = cg.get_price(ids=crypto_id, vs_currencies='usd')
    price = crypto[crypto_id]['usd']
    print(price)
    await callback_query.message.edit_text('Теперь сделайте ставку', reply_markup=inline_kb_st)

@dp.callback_query_handler(lambda c: c.data == 'button_eth')
async def change_eth(callback_query: types.CallbackQuery):
    global crypto_id
    global price
    crypto_id = 'ethereum'
    crypto = cg.get_price(ids=crypto_id, vs_currencies='usd')
    price = crypto[crypto_id]['usd']
    await callback_query.message.edit_text('Теперь сделайте ставку', reply_markup=inline_kb_st)

@dp.callback_query_handler(lambda c: c.data == 'button_bnb')
async def change_bnb(callback_query: types.CallbackQuery):
    global crypto_id
    global price
    crypto_id = 'binancecoin'
    crypto = cg.get_price(ids=crypto_id, vs_currencies='usd')
    price = crypto[crypto_id]['usd']
    await callback_query.message.edit_text('Теперь сделайте ставку', reply_markup=inline_kb_st)

@dp.callback_query_handler(lambda c: c.data == 'button_more')
async def button_more(callback_query: types.CallbackQuery):
    print(callback_query.id)
    await callback_query.message.edit_text("Пожалуйста подождите 20 секунд")
    await asyncio.sleep(20)
    await callback_query.message.edit_text(crypto_crash(crypto_id, 'больше', price))

@dp.callback_query_handler(lambda c: c.data == 'button_less')
async def button_more(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Пожалуйста подождите 20 секунд")
    await asyncio.sleep(20)
    await callback_query.message.edit_text(crypto_crash(crypto_id, 'меньше', price))



if __name__ == '__main__':
    executor.start_polling(dp)