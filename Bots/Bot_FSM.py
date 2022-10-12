from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from Bots.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

class UserState(StatesGroup):
    name = State()
    address = State()

    #что-то

@dp.message_handler(commands=['start'])
async def user_register(message: types.Message):
    await message.answer("Регистрация"
                         "Введите своё имя")
    await UserState.name.set()

@dp.message_handler(text=['приветик'])
async def user_register(message: types.Message):
    await message.answer("Привет, лови пасхалку\n"
                         "Регистрация!\n"
                         "Введите своё имя")
    await UserState.name.set()

@dp.message_handler(state=UserState.name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("Отлично! Теперь введите ваш адрес.")
    await UserState.address.set()

@dp.message_handler(state=UserState.address)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()
    await message.answer(f"Имя: {data['username']}\n"
                         f"Адрес: {data['address']}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp)