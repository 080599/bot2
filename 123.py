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


@bot.message_handler(content_types=['text'])
def main_menu(message):
    user_id = message.from_user.id
    text = message.text
    if text == 'Menu':
        all_products = db.get_pr_id_name()
        bot.send_message(user_id, 'Chose the product', reply_markup=bt.products_in(all_products))
    elif text == 'Cart':
        bot.send_message(user_id, 'Your cart')
    elif text == 'Comment':
        bot.send_message(user_id, 'Send your comment')


bot.infinity_polling()


bot.infinity_polling()