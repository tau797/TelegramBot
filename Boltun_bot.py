# Телеграм-бот "Болтун"
# (C) TAU июль 2024

# Библиотеки
import random
import telebot as tb
from telebot import types

token = '7253469934:AAHnBx0xCAeD3zhagbqOY3gYnMqeNyL3FYA'

# задаем список состояний бота
user_states = {}

#Создание бота
bot = tb.TeleBot(token)

HELP = '''
Это бот "Болтун".

Он умеет общаться на разные темы:
-- музыка
-- кино
-- погода
-- спорт
-- еда

/start - перезапуск бота
/help (или /помоги) - эта  подсказка

'''

#При запуске
@bot.message_handler(commands=['start'])
def privet(message):
    # Начальное состояние - беседа на общие темы

    markup = types.ReplyKeyboardMarkup()
    k1 = types.KeyboardButton('/спорт')
    k2 = types.KeyboardButton('/погода')
    k3 = types.KeyboardButton('/фильмы')
    k4 = types.KeyboardButton('/еда')
    k5 = types.KeyboardButton('/музыка')
    markup.row(k1, k2, k3, k4, k5)
    bot.send_message(message.chat.id, f'<i>Чатбот Болтун приветствует <b>{message.from_user.first_name}!</b></i>',parse_mode='html',reply_markup=markup)
    bot.send_message(message.chat.id, "Пишите боту на разные темы!")

    message.chat.id = 'Frazy'

# добавляем реакцию бота на команду 'сказать'
@bot.message_handler(commands=['say','сказать','вопрос','answer','c','s','с'])
def otvet(message):
    if len(message.text)<=4:
        bot.send_message(message.chat.id, 'Говорите, я жду!')
        return


# добавляем реакцию бота на команду 'спорт'
@bot.message_handler(commands=['sport','спорт'])
def set_sport(message):
    user_states[message.chat.id] = 'Sport'
    bot.send_message(message.chat.id, 'Ну что ж, поговорим о спорте... \nСмотришь хоккей?')

# добавляем реакцию бота на команду 'музыка'
@bot.message_handler(commands=['music','музыка'])
def set_music(message):
    user_states[message.chat.id] = 'Music'
    bot.send_message(message.chat.id, 'Ну что ж, поговорим о музыке... Любишь рок?')

# добавляем реакцию бота на команду 'погода'
@bot.message_handler(commands=['weather','погода'])
def set_weather(message):
    user_states[message.chat.id] = 'Weather'
    bot.send_message(message.chat.id, 'Ну что ж, поговорим о погоде... \nЖарковато, да?')

# добавляем реакцию бота на команду 'фильмы'
@bot.message_handler(commands=['films','кино','фильмы'])
def set_films(message):
    user_states[message.chat.id] = 'Films'
    bot.send_message(message.chat.id, 'Ну что ж, поговорим о кино... \nКто у тебя любимый режиссер?')

# добавляем реакцию бота на команду 'еда'
@bot.message_handler(commands=['dishes','еда','пища'])
def set_dishes(message):
    user_states[message.chat.id] = 'Dishes'
    bot.send_message(message.chat.id, 'Ну что ж, поговорим о еде... Я бы не отказался поесть, а ты?')


# добавляем реакцию бота на команду 'help'
@bot.message_handler(commands=['help','помоги'])
def help(message):
    bot.send_message(message.chat.id, HELP)

# обработка сообщений БЕЗ команд - произвольных сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):

    # Детектор тем

    themes = {
      'Weather': ['холодно', 'жарко', 'дождь', 'снег', 'погода','лето','зима'],
      'Music': ['рок', 'музыка', 'попса', 'композитор', 'классику','слушаешь'],
      'Sport':['Спартак', 'ЦСКА', 'хоккей', 'футбол', 'теннис', 'спорт', 'чемпионат','чемпион'],
      'Films':['фильм', 'кино', 'режиссер', 'боевик', 'ужасы', 'смотреть','смотришь','жанр'],
      'Dishes':['еда', 'сосиски', 'малина', 'пельмени', 'кушать','завтрак', 'блюда','пить','обед'],
    }

    i = 0
    FileFraz = "Frazy.txt"  # Имя файла с предопределенными заранее фразами
    #FileOtv = "Otvety.txt"  # Имя файла с предопределенными заранее фразами

    chat_id = message.chat.id
    if chat_id not in user_states:
        user_states[chat_id] = 'Frazy'

    for key,value in themes.items():
        for slov in value:
          if slov in message.text.lower():
              user_states[chat_id] = key
              #bot.send_message(message.chat.id, 'Распознали тему '+key)


    # По состоянию беседы в ТГ чате определяем тему
    FileFraz = user_states[chat_id] +'1.txt'
    #bot.send_message(message.chat.id, "Открываем файл "+FileFraz)

    # Основной массив для хранения фраз, вводимых пользователем
    # Заранее внесены предопределенные фразы 'ни о чем' и вопросы
    Frazy = ["Как дела?", "Как тебе погодка?", "За Спартак болеешь или за ЦСКА?"]

    Otvety = ["Вы вообще с какой целью интересуетесь?", "Сам как думаешь?", "Да!", "Нет!",
               "Штирлиц никогда еще не был столь близок к провалу...", "Не скажу!",
               "Надо подумать!", "Сразу и не ответишь..."
               ]

    f = open(FileFraz, "r") # открываем файл фраз
    Frazy=f.readlines()
    f.close()

    i = len(Frazy)  # подсчитываем, сколько у нас предопределенных фраз

    # f = open(FileOtv, "r") # открываем файл ответов
    # Otvety = f.readlines()
    # f.close()

    k = len(Otvety)  # подсчитываем, сколько у нас предопределенных ответов

    Frazy.append(message.text+'\n')
    # Иногда добавляем имя пользователя для интимности
    if random.randint(0, 9) > 7:
       lin=message.from_user.first_name+', '
    else:
       lin = ""

    # Выбираем случайный ответ из имеющихся
    if message.text.endswith('?'):
      j = random.randint(0, k - 1)
      lin += Otvety[j]
    else:
      j = random.randint(0, i - 1)
      lin += Frazy[j]

    i += 1

    # Для сохранения сказанного
    f = open(FileFraz, "w") # открываем файл фраз
    f.writelines(Frazy)
    f.close()

    bot.send_message(message.chat.id, lin)

bot.polling(none_stop=True)
