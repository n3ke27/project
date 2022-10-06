import telebot

bot = telebot.TeleBot("5569374220:AAEoyEM5zkZBNa7QjB-rIiP-Hfs5lideIWo")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.reply_to( message, "You send:" + message.text + "   " + message.from_user.username + "   " + str(message.from_user.id))  
    

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)

@bot.message_handler(commands=['add'])
def greatings(message):
    pass


bot.infinity_polling(interval=0, timeout=20)