import telebot
import buttons
bot=telebot.TeleBot(token="7350131505:AAGYspou2bGTrlNKSIihkv7t8PkbtByrcXQ")
@bot.message_handler(commands=['start'])
def start(message):
    user_id=message.from_user.id
    bot.send_message(chat_id=user_id,
                     text="Translator bot",
                     reply_markup=buttons.knopka())
@bot.message_handler(content_types=['text'])
def translate(message):
    user_id=message.from_user.id
    user_text=message.text
    if user_text.lower=="trqanslate":
        bot.send_message(user_id, text='Send word to translate' )
    else:
        bot.send_message(user_id, text='wrong command' )

bot.infinity_polling()