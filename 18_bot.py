'''
    Content types:
    text, audio, photo, voice.
'''
# pip3 install pyTelegramBotAPI
import telebot

bot = telebot.TeleBot('1833852066:AAEJO3C4KJllccymXLilsD3csOkKfqiZRnI')


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handler_start_help(message):
    #print(message.text)
    bot.send_message(message.chat.id, f'Привет, {message.chat.username}')
#    pass

# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['sticker'])
def stiker(message):
    bot.reply_to(message, 'рассмешил')

@bot.message_handler(content_types=['audio'])
def audio(message):
    bot.reply_to(message, 'Отличный звук')

@bot.message_handler(content_types=['voice'])
def voice(message):
    bot.reply_to(message, 'У тебя интересный голос!')

@bot.message_handler(content_types=['photo',])
def photo(message):
    bot.reply_to(message, 'Интересное фото!')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.reply_to(message, 'Продолжайте писать.')

#@bot.message_handler(content_types=['sticker'])
#def sticker_id(message):
#    print(message)

#    pass

bot.polling(none_stop=True)
