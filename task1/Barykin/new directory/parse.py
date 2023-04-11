from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import psycopg2
import wget

main = 'https://carsdb.ru'
connection = psycopg2.connect(host='localhost', dbname='db', user='postgres', password='123')

cursor=connection.cursor()
links = "https://carsdb.ru/super/rating/design/"
s=Service('C:\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(links)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
link = soup.find_all('div', class_="car_block")

count=0

for i in link:
    mark = i.find('div', class_='car_char')
    model= i.find('h3', class_='car_h3')
    block = i.find('img', class_='car_photo')
    url = block.get('src')
    model= "".join(model.text.strip().split('\n'))
    mark = "".join(mark.text.strip().split('\n'))
    print(url)
    print(mark)
    print(model)
    count +=1

    insert_query=f"""INSERT INTO cars(id, description, model) VALUES ({count}, '{mark}', '{model}');"""
    cursor.execute(insert_query)