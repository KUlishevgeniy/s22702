from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import psycopg2
import wget

connection = psycopg2.connect(host='localhost', dbname='db', user='postgres', password='q1w2e3r4')

cursor=connection.cursor()
links = "https://russ-tur.ru/spisok-vsex-turov-po-rossii/"
s=Service('C:\chromdriver\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(links)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
link = soup.find_all('div', class_="atlist__item margin-bottom")

image_number=0
for i in link:
    path= (f"imagine\{image_number}.jpg")
    image = soup.find('img', class_='attachment-thumb_tour_box size-thumb_tour_box wp-post-image')
    result_image = image.get('src')
    wget.download(result_image, path)
    url = i.find('a').get('href')
    browser.get(f'{url}')
    html_text = browser.page_source
    new_soup=BeautifulSoup(html_text, 'lxml')
    cost = new_soup.find('span', class_= 'woocommerce-Price-amount amount')
    time = new_soup.find('ul', style = 'list-style-type: disc;')
    name = new_soup.find('div', class_= 'header-section__title-wrap')
    cost=cost.text.strip()
    time=time.text.strip()
    name = name.text.strip()
    print(f'{image_number} :', name)
    print(cost)
    print(time)
    image_name=f'{image_number}.jpg'
    insert_query=f"""INSERT INTO travel(id, name, cost, period, image) VALUES ({image_number}, '{name}', '{cost}', '{time}', '{image_name}');"""
    cursor.execute(insert_query)
    connection.commit()
    image_number = image_number + 1