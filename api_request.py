import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '5922136610:AAHpecQUXLSkuJDoglLXLOtg1xGgXyIJmbY'
TEXT: str = 'Ура! Классный апдейт!'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)




##if updates['result']
# {
#   "ok": true,
#   "result": [
#     {
#       "update_id": 792864383,
#       "message": {
#         "message_id": 32,
#         "from": {
#           "id": 413281115,
#           "is_bot": false,
#           "first_name": "...",
#           "username": "username22549",
#           "language_code": "ru"
#         },
#         "chat": {
#           "id": 413281115,
#           "first_name": "...",
#           "username": "username22549",
#           "type": "private"
#         },
#         "date": 1675091908,
#         "text": "\u043f\u0440\u0438\u0432\u0435\u0442"
#       }
#     }
#   ]
# }
