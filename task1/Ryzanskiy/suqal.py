import psycopg2
import first


connection = psycopg2.connect(host='localhost', dbname='youtube',
                               user='postgres', password='3107asdzxc')
cursor=connection.cursor()
data = first.pars()
n=0
while n<10:
    rang=data[n][0]
    name=data[n][1]
    channel=data[n][2]
    views = data[n][3]
    insert_query= f"""INSERT INTO public.youtube(
	                    rang, name, channel, views)
	                    VALUES ({rang}, '{name}', '{channel}', '{views}');"""
    cursor.execute(insert_query)
    connection.commit()
    n+=1