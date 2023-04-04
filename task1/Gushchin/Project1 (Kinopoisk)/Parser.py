from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import wget


def kinopoisk_parse():
    s = Service('F:\Chromedriver\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    place = 0
    data = []
    for page in range(1, 6):
        browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page={page}')
        html_text = browser.page_source
        soup = BeautifulSoup(html_text, 'lxml')
        films = soup.find_all("div", class_="styles_root__ti07r")
        for film in films:
            place += 1
            rusfilm = False
            url = film.find("a", class_="base-movie-main-info_link__YwtP1").get("href")
            browser.get("https://www.kinopoisk.ru" + url)
            html_text = browser.page_source
            soup = BeautifulSoup(html_text, 'lxml')
            url = soup.find("img", class_="film-poster")
            wget.download("https:" + url.get("src"), f"Pictures/FILMS/FILM{place}.jpeg")

            russian_title = film.find("span", class_="styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj").get_text()
            try:
                english_title = film.find("span", class_="desktop-list-main-info_secondaryTitle__ighTt").get_text()
            except AttributeError:
                english_title = "---"
                rusfilm = True
            tmp = film.find("span", class_="desktop-list-main-info_secondaryText__M_aus").get_text()
            if rusfilm:
                release_year = tmp[0:4]
                length = tmp[5:]
            else:
                release_year = tmp[2:6]
                length = tmp[7:]
            mark = film.find("span", class_="styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg styles_top250Type__mPloU").get_text()
            data.append(f"{place}| {russian_title}| {english_title}| {release_year}| {length}| {mark}")
    browser.close()
    return data


def kanobu_parse():
    s = Service('F:\Chromedriver\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    data = []
    place = 0
    for page in range(1, 33):
        browser.get(f"https://kanobu.ru/games/pc/popular/?page={page}")
        html_text = browser.page_source
        soup = BeautifulSoup(html_text, 'lxml')
        games = soup.find_all("div", class_="BaseElementCard_card__ZIifM knb-card knb-grid-cell")
        for game in games:
            place += 1
            title = game.find("div", class_="BaseElementCard_body__fcrUh").find("a").get_text()

            try:
                release_date = game.find("div", class_="BaseElementCard_body__fcrUh").find("div", class_="BaseElementCard_date__FPfgY").get_text()
            except:
                release_date = '---'

            try:
                mark = game.find("div", class_="KnbCardMark_label__hg6Pg tv-series-mark KnbCardMark_isGreen__G_FLl").get_text()
            except:
                mark = '---'

            url = game.find("img", class_="knb-card--image").get("src")
            wget.download(url, f"Pictures/GAMES/GAME{place}.jpeg")
            browser.get(f"https://kanobu.ru" + game.find("div", class_="BaseElementCard_body__fcrUh").find("a").get("href"))
            html_text = browser.page_source
            soup = BeautifulSoup(html_text, 'lxml')

            try:
                description = soup.find("p", class_="DatabaseElementContent_description__fl9pf").get_text()
            except:
                description = '---'

            try:
                platforms = soup.find_all("span",  class_="DatabaseElementOption_option_value__U0zWT")[2].get_text()
            except:
                platforms = '---'

            try:
                genres = soup.find_all("span",  class_="DatabaseElementOption_option_value__U0zWT")[3].get_text()
            except:
                genres = '---'

            try:
                publisher = soup.find_all("span",  class_="DatabaseElementOption_option_value__U0zWT")[4].get_text()
            except:
                publisher = '---'

            try:
                developer = soup.find_all("span",  class_="DatabaseElementOption_option_value__U0zWT")[5].get_text()
            except:
                developer = '---'

            data.append(f"{place}| {title}| {release_date}| {mark}| {description}| {platforms}| {genres}| {publisher}| {developer}")
    browser.close()
    return data


