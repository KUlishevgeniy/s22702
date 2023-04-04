from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import wget

place = 0
count = 0

s = Service('C:\1\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://buklya.com/top-100-knig?ysclid=lfinv2w7q1549007652')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
books = soup.find_all('div', class_='top_100_book')

for book in books:
    place += 1
    name = book.find('span', class_='top_100_book_title')
    author = book.find('span', class_='top_100_book_author')
    print(place, ') ', name.get_text(), ', ', author.get_text(), sep="")

for count in range(1, 101):
    url = f'https://buklya.com/uploads/top100/{count}.jpg'
    wget.download(url, f'img/{count}.jpg')
    count += 1