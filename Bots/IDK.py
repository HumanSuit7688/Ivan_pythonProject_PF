from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from Bots.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


Tables = InlineKeyboardMarkup()
table1 = InlineKeyboardButton("t 5 people", callback_data='button_1table_5p')
table2 = InlineKeyboardButton("t 3 people", callback_data='button_table_3p')
table3 = InlineKeyboardButton("t 5 people", callback_data='button_2table_5p')
Tables.row(table1, table2, table3)


Exit = InlineKeyboardMarkup()
exit = InlineKeyboardButton("Выход", callback_data='exit')
Exit.row(exit)


class UserState(StatesGroup):
    lobby = State()
    room = State()


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    await message.answer("Добро Пожаловать, У меня есть две комнаты на 5 человек \n и одна комната на 3-ёх человек", reply_markup=Tables)
    await UserState.lobby.set()

@dp.callback_query_handler(lambda c: c.data == 'button_1table_5p')
async def table1_5p(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Вы зашли в первую комнату.", reply_markup=Exit)


@dp.callback_query_handler(lambda c: c.data == 'button_table_3p')
async def table_3p(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Вы зашли во вторую комнату.", reply_markup=Exit)


@dp.callback_query_handler(lambda c: c.data == 'button_2table_5p')
async def table2_5p(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Вы зашли в третью комнату.", reply_markup=Exit)



if __name__ == '__main__':
    executor.start_polling(dp)