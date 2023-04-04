import psycopg2
import  telebot
import random
from telebot import types

connection = psycopg2.connect(host='localhost', dbname='db', user='postgres', password='q1w2e3r4')
cursor=connection.cursor()

sqlite_select_query = """SELECT * from travel"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
answer = random.choice(records)
for i in answer:
    i=str(i)
    print(i)
print(answer[0])