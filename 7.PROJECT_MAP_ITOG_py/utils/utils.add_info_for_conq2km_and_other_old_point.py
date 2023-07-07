from func_old import *
from statistics import mean

if __name__ == "__main__":
    """чтение из листа"""
    with open("houses_obrabotannie_with_coords_ITOG.json", "r", encoding='utf-8') as read_file:
        data_house = json.load(read_file)[:10]
    # pprint(data_house)
    with open("Zagot_pod_doma.json", "r", encoding='utf-8') as read_file:
        data_point= json.load(read_file)[:10]

    """ удаление пропусков 141 шт"""
    list_pr = []
    for i in data_house:
        i['Зарегистрировано жителей'] = str(i['Зарегистрировано жителей']).replace(' ', '')
        if i['Зарегистрировано жителей'] == '':
            i['Зарегистрировано жителей'] = 274
        else:
            continue
        try:
            i['Зарегистрировано жителей'] = float(i['Зарегистрировано жителей'])
        except Exception as e:
            print("ВОТ ЭТИ ПРОБЛЕМЫНЕ")
            print(i['Зарегистрировано жителей'])
            list_pr.append(i['Зарегистрировано жителей'])
        if type(i['Зарегистрировано жителей']) == float:
            print('Замена типов прошла')
            continue
        else:
            print('не заменились типы')
    pprint(list_pr)
    print(len(list_pr))
    """ Предварительная обработка данных"""
    df = pd.DataFrame(data_house)

    df.dropna(subset=['coords'], inplace=True)
    print(df['coords'].isna().sum())
    print(df.isna().sum())
    df1 = pd.DataFrame(data_point)
    print(df1['dist_to_closer_metro'].mean())
    df1.dropna(subset=['coordinates'], inplace=True)

    print(f'ВОТ ДЛИНА ДО ИСКЛЮЧЕНИЯ ТОЧЕК С ДАЛЬНОСТЬЮ ДО МЕТРО БОЛЕЕ 2000 метров: {len(data_point)}')
    """"оставляем только точки которые не далее 2 кв до метро"""
    nn_list_1 = []
    for i in data_point:
        if i.get('dist_to_closer_metro') <= 2000:
            nn_list_1.append(i)
        else:
            continue
    data_point = nn_list_1
    print(f'ВОТ ДЛИНА после исключения  ТОЧЕК С ДАЛЬНОСТЬЮ ДО МЕТРО БОЛЕЕ 2000 метров: {len(data_point)}')
    dist = get_midle_list_info(data_point, categ=None)[0]
    dist_two_km = float(2000)
    data_point = get_info_oldp_house(data_house, data_point, dist,dist_two_km)
    data_point = get_conquer_qantity(data_point, dist_two_km)

    with open("ITOG_NEW_COORDS_WITH_ALL_INFO_24.02.2020_s_old.json", "w") as write_file:
        json.dump(data_point, write_file)
    print('Все записано')
    print(len(data_point))
