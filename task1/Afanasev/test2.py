from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

for i in range (251):
    i='?page='+ str(i+1)

    s=Service('C:\chromdriver\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get('https://www.kinopoisk.ru/lists/movies/top250/'+str(i))
    time.sleep(20)
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    films = soup.find_all("a", class_="base-movie-main-info_link__YwtP1")

    for film in films:
        print(film.text)
        print()
    films.clear()
