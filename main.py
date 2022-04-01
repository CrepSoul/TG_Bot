import telebot
import requests
from telebot import types

token = "5256435350:AAH_rE7i0n655zdX-Z5qB_8NPavLSBpXaY0"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Узнать курс", "/help")
    bot.send_message(message.chat.id, 'Привет! Этот бот подскажет тебе текущие курсы валют', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Вот что я могу:\n/help - помощь по командам\n'
                                      '/info - покажу сайт с которого я получаю информацию')
    bot.send_message(message.chat.id, 'Ты так же можешь просто написать в чат USD или EUR и я сразу покажу '
                                      'тебе курс валюты')

@bot.message_handler(commands=['info'])
def info_message(message):
    bot.send_message(message.chat.id, 'Информацию о курсе валют я получаю с сайта: https://cbr.ru/currency_base/daily/\n'
                                      'Это официальный сайт ЦБ РФ')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "узнать курс":
        keyboard2 = types.ReplyKeyboardMarkup()
        keyboard2.row("USD", "EUR")
        bot.send_message(message.chat.id, 'Выбери нужную валюту', reply_markup=keyboard2)

    if message.text.lower() == "usd":
        bot.send_message(message.chat.id, 'Курс на сегодня: %.2f руб.\nДля возвращения в главное меню введите /start' % get_curr('USD'))

    if message.text.lower() == "eur":
        bot.send_message(message.chat.id, 'Курс на сегодня: %.2f руб.\nДля возвращения в главное меню введите /start' % get_curr('EUR'))

def get_curr(Valuta):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    curr = data['Valute'][Valuta]['Value']
    return curr


bot.polling(none_stop=True, interval=0)