import asyncio
from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from Bots.config import TOKEN
from back_end_BTC import crypto_crash, inline_kb_st, inline_kb_ch, inline_kb_st_int
from pycoingecko import CoinGeckoAPI
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
cg = CoinGeckoAPI()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, Хочешь сыграть в безобидный симулятор казино?\n'
                         'Тогда выбирай криптовалюту и делай ставку!', reply_markup=inline_kb_ch)


price = 0
crypto_id = ''
stv = ''


@dp.callback_query_handler(lambda c: c.data == 'button_btc')
async def change_btc(callback_query: types.CallbackQuery):
    global crypto_id
    global price
    crypto_id = 'bitcoin'
    crypto = cg.get_price(ids=crypto_id, vs_currencies='usd')
    price = crypto[crypto_id]['usd']
    print(price)
    await callback_query.message.edit_text('Отлично, теперь сделай ставку', reply_markup=inline_kb_st)


@dp.callback_query_handler(lambda c: c.data == 'button_eth')
async def change_eth(callback_query: types.CallbackQuery):
    global crypto_id
    global price
    crypto_id = 'ethereum'
    crypto = cg.get_price(ids=crypto_id, vs_currencies='usd')
    price = crypto[crypto_id]['usd']
    await callback_query.message.edit_text('Найс, теперь делай ставку', reply_markup=inline_kb_st)


@dp.callback_query_handler(lambda c: c.data == 'button_bnb')
async def change_bnb(callback_query: types.CallbackQuery):
    global crypto_id
    global price
    crypto_id = 'binancecoin'
    crypto = cg.get_price(ids=crypto_id, vs_currencies='usd')
    price = crypto[crypto_id]['usd']
    await callback_query.message.edit_text('Хорош, теперь сделай ставку', reply_markup=inline_kb_st)


@dp.callback_query_handler(lambda c: c.data == 'button_more')
async def button_more(callback_query: types.CallbackQuery):
    global stv
    print(callback_query.id)
    stv = 'больше'
    await callback_query.message.edit_text("И последнее, выбери размер твоей ставки", reply_markup=inline_kb_st_int)


@dp.callback_query_handler(lambda c: c.data == 'button_less')
async def button_more(callback_query: types.CallbackQuery):
    global stv
    stv = 'меньше'
    await callback_query.message.edit_text("И последнее, выбери размер твоей ставки", reply_markup=inline_kb_st_int)


@dp.callback_query_handler(lambda c: c.data == 'button_100c')
async def button_st_100c(callback_query: types.CallbackQuery):
    global stv
    await callback_query.message.edit_text("Супер, подожди минутку и увидишь результат")
    await asyncio.sleep(60)
    await callback_query.message.edit_text(crypto_crash(crypto_id, stv, price, 100)[0])
    await callback_query.message.answer("Ваш баланс: " + crypto_crash(crypto_id, stv, price, 100)[1] + "монет")


@dp.callback_query_handler(lambda c: c.data == 'button_200c')
async def button_st_100c(callback_query: types.CallbackQuery):
    global stv
    await callback_query.message.edit_text("Супер, подожди минутку и увидишь результат")
    await asyncio.sleep(60)
    await callback_query.message.edit_text(crypto_crash(crypto_id, stv, price, 200)[0])
    await callback_query.message.answer("Ваш баланс: " + crypto_crash(crypto_id, stv, price, 200)[1] + " монет")


@dp.callback_query_handler(lambda c: c.data == 'button_500c')
async def button_st_100c(callback_query: types.CallbackQuery):
    global stv
    await callback_query.message.edit_text("Супер, подожди минутку и увидишь результат")
    await asyncio.sleep(60)
    await callback_query.message.edit_text(crypto_crash(crypto_id, stv, price, 500)[0])
    await callback_query.message.answer("Ваш баланс: " + crypto_crash(crypto_id, stv, price, 500)[1] + "монет")


@dp.callback_query_handler(lambda c: c.data == 'button_1000c')
async def button_st_100c(callback_query: types.CallbackQuery):
    global stv
    await callback_query.message.edit_text("Супер, подожди минутку и увидишь результат")
    await asyncio.sleep(60)
    await callback_query.message.edit_text(crypto_crash(crypto_id, stv, price, 1000)[0])
    await callback_query.message.answer("Ваш баланс: " + crypto_crash(crypto_id, stv, price, 1000)[1] + "монет")


if __name__ == '__main__':
    executor.start_polling(dp)
