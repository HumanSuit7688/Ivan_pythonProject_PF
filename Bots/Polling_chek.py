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
    big = 0
    var_count = 0
    for i in vot_counts:
        big = i
        if i > big:
            big = i
            var_count = x
        else:
            pass
        x += 1

    big_var = polling.options[var_count].text
    tot_voit = polling.total_voter_count
    big_var_c = polling.options[var_count].voter_count
    await message.answer(f'Всего голосов - {tot_voit}\nБольше всего голосов набрал вариант - "{big_var}" {big_var_c}- голосов')
    print(polling)



if __name__ == '__main__':
    executor.start_polling(dp)
