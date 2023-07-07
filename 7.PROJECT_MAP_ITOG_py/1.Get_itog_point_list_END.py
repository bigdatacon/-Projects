from utils.func_new import *
from statistics import mean
import openpyxl
if __name__ == "__main__":
    """чтение из файлов"""
    with open("files/houses_obrabotannie_with_coords_ITOG.json", "r", encoding='utf-8') as read_file:
        data_house = json.load(read_file)
    # pprint(data_house)
    with open("files/OLD_COORDS_ITOG_ITOGOVIY_s_new_chisl_24_02_2021.json", "r", encoding='utf-8') as read_file:
        data_point= json.load(read_file)
    with open("files/ZAGOT_VSE_NOV_COORD_S_METRO.json", "r", encoding='utf-8') as read_file:
        data_new_point = json.load(read_file)[::5]
    """ Предварительная обработка данных"""
    df = pd.DataFrame(data_house)
    df.dropna(subset=['coords'], inplace=True)
    df1 = pd.DataFrame(data_point)
    df1.dropna(subset=['coordinates'], inplace=True)
    pprint(f'длина списка старых точек до слива: {len(data_point)}')
    nn_list_1 = []
    for i in data_point:
        if i.get('dist_to_closer_metro') <= 4000:
            nn_list_1.append(i)
        else:
            continue
    data_point = nn_list_1
    """ удаление пропусков 141 шт"""
    ilist_pr = []
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
            ilist_pr.append(i['Зарегистрировано жителей'])
        if type(i['Зарегистрировано жителей']) == float:
            print('Замена типов прошла')
            continue
        else:
            print('не заменились типы')

    print(f'длина списка действ точек: {len(data_point)}')
    print(f'длина списка новых точке: {len(data_new_point)}')
    dist = get_midle_list_info(data_point, categ=None)[0]
    dist_two_km = float(2000)
    data_new_point = get_info_newp_house(data_house, data_new_point, dist,dist_two_km, data_point)
    data_new_point = get_itog_dots_list_with_options(data_new_point)
    data_new_point = get_one_list_from_twoe(data_point, data_new_point)

    with open("files/test_26_before_rating.json", "w") as write_file:
        json.dump(data_new_point, write_file)
    df2 = pd.DataFrame(data_new_point).to_excel("files/ITOGI_FOR_MANY_POINS.xlsx")
    pprint(data_new_point)
    print(len(data_new_point))
    pprint(f"ИТОГОВЫЙ ПРИНТ вот длина {len(data_new_point)}")

