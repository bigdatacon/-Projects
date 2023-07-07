import json
import tqdm
import time
from pprint import pprint
# import pandas as pd
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 RuxitSynthetic/1.0 v8089137528 t38550 ath9b965f92 altpub cvcv=2'}
import requests
from lxml import html
from pprint import pprint
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
# main_link ='https://www.arendator.ru/objects/office/'

"""ниже итоговый код по сбору ссылок - работает"""
all_houses_vaq = {}
all_houses_list = []
count = 0
page = 0
"""предварительный операции"""
driver = webdriver.Chrome()
driver.get('https://www.arendator.ru/objects/office/')

time.sleep(2)
while True:
    try:
        data = driver.find_elements_by_xpath('//div[contains(@class, "objects-list__wrapper")]/a')
        for i in data:
            d = i.get_attribute("href")
            all_houses_list.append(d)
        link = driver.find_elements_by_xpath('//ul[contains(@class, "abc-paginator")]//li/a')[-1].get_attribute('href')
        driver.get(link)
        time.sleep(0.5)
        with open("files_pars/centers_links.json", "w") as write_file:
            json.dump(all_houses_list, write_file)
        count +=1
        print(f'WRITE FILE: {len(all_houses_list)}')
        print(f'ПРОШЛА ЗАПИСЬ СО СТРАНИЦЫ : {count}')
        print(len(all_houses_list))
    except Exception as e:
        print(f'ПРОБЛЕМА С ПЕРЕХОДОМ СО СТРАНИЦЫ {count}')

"""удаляем дубликаты"""
# with open("files_pars/centers_links_copy.json", "r", encoding='utf-8') as read_file:
#     data_all = json.load(read_file)
#
# print(len(data_all))
# data_all = set(data_all)
# print(len(data_all))
# from itertools import groupby
# new_x = [el for el, _ in groupby(data_all)]
# print(len(new_x))
# with open("files_pars/centers_links_itg.json", "w") as write_file:
#     json.dump(new_x, write_file)
# print(f'Все готово, длина итогового списка : {len(new_x)}')