import telebot
import sqlite3

bot = telebot.TeleBot('6672277852:AAHyrFEhAydUmM5dZt5nHpduxZ_c1Yzqn0I')



@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('video.db')
    sql = connect.cursor()
    sql.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER);')
    connect.commit()


    user_id = message.chat.id
    sql.execute(f'SELECT id FROM users WHERE id = {user_id}')
    d  = sql.fetchone()
    if d is None:

        data = [message.chat.id]
        sql.execute('INSERT INTO users VALUES(?);', data)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'This user is already exist')




@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sqlite3.connect('video.db')
    sql = connect.cursor()

    user_id = message.chat.id

    sql.execute(f'DELETE FROM users WHERE id = {user_id}')
    connect.commit()
























