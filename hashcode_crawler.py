from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from bs4 import BeautifulSoup
import pickle

site_keyword = " site:https://hashcode.co.kr"
driver = webdriver.Chrome('./data/chromedriver')
tag_list = []
no_result_list = []
tag_set = ['c', 'c++', 'java', 'javascript', 'python']

with open('./data/hashcode_classification2020_test.csv') as f:
    spamreader = csv.DictReader(f)
    idx = 0
    for row in spamreader:
        info = [idx, row['title']]

        try:
            driver.get("https://hashcode.co.kr/questions/search?utf8=%E2%9C%93&text=" + row['title'])
            elem = driver.find_element_by_xpath("//li[@class='question-list-item']/div[@class='question']/div/h4/a")
            info.append(elem.text)
            info.append(elem.get_attribute('href'))

            elem.click()
            time.sleep(2)
        except:
            print('{} 검색 결과 없음 : {}'.format(idx, row['title']))
            no_result_list.append((idx, row['title']))
            idx += 1
            continue


        try:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            t_list = []
            information_list = soup.select("h6[class='tag']")
            for information in information_list:
                t_list.append(information.text)
            info.append(t_list)
        except:
            print('{} 파싱에러 : {}'.format(idx, row['title']))
            no_result_list.append((idx, row['title']))
            idx += 1
            continue
        print(info)
        tag_list.append(info)
        idx += 1
        print("")

with open('./data/correct.pkl', 'wb') as f:
    pickle.dump(tag_list, f)

with open('./data/no_result.pkl', 'wb') as f:
    pickle.dump(no_result_list, f)
driver.close()

