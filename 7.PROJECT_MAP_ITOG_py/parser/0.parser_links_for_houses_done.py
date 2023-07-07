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
m_link = 'https://gosjkh.ru'
main_link ='https://gosjkh.ru/houses/moskva/moskva'

all_houses_vaq = {}
all_houses_list = []
count = 0
page = 0

driver = webdriver.Chrome()
driver.get('https://gosjkh.ru/houses/moskva/moskva')
time.sleep(2)
count = 1

""" записываем данные с 1 двух страниц отдельно так как там другая верстка """
data = driver.find_elements_by_xpath("//div[@class='row']//tbody//tr//td[2]/a")
for i in data:
    d = i.get_attribute("href")
    all_houses_list.append(d)
link = driver.find_element_by_xpath('//div/ul[contains(@class, "pagination")]//li[4]/a').get_attribute('href')


driver.get(link)
data = driver.find_elements_by_xpath("//div[@class='row']//tbody//tr//td[2]/a")
for i in data:
    d = i.get_attribute("href")
    all_houses_list.append(d)
#
""" зписываем в файл данные со всех остальных страниц"""
while True:
    try:
        data = driver.find_elements_by_xpath("//div[@class='row']//tbody//tr//td[2]/a")
        for i in data:
            d = i.get_attribute("href")
            all_houses_list.append(d)
        link = driver.find_elements_by_xpath('//div/ul[contains(@class, "pagination")]//li/a')[-2].get_attribute('href')
        driver.get(link)
        time.sleep(0.5)
        with open("files_pars/HOUSES_links.json", "w") as write_file:
            json.dump(all_houses_list, write_file)
        count +=1
        print(f'WRITE FILE: {len(all_houses_list)}')
        print(f'ПРОШЛА ЗАПИСЬ СО СТРАНИЦЫ : {count}')
        print(len(all_houses_list))
    except Exception as e:
        print(f'ПРОБЛЕМА С ПЕРЕХОДОМ СО СТРАНИЦЫ {count}')




# with open("HOUSES_links.json", "r", encoding='utf-8') as read_file:
#     data = json.load(read_file)
