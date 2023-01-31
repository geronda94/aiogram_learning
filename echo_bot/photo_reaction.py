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
@dp.message(F.content_type == ContentType.PHOTO)
async def send_photo_echo(message: Message):
    print(message) #message_id=148 date=datetime.datetime(2023, 1, 31, 9, 51, 54, tzinfo=datetime.timezone.utc) chat=Chat(id=413281115, type='private', title=None, username='username22549', first_name='...', last_name=None, is_forum=None, photo=None, active_usernames=None, emoji_status_custom_emoji_id=None, bio=None, has_private_forwards=None, has_restricted_voice_and_video_messages=None, join_to_send_messages=None, join_by_request=None, description=None, invite_link=None, pinned_message=None, permissions=None, slow_mode_delay=None, message_auto_delete_time=None, has_protected_content=None, sticker_set_name=None, can_set_sticker_set=None, linked_chat_id=None, location=None) message_thread_id=None from_user=User(id=413281115, is_bot=False, first_name='...', last_name=None, username='username22549', language_code='ru', is_premium=None, added_to_attachment_menu=None, can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None) sender_chat=None forward_from=None forward_from_chat=None forward_from_message_id=None forward_signature=None forward_sender_name=None forward_date=None is_topic_message=None is_automatic_forward=None reply_to_message=None via_bot=None edit_date=None has_protected_content=None media_group_id=None author_signature=None text=None entities=None animation=None audio=None document=None photo=[PhotoSize(file_id='AgACAgIAAxkBAAOUY9jkuuwlEe28wDasDE3hGZvd82EAAtrDMRt8ZclKw_FaRU7XjBABAAMCAANzAAMtBA', file_unique_id='AQAD2sMxG3xlyUp4', width=40, height=90, file_size=1023), PhotoSize(file_id='AgACAgIAAxkBAAOUY9jkuuwlEe28wDasDE3hGZvd82EAAtrDMRt8ZclKw_FaRU7XjBABAAMCAANtAAMtBA', file_unique_id='AQAD2sMxG3xlyUpy', width=144, height=320, file_size=13743), PhotoSize(file_id='AgACAgIAAxkBAAOUY9jkuuwlEe28wDasDE3hGZvd82EAAtrDMRt8ZclKw_FaRU7XjBABAAMCAAN4AAMtBA', file_unique_id='AQAD2sMxG3xlyUp9', width=360, height=800, file_size=55668), PhotoSize(file_id='AgACAgIAAxkBAAOUY9jkuuwlEe28wDasDE3hGZvd82EAAtrDMRt8ZclKw_FaRU7XjBABAAMCAAN5AAMtBA', file_unique_id='AQAD2sMxG3xlyUp-', width=576, height=1280, file_size=92940)] sticker=None video=None video_note=None voice=None caption=None caption_entities=None contact=None dice=None game=None poll=None venue=None location=None new_chat_members=None left_chat_member=None new_chat_title=None new_chat_photo=None delete_chat_photo=None group_chat_created=None supergroup_chat_created=None channel_chat_created=None message_auto_delete_timer_changed=None migrate_to_chat_id=None migrate_from_chat_id=None pinned_message=None invoice=None successful_payment=None connected_website=None passport_data=None proximity_alert_triggered=None forum_topic_created=None forum_topic_closed=None forum_topic_reopened=None video_chat_scheduled=None video_chat_started=None video_chat_ended=None video_chat_participants_invited=None web_app_data=None reply_markup=None

    await message.reply_photo(message.photo[0].file_id)




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
