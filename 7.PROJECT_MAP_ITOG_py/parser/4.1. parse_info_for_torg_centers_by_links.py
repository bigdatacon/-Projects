import json
import pprint
import requests
from lxml import html
import tqdm
import time
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 RuxitSynthetic/1.0 v8089137528 t38550 ath9b965f92 altpub cvcv=2'}
main_link ='https://roomfi.ru/torgovye-tsentry/51069-torgovyy-tsentr-elektronika-na-presne/'
with open("files_pars/togrovie_centers_links_itg.json", "r", encoding='utf-8') as read_file:
    data_all = json.load(read_file)

list_a = []
list_false = []
for i in tqdm.tqdm(data_all):
    try:
        import urllib3
        urllib3.disable_warnings()
        r = requests.get(i, headers=headers, verify=False)
        link = i
        index_i = data_all.index(i)+1
        root = html.fromstring(r.text)
        # data_adr = root.xpath('//div[contains(@class, "padding-sm-vr")]//span[contains(@class, "no-padding-l")]//span[contains(@itemprop, "streetAddress")]/text()')
        # data_adr = 'Москва,' + data_adr[0]
        data_adr = root.xpath('//div[contains(@class, "padding-sm-vr")]//span[contains(@class, "no-padding-l")]//span[contains(@itemprop, "streetAddress")]/text()')
        if data_adr:
            data_adr = 'Москва,' + ' '+ data_adr[0]

        else:
            data_adr = root.xpath('//div[contains(@class, "padding-sm-vr")]//span[contains(@class, "no-padding-l")]/text()')[0]
        data_name = root.xpath('//div[contains(@class, "row")]//div[contains(@class, "col-lg-7")]/h1/text()')
        data_name = str(data_name[0].replace('\n', ''))
        data_name = data_name.replace('\t', '').replace(' ', '')

        data_sq1 = root.xpath('//div[contains(@class, "right-block-params-offer2")]//ul[contains(@class, "no-border-last-child ")]//li[contains(@class, "list-group-item ")]//span[contains(@class, "no-padding-l")]/text()')
        # data_sq1 = root.xpath('//ul[contains(@class, "no-border-last-child ")]//li[contains(@class, "list-group-item ")]//span[contains(@class, "no-padding-l")]/text()')
        data_sq2 = root.xpath('//ul[contains(@class, "no-border-last-child ")]//li[contains(@class, "list-group-item ")]//span[contains(@class, "text-right")]/text()')
        new = zip(data_sq1, data_sq2)
        for i in new:
            if i[0] == 'Общая площадь':
                square = float(i[1].replace('\xa0', '')[:-2])
            else:
                continue

        vaq = {}
        vaq = {'name': data_name, 'link_torg_c' : link, 'status': 'torg_cntr', 'adress' : data_adr, 'square':square}
        list_a.append(vaq)
        with open("files_pars/torg_centers_links_with_all_inf_3.json", "w") as write_file:
            json.dump(list_a, write_file)
        print(f'прошла обработка со ссылки номер: {index_i}')
        time.sleep(0.00001)
    except Exception as e:
        print(f'что то не так не ссылке номер: {index_i, link}')
        list_false.append(link)
        with open("files_pars/torg_centers_links_with_all_inf_3_false.json", "w") as write_file:
            json.dump(list_false, write_file)

print(f'вске закончено длина итогового списка : {len(list_a)}')
print(f'вске закончено длина incorrect списка : {len(list_false)}')
for i in list_false:
    print(i)


""" обработка тех ссылок что не сработали сразу"""
with open("files_pars/torg_centers_links_with_all_inf_3_false.json", "r", encoding='utf-8') as read_file:
    data_all = json.load(read_file)

list_a = []
list_false = []
for i in tqdm.tqdm(data_all):
    try:
        import urllib3
        urllib3.disable_warnings()
        r = requests.get(i, headers=headers, verify=False)
        link = i
        index_i = data_all.index(i)+1
        root = html.fromstring(r.text)
        data_adr = root.xpath('//div[contains(@class, "padding-sm-vr")]//span[contains(@class, "no-padding-l")]//span[contains(@itemprop, "streetAddress")]/text()')
        if data_adr:
            data_adr = 'Москва,' + ' ' + data_adr[0]
        else:
            data_adr = root.xpath('//div[contains(@class, "padding-sm-vr")]//span[contains(@class, "no-padding-l")]/text()')[0]

            # if data_adr\
            # else data_adr = root.xpath('//div[contains(@class, "padding-sm-vr")]//span[contains(@class, "no-padding-l")]/text()')
        # data_adr = root.xpath('//div[contains(@class, "padding-sm-vr")]//span[contains(@class, "no-padding-l")]/text()')
        # data_adr = 'Москва,' + data_adr[0]

        data_name = root.xpath('//div[contains(@class, "row")]//div[contains(@class, "col-lg-7")]/h1/text()')
        data_name = str(data_name[0].replace('\n', ''))
        data_name = data_name.replace('\t', '').replace(' ', '')

        data_sq1 = root.xpath('//div[contains(@class, "right-block-params-offer2")]//ul[contains(@class, "no-border-last-child ")]//li[contains(@class, "list-group-item ")]//span[contains(@class, "no-padding-l")]/text()')
        data_sq2 = root.xpath('//div[contains(@class, "right-block-params-offer2")]//ul[contains(@class, "no-border-last-child ")]//li[contains(@class, "list-group-item ")]//span[contains(@class, "text-right")]/text()')
        new = zip(data_sq1, data_sq2)
        for i in new:
            if i[0] == 'Общая площадь':
                square = float(i[1].replace('\xa0', '')[:-2])
            else:
                continue

        vaq = {}
        vaq = {'name': data_name, 'link_torg_c' : link, 'status': 'torg_cntr', 'adress' : data_adr, 'square':square}
        list_a.append(vaq)
        with open("files_pars/after_false_torg_centers_links_with_all_inf_3.json", "w") as write_file:
            json.dump(list_a, write_file)
        print(f'прошла обработка со ссылки номер: {index_i}')
        time.sleep(0.00001)
    except Exception as e:
        print(f'что то не так не ссылке номер: {index_i, link}')
        list_false.append(link)
        with open("files_pars/after_false_torg_centers_links_with_all_inf_3_false.json", "w") as write_file:
            json.dump(list_false, write_file)
#
print(f'вске закончено длина итогового списка : {len(list_a)}')
print(f'вске закончено длина итогового списка incorrect : {len(list_false)}')
for i in list_a:
    print(i)

#
# """склеивание 2 списков в 1"""

with open("files_pars/torg_centers_links_with_all_inf_3.json", "r", encoding='utf-8') as read_file:
    data_all = json.load(read_file)

with open("files_pars/after_false_torg_centers_links_with_all_inf_3.json", "r", encoding='utf-8') as read_file:
    data_small = json.load(read_file)

print(len(data_all), len(data_small))
for i in data_small:
    data_all.append(i)
print(len(data_all), len(data_small))
with open("files_pars/torg_centers_itog_before_coords.json", "w") as write_file:
    json.dump(data_all, write_file)
print('все готово')