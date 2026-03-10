import telebot
import random
import os
from datetime import datetime
from telebot import types
from api import pogoda, pogoda2
from keyboardstg import create_keyboards

bot = telebot.TeleBot('8379602830:AAFYS3OLfvC5SPw2qEQesZWyE9fAwIZzGvU')
#клавиатуры
KEYBOARDS = {}
create_keyboards(KEYBOARDS)

#логгер сообщений
def log_message(message):
    user = message.from_user
    chat_type = message.chat.type
    print(f"\n{'='*50}")
    print(f"👤 Пользователь: @{user.username} | ID: {user.id} | Имя: {user.first_name} {user.last_name or ''}")
    print(f"💬 Чат: {chat_type} | ID чата: {message.chat.id}")
    print(f"📝 Сообщение: {message.text}")
    print(f"⏰ Время: {datetime.fromtimestamp(message.date)}")
    print(f"{'='*50}\n")

#обработчик команд
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет @{message.from_user.username}! Это я, СаняGPT. Чем я могу помочь?????", reply_markup=KEYBOARDS['main'])
    print(message.chat.id, message.from_user.username, "start")

#send message
@bot.message_handler(commands=['send'])
def send_to_user(message):
    try:
        #проверка формата
        parts = message.text.split()
        
        if len(parts) < 2:
            bot.reply_to(message, "Не хватает аргументов. Используй: /send ID")
            return
        
        #получение id
        try:
            user_id = int(parts[1])
        except ValueError:
            bot.reply_to(message, f"ID должен быть числом, а получено: {parts[1]}")
            return
        
        #текст сообщения
        if len(parts) >= 3:
            text = ' '.join(parts[2:])
        else:
            text = "Пустое сообщение"
        
        #отправка
        try:
            bot.send_message(user_id, f"Сообщение:\n{text}")
            bot.reply_to(message, f"Отправлено пользователю {user_id}")
        except Exception as send_error:
            bot.reply_to(message, f"Не могу отправить: {send_error}")
            
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")
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

    log_message(message)

    #хелпа и жопа
    if message.text == 'Helpaa':
        bot.send_message(message.chat.id, f'Ну бля, я СаняДжПиТи, хз чем helpaaнуть. Можешь мне отправить фотку и я её оценю. Можешь написать привет или пока. Я разрабатываюсь одним человеком, поэтому мой функционал пока не богат. Жди обновлений, ещё можешь накинуть идей моему создателю: @tmn7t')
        print(message.chat.id, message.from_user.username, "helpaa")
    elif message.text == 'Жопа':
        bot.send_message(message.chat.id, 'Сам(а) ты жопа', reply_markup=KEYBOARDS['ass_confirmation'])

    #мемчики
    elif message.text == 'Мемчик':
            photo_count = len(os.listdir('./photo'))
            memchik = random.randint(1, photo_count)
            file = open(f'./photo/{memchik}.png', 'rb')
            bot.send_photo(message.chat.id, file, timeout=60)

            if memchik == 8:
                bot.send_message(message.chat.id, 'Это правда')

            file.close()
            print(message.chat.id, message.from_user.username, "meme")

    #привет пока
    elif message.text.lower() == 'привет':
         bot.send_message(message.chat.id, 'Уже здоровались')
    elif message.text.lower() == 'пока':
         bot.send_message(message.chat.id, 'Вот и иди нахуй')

    #погода
    elif message.text == 'Погода':
        bot.send_message(message.chat.id, 'В каком городе нахуй?', reply_markup=KEYBOARDS['weather'])
    #погоды
    elif message.text == 'Всеша':
        a = pogoda() 
        bot.send_message(message.chat.id, a, reply_markup=KEYBOARDS['main'])
    elif message.text == 'Валенсия':
        a = pogoda2() 
        bot.send_message(message.chat.id, a, reply_markup=KEYBOARDS['main'])
    #жопа
    elif message.text == 'Ты ахуел?':
        bot.send_message(message.chat.id, 'Ладно, я ахуел', reply_markup=KEYBOARDS['main'])

#callback
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)


#работа
bot.polling(none_stop=True)