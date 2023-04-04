import psycopg2

connection = psycopg2.connect(host="localhost", dbname="Data", user="postgres", password="9275")
cursor = connection.cursor()


def insert_films(data):
    for i in range(len(data)):
        place, runame, enname, releaseyear, leng, mark = data[i].split('|')
        insert_query = f"""INSERT INTO "FILMS"
                           VALUES ('{place}', '{runame}', '{enname.replace("'", "")}', '{releaseyear}', '{leng}', '{mark}');"""
        cursor.execute(insert_query)
    connection.commit()


def get_films(place):
    cursor.execute(f"""SELECT * FROM "FILMS"
                       WHERE place = '{place}'""")
    answer = cursor.fetchall()
    return f'✅ МЕСТО - {answer[0][0].strip()}\n\n📄 НАЗВАНИЕ - {answer[0][1].strip()}\n\n📃 АНГЛИЙСКОЕ НАЗВАНИЕ - {answer[0][2].strip()}\n\n📆 ГОД ВЫПУСКА - {answer[0][3].strip()}\n\n⌛ ВРЕМЯ - {answer[0][4].strip()}\n\n⭐ ОЦЕНКА - {answer[0][5].strip()}'


def insert_games(data):
    for i in range(len(data)):
        place, title, release_date, mark, description, platforms, genres, publisher, developer = data[i].split('|')
        insert_query = f"""INSERT INTO "GAMES"
                                   VALUES ('{place}', '{title.replace("'", "")}', '{release_date}', '{mark}', '{description.replace("'", "")}', '{platforms}', '{genres}', '{publisher}', '{developer}');"""
        cursor.execute(insert_query)
    connection.commit()


def get_games(place):
    cursor.execute(f"""SELECT * FROM "GAMES"
                           WHERE place = '{place}'""")
    answer = cursor.fetchall()
    return f'✅ МЕСТО - {answer[0][0].strip()}\n\n📄 НАЗВАНИЕ - {answer[0][1].strip()}\n\n📆 ДАТА ВЫПУСКА - {answer[0][2].strip()}\n\n⭐ ОЦЕНКА - {answer[0][3].strip()}\n\n🎮 ПЛАТФОРМЫ - {answer[0][5].strip()}\n\n🎲 ЖАНРЫ - {answer[0][6].strip()}\n\n↗️ ИЗДАТЕЛЬ - {answer[0][7].strip()}\n\n⚙️ РАЗРАБОТЧИК - {answer[0][8].strip()}\n\n💬 ОПИСАНИЕ - {answer[0][4].strip()}'
