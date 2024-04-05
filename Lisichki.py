import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7170566938:AAHnm7QlruETXKwHO9EmRDxTBfe8Lp4QwNQ'
TEXT = 'Надо подумать над '

API_CATS_URL = 'https://randomfox.ca/floof/'

ERROR_TEXT = 'Здесь должна была быть картинка с лисой:('
MAX_COUNTER = 111111

offset = -2
counter = 0
chat_id: int
i_link: str

while counter < MAX_COUNTER:
    #print('заход =', counter)  #отладочная печать
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
      for result in updates['result']:
        offset = result['update_id']
        chat_id = result['message']['from']['id']
        i_response = requests.get(API_CATS_URL)

        if i_response.status_code == 200:
          sod = str(i_response.json())
          i_link = i_response.json()['image']
          requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={i_link}')
          #requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={sod}')
        else:
          requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            TEXT+=(','+result['message']['text'])
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1
