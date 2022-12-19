from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from Bots.config import TOKEN

import sqlite3 as sl
con = sl.connect('../my-test.db')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

inline_kb1 = InlineKeyboardMarkup()
inline_btn_click = InlineKeyboardButton('Click!', callback_data='button_click')
inline_kb1.row(inline_btn_click)

clicks = 0
@dp.message_handler(commands='start')
async def clicker(msg: types.Message):
    global clicks
    user_id = msg.from_user.id
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id, ))
    row = cur.fetchall()
    if row:
        cur.execute("SELECT click_count FROM users WHERE id = ?", (user_id, ))
        clicks = cur.fetchall()[0][0]
    else:
        cur.execute("INSERT INTO users VALUES(?, ?)", (user_id, 0))
        con.commit()
    msg = await msg.answer(f'Ваше количество кликов {clicks}', reply_markup=inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'button_click')
async def click(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.answer_callback_query(callback_query.id)
    cur = con.cursor()
    cur.execute("SELECT click_count FROM users WHERE id = ?", (user_id, ))
    clicks = cur.fetchall()[0][0]
    clicks += 1
    cur.execute("UPDATE users SET click_count = ? WHERE id = ?", (clicks, user_id,))
    con.commit()
    await bot.edit_message_text(f'Ваше количество кликов {clicks}',
                                message_id = callback_query.message.message_id,
                                chat_id= callback_query.message.chat.id,
                                reply_markup=inline_kb1)


if __name__ == '__main__':
    executor.start_polling(dp)