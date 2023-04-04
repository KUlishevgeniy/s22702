from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import psycopg2
import wget

place = 0
s = Service('C:\Юля\универ\инфа\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(f'https://www.livelib.ru/books/mob/listview/biglist/~1')
time.sleep(5)

for page in range(1, 2):
    i = 0
    browser.get(f'https://www.livelib.ru/books/mob/listview/biglist/~{page}')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    books = soup.find_all("div", class_="book-item__inner")
    pic = soup.find_all("", class_="")

    for book in books:
        place += 1
        str1 = book.find("a", class_="book-item__title")
        str2 = book.find("a", class_="book-item__author")
        img = book.find("a", class_="book-item__link").find("img")["src"]
        i += 1
        print(str1.get_text(), ', ', str2.get_text(), ', ', wget.download(img, f'bk/{place}.jpg'))
        connection = psycopg2.connect(host='localhost', dbname='data', user='postgres', password='q1w2e3r4')
        cursor = connection.cursor()
        insert_qwery = f"""INSERT INTO public.lib(
              place, title, author)
              VALUES ( {place}, '{str1.get_text()}', '{str2.get_text()}');"""
        cursor.execute(insert_qwery)
        connection.commit()

