import psycopg2
import parser


connection = psycopg2.connect(host='localhost', dbname='auto',
                               user='postgres', password='3107asdzxc')
cursor=connection.cursor()
data = parser.pars()
a=0
n=0
m=0
while n<=49:
    place=data[a]
    brand=data[a+1]
    price=data[a+2]
    insert_query= f"""INSERT INTO public.auto(
	                    id, brand, price)
	                    VALUES ({place}, '{brand}', '{price}');"""
    cursor.execute(insert_query)
    connection.commit()
    n+=1
    a+=3
