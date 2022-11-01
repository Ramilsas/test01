# импортируем нужные библеотеки
import telebot
from telebot import types
import random

# сохранили ключ доступа к нашему чату с ботом
token = '5446762495:AAGrHAr-DcxrNffiXxsAHOpWN3qdN67hNYg'  # (""" @rambl4_bot """)
# создали программу для управления ботом
bot = telebot.TeleBot(token)

# создаем клавиатуру
keyboard = types.ReplyKeyboardMarkup()
# создаем кнопки
button1 = types.KeyboardButton('Играть')
button2 = types.KeyboardButton('Нет')
# добавляем кнопки в клавиатуру
keyboard.add(button1, button2)

# функция отвечающая на комманды ('/start', '/hello', '/hi')
@bot.message_handler(commands=['start', 'hello', 'hi'])
def start_massage(message):
  # отправляем стикер в чат
  bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFesJi7hsHz8vHWfgn8JejDL2P9vYtvQACdg0AApXHgEvZ0vMO3xyeRCkE')
  # отправляем сообщение в чат и с помощью reply_markup добавляем клавиатуру
  msg = bot.send_message(message.chat.id, f'Привет {message.chat.first_name}, начнем игру?', reply_markup=keyboard)
  # дожидаемся, когда пользователь напишет что-то и запускаем функцию check_answer
  bot.register_next_step_handler(msg, check_answer)

# функция, которая проверяет, какую кнопку нажал пользователь
def check_answer(message):
  # если пользователь нажал на кнопку Играть
  if message.text == 'Играть':
    # отправляем правила игры в чат
    bot.send_message(message.chat.id, 'Ок, тогда вот правила, нужно угадать число от 1 до 10 за 3 попытки')
    # генерируем случайное число в диапазоне от 1 до 10
    random_number = random.choice(range(1, 11))
    # выводим это число в терминал (в телеграм это не отправится)
    print(random_number)
    # запускам функцию game
    game(message, 3, random_number)

  # если пользователь нажал кнопку Нет
  else:
    bot.send_message(message.chat.id, 'Окей, до встречи')

# функция которая принимает число от пользователя
def game(message, attempts, random_number):
  msg = bot.send_message(message.chat.id, 'Выберите число')
  # дожидаемся числа от пользователя и запускаем функцию check_number, передав ей количество попыток (- 1) и случайное число
  bot.register_next_step_handler(msg, check_number, attempts - 1, random_number)

# функция проверяющая правильность введенного числа и кол-во попыток
def check_number(message, attempts, random_number):
  # если введенное число равно загаданному
  if message.text == str(random_number):
    # отправляем сообщение и стикер в чат
    bot.send_message(message.chat.id, 'Вы победили')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI9JGKka3Av2d8cRR-xvrtehZ1_IJc0AAJKAAPANk8TL8ASxcW9exEkBA')
  
  # если число не угадано и закончились попытки
  elif attempts == 0:
    bot.send_message(message.chat.id, f'Извините, у вас закончились попытки, число было {random_number}')
  
  # если число не угадано и попытки еще есть
  else:
    bot.send_message(message.chat.id, f'Попробуйте еще раз, у вас осталось {attempts} попыток')
    # снова запускаем функцию game
    game(message, attempts, random_number)

# запускаем бота
bot.polling()