from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from bot import dp

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])