import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from back_end import register_handler_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


async def main():
    register_handler_menu(dp)
    await dp.skip_updates()
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
