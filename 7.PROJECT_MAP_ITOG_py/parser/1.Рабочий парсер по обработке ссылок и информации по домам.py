import json
import pprint
import requests
from lxml import html
import tqdm
import time

def get_house(data_all):
    for i in tqdm.tqdm(data_all):
        try:
            req = requests.get(i).text
            root = html.fromstring(req)
            count = data_all.index(i)
            data = root.xpath('//dl[contains(@class, "dl-horizontal wide")]//dd/text()')
            all_houses_vaq = {'number': count, 'adress': data[2], 'ful_adres': data[3], 'ploshad_doma': data[5], 'colich_giteley': data[6]}
            all_houses_list.append(all_houses_vaq)
            print(f' ЭТОТ ЭЛЕМЕНТ ОБРАБОТАН: {count}')
            with open("files_pars/HOUSES_full_else.json", "w") as write_file:
                json.dump(all_houses_list, write_file)
            time.sleep(0.001)
        except Exception as e:
            print(f'TROUBLE on element: {count}')
    # time.sleep(0.001)
    return all_houses_list

if __name__ == "__main__":
    with open("files_pars/HOUSES_links.json", "r", encoding='utf-8') as read_file:
        data_all = json.load(read_file)
    data_all = data_all[16861:]
    all_houses_vaq = {}
    all_houses_list = []
    all_houses_list = get_house(data_all)
    print('ВСЕ ЗАПИСАНО')
