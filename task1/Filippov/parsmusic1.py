from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

data = []
def pars():
    s = Service('C:\PycharmProjects\pythonProject\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get('https://mp3bob.ru/luchshee-russkaya-muzyka/')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    place = 1
    artist = soup.find_all("span", class_="song_artist __adv_artist")
    song = soup.find_all("span", class_="song_nazv __adv_name")
    i=0
    while i <= 49:
        data.append(place)
        data.append(artist[i].text)
        data.append(song[i].text)
        i+=1
        place += 1
    print(data)
    return data
pars()