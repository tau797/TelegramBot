# подключаем библиотеку Телебот
import telebot as tb

# объявляем токен Телеграм-бота
token = '6886566042:AAGlHIz56IneBdd-G_QKHTmlYZ2fOxBSBOA'

#моё имя Андрей
hoz = 'Андрей'

#Создание бота 
bot = tb.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)
    if (hoz in message.text): bot.send_message(message.chat.id, 'Здравствуй, Хозяин!')

# постоянно обращается к серверам ТГ, none stop - не обращать внимание на ошибки!
bot.polling(none_stop=True)
