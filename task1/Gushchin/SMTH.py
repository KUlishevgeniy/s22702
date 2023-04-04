from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def login(number, password):
    num1 = browser.find_element(By.CLASS_NAME, "VkIdForm__input")
    num1.send_keys(number)
    accept = browser.find_element(By.CLASS_NAME, "VkIdForm__signInButton")
    accept.click()
    time.sleep(10)


s = Service('F:\Chromedriver\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get("https://habr.com/ru/company/otus/blog/596071/")
print(browser.window_handles)
browser.get('https://vk.com/')
login(12314123, 1231323)
