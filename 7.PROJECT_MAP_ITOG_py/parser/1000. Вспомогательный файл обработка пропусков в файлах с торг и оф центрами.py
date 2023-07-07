import json
import pprint
import csv
import pandas as pd

with open("files_pars/torg_centers_obrabotannie_with_coords.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)
with open("files_pars/office_centers_obrabotannie_with_coords.json", "r", encoding='utf-8') as read_file:
    data_o = json.load(read_file)

for i in data_o:
    if i.get('coords') == None:
        i['coords'] = [55.857781, 37.602391]


rating_torg = float(50)
rating_office = float(50)
for i in data:
    i['rating'] = rating_torg
    i['Класс:'] = 'Not_defined'
for i in data_o:
    i['rating'] = rating_office

for i in data_o:
    if i.get('Площадь:') == '.м²':
        i['Площадь:'] = None
    elif i.get('Площадь:') == 'м²':
        i['Площадь:'] = None
    else:
        continue

df = pd.DataFrame.from_records(data)
df.rename(columns={'link_torg_c': 'link', 'old_name_2': 'new_name_2'}, inplace=True)
df.to_csv('torg_centers.csv')


df_o = pd.DataFrame.from_records(data_o)
df1 = df_o.iloc[:,0:14]
df1 = df1[['name', 'link', 'status', 'adress', 'Площадь:', 'coords', 'longitude', 'latitude', 'Класс:', 'rating']]
df1.rename(columns={'Площадь:': 'square'}, inplace=True)


df_good = df1[~df1['square'].isna()]
df_good['square'].astype(float)
df1['square'].fillna(df_good['square'].mode())

print('данные по офисным центрам')
print(f" Среднее: {df1['square'].mean()}")
print(f" медиана {df1['square'].median()}")
print(f" moda {df1['square'].mode()}")

print("данные по торкговым центрам")
print(f"среднее {df['square'].mean()}")
print(f"MODA : {df['square'].mode()}")
print(f"MEDIANA {df['square'].median()}")

df1.to_csv('office_centers.csv')

""" перевод файлов обратно в json"""
json_list_of = json.loads(json.dumps(list(df.T.to_dict().values())))
json_list_torg = json.loads(json.dumps(list(df1.T.to_dict().values())))
# print(len(json_list_of), len(json_list_torg))
for i in json_list_torg:
    json_list_of.append(i)
# print(len(json_list_of), len(json_list_torg))


for i in json_list_of:
    if type(i['name']) == list:
        i['name'] = i['name'][0]
    elif type(i['adress']) == list:
        i['adress'] = str(i.get('adress')[0])
    else:
        continue

for i in json_list_of:
    if type(i['adress']) == list:
        adr = i.get('adress')[0]
        i['adress'] = adr

for i in json_list_of:
    if type(i['adress']) == list:
        print(i)
with open("files_pars/torg_and_office_together.json", "w") as write_file:
    json.dump(json_list_of, write_file)

df_itog = pd.DataFrame.from_records(json_list_of)
df_itog.to_csv('together_office_and_torg.csv')


""" Формируем отдельно файл с данными где все выше среднего"""
list_itog_more_then_avg =[]
for i in json_list_of:
    if i.get('status') == 'torg_cntr':
        if i.get('square') > float(35000):
            list_itog_more_then_avg.append(i)
        else:
            continue
    else:
        if i.get('square') > float(25000):
            list_itog_more_then_avg.append(i)
        else:
            continue

print(len(json_list_of), len(list_itog_more_then_avg))

with open("files_pars/torg_and_office_together_only_high_values.json", "w") as write_file:
    json.dump(list_itog_more_then_avg, write_file)

print('DONE')


for i in data_o:
    if i.get('coords') == None:
        print(f"вот это нулевые: {i}")
    else:
        print('ничего нет')


