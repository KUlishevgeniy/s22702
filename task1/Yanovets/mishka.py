from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import psycopg2
import wget
a=[]
b=[]
connection = psycopg2.connect(host='localhost', dbname='db', user='postgres', password='q1w2e3r4')

cursor=connection.cursor()
links = "https://www.tutu.ru/poezda/rasp_d.php?nnst1=2000000&nnst2=2004000&date=14.04.2023"
s=Service('C:\chromdriver\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(links)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
time = soup.find_all('div', class_='o33810')
count=0
for i in time:
    if count%2==0: a.append(i.text)
    if count%2==1: b.append(i.text)
    count+=1
for i in range(count//2):
    insert_query = f"""INSERT INTO poezda(id, departure, arrival) VALUES ({i}, '{a[i]}', '{b[i]}');"""
    cursor.execute(insert_query)
    connection.commit()



