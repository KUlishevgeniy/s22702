import psycopg2
connection = psycopg2.connect(host = "localhost", dbname = "Data", user = "postgres", password = "9275")
cursor = connection.cursor()

insert_query = """INSERT INTO public.user_table(
    firstname, lastname, age)
	VALUES ('Денчик', 'Кудинов', 18),
		   ('Димон', 'хуй', 43),
		   ('Кирилл', 'пизда', 23);"""

cursor.execute(insert_query)
cursor.execute("SELECT * FROM user_table")
print(cursor.fetchall())
#connection.commit()