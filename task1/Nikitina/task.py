from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

place = 0

s = Service('C:\1\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.kinopoisk.ru/lists/movies/top250/')
time.sleep(10)

for pages in range (1, 6):
    browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page={pages}')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    films = soup.find_all('a', class_='base-movie-main-info_link__YwtP1')
    for film in films:
        place += 1
        name = film.find('div', class_='base-movie-main-info_mainInfo__ZL_u3')
        info = film.find('div', class_='desktop-list-main-info_secondaryTitleSlot__mc0mI')
        print(place, ') ', name.get_text(), ', ', info.get_text(), sep="")
