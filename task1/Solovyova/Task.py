from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
s= Service('C:\1\chromedriver.exe')
browser=webdriver.Chrome(service=s)
browser.get('https://www.kinopoisk.ru/lists/movies/top250/')
time.sleep(10)
html_text=browser.page_source
print(html_text)
soup=BeautifulSoup(html_text,'lxml')
films=soup.find_all('div', class_='base-movie-main-info_mainInfo__ZL_u3')
print (films[0].text)
