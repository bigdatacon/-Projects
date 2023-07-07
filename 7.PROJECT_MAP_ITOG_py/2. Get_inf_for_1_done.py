from utils.func_one import *
import pandas as pd
import openpyxl

if __name__ == "__main__":
    # categ=categ
    with open("files/FOR_CHEK_SPISOK_TEK_KOORD_WITH_ALL_INFO.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)

    input_coord_list = []
    input_coord_list_lat = float(input('введите координаты адреса в формате 55.7751502 широто, долгота: '))
    input_coord_list_long = float(input('введите координаты адреса в формате 37.4697764 широто, долгота: '))
    input_coord_list.append(input_coord_list_lat)
    input_coord_list.append(input_coord_list_long)
    # input_coord_list = [55.7751502, 37.4697764]

    itog_list_coords = get_dots_all_info_one_point(input_coord_list, data)
    point_info = (pd.DataFrame(itog_list_coords[-1])).iloc[0]


    with open("files/ITOGI_fift_one_point.json", "w") as write_file:
        json.dump(itog_list_coords, write_file)
    print(f'FILE WITH INFO FOR ONE POINT WRITE: {len(itog_list_coords)}')

    print('--------------------------------------------------------')
    # df2 = (pd.DataFrame(point_info)).loc[1].to_excel("1_POINT_INFO.xlsx")
    df2 = point_info.to_excel("files/one_POINT_INFO.xlsx")
    df3 = pd.DataFrame(itog_list_coords).to_excel("files/ALL_POINT_INFO.xlsx")
    print('INFO _BY_NEW_POINT')
    pprint(point_info)