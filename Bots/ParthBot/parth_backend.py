from bs4 import BeautifulSoup
import requests
import random
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


def random_news():
    url = 'https://www.igromania.ru'
    page = requests.get(url + '/news/')
    soup = BeautifulSoup(page.text, "html.parser")
    # print(soup)
    all_news = soup.findAll('div', class_='aubl_item')
    # print(all_news)
    ln = len(all_news)
    x = random.randint(1, ln)
    news = all_news[x]
    # print(news)
    name = news.find('img')['alt']
    img = news.find('img')['src']
    date = news.find('span').get_text(strip=True)
    link = url + news.find('a')['href']
    tags = news('div', class_='tags')
    tag = ''
    for i in tags:
        tag += i.text
    return [name, img, date, link, tag]


func = random_news()
print(func)


scroll = InlineKeyboardMarkup()
next_button = InlineKeyboardButton('Next>>>', callback_data='button_next_scr')
previous_button = InlineKeyboardButton('<<<Previous', callback_data='button_prev_scr')
scroll.add(previous_button, next_button)
