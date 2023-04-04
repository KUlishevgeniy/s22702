import psycopg2
connection = psycopg2.connect(host='localhost', dbname='DB1', user='postgres', password='q1w2e3r4')

cursor = connection.cursor()

inser_qwery="""INSERT INTO public.table1(
firstname,lastname, age)
VALUES ('Иван', 'Иванов', 3),
('Дмитрий', 'Ивановыва', '33');""";
cursor.execute(inser_qwery)
#connection.commit()
cursor.execute('select * from table1')
print ("Результат", cursor.fetchall())