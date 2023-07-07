import json
import pprint
import requests
from lxml import html
import tqdm
import time
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 RuxitSynthetic/1.0 v8089137528 t38550 ath9b965f92 altpub cvcv=2'}
main_link ='https://www.arendator.ru/objects/9923-planeta-7/'

with open("files_pars/centers_links_itg.json", "r", encoding='utf-8') as read_file:
    data_all = json.load(read_file)[1460:]
list_a = []
for i in tqdm.tqdm(data_all):
    try:
        import urllib3
        urllib3.disable_warnings()
        r = requests.get(i, headers=headers, verify=False)
        link = i
        index_i = data_all.index(i)+1
        root = html.fromstring(r.text)
        data_adr = root.xpath('//div[contains(@class, "indexcard-info-params__adress")]/text()')
        data_name = root.xpath('//h1[contains(@class, "indexcard__title")]/text()')
        data_sq = root.xpath('//div[contains(@class, "indexcard-info-params-box__row")]//div[contains(@class, "indexcard-info-params-box__value")]//span/text()')
        dat_n = root.xpath('//div[contains(@class, "indexcard-info-params-box__row")]//div[contains(@class, "indexcard-info-params-box__name")]/text()')
        c = zip(dat_n,data_sq)
        listi = []
        for i in c:
            listi.append([i[0].replace('\n', '').replace(' ', ''), i[1].replace('\n', '').replace(' ', '')])
        vaq = {}
        vaq = {'name': data_name, 'link' : link, 'status': 'torg_office_cntr', 'adress' : data_adr }
        for i in listi:
            vaq[i[0]] = i[1]
        list_a.append(vaq)
        with open("files_pars/centers_links_with_all_inf_3.json", "w") as write_file:
            json.dump(list_a, write_file)
        print(f'прошла обработка со ссылки номер: {index_i}')
        time.sleep(0.00001)
    except Exception as e:
        print(f'что то не так не ссылке номер: {index_i}')

print(f'вске закончено длина итогового списка : {len(list_a)}')


""" обрабокт площади и слив списков в 1 файл"""
with open("files_pars/centers_links_with_all_inf_3.json", "r", encoding='utf-8') as read_file:
    data_all = json.load(read_file)
with open("files_pars/centers_links_with_all_inf_2.json", "r", encoding='utf-8') as read_file:
    data_all_b = json.load(read_file)
print(len(data_all_b))

for i in data_all:
    data_all_b.append(i)

for i in data_all_b:
    a = i.get('Площадь:')
    if a is not None and a != 'м²' and a != '.м²' and len(a) >=3:
        # print(i['Площадь:'])
        i['Площадь:'] = float(a[:-2])
        # print(float(a[:-2]))
        # print(i)
        i['Площадь:'] = float(a[:-2])
    else:
        continue

for i in data_all_b:
    print(i.get('Площадь:'))
#
with open("files_pars/centers_links_with_all_inf_itog_before_coords.json", "w") as write_file:
    json.dump(data_all_b, write_file)

print(len(data_all_b))