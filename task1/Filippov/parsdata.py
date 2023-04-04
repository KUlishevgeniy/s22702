import psycopg2
import parsmusic1
connection = psycopg2.connect(host='localhost', dbname='music',
                               user='postgres', password='Q1w2e3r4')
cursor=connection.cursor()
data = parsmusic1.pars()
a=0
n=0
m=0
while n<=49:
    top=data[a]
    artist=data[a+1]
    song=data[a+2]
    insert_query= f"""INSERT INTO public.topmusic(
                     id, artist, song)
                     VALUES ({top}, '{artist}', '{song}');"""
    cursor.execute(insert_query)
    connection.commit()
    n+=1
    a+=3