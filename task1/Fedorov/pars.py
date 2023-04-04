from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

data = []


def pars():
    s = Service('/Users/ar.galanin/Downloads/chromedriver_mac_arm64/chromedrive')
    browser = webdriver.Chrome(service=s)

    browser.get('https://www.avito.ru/moskva/avtomobili/volvo/xc60/ii-ASgBAgICA0Tgtg26mSjitg3StCjqtg3O7Sg?cd=1&radius=0&searchRadius=0')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    cars = soup.find_all('div', class_='iva-item-body-KLUuy')
    place = 1
    name = soup.find_all('h3', class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO')
    price = soup.find_all('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL')
    i=0

    while i <= 49:
            data.append(place)

            data.append(name[i].text)

            data.append(price[i].text)

            i+=1
            place += 1
    return data
pars()