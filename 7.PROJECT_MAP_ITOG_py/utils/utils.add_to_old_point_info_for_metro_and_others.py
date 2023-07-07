from func_old import *
with open("files/csvjs.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)
# data = data[:]
list_all = prep_data(data)
"""получаем данные по расстоянию до ближайшего конкурента для каждой компании"""
list_all = get_closer_conquer(list_all)
"""получаем данные по расстоянию до ближайшего метро для каждой компании"""
list_all = get_closer_metro_info(list_all)
"""получаем данные по площади в радиусе до конкурента и численности населения в радиусе до ближайшего конкурента """
list_all = get_square(list_all)
list_all_2 = list_all.copy()
with open("Zagot_pod_doma.json", "w") as write_file:
    json.dump(list_all, write_file)
print(f'WRITE FILE: {len(list_all)}')
print('END')
