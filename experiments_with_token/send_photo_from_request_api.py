import requests
import time
from data import TOKEN

#  в результате работы этого скрипта получаем гет запррос такого формата
'https://api.telegram.org/bot5922136610:AAHpecQUXLSkuJDoglLXLOtg1xGgXyIJmbY/sendPhoto' \
'?chat_id=413281115&photo=https://purr.objects-us-east-1.dream.io/i/img-20170715-wa0004.jpg'

#https://api.telegram.org/bot5922136610:AAHpecQUXLSkuJDoglLXLOtg1xGgXyIJmbY/sendPhoto?chat_id=413281115&photo=https://purr.objects-us-east-1.dream.io/i/img-20170715-wa0004.jpg

https://api.telegram.org/bot5922136610:AAHpecQUXLSkuJDoglLXLOtg1xGgXyIJmbY/getUpdates?offset=-1


API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://aws.random.cat/meow'
BOT_TOKEN: str = TOKEN
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('

offset: int = -2
counter: int = 0
cat_response: requests.Response
cat_link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1