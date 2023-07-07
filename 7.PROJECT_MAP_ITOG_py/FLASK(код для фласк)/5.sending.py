from flask import request
import flask
from flask import Flask
import pandas as pd
import json
from func_flask import *
from flask import Flask, redirect, url_for
from flask import send_file
import zipfile
import os
from flask import abort, Flask, redirect, url_for
""" Для проверки работы ввести в бразуере ввести строку ниже, где цифры latitude и longitude = координаты точки по 
которой нужна информация"""
# http://127.0.0.1:5002/data?latitude=55.54&long=37.65



app = Flask(__name__)
@app.route('/data')
def data():
    latitude = request.args.get('latitude', 0)
    long = request.args.get('long', 0)
    input_coord_list=[]

    with open("FOR_CHEK_SPISOK_TEK_KOORD_WITH_ALL_INFO.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)

    input_coord_list = [latitude, long]

    data = data[:100]
    itog_list_coords = get_dots_all_info_one_point(input_coord_list, data)
    point_info = (pd.DataFrame(itog_list_coords[-1])).iloc[0]
    with open("ITOGI_fift_one_point.json", "w") as write_file:
        json.dump(itog_list_coords, write_file)
    print(f'FILE WITH INFO FOR ONE POINT WRITE: {len(itog_list_coords)}')

    print('--------------------------------------------------------')
    # df2 = (pd.DataFrame(point_info)).loc[1].to_excel("1_POINT_INFO.xlsx")
    df2 = point_info.to_excel("send/1_POINT_INFO.xlsx")
    df3 = pd.DataFrame(itog_list_coords).to_excel("send/ALL_POINT_INFO.xlsx")
    print('INFO _BY_NEW_POINT')
    # path = "1_POINT_INFO.xlsx"
    # path_2 = "ALL_POINT_INFO.xlsx"
    zipfolder = zipfile.ZipFile('Audiofiles.zip', 'w', compression=zipfile.ZIP_STORED)  # Compression type

    for root, dirs, files in os.walk('send'):
        for file in files:
            # zipfolder.write('send/'+file)
            zipfolder.write(file)

    zipfolder.close()
    # os.remove("Audiofiles.zip")
    return send_file('Audiofiles.zip', as_attachment=True)



if __name__ == "__main__":
    app.run(port = 5002, debug=True)
