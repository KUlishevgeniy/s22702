from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import wget

s = Service(r"C:\Users\mihon\Downloads\chromedriver_win32\chromedriver.exe")
browser = webdriver.Chrome(service=s)

browser.get('https://www.fontanka.ru/2022/06/24/71437451/')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
photos=soup.find_all('div', class_='M9at M9dl')
j=0
for i in photos:
    j+=1
    url=i.find('img', class_='D3dl')
    k=url.get('src')
    wget.download(k, f'C:/Users/mihon/Documents/МИФИ/Инфа/picpic/{j}.jpg')
