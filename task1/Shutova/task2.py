from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import wget

place=0
s = Service('\\Users\\viktoria_shutova\\Downloads\\chromedriver_mac_arm64\\chromedriver')
browser = webdriver.Chrome(service=s)
browser.get(f'https://metarankings.ru/best-games/page/1/')
time.sleep(10)

for page in range(1, 2):
    i = 0
    count = 0
    k = 0
    browser.get(f'https://metarankings.ru/best-games/page/{page}/')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')

    games = soup.find_all("div", class_="post clear")
    marks = soup.find_all("div", class_="small-score mark-10")
    photos = soup.find_all('div', class_="post clear")

    for k in photos:
        photos = 50
        count += 1
        url = k.find('img', class_="post-image")
        l = url.get('src')
        wget.download(l, f'/Users/viktoria_shutova/Documents/s22702-master/task1/Shutova/photo/{count}.jpg')

    for game in games:
        place +=1
        name = game.find("a", class_="name")
        consol = game.find("div", class_="post-meta")

        i +=1

        print(place,") ", name.get_text(), consol.get_text())
