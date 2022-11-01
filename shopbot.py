import telebot
from telebot import types
from config import TOKEN1

bot = telebot.TeleBot(TOKEN1)

@bot.message_handler(commands=['start'])
def start(message):
    # bot.send_message(message.chat.id,f"Whats up? {message.from_user.first_name}")
    bot.send_message(message.chat.id, 'Напиши или нажми: /help для продолжения!')



# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Can't complain" or message.text == "can't complain":
#         bot.send_message(message.chat.id,"Ok")
#     elif message.text == "Everything is bad" or message.text == "everything is bad":
#         bot.send_message(message.chat.id, "It's fine,don't give up dude")
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFesJi7hsHz8vHWfgn8JejDL2P9vYtvQACdg0AApXHgEvZ0vMO3xyeRCkE' )
#     elif message.text == 'sticker':
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGM79jWM5-j-DIl-UcdgJ4dNrWGGAyDwACUwsAAlY_eEqt4UJ1MU9jkyoE')
#     else:
#         bot.send_message(message.chat.id, "На большее я не способен :(")


# # ( Создние кнопок )
# @bot.message_handler(commands=['website'])
# def social_media(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Instagram", url='https://www.instagram.com/ramil_btw/'))


@bot.message_handler(commands=['help'])
def social_media(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Соц сети')
    novembers_photo = types.KeyboardButton('Аватарки для ноября')
    markup.add(website)
    markup.add(novembers_photo)
    bot.send_message(message.chat.id,"Выберите что вам нужно", reply_markup=markup)


@bot.message_handler()
def photo(message):
    if message.text == 'Аватарки для ноября':
        photo = open('jedi.jpg', 'rb')
        photo1 = open('sith.jpg', 'rb')
    # if message.text == 'Аватарки для ноября':
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1)
    # else:
    #     bot.send_message(message.chat.id, 'Перезапустите бота при помощи команды /start')


@bot.message_handler()
def get_user_text(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Instagram", url='https://www.instagram.com/ramil_btw/'))
    markup.add(types.InlineKeyboardButton("VKontakte", url='https://vk.com/sas_rambl4'))
    markup.add(types.InlineKeyboardButton("Twitch", url='https://www.twitch.tv/zxc_rambl4'))
    markup.add(types.InlineKeyboardButton("FACEIT", url='https://www.faceit.com/ru/players/Rambl4'))
    markup.add(types.InlineKeyboardButton("Telegram Group", url='https://t.me/+3p6p-Itdg-8wNDBi'))
    if message.text == "Соц сети":
        bot.send_message(message.chat.id,"Подпишись на мои соц сети :)", reply_markup=markup)
    # else:
    #     bot.send_message(message.chat.id, 'Перезапустите бота при помощи команды /start')



bot.polling(non_stop=True)