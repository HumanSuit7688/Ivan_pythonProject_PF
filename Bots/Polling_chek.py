from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from Bots.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


polling = ''
@dp.message_handler(commands='pol')
async def check_polling(message: types.Message):
    global polling
    polling = await message.answer_poll('Как дела?', ['Хорошо', 'Нормально', 'Плохо'])

print(polling)
@dp.message_handler(commands='test')
async def check_polling(message: types.Message):
    global polling
    await message.answer('Проверка...')
    print(polling.options)
@dp.message_handler(commands='chat')
async def check_polling(message: types.Message):
    await bot.send_message(-1001810098186, 'Hellor from PM')

if __name__ == '__main__':
    executor.start_polling(dp)
