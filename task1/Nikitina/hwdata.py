import psycopg2
import task2

i = 0
connection = psycopg2.connect(host='localhost', dbname='hwdata',
                              user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()
data = task2.main()
for book in data:
    place, name, author = book.split("|")
    insert_query = f"""INSERT INTO public.books(
	                    id, nameru, author)
	                    VALUES ({place}, '{name}', '{author}');"""
    cursor.execute(insert_query)
    connection.commit()
