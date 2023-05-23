from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import wget


def parse():
    s = Service('D:\Webdriver\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page=1')
    time.sleep(5)
    data = []
    place = 0
    for page in range(1, 6):
        counter = 0
        browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page={page}')
        html_text = browser.page_source
        soup = BeautifulSoup(html_text, 'lxml')
        imgs = soup.find_all("img", class_="styles_image__gRXvn styles_mediumSizeType__fPzdD image styles_root__DZigd")
        films = soup.find_all("a", class_="base-movie-main-info_link__YwtP1")
        print(len(imgs))
        marks = soup.find_all("span", class_="styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg styles_top250Type__mPloU")
        for film in films:
            counter += 1
            place += 1
            runame = film.find("div", class_="base-movie-main-info_mainInfo__ZL_u3")
            try:
                enname = film.find("div", class_="desktop-list-main-info_secondaryTitleSlot__mc0mI")
            except:
                enname = '---'
            print(counter)
            wget.download("https:" + imgs[counter - 1].get("src"), f"pics/{place}.jpeg")
            data.append(f"{place} | {runame.get_text()} | {enname.get_text()} | {marks[counter - 1].get_text()}")
    for film in data:
        print(film)
    return data


if __name__ == '__main__':
    parse()
