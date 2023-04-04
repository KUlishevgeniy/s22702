from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import requests
import wget


main='https://market.yandex.ru'
for i in range(5):
    link= 'https://market.yandex.ru/catalog--smartfony/61808/list?hid=91491&allowCollapsing=1&local-offers-first=0&glfilter=21194330%3A34066443&page=' + str(i+1)
    s=Service('C:\chromdriver\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get(link)
    time.sleep(5)
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    link = soup.find_all('div', class_="_2im8- _2S9MU _2jRxX")

    image_number=1
    for i in link:
        path= (f"imagine\{image_number}.jpg")
        url = i.find('a').get('href')
        browser.get(f'{main}{url}')
        time.sleep(5)
        html_text = browser.page_source
        new_soup=BeautifulSoup(html_text, 'lxml')
        block = new_soup.find('table', class_ = 'Ksay3')
        cost = new_soup.find('div', class_= '_37Axw cia-cs')
        name = new_soup.find('h1', class_= '_1BWd_ _2OAAC undefined cia-cs')
        print(f'{image_number} :', name.text)
        print(block.text)
        print(cost.text)
        image = new_soup.find('img', class_='_3Wp6V')
        result_image=image.get('src')
        result_image='https:' + str(result_image)
        if result_image== True: wget.download(result_image, path)
        image_number = image_number + 1