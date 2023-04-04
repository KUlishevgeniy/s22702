import psycopg2

connection = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "123123qwe")
cursor = connection.cursor()


def insert(data):
    for i in range(len(data)):
        place, runame, enname, mark = data[i].split('|')
        insert_query = f"""INSERT INTO public.data
                           VALUES ('{place}', '{runame}', '{enname.replace("'", "")}', '{mark}');"""
        cursor.execute(insert_query)
    connection.commit()


def get(place):
    cursor.execute(f"""SELECT * FROM public.data
                      WHERE place = '{place} '""")
    answer = cursor.fetchall()
    print(answer)
    return f'Место - {answer[0][0].strip()}\nНазвание - {answer[0][1].strip()}\nНазвание на английском, год, длина- {answer[0][2].strip()}\nБалл - {answer[0][3].strip()}'