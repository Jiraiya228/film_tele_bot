import telebot
from myparser import random_film
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(content_types=['text'])
def start_message(message):
    answer1 = 'Добро пожаловать! Я бот, который будет помогать вам с поиском интересных фильмов'

    keyboard = types.InlineKeyboardMarkup()
    key_rfb = types.InlineKeyboardButton(text='Рандомный фильм', callback_data='random_film')
    keyboard.add(key_rfb)

    bot.send_message(message.chat.id, answer1, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    keyboard = types.InlineKeyboardMarkup()
    key_rfb = types.InlineKeyboardButton(text='Да', callback_data='info')
    keyboard.add(key_rfb)
    key_rfb = types.InlineKeyboardButton(text='Нет', callback_data='random_film')
    keyboard.add(key_rfb)

    if call.data == 'random_film':
        bot.send_message(call.from_user.id, random_film())
        bot.send_message(call.from_user.id, 'Хотите посмотреть этот фильм?', reply_markup=keyboard)
    if call.data == 'info':
        bot.send_message(call.from_user.id, 'Типа какая-то инфа')


bot.polling(none_stop=True, interval=0)
