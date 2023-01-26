import os, sys

import telebot

bot = telebot.TeleBot("5569374220:AAEoyEM5zkZBNa7QjB-rIiP-Hfs5lideIWo")


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    # bot.reply_to(message,"You send:" + message.text + "   " + message.from_user.username + "   " + str(message.from_user.id))
    bot.send_message(message.chat.id, "Done")
    file = open("test1.txt")
    text = file.read()
    file.close()
    os.system('start test1.txt')
    bot.send_message(message.chat.id, str(text))



# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#	bot.reply_to(message, message.text)

@bot.message_handler(commands=['add'])
def greatings(message):
    bot.send_message(message.chat.id, "Done")
    os.system("project/test1.txt")


bot.infinity_polling(interval=0, timeout=20)
