import telebot


def send_notify(message):
    bot = telebot.TeleBot("")  # Токен бота
    bot.send_message(1111111111, message)  # чат айди

