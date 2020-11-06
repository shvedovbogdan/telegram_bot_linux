import types

import telebot
import config
import constants
import utils
import utils_2

bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=['start'])
def start_menu(message, post=None):
    message_text = 'Здравствуйте!\n' \
                    + 'Когда вы закажите подписку, вы получите весь список команд.\n' \
                   + 'Наберите /help - для отображения списка доступных команд.'
    bot.send_message(message.chat.id, message_text)

    @bot.message_handler(commands=['help'])
    def print_menu(message):
        message_text = 'Вот, что умеет этот бот:\n' \
                      + '/go - Запуск\n' \
                      + '/info - Подробнее\n' \
                      + '/shop - Магазин\n' \
                      + '/help - Помощь\n' \
                      + '/settings - Настройки\n' \
                      + '/services - Сервис\n' \
                       + '/markdown - markdown Сервис\n' \
                       + '/HTML - HTML Сервис\n' \
                       + '/read_rss - RSS'


    # Info
    @bot.message_handler(commands=['info'])
    def default_test(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Info')

    # Info
    @bot.message_handler(commands=['go'])
    def start_handler(message):
        bot.send_message(message.chat.id, 'Для начала, необходимо настроить форматирование, которое будет использоваться по умолчанию при создании постов.'
                     ' Отправьте /markdown или /HTML, чтобы получить подсказку.'
                     ' Чаще всего пользователи используют Markdown, потому он короче и проще.'
                     'Наш бот также поддерживает и нативное форматирование.')

    @bot.message_handler(commands=['markdown'])
    def start_handler(message):
        bot.send_message(message.chat.id, 'markdown настройки')

    @bot.message_handler(commands=['HTML'])
    def start_handler(message):
        bot.send_message(message.chat.id, 'HTML настройки')

    # handlers
    @bot.message_handler(commands=['shop'])
    def start_handler(message):
        bot.send_message(message.chat.id, 'Shop')

    # handlers
    @bot.message_handler(commands=['settings'])
    def start_handler(message):
        bot.send_message(message.chat.id, 'Настройки')

    # handlers
    @bot.message_handler(commands=['services'])
    def start_handler(message):
        bot.send_message(message.chat.id, 'Сервис')


    @bot.message_handler(commands=['read_rss'])
    def read_rss(message):
        post = utils.feed_parser()
        bot.send_message(message.chat.id, 'Новая информация на выбранных площадках:')
    for key in post.keys():
        bot.send_message(message.chat.id, key + '\n' + post[key])






    if __name__ == '__main__':
        bot.infinity_polling()
