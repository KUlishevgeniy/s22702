from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as BS
import wget

s = Service(r'C:\1\chromedriver')
browser = webdriver.Chrome(service=s)
r = browser.get("https://pogoda7.ru/prognoz/RU-Russia")
html_text = browser.page_source
html = BS(html_text, 'html.parser')

list = html.find("div", class_ = "listing").find("ul")
for item in list:
    print(item.text)

url= 'https://pogoda7.ru/templates/pogoda/images/logo.png'
wget.download (url, 'logo.jpg')