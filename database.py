import sqlite3
import colorama
import telebot
from sqlite3 import Error

bot = telebot.TeleBot("5569374220:AAEoyEM5zkZBNa7QjB-rIiP-Hfs5lideIWo")

def sql_conn():
 
    try:
 
        con = sqlite3.connect('customers.db', check_same_thread=False)
 
        return con
 
    except Error:
 
        sql_table(con)
 
con = sql_conn()
cursorObj = con.cursor()

def sql_table():
    cursorObj.execute("CREATE TABLE registration(id integer PRIMARY KEY, name text)")
    con.commit()
 

def sql_add(message):
    entity = (int(message.from_user.id), str(message.from_user.first_name))
    print(colorama.Fore.GREEN + str(message.from_user.id) + ' ' + message.from_user.first_name)
    print(colorama.Style.RESET_ALL)
    cursorObj.execute("INSERT INTO registration(id, name) VALUES(?, ?)", entity)
    con.commit()
    
def sql_fetch(message):
    cursorObj.execute('SELECT * FROM registration')
    rows = cursorObj.fetchall()
    for row in rows:
        bot.send_message(message.chat.id, row)




