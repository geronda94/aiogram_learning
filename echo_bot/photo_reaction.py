from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from data import TOKEN
from aiogram.types import ContentType
from aiogram import F


API_TOKEN: str = TOKEN

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')



# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)




# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=f'Даже не знаю что вам ответить на: {message.text}') #.answer - отправка ответа без пересылки

    #если нужно отправить в другой чат сообщение то можем написть такие параметры в функцию
    #await bot.send_message(chat_id='ID или название чата', text='Какой-то текст') #413281115
    #Аналогичные действия другим способом, автоматичски вставляетя чат оправителя
    #await bot.send_message(message.chat.id, message.text) # Вместо message.text  можно указать параметр text='Привет'




dp.run_polling(bot)
