# pip install -U aiogram
# pip install environs
from environs import Env
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import random


env = Env()
env.read_env()

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = env("BOT_TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
arrId = dict()

# Этот хэндлер будет срабатывать на команду "/start"
# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')




async def send_echo(message: Message):
    chat_id = str(message.chat.id)
    print(arrId)
    if chat_id in arrId or message.text == '/yes':
        if chat_id not in arrId:        
            num = str(random.randint(0,100))
            arrId[chat_id]=[1,5,num]
            await message.answer(text="Введите число")
        elif arrId[chat_id][0]==1:
            if message.text==arrId[chat_id][-1]:
                arrId.pop(chat_id)
                await message.answer(text= "Вы угадали")
            else:
                arrId[chat_id][1]-=1
                print(arrId)
                if not arrId[chat_id][1]:
                    arrId.pop(chat_id)
                    await message.answer(text= "попытки исчерпаны вы проиграли")
                await message.answer(text= "Вы не угадали попробуйте ещё")
    else:
        await message.answer(text="давайте сыграем в Игру 'Угадай число'/yes")


# dp.message.register(process_start_command, Command(commands='start'))
# dp.message.register(process_help_command, Command(commands='help'))
# dp.message.register(test_command, Command(commands='test'))
# dp.message.register(testRU_command, Command(commands='тест'))
# dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)



if __name__ == '__main__':
    dp.run_polling(bot)