from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import psycopg2
connection = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='22882')
cursor=connection.cursor()

place = 0
s= Service('C:\chromedriver.exe')
browser=webdriver.Chrome(service=s)
browser.get('https://www.kinonews.ru/games_top100/')
time.sleep(1)
for page in range(1, 3):
    i = 0
    browser.get(f'https://www.kinonews.ru/games_top100_p2/')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    vacancies = soup.find_all("div", class_="bigtext")
    for vacancy in vacancies:
        place += 1
        str1 = vacancy.find("a", class_="titlefilm")
        i += 1
        print(place, str1.get_text(), '/n')
        insert_qwery = f"""INSERT INTO public.game( place, title)
                VALUES ( {place}, '{str1.get_text()}' );"""
        cursor.execute(insert_qwery)
        connection.commit()
