import math
import json
from statistics import mean
import pprint
# print ("math.log(math.10) : ", math.log(10000000))
# print ("math.log(math.10) : ", math.log(0))

with open("files/test_26_before_rating.json", "r", encoding='utf-8') as read_file:
    data_p = json.load(read_file)
mult = float(12660/6700)
print(mult)
"""1. В новых точках"""
'количество жителей в радиусе 2 км методом домов' # ok
'количество жителей в радиусе до конкурента методом домов' #ok
'население на 1 конкурента в радиусе 2 км методом по домам' #ok
""'это справочно""'
'среднее расстояние до конкурента по действ точкам'
'среднее расстояние до метро по действ точкам'
'среднея численность в радиусе до конкурента по действ точкам'
""" 2. Это в старых точках"""
'население на 1 конкурента в радиусе 2 км методом по домам' # ok
'количество жителей в радиусе до конкурента методом домов' # ok
'количество жителей в радиусе 2 км методом домов' # ok

# pprint.pp(data_p)
print(len(data_p))
l_n = []
l_o = []
for i in data_p:
    if i['status'] == 'new':
        l_n.append(i)
    else:
        continue
for i in data_p:
    if i['status'] == 'old':
        l_o.append(i)
    else:
        continue
print(len(l_n))
# pprint.pprint(l_n[:1])


for i in data_p:
    i['население на 1 конкурента в радиусе 2 км методом по домам']  = float(i['население на 1 конкурента в радиусе 2 км методом по домам'])*mult
    i['количество жителей в радиусе до конкурента методом домов']  = float(i['количество жителей в радиусе до конкурента методом домов'])*mult
    i['количество жителей в радиусе 2 км методом домов']  = float(i['количество жителей в радиусе 2 км методом домов'])*mult
for i in data_p:
    if i['status'] == 'new':
        ch = float(i['chisl']) if float(i['chisl'])>0 else None
        nas_2 = float(i['население на 1 конкурента в радиусе 2 км методом плотности']) if float(i['население на 1 конкурента в радиусе 2 км методом плотности']) >0 else None
        dist_m = float(i['dist_to_closer_metro']) if float(i['dist_to_closer_metro']) >0 else None
        dist_ost = float(i['dist_to_closer_ostanovk']) if float(i['dist_to_closer_ostanovk'])>0 else None
        dist_conc = float(i['dist_to_closest_conquer']) if float(i['dist_to_closest_conquer']) > 0 else None
        i['rating'] = 0
        if nas_2:
            i['rating'] += math.log(nas_2)*10
        elif ch:
            i['rating'] += math.log(ch)*10
        elif dist_m:
            i['rating'] -= math.log(dist_m)*10
        elif dist_ost:
            i['rating'] -= math.log(dist_ost)*10
        elif dist_conc:
            i['rating'] -= math.log(dist_conc)*10
        else:
            continue
    else:
        continue
print('done data_p')

# pprint.pprint(data_p['rating'])
#
# with open("files/add_rating.json", "w") as write_file:
#     json.dump(data_p, write_file)
with open("files/add_rating_only_new.json", "w") as write_file:
    json.dump(data_p, write_file)
print(len(data_p))
pprint.pprint(data_p[:5])
