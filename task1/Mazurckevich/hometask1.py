from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

place = 0
s= Service('D:\driverselenium\chromedriver.exe')
browser=webdriver.Chrome(service=s)
browser.get('https://www.avito.ru/moskva?q=%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%D0%B5%D1%80+%D0%BF%D1%80%D0%B5%D0%B7%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B9&p=1')
time.sleep(1)

for page in range(1, 3):
    i = 0
    browser.get(f'https://www.avito.ru/moskva?q=%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%D0%B5%D1%80+%D0%BF%D1%80%D0%B5%D0%B7%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B9&p={page}')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    vacancies = soup.find_all("div", class_="iva-item-body-KLUuy")
    for vacancy in vacancies:
        place += 1
        str1 = vacancy.find("h3", class_="title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO")
        str2 = vacancy.find("span", class_="price-text-_YGDY text-text-LurtD text-size-s-BxGpL")
        i += 1
        print(place,") ", str1.get_text(), str2.get_text(), "\n")