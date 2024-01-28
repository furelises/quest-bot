from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message


class Btn:
    def __init__(self, title: str, layer_id: str):
        self.layer_id = layer_id
        self.title = title


def create_menu(list: [Btn]) -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    for i in list:
        btn = types.InlineKeyboardButton(text=i.title, callback_data=i.layer_id)
        markup.add(btn)
    return markup


