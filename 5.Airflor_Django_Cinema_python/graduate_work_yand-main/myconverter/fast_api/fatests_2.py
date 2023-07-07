"""Файл для тестирования работы API N2"""
import requests
import os

# film_uuid = os.getenv('FILM_TEST_UUID', "9f4bc97f-917c-4f1d-b099-cd1d16ec7269")
film_uuid = os.getenv('FILM_TEST_UUID', "85229cbf-b09d-4f19-beb0-e47baa3c0c93")
try:
    answer = requests.post(f"http://127.0.0.1:8001/api/v1/modelhandlerapi/resize_full/?file_id={film_uuid}")
    print(f'here answer.json for resize_full : {answer.json()}')
except Exception as e:
    print(f' except in resize_full : {e.args}')

print(f'закончил resize в ручке resize_full')

