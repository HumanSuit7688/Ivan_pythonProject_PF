from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from Bots.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

inline_kb1 = InlineKeyboardMarkup()
inline_btn_click = InlineKeyboardButton('Click!', callback_data='button_click')
inline_kb1.row(inline_btn_click)

x = 0
@dp.message_handler(commands='start')
async def clicker(message: types.message):
    await message.answer(f'Ваше количество кликов {x}', reply_markup=inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'button_click')
async def click(callback_query: types.CallbackQuery):
    global x
    await bot.answer_callback_query(callback_query.id)
    x += 1
    await bot.edit_message_text(f'Ваше количество кликов {x}',
                                message_id = callback_query.message.message_id,
                                chat_id= callback_query.message.chat.id,
                                reply_markup=inline_kb1)


if __name__ == '__main__':
    executor.start_polling(dp)