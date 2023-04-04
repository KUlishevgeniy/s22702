from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

place = 0
s = Service('C:\Юля\универ\инфа\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page=1')
time.sleep(10)

for page in range(1, 6):
    i = 0
    browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page={page}')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    films = soup.find_all("a", class_="base-movie-main-info_link__YwtP1")
    marks = soup.find_all("span", class_="styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg styles_top250Type__mPloU")

    for film in films:
        place += 1
        str1 = film.find("div", class_="base-movie-main-info_mainInfo__ZL_u3")
        str2 = film.find("div", class_="desktop-list-main-info_secondaryTitleSlot__mc0mI")
        i += 1
        print(place,") ", str1.get_text(), str2.get_text(), marks[i - 1].get_text(), "\n")

