import os, sys
import source
import parser_1
import database
import telebot


bot = telebot.TeleBot("5569374220:AAEoyEM5zkZBNa7QjB-rIiP-Hfs5lideIWo")

"""@bot.message_handler(commands=['add'])
def skip(message):
    bot.send_message(message.chat.id, "Ok" )
    file = open("test1.txt", 'w')
    text = input("Напиши что-то:")
    file.write(text)
    file.close()
"""
@bot.message_handler(commands=['start'])
def greeting(message):
    bot.send_message(message.chat.id, "Hello!")
    database.sql_add(message)


@bot.message_handler(commands=['news'])
def get_news(message):
    bot.send_message(message.chat.id, parser_1.get_news())

@bot.message_handler(commands=['data'])
def data(message):
    database.sql_fetch(message)

@bot.message_handler(content_types=['text'])
def test(message):
    file = open("test1.txt")
    text = str(file.read())
    file.close()
    bot.send_message(message.chat.id, text)




    
"""@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
        
os.system('start test1.txt')
    bot.send_message(message.chat.id, str(text))"""

# bot.reply_to(message,"You send:" + message.text + "   " + message.from_user.username + "   " + str(message.from_user.id))
"""bot.send_message(message.chat.id, "Done")"""

"""@bot.message_handler(commands=['add'])
def skip(message):
    bot.send_message(message.chat.id, "Ok" )
    file = open("test1.txt", 'w')
    text = input("Напиши что-то:")
    file.write(text)
    file.close()
"""

bot.infinity_polling(interval=0, timeout=20)
