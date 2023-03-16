import telebot

bot = telebot.TeleBot("5569374220:AAEoyEM5zkZBNa7QjB-rIiP-Hfs5lideIWo")

def hello(message):
    bot.send_message(message.chat.id, 'Hello!!!')

def remote(message, text):
    bot.send_message(message.chat.id, 'Fine')
    with open("test1.txt", 'r+') as f:
        f.truncle()
    file = open("test1.txt", 'w')
    file.write('default')
    file.close()
 
         
    
