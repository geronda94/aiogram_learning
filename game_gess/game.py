import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
from data import TOKEN


bot: Bot = Bot(TOKEN)
dp: Dispatcher = Dispatcher()

ATTEMPTS: int = 5
user: dict = {
    'in_game':False,
    'secret_number':None,
    'attempts':None,
    'total_games':0,
    'wins':0 }

def get_randon_number() -> int:
    return random.randint(0,100)

@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду /help')


@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


@dp.message(Command(commands=['stat']))
async def stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {user["total_games"]}\n'
                         f'Игр выиграно: {user["wins"]}')






dp.run_polling(bot)


