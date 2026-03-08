import telebot

bot = telebot.TeleBot('8379602830:AAFYS3OLfvC5SPw2qEQesZWyE9fAwIZzGvU')

@bot.message_handler(commands=['start'])
def huy(message):
    bot.send_message(message.chat.id, f"Привет @{message.from_user.username}! Это я, Саня Комков. Чем я могу помочь?????")

@bot.message_handler(commands=['help'])
def huy(message):
    bot.send_message(message.chat.id, "Nema helpy", parse_mode = "html")

@bot.message_handler()
def main(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Уже здоровались")

bot.infinity_polling()