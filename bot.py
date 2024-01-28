import telebot
import info
from dotenv import dotenv_values
from user import User
import btn

config = dotenv_values(".env")
token = config['token']
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     'Привет,это бот-квест! В этом боте вы можете пройти квест. Я надеюсь, что вам понравится моя работа и вы прорекламируете меня друзьям!😁(Еще бот умеет отвечать на простые сообщения, типа - привет или пока)')
    bot.send_message(message.chat.id, "Это список команд, которые я умею выполнять:\n"
                                      "/start ; Приветствует пользователя и отправляет ему меню.\n"
                                      "/help ; Предоставляет пользователю инструкцию по использованию бота и отправляет ему меню.\n"
                                      "/play ; Начинает или продолжает прохождение квеста.\n"
                                      "/restart ; Начинает прохождение квеста заново.\n")
    bot.send_message(message.chat.id, info.project_to_str())


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'Инструкция пользования ботом-квестом : ...')
    bot.send_message(message.chat.id, "Это меню команд, которые я умею выполнять:\n"
                                      "/start ; Приветствует пользователя и отправляет ему меню.\n"
                                      "/help ; Предоставляет пользователю инструкцию по использованию бота и отправляет ему меню.\n"
                                      "/play ; Начинает или продолжает прохождение квеста.\n"
                                      "/restart ; Начинает прохождение квеста заново.\n")


def next_layer(user: User, chat_id: int):
    current_layer = info.get_current_layer(user)
    answer = user.get_path()
    if current_layer.is_last():

        bot.send_message(chat_id, "квест завершен.")
        bot.send_message(chat_id, "Если хотите начать игру заново, нажмите /restart")
        if info.is_winner(user):
            bot.send_message(chat_id, "winner")
            bot.send_message(chat_id, 'Вы выиграли и выбрались из подземелья! Поздравляем вас!')
            bot.send_photo(chat_id, open("./i/win.jpg", 'rb'))
        else:
            bot.send_message(chat_id, "lose")
            bot.send_message(chat_id, "К сожалению вы проиграли... Удачи в загробном мире. ")
            bot.send_photo(chat_id, open("./i/lose.jpg", 'rb'))
        return
    desc = current_layer.desc
    buttons = current_layer.get_sub_buttons()
    bot.send_photo(chat_id, current_layer.get_picture())
    bot.send_message(chat_id, desc, reply_markup=btn.create_menu(buttons))


@bot.message_handler(commands=['play'])
def play_command(message):
    try:
        user_id = message.from_user.id
        user = User(user_id)
        next_layer(user, message.chat.id)
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id, "shit happens...")


@bot.message_handler(commands=['restart'])
def play_command(message):
    try:
        user_id = message.from_user.id
        user = User(user_id)
        user.restart()
        bot.send_message(message.chat.id, "Нажмите /play чтобы начать квест заново.")
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id, "shit happens...")


@bot.message_handler(content_types=['text'])
def hello_saying(message):
    if "привет" in message.text.lower():
        bot.send_message(message.chat.id, "Привет!")
    elif "пока" in message.text.lower():
        bot.send_message(message.chat.id, "Пока!")
    else:
        bot.send_message(message.chat.id, "Я подумаю об этом ... :)")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        user_id = call.from_user.id
        user = User(user_id)
        user.handler(call.data)
        next_layer(user, call.message.chat.id)
    except Exception as ex:
        print(ex)
        bot.send_message(call.message.chat.id, "shit happens...")


bot.polling()
