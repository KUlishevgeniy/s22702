from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import wget


data = []
def pars():
    j = 0
    start_pos = 0
    end_pos = 1080
    counter = 0
    s = Service('C:\Chromedriver\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    #print("input 1 for parsing trends, input 2 for parsing search")
    #a = int(input())
    #time.sleep(5)
    #if a == 1:
    browser.get(f'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl')
    #if a == 2:
       # print("input the tittle of channel or video")
      #  link = input()
      #  time.sleep(6)
      #  for i in range(len(link)):
        #    if link[i] == " ":
      #          link = link[:i] + '+' + link[i+1:]
      #  browser.get(f'https://www.youtube.com/results?search_query={link}')

    while (j != 20):
        browser.execute_script(f"window.scrollTo({start_pos}, {end_pos})")
        j += 1
        start_pos = end_pos
        end_pos += 1080
        time.sleep(1)

    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    videos = soup.find_all("ytd-video-renderer", class_="style-scope ytd-expanded-shelf-contents-renderer")
    pictures = []

    for video in videos:
        tmp =[]
        counter += 1
        name = video.find("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")
        channel = video.find("yt-formatted-string", class_="style-scope ytd-channel-name complex-string")
        views = video.find("span", class_="inline-metadata-item style-scope ytd-video-meta-block")
        images = video.find("img")
        link = images.get('src')

        tmp.append(counter)
        tmp.append(name.text)
        tmp.append(channel.text)
        tmp.append(views.text)
        data.append(tmp)
        if counter == 10:
            break
        #pictures.append(link)
        #print(name.get_text(), channel.get_text(), views.get_text() , link)
    #for i in range(len(pictures)):
        #wget.download(pictures[i], 'picture'+str(i)+'.jpeg')

    return data
