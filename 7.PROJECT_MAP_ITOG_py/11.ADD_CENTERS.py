import math
import json
import pandas as pd
from geopy.distance import geodesic
import tqdm
import time
# from utils.func_new import *
# from utils.func_old import *
from statistics import mean
import pprint
# print ("math.log(math.10) : ", math.log(10000000))
# print ("math.log(math.10) : ", math.log(0))

""""Ниже код работает"""

with open("files/add_rating_only_new.json", "r", encoding='utf-8') as read_file:
    data_p = json.load(read_file)

with open("files/torg_and_office_together_only_high_values.json", "r", encoding='utf-8') as read_file:
    data_centers = json.load(read_file)


list_new = []
list_old = []
for i in data_p:
    if i['status'] == 'new':
        list_new.append(i)
    else:
        continue
for i in data_p:
    if i['status'] == 'old':
        list_old.append(i)
    else:
        continue
print(len(list_new), len(list_old))
dist = float(1000)


# 'coords'
def get_conquer_qantity_tw(list_dist, dist_two_km):
    count = 0
    for i in list_dist:
        if i < dist_two_km:
            count +=1
        else:
            continue
    return count
def distance_point_metro(a, b):
    # a = list(a)
    # b = list(b)
    return geodesic(a, b).meters
def lambda_high_h(multiple, data_house):
    massive_list = []
    for i in data_house:
        massive_list.append(i.get('coords'))
    res = list(map(lambda x: distance_point_metro(multiple, x), massive_list))
    return res
def get_info_newp_house(data_office, list_new, dist):
    for i in tqdm.tqdm(list_new):
           multiple = i.get('coordinates')
           res = lambda_high_h(multiple, data_centers)
           numb = get_conquer_qantity_tw(res, dist)
           i['колич крупн торгово-офисн центр рядом'] = numb
           time.sleep(0.00000000000000000000001)
    return list_new

data_p = get_info_newp_house(data_centers, data_p, dist)
for i in data_p:
    print(i.get('колич крупн торгово-офисн центр рядом'))

with open("files/all_dots_with_infor_for_quantity_of_conquers.json", "w") as write_file:
    json.dump(data_p, write_file)

print(f'все записано вот длина итогового списка: {len(data_p)}')

""""выше код работает просто нужно раскоментировать"""
with open("files/torg_and_office_together.json", "r", encoding='utf-8') as read_file:
    data_centers  = json.load(read_file)

with open("files/all_dots_with_infor_for_quantity_of_conquers.json", "r", encoding='utf-8') as read_file:
    data_point = json.load(read_file)

for i in data_point:
    if i.get('rating'):
        i['rating'] = float(i.get('rating') + float(i.get('колич крупн торгово-офисн центр рядом'))*10)
    else:
        continue

data_point_copy = data_point
with open("files/itog_without_centers.json", "w") as write_file:
    json.dump(data_point, write_file)

print(len(data_centers), len(data_point))

df_centers = pd.DataFrame.from_records(data_centers)
df_point = pd.DataFrame.from_records(data_point)
df_centers.rename(columns={'name': 'Название', 'link': 'Сайт', 'adress': 'Адрес', 'square': 'площадь объекта'}, inplace=True)
df_centers_only = df_centers
df_centers_only.to_csv('files/itog_only_centers.csv')

# print(df_centers.columns)
# print(df_point.columns)
data_centers = json.loads(json.dumps(list(df_centers.T.to_dict().values())))
for i in data_centers:
    data_point.append(i)
print('Все слито')
print(len(data_centers), len(data_point))

df_point_all = pd.DataFrame.from_records(data_point)

# print(df_point_all.columns)

with open("files/itog_with_all.json", "w") as write_file:
    json.dump(data_point, write_file)
#
df_point_all.to_csv('files/itog_with_all.csv')


for i in data_point:
    print(i.get('metro_name'))