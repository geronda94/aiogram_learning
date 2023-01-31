from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from data import TOKEN

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Ну давай тогда начнем!')

@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(text=f'Я много чего умею, обо всем не рассказать')

@dp.message()
async def send_echo(message: Message):
    await message.reply(text=f'Все говорят {message.text} а ты купи слона!')

dp.run_polling(bot)
