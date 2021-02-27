import telebot
from myparser import random_film
from telebot import types
from requests import get
import random

bot = telebot.TeleBot('')
stickers = ['CAACAgIAAxkBAALbtWAxP2IEw4BsDmbbwoa39chwgS-pAAK8AAP0Pkchqrf9txcCRgseBA','CAACAgIAAxkBAALlK2A6LrigzASZVpJU5WLdE29--KLkAALAAAPTchcpYXSNi3gYFvgeBA','CAACAgIAAxkBAALlMWA6LuIIcFviUl9_KwG8PisZDSKKAAJcAAMOevsK5KE8IBxlZs8eBA']

@bot.message_handler(content_types=['text'])
def start_message(message):
    answer1 = 'Добро пожаловать! Я бот, который будет помогать вам с поиском интересных фильмов'

    keyboard = types.InlineKeyboardMarkup()
    key_rfb = types.InlineKeyboardButton(text='Рандомный фильм', callback_data='random_film')
    keyboard.add(key_rfb)

    bot.send_message(message.chat.id, answer1, reply_markup=keyboard)


@bot.message_handler(content_types=['sticker'])
def send_img(message):
    i = random.randint(0, len(stickers)-1)
    bot.send_sticker(message.chat.id, stickers[i])

    #bot.delete_message(message.chat.id, message.message_id)
    #bot.send_message(message.chat.id, 'Не шли мне стикеры!!!')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    film_and_poster = random_film()
    keyboard = types.InlineKeyboardMarkup()
    key_rfb = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_rfb)
    key_rfb = types.InlineKeyboardButton(text='Нет', callback_data='random_film')
    keyboard.add(key_rfb)

    if call.data == 'random_film':
        bot.send_photo(call.from_user.id, get(film_and_poster[1]).content)
        bot.send_message(call.from_user.id, '*** ' + film_and_poster[0] + ' ***' + '\n\n' + film_and_poster[2], parse_mode="Markdown")
        bot.send_message(call.from_user.id, 'Хотите посмотреть этот фильм?', reply_markup=keyboard)
    if call.data == 'yes':
        bot.send_message(call.from_user.id, '*** Отлично! Приятного просмотра! ***', parse_mode="Markdown")


bot.polling(none_stop=True, interval=0)
