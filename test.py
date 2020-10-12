from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from bs4 import BeautifulSoup
import pickle
from pprint import pprint

def levenshtein(s1, s2, debug=False):
    if len(s1) < len(s2):
        return levenshtein(s2, s1, debug)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))

        if debug:
            print(current_row[1:])

        previous_row = current_row

    return previous_row[-1]

with open('./data/correct.pkl', 'rb') as f:
    tag_list = pickle.load(f)

for tag in tag_list:
    if tag[0] == 52:
        print(tag)

tag_dic = ['java', 'c', 'c++', 'javascript', 'python']
tags = {'java':3, 'c':1, 'c++':2, 'javascript':4, 'python':5}
ex_tag = []
non_ex_tag = []


with open('./data/label.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f)
    wr.writerow(['idx', 'title', 'crawl_title', 'sim', 'lang', 'lang_code', 'tags', 'link'])
    for tag in tag_list:
        is_exe = False
        for l in tag_dic:
            if l in tag[4]:
                is_exe = True
                wr.writerow([tag[0], tag[1], tag[2], levenshtein(tag[1], tag[2]), l, tags[l], tag[4], tag[3]])
                break
        if is_exe is False:
            wr.writerow([tag[0], tag[1], tag[2], levenshtein(tag[1], tag[2]), 'no_tag', 'no_tag', tag[4], tag[3]])



idxx = []
idxx2 = list(range(500))

for info in tag_list:
    idxx.append(int(info[0]))

print(set(idxx2) - set(idxx))