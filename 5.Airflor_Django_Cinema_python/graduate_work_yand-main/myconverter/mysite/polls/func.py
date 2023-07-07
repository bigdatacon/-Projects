import requests
from pathlib import Path
import os

def replace_slash(path):
    path_list = path.split("\\")
    new_path = ''
    for i in path_list:
        # print(f' eto i : {i}')
        new_path += str(i.replace(' ', '').replace('', '\\f')) + str('\\\\')
        # print(f'here new_path in cycle: {new_path}')
    return new_path[:-2]

def load_file_to_model(path):
    #get path for all files in path directory
    files = []
    for p in Path(path).rglob('*'):
        # print(f' eto p : {str(p)}, type: {type(str(p))}')
        files.append(str(p.parent) + p.name)

    #write file to model
    print(f' start write : {files}')
    try:
        for file in files:
            print(f' eto file : ')
            print(str(file))
            i = 1
            fd = open(str(file), "rb")
            # print(f' etp fd : {fd}, eto str(file) : {str(file)}')
            # fields = ['id', 'title', 'certificate', 'file_path']

            ans_file = requests.post("http://127.0.0.1:8000/filmwork/", {'title': f"test_api_{i}", 'certificate': f"test_api_{i}"},
                                     files={'file_path': fd})
            print(f"Answer is with load_file_to_model {ans_file.status_code}: {ans_file.json()}")
            i +=1
            return True
    except Exception as e:
        print(f'  Exception in load_file_to_model : {e.args}')


if __name__ == '__main__':
    path = 'C:\Yand_final_sprint\myconverter\mysite\files'
    ## Функция не работает
    path = replace_slash(path)
    # load_file_to_model(path)

    files = []
    i = 1
    for p in Path(path).rglob('*'):
        print(f' {i:} eto p : {str(p)}, type: {type(str(p))}')

        file_path = str(p.parent) + p.name
        print(f'eto file_path :')
        print(file_path)
        ans_file = requests.post("http://127.0.0.1:8000/filmwork/",
                                 {'title': f"test_api_{i}", 'certificate': f"test_api_{i}"},
                                 files={'file_path': file_path})
        print(f"Answer is with load_file_to_model {ans_file.status_code}: {ans_file.json()}")
        i += 1

