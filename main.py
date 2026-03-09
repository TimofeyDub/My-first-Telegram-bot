import telebot
import random
import os
from telebot import types
from api import pogoda

bot = telebot.TeleBot('8379602830:AAFYS3OLfvC5SPw2qEQesZWyE9fAwIZzGvU')

#обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Жопа')
    btn2 = types.KeyboardButton('Helpaa')
    btn3 = types.KeyboardButton('Мемчик')
    btn4 = types.KeyboardButton('Погода во Всеше')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4)
    bot.send_message(message.chat.id, f"Привет @{message.from_user.username}! Это я, СаняGPT. Чем я могу помочь?????", reply_markup=markup)
    print(message.chat.id, message.from_user.username, "start")

#медиа
@bot.message_handler(content_types=['photo'])
def getPhoto(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Тебе туда', url='https://rt.pornhub.org/')
    btn2 = types.InlineKeyboardButton('Удалить нахуй', callback_data='delete')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'че за хуйню ты мне отправил?', reply_markup=markup)
    print(message.chat.id, message.from_user.username, "photo")

#обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def on_click(message):
    if message.text == 'Helpaa':
        bot.send_message(message.chat.id, 'Nema helpi')
        print(message.chat.id, "helpaa")
    elif message.text == 'Жопа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton('Ты ахуел?')
        markup.row(btn5)
        bot.send_message(message.chat.id, 'Сам(а) ты жопа', reply_markup=markup)
    elif message.text == 'Мемчик':
            photo_count = len(os.listdir('./photo'))
            memchik = random.randint(1, photo_count)
            file = open(f'./photo/{memchik}.png', 'rb')
            bot.send_photo(message.chat.id, file, timeout=60)
            file.close()
            print(message.chat.id, message.from_user.username, "meme")
    elif message.text.lower() == 'привет':
         bot.send_message(message.chat.id, 'Уже здоровались')
    elif message.text.lower() == 'пока':
         bot.send_message(message.chat.id, 'Вот и иди нахуй')
    elif message.text == 'Погода во Всеше':
         a = pogoda()
         bot.send_message(message.chat.id, a)
    elif message.text == 'Ты ахуел?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Жопа')
        btn2 = types.KeyboardButton('Helpaa')
        btn3 = types.KeyboardButton('Мемчик')
        btn4 = types.KeyboardButton('Погода во Всеше')
        markup.row(btn1, btn2, btn3)
        markup.row(btn4)
        bot.send_message(message.chat.id, 'Ладно, я ахуел', reply_markup=markup)

#callback
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)


#работа
bot.polling(none_stop=True)
