from telebot import types
def knopka():
    kb=types.ReplyKeyboardMarkup()
    knopka_pervod=types.KeyboardButton(text="Translate")
    kb.add(knopka_pervod)
    return kb
