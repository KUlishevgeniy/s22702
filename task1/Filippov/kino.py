from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

s = Service('C:\PycharmProjects\pythonProject\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page=1')
time.sleep(20)
t=0

for page in range (1,6):
    browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page={page}')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    NameFilms = soup.find_all("div", class_="base-movie-main-info_mainInfo__ZL_u3")
    for n in NameFilms:
        t+=1
        print(t, n.text)