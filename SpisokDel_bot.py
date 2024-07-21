# Телеграм-бот, ведущий список задач
# (C) TAU март 2024

# Библиотеки
from random import choice
import telebot as tb
from telebot import types

token = '6886566042:AAGlHIz56IneBdd-G_QKHTmlYZ2fOxBSBOA'

#моё имя Андрей
#hoz = 'Андрей'

#задаем признак тега
tg = '#'

#Создание бота
bot = tb.TeleBot(token)

RANDOM_TASKS = ["Написать книгу #работа", "Написать Телеграм-бота #работа", "Починить машину #авто"]

todos = dict()

HELP = '''
Список доступных команд:
/покажи - напечать все задачи на заданную дату
например:
'/покажи сегодня' или '/покажь 29.03'

/все -  показать все имеющиеся задачи

/по - показать задачи выбранного вида
например: '/по #дом'

/еще - добавить задачу
например:
'/еще сегодня совершить подвиг'

Вы можете указать род задачи после тега '#', например
'/еще сегодня написать статью #работа'

/random - добавить на сегодня случайную задачу

/help - эта  подсказка

'''

#При запуске
@bot.message_handler(commands=['start'])
def privet(message):
    markup = types.ReplyKeyboardMarkup()
    k1 = types.KeyboardButton('/помоги')
    k2 = types.KeyboardButton('/покажи сегодня')
    k3 = types.KeyboardButton('/все')
    markup.row(k1, k2, k3)
    bot.send_message(message.chat.id, f'<i>Приветствую, <b>{message.from_user.first_name}</b></i>',parse_mode='html',reply_markup=markup)

    add_todo('сегодня', 'изучить бота TAU!') # шутка
    #todos['сегодня'] = 'изучить бота TAU!'

#       bot.send_message(message.chat.id, "Как Вас зовут? Чтобы узнать возможности, пиши /help")
#       if (hoz in message.text):
#           bot.send_message(message.chat.id, 'Здравствуй, Хозяин!')


# добавление задачи на дату
def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
      if not task in todos[date]: #добавляем ежели не дубль
        todos[date].append(task)
        return f'Задача {task} добавлена на дату {date}'
      else:
        return f'Задача {task} уже была запланирована на {date}'
    else:
        todos[date] = [task]

# добавляем реакцию бота на команду 'help'
@bot.message_handler(commands=['help','помоги'])
def help(message):
    bot.send_message(message.chat.id, HELP)


# добавляем реакцию бота на команду 'random'
@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    bot.send_message(message.chat.id, add_todo('сегодня', task))


# добавляем реакцию бота на команду 'add'
@bot.message_handler(commands=['add','еще','ещё'])
def add(message):
    # обработка пустого задания
    if len(message.text)==4:
        bot.send_message(message.chat.id, 'нужно указать дату и задачу')
        return
    _, date, tail = message.text.split(maxsplit=2)
    #print(date,tail)

    task = ' '.join([tail])
    #print (task)
    add_todo(date, task)
    bot.send_message(message.chat.id, 'Задача добавлена!')

# добавляем реакцию бота на команду 'print'
@bot.message_handler(commands=['print','покажь','покажи'])
def print_(message):
    # обработка пустого задания
    if len(message.text)<10:
        bot.send_message(message.chat.id, 'нужно указать дату')
        return
    date = message.text.split()[1].lower()

    if date in todos:
        tasks = ''
        for task in todos[date]:
            #tasks += f'[ ] {task}\n'
            tasks += (task+'\n')
    else:
        tasks = 'На этот день ничего не найдено'
    bot.send_message(message.chat.id, tasks)

# добавляем реакцию бота на команду 'all'
@bot.message_handler(commands=['all','все','всё'])
def all_(message):
    #показываем все
    ll = " "
    for date,task in todos.items():
          ll += str(date)+': '+str(task)+'\n'
    bot.send_message(message.chat.id, ll)


# добавляем реакцию бота на команду 'show'
@bot.message_handler(commands=['show','по','вид'])
def show_(message):
    if len(message.text)==0:
        vid=' '
    else:
      if tg in message.text:
        ll = '-'
        vid = message.text.split(tg)[1].lower()

        for date,task in todos.items():
          for el in task:
            #print(task) отладочная печать
            if (vid in str(el)):
              ll += str(date)+': '+str(el)+'\n'
      else:
        ll = 'Укажите вид задачи после '+tg

    bot.send_message(message.chat.id, ll)

bot.polling(none_stop=True)
