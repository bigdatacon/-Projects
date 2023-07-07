"""Файл для тестирования работы API N1"""

import requests
import os
print('начат main')
import sys
import uuid

film_uuid = os.getenv('FILM_TEST_UUID', "9f4bc97f-917c-4f1d-b099-cd1d16ec7269")

answer = requests.get(f"http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/?film_uuid={film_uuid}")
print(f'here answer.json for get_model_object_by_id : {answer.json().get("file_path").replace("django", "127.0.0.1")}')
file_path = answer.json().get("file_path").replace('django', '127.0.0.1')
output_file_path = f"{uuid.uuid4()}loaded.mp4"
# url = 'https://www.facebook.com/favicon.ico'
r = requests.get(file_path, allow_redirects=True)
open(f'./loaded/{output_file_path}', 'wb').write(r.content)
print('WRITE')


#0 Добавление данных в базу post методом
object_data = {"title": "test", "certificate": "test"}
title =  {"title": "test"}
certificate = {"certificate": "test"}
file_path = os.path.join("..", "mysite", "files", "тест.mp4")
fd = open(file_path, 'rb')
response = requests.post("http://127.0.0.1:8000/filmwork/", {"title": "test", "certificate": "test"},
                         files={'file_path': fd})
print(f' в тесте fatests : {response.status_code, response.json()}')
fd.close()
fd = open(file_path, 'rb')


#1добавляю объект в базу через API
try:
    response = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/add_one_object_to_table/", object_data, files={'file_path': fd})
    if response.status_code >= 400:
        sys.exit(1)
    print(f"RESULT ....")
    print(response.json())
except Exception as e:
    print(f'except in add_one_object_to_table : {e.args}')

fd.close()

