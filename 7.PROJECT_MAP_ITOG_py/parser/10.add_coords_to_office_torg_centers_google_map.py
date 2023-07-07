# place = "Москва, ул. Вавилова, д. 44, к. 3"
import googlemaps
import pandas as pd
import json
import pprint
import time
import tqdm
gmaps = googlemaps.Client(key='')
from datetime import datetime
with open("files_pars/torg_centers_itog_before_coords.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

coord_dict = {}
coord_list = []
count = 0

for i in tqdm.tqdm(data):
    try:
        geocode_result = gmaps.geocode(i.get('adress'))
        # pprint.pprint(geocode_result[0]['geometry']['location'])
        coord_list = [geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']]
        i['coords'] = coord_list
        i['longitude'] = geocode_result[0]['geometry']['location']['lng']
        i['latitude'] = geocode_result[0]['geometry']['location']['lat']
        with open("files_pars/torg_centers_obrabotannie_with_coords.json", "w") as write_file:
            json.dump(data, write_file)
        time.sleep(0.1)
        count +=1
        print(f'записана строка номер: {count}')
    except Exception as e:
        print(f'TROUBLE on iter = {count}')
#
#
with open("files_pars/torg_centers_obrabotannie_with_coords.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)
pprint.pprint(data[-20:])
print(len(data))