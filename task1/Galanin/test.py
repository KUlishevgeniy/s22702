from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import wget

s = Service('/Users/ar.galanin/Downloads/chromedriver_mac_arm64/chromedrive')
browser = webdriver.Chrome(service=s)

browser.get('https://www.avito.ru/moskva/kvartiry/prodam/novostroyka-ASgBAgICAkSSA8YQ5geOUg?cd=1')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
time.sleep(3)
count=0

photos=soup.find_all('div', class_='photo-slider-root-Exoie photo-slider-redesign-q6DEc')
for i in photos:
        count+=1
        url=i.find('img', class_='photo-slider-image-YqMGj')
        k=url.get('src')
        wget.download(k, f'/Users/ar.galanin/Desktop/photo/{count}.jpg')






