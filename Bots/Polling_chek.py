from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from Bots.config import TOKEN
import asyncio
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


polling = ''
@dp.message_handler(commands='pol')
async def check_polling(message: types.Message):
    global polling
    poll = await bot.send_poll(chat_id=message.chat.id, question='Как дела?', options=['Хорошо', 'Нормально', 'Плохо'])
    time = 10
    await asyncio.sleep(time)
    polling = await bot.stop_poll(chat_id=message.chat.id, message_id=poll.message_id)
    print(polling)


@dp.message_handler(commands='test')
async def check_polling(message: types.Message):
    global polling
    polling = await bot.stop_poll(chat_id=message.chat.id, message_id=message.message_id)
    print(polling)
    await message.answer('Проверка...')


@dp.message_handler(commands='chat_pol')
async def check_polling(message: types.Message):
    global polling
    time = 7
    await bot.send_message(-1001810098186, 'Привет, у меня тут опросик...')
    poll = await bot.send_poll(-1001810098186, 'Как дела?', ['Хорошо', 'Нормально', 'Плохо'])
    await asyncio.sleep(time)
    polling = await bot.stop_poll(-1001810098186, message_id=poll.message_id)
    vot_counts = []
    x = 0
    for u in polling.options, range(len(polling.options)):
        vot_counts.append(polling.options[x].voter_count)
        x += 1
    max_vot = max(vot_counts)
    ind_max_vot = vot_counts.index(max_vot)
    big_var = polling.options[ind_max_vot].text
    tot_voit = polling.total_voter_count
    big_var_c = max_vot
    await message.answer(f'Всего голосов - {tot_voit}\nБольше всего голосов набрал вариант - "{big_var}" {big_var_c} голосов')
    print(polling)



if __name__ == '__main__':
    executor.start_polling(dp)
