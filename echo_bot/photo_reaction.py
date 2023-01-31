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
    print(message.json())
    #{"message_id": 150, "date": 1675163969, "chat": {"id": 413281115, "type": "private", "title": null, "username": "username22549", "first_name": "...", "last_name": null, "is_forum": null, "photo": null, "active_usernames": null, "emoji_status_custom_emoji_id": null, "bio": null, "has_private_forwards": null, "has_restricted_voice_and_video_messages": null, "join_to_send_messages": null, "join_by_request": null, "description": null, "invite_link": null, "pinned_message": null, "permissions": null, "slow_mode_delay": null, "message_auto_delete_time": null, "has_protected_content": null, "sticker_set_name": null, "can_set_sticker_set": null, "linked_chat_id": null, "location": null}, "message_thread_id": null, "from_user": {"id": 413281115, "is_bot": false, "first_name": "...", "last_name": null, "username": "username22549", "language_code": "ru", "is_premium": null, "added_to_attachment_menu": null, "can_join_groups": null, "can_read_all_group_messages": null, "supports_inline_queries": null}, "sender_chat": null, "forward_from": null, "forward_from_chat": null, "forward_from_message_id": null, "forward_signature": null, "forward_sender_name": null, "forward_date": null, "is_topic_message": null, "is_automatic_forward": null, "reply_to_message": null, "via_bot": null, "edit_date": null, "has_protected_content": null, "media_group_id": null, "author_signature": null, "text": null, "entities": null, "animation": null, "audio": null, "document": null, "photo": [{"file_id": "AgACAgIAAxkBAAOWY9j5Qcm-20vd97jJBeUDp4rtoFkAAtrDMRt8ZclKw_FaRU7XjBABAAMCAANzAAMtBA", "file_unique_id": "AQAD2sMxG3xlyUp4", "width": 40, "height": 90, "file_size": 1023}, {"file_id": "AgACAgIAAxkBAAOWY9j5Qcm-20vd97jJBeUDp4rtoFkAAtrDMRt8ZclKw_FaRU7XjBABAAMCAANtAAMtBA", "file_unique_id": "AQAD2sMxG3xlyUpy", "width": 144, "height": 320, "file_size": 13743}, {"file_id": "AgACAgIAAxkBAAOWY9j5Qcm-20vd97jJBeUDp4rtoFkAAtrDMRt8ZclKw_FaRU7XjBABAAMCAAN4AAMtBA", "file_unique_id": "AQAD2sMxG3xlyUp9", "width": 360, "height": 800, "file_size": 55668}, {"file_id": "AgACAgIAAxkBAAOWY9j5Qcm-20vd97jJBeUDp4rtoFkAAtrDMRt8ZclKw_FaRU7XjBABAAMCAAN5AAMtBA", "file_unique_id": "AQAD2sMxG3xlyUp-", "width": 576, "height": 1280, "file_size": 92940}], "sticker": null, "video": null, "video_note": null, "voice": null, "caption": null, "caption_entities": null, "contact": null, "dice": null, "game": null, "poll": null, "venue": null, "location": null, "new_chat_members": null, "left_chat_member": null, "new_chat_title": null, "new_chat_photo": null, "delete_chat_photo": null, "group_chat_created": null, "supergroup_chat_created": null, "channel_chat_created": null, "message_auto_delete_timer_changed": null, "migrate_to_chat_id": null, "migrate_from_chat_id": null, "pinned_message": null, "invoice": null, "successful_payment": null, "connected_website": null, "passport_data": null, "proximity_alert_triggered": null, "forum_topic_created": null, "forum_topic_closed": null, "forum_topic_reopened": null, "video_chat_scheduled": null, "video_chat_started": null, "video_chat_ended": null, "video_chat_participants_invited": null, "web_app_data": null, "reply_markup": null}

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
