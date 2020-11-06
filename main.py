import telebot
import constants

bot = telebot.TeleBot(constants.token)

#bot.send_message(578450831,"text")

#upd = bot.get_updates()
#print(upd)

#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда вы закажите подписку, вы получите весь список команд')



@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - Custudio.')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    else:
        bot.send_message(chat_id, 'Простите, я ваc не понял :(')

@bot.message_handler(content_types=['commands'])
def handle_command(message):
    print("Пришла команда")
@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Мои возможности весьма специфичны""")
@bot.message_handler(content_types=['text'])
def handle_text(message):
   print("Пришло простое сообщение")
@bot.message_handler(content_types=['document'])
def handle_document(message):
    print("Пришел документ")
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    print("Пришла аудиозапись")

@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво.')

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    print("Пришел стикер")


bot.polling(none_stop=True, interval=0)
