from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from data import TOKEN
from aiogram.types import ContentType
from aiogram import F

bot: Bot = Bot(TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Ну что, начем?')


@dp.message(Command(commands=['help', 'functions']))
async def help_command(message: Message):
    await message.answer('Я много чего умею! Всего не перечесть!')



@dp.message(F.photo)
async def resend_photo(message: Message):
    print(message.json())

    photo_file =message.photo[0].file_id
    user = message.from_user.id

    await message.answer_photo(photo_file)
    await bot.send_photo(413281115, photo_file)
    await bot.send_message(413281115, f'Новое фото от пользователя {user}')



@dp.message(F.content_type == ContentType.STICKER)
async def resend_sticker(message: Message):
    print(message.json())
    self_sticker = message.sticker.file_id
    await message.reply_sticker(self_sticker)


@dp.message(F.content_type == ContentType.VOICE)
async def resend_voice(message: Message):
    self_voice = message.voice.file_id

    await message.reply_voice(self_voice)



@dp.message()
async def send_echo(message: Message):
    await message.reply(message.text)


dp.run_polling(bot)

