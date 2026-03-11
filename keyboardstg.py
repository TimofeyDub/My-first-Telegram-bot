from telebot import types

#клавиатуры
def create_keyboards(KEYBOARDS):
    #главная клавиатура
    markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Жопа')
    btn2 = types.KeyboardButton('Helpaa')
    btn3 = types.KeyboardButton('Мемчик')
    btn4 = types.KeyboardButton('Погода')
    markup_main.row(btn1, btn2, btn3)
    markup_main.row(btn4)
    KEYBOARDS['main'] = markup_main
    
    #выбор города
    markup_weather = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn6 = types.KeyboardButton('Всеша')
    btn7 = types.KeyboardButton('Валенсия')
    btn8 = types.KeyboardButton('Ташкент')
    markup_weather.row(btn6, btn7)
    markup_weather.row(btn8)
    KEYBOARDS['weather'] = markup_weather
    
    #ты ахуел?
    markup_ass = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn5 = types.KeyboardButton('Ты ахуел?')
    markup_ass.row(btn5)
    KEYBOARDS['ass_confirmation'] = markup_ass
