import csv
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./data/chromedriver')

i = 1
driver.get('http://www.etoland.co.kr/bbs/board.php?bo_table=etohumor03&sca=%C8%C4%B9%E6&page='+str(i))
soup = BeautifulSoup(driver.page_source, 'html.parser')

board = soup.find_all('td', class_='mw_basic_list_subject')
for bbs in board:
    print(bbs.find_all('a')[1].attrs['href'])

driver.close()
# driver.get('http://www.etoland.co.kr/bbs/board.php?bo_table=hit&wr_id=2515043&sca=')
# soup = BeautifulSoup(driver.page_source, 'html.parser')
#
# content = soup.find('td', class_='mw_basic_view_content')
#
# videos = content.find_all('video')
# for video in videos:
#     print(video.find('source').attrs['src'])
#
# imgs = content.find_all('img')
# for img in imgs:
#     print(img.attrs['src'])
#
# driver.close()