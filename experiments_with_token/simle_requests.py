import requests
import time
from data import TOKEN


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = TOKEN
TEXT: str = 'Мы законектились!'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int


while counter < MAX_COUNTER:
    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        print(updates['result'])
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1


##if updates['result']  если все ок то updates['result'] будет в таком JSON формате
# [
#   {
#     'update_id': 792864391,
#     'message': {
#       'message_id': 44,
#       'from': {
#         'id': 413281115,
#         'is_bot': False,
#         'first_name': '...',
#         'username': 'username22549',
#         'language_code': 'ru'
#       },
#       'chat': {
#         'id': 413281115,
#         'first_name': '...',
#         'username': 'username22549',
#         'type': 'private'
#       },
#       'date': 1675094450,
#       'text': 'пр'
#     }
#   }
# ]