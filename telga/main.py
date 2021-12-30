import telebot
from telebot import types
import psycopg2
from datetime import date

bot = telebot.TeleBot('2109818208:AAE0r8zemWWNCP0lbs86rc2MjSfluqrCa1E')

conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="1337",
                        host="localhost",
                        port="5432")

def get_week_num():
    first_day = date(2021, 8, 30)
    today = date.today()
    delta = (today - first_day).days
    week_number = (delta // 7) + 1
    return week_number

def execute_read_query(connection, query):
    cursor = conn.cursor()
    result = None
    cursor.execute(query)
    result = cursor.fetchall()
    return result


@bot.message_handler(commands=['start', 'back'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/teachers')
    btn3 = types.KeyboardButton('/timetable')
    btn4 = types.KeyboardButton('/subjects')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, 'Для того, чтобы узнать все команды пропишите команду /help '
                                      'или нажмите на кнопку Help', reply_markup=markup)


@bot.message_handler(commands=['help'])
def helper(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/teachers')
    btn2 = types.KeyboardButton('/timetable')
    btn3 = types.KeyboardButton('/subjects')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_message(message.chat.id, 'имена преподавателей - '
                                      '/teachers или нажмите соответствующую кнопку.\n'
                                      'расписание - '
                                      '/timetable или нажмите соответствующую кнопку.\n'
                                      'список предметов - '
                                      '/subjects или нажмите соответствующую кнопку.', reply_markup=markup)

@bot.message_handler(commands=['subjects'])
def sub(message):
    text = "SELECT * FROM list.subject"
    subjects = execute_read_query(conn, text)
    for row in subjects:
        otv = str(row[0]) + ' | ' + str(row[1])
        bot.send_message(message.chat.id, otv)



@bot.message_handler(commands=['teachers'])
def teach(message):
    text = "SELECT * FROM list.teacher"
    subjects = execute_read_query(conn, text)
    for row in subjects:
        otv = str(row[0]) + ' | ' + str(row[1]) + ' | ' + str(row[2])
        bot.send_message(message.chat.id, otv)


@bot.message_handler(commands=['timetable'])
def timetable(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/monday')
    btn2 = types.KeyboardButton('/tuesday')
    btn3 = types.KeyboardButton('/wednesday')
    btn4 = types.KeyboardButton('/thursday')
    btn5 = types.KeyboardButton('/friday')
    btn6 = types.KeyboardButton('/saturday')
    btn7 = types.KeyboardButton('/chet')
    btn8 = types.KeyboardButton('/nechet')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.add(btn6)
    markup.add(btn7)
    markup.add(btn8)
    bot.send_message(message.chat.id, 'Выберите день недели для которого хотите узнать расписание', reply_markup=markup)


@bot.message_handler(commands=['monday'])
def mon(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    week_num = '2' if get_week_num()%2 == 1 else ''
    text = f"SELECT subject, room_numb, start_time FROM list.timetable{week_num} WHERE day = 'monday'"
    subjects = execute_read_query(conn, text)
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv, reply_markup=markup)


@bot.message_handler(commands=['tuesday'])
def tue(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    week_num = '2' if get_week_num() % 2 == 1 else ''
    text = f"SELECT subject, room_numb, start_time FROM list.timetable{week_num} WHERE day = 'tuesday'"
    subjects = execute_read_query(conn, text)
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv, reply_markup=markup)


@bot.message_handler(commands=['wednesday'])
def wed(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    week_num = '2' if get_week_num() % 2 == 1 else ''
    text = f"SELECT subject, room_numb, start_time FROM list.timetable{week_num} WHERE day = 'wednesday'"
    subjects = execute_read_query(conn, text)
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv, reply_markup=markup)


@bot.message_handler(commands=['thursday'])
def thu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    week_num = '2' if get_week_num() % 2 == 1 else ''
    markup.add(btn1)
    text = f"SELECT subject, room_numb, start_time FROM list.timetable{week_num} WHERE day = 'thursday'"
    subjects = execute_read_query(conn, text)
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv, reply_markup=markup)


@bot.message_handler(commands=['friday'])
def fri(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    week_num = '2' if get_week_num() % 2 == 1 else ''
    text = f"SELECT subject, room_numb, start_time FROM list.timetable{week_num} WHERE day = 'friday'"
    subjects = execute_read_query(conn, text)
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv, reply_markup=markup)


@bot.message_handler(commands=['saturday'])
def fri(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    week_num = '2' if get_week_num() % 2 == 1 else ''
    text = f"SELECT subject, room_numb, start_time FROM list.timetable{week_num} WHERE day = 'saturday'"
    subjects = execute_read_query(conn, text)
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv, reply_markup=markup)


@bot.message_handler(commands=['chet'])
def chet(message):
    text = "SELECT subject, room_numb, start_time FROM list.timetable where day = 'monday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Понедельник~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable where day = 'tuesday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Вторник~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable where day = 'wednesday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Среда~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable where day = 'thursday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Четверг~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable where day = 'friday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Пятница~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable where day = 'saturday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Суббота~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)


    ########################

@bot.message_handler(commands=['nechet'])
def nechet(message):
    text = "SELECT subject, room_numb, start_time FROM list.timetable2 where day = 'monday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Понедельник~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable2 where day = 'tuesday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Вторник~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable2 where day = 'wednsday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Среда~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable2 where day = 'thursday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Четверг~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable2 where day = 'friday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Пятница~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

    text = "SELECT subject, room_numb, start_time FROM list.timetable2 where day = 'saturday'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, '~~~~~~~~~~~~Суббота~~~~~~~~~~~~')
    for row in subjects:
        otv = ''
        otv = row[0] + ' | ' + row[1] + ' | ' + row[2]
        bot.send_message(message.chat.id, otv)

bot.infinity_polling()