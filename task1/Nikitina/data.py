import psycopg2
connection = psycopg2.connect(host='localhost', dbname='data',
                              user='postgres', password='Q1w2e3r4')

cursor = connection.cursor()
inser_qwery = """INSERT INTO public.user_table(
	firstname, lastname, age)
	VALUES ('Иван', 'Иванов', 33),
	('Дмитрий', 'Иванов', 3);"""

#cursor.execute(inser_qwery)
#connection.commit()

cursor.execute("select  * from user_table")
print("Результат", cursor.fetchall())
