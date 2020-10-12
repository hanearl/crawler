from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from bs4 import BeautifulSoup
import random

driver = webdriver.Chrome('./data/chromedriver')

# driver.get("https://www.ygosu.com/community/yeobgi/?page=1")
#
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# # time.sleep(random.uniform(1, 10))
#
# link_tag = soup.find("table", class_='bd_list').find_all("td", class_='tit')
# for link in link_tag:
#     try:
#         post_tag_list = link.find_all("a")
#         for post in post_tag_list[1:]:
#             print(post.attrs)
#
#     except:
#         print("[error] : {}".format(link))
#     # time.sleep(random.uniform(1, 10))
#
# driver.close()

driver.get('https://www.ygosu.com/community/yeobgi/1755224')
soup = BeautifulSoup(driver.page_source, 'html.parser')

vote = soup.find_all('li', class_='vot')
for v in vote:
    print(v.text)
    print(v.attrs)

user_nick = soup.find('div', class_='nickname').find('a')
print(user_nick.text)
print(user_nick.attrs['onclick'])

date_and_read = soup.find('div', class_='date')
print(date_and_read.text)

table = soup.find('div', class_='container')
print(table.text)

for img in table.find_all('img'):
    print('img ', img.attrs)

for video in table.find_all('video'):
    print('video ', video.attrs)

for video in table.find_all('source'):
    print('video ', video.attrs)


# reply = soup.find('table', id='reply_list_layer').find_all()

driver.close()