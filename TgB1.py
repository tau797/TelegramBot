# подключаем библиотеку Телебот
import telebot as tb

# объявляем токен Телеграм-бота
token = '6886566042:AAGlHIz56IneBdd-G_QKHTmlYZ2fOxBSBOA'

bot = tb.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
