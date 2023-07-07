import requests

import os
from rest_framework import status
# from .models import FilmWork
# from .views import FilmWorkViewSet
# print("Getting the list of all questions")
# ans = requests.get("http://127.0.0.1:8000/polls/question/")
# print(f"Answer is {ans.status_code}: {ans.json()}")
# print("Adding a new question")
# ans = requests.post("http://127.0.0.1:8000/polls/question/", json={'question_text': "New question"})
# print(f"Answer is {ans.status_code}: {ans.json()}")
#
# fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")
#
# ans_file = requests.post("http://127.0.0.1:8000/questions/", {'question_text': "With file"}, files={'file_path': fd})
# print(f"Answer is {ans_file.status_code}: {ans_file.json()}")


### Пишу в модель для Фильмов - работает
# fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")
# # fields = ['id', 'title', 'certificate', 'file_path']
#
# ans_file = requests.post("http://127.0.0.1:8000/filmwork/", {'title' : "test_api", 'certificate': "test_api"}, files={'file_path': fd})
# print(f"Answer is {ans_file.status_code}: {ans_file.json()}")
#Пробую пример с гет запросом из теории
# from rest_framework.test import force_authenticate, APIRequestFactory
#
#
# factory = APIRequestFactory()
# user = FilmWork.objects.get(id='8f47c55a-e16a-42e5-a9f9-188fec5ed5de')
# view = FilmWorkViewSet.as_view()
#
# # Make an authenticated request to the view...
# request = factory.get('/filmwork/')
# force_authenticate(request, user=user)
# response = view(request)

# Проверяю методы putt, update, delete для модели FilmWork
# {
#     "id": "8f47c55a-e16a-42e5-a9f9-188fec5ed5de",
#     "title": "five",
#     "certificate": "f",
#     "file_path": "http://127.0.0.1:8000/film_works/bandicam_2022-09-02_11-44-41-932.mp4"
# },
# Сначала гет по ключу
# ans_file = requests.get("http://127.0.0.1:8000/filmwork/", {'id': '8f47c55a-e16a-42e5-a9f9-188fec5ed5de', 'title' : "five", 'certificate': "f"})
# ans_file = requests.get("http://127.0.0.1:8000/filmwork/8f47c55a-e16a-42e5-a9f9-188fec5ed5de")
# print(f"Answer is {ans_file.status_code}: {ans_file.json()}")



# cоздание и удаление  объекта работает
# fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")
# ans_file = requests.post("http://127.0.0.1:8000/filmwork/", {"title": "test", "certificate": "test"}, files={'file_path': fd})
# print(f"Answer is {ans_file.status_code}: {ans_file.json()},  id : {ans_file.json().get('id')}")
#Answer is 201:
# id = ans_file.json().get('id')
# ans_file = requests.delete(f"http://127.0.0.1:8000/filmwork/{id}")
# print(f"Answer is {ans_file.status_code}")
#Answer is 204


# update объекта
# fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")
# response = requests.put("http://127.0.0.1:8000/filmwork/c4563b47-e3a6-4ae0-a450-563901bde8e4/",
#                          {"title": "test_UPDATE", "certificate": "test"},
#                          files={'file_path': fd})
#
# print(f'response.status_code : {response.status_code} Answer after update : {response.json().get("title")}, send to update : {"test_UPDATE"}')
#Answer AttributeError: module 'requests' has no attribute 'update'

# model_url = 'http://127.0.0.1:8000/filmwork/'
object_data = {"title": "test", "certificate": "test"}
# file_path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4'
file_path_new =  os.path.join('C:', 'Yand_final_sprint', 'myconverter', 'mysite', 'files', 'тест.mp4')    # 'C:Yand_final_sprint\myconverter\mysite\polls\files\тест.mp4'
# file_path = os.path.join('C:', 'Yand_final_sprint', 'myconverter', 'mysite', 'polls', 'files', 'тест.mp4')
# fd = open(file_path.encode('utf-8'), 'rb')
fd = open(file_path_new.encode('utf-8'), 'rb')
#get_model_object_by_id
# print("http://127.0.0.1:8000/filmwork/763af035-a450-4e62-931b-d59815c3d028")
# id = '763af035-a450-4e62-931b-d59815c3d028'
# print(f'"http://127.0.0.1:8000/filmwork/{id}"')
#
# response = requests.get("http://127.0.0.1:8000/filmwork/763af035-a450-4e62-931b-d59815c3d028")
# print(f'response.json : {response.json()}')

# response = requests.get(f"{model_url}{id}")
# print(f'response.json : {response.json()}')


# add_one_object_to_table(self, object_data: dict):

response = requests.post("http://127.0.0.1:8000/filmwork/", {"title": "test", "certificate": "test"},
                         files={'file_path': fd})
print(f' в тесте reqfile : {response.status_code, response.json()}')

# response = requests.post(f'{model_url}', object_data,
#                          files={'file_path': fd})
# print(f' another way :  : {response.status_code}, response.json() : {response.json()}, {response.status_code==201}')


import os



# file_path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4' #C:\Yand_final_sprint\myconverter\mysite\polls\files\тест.mp4

# file_path_new =  os.path.join('C:',  '\\', 'Yand_final_sprint', 'myconverter', 'mysite', 'polls', 'files', 'bandicam_2022-09-02_00-50-24-003.mp4')    # 'C:Yand_final_sprint\myconverter\mysite\polls\files\тест.mp4'
# file_path_new =  os.path.join('C:',  '\\', 'Yand_final_sprint', 'myconverter', 'mysite', 'polls', 'files', 'тест.mp4')
# print(f' eto file_path_new : {file_path_new}')


# file_path_new =  str(os.path.join('C:', 'Yand_final_sprint', 'myconverter', 'mysite', 'polls', 'files', 'тест.mp4')).encode('utf-8')    # 'C:Yand_final_sprint\myconverter\mysite\polls\files\тест.mp4'
# file_path = os.path.join('C:', 'Yand_final_sprint', 'myconverter', 'mysite', 'polls', 'files', 'тест.mp4')
# fd = open(file_path.encode('utf-8'), 'rb')
# fd_new = open(file_path_new, 'rb')

# response = requests.post("http://127.0.0.1:8000/filmwork/", {"title": "test", "certificate": "test"},
#                          files={'file_path': fd})
# print(response.status_code, response.json())
# response = requests.post("http://127.0.0.1:8000/filmwork/", {"title": "test", "certificate": "test"},
#                          files={'file_path': fd_new})
#
# print(response.status_code, response.json())


"""без слешей"""
""" ПРОВЕРКА """
# {
#     "id": "d90e9345-09c2-4d46-97a3-d6505b767f30",
#     "title": "test",
#     "certificate": "test",
#     "file_path": "http://127.0.0.1:8000/film_works/%D1%82%D0%B5%D1%81%D1%82_4c0oXm9.mp4"
# }


file_path = "http://127.0.0.1:8000/film_works/%D1%82%D0%B5%D1%81%D1%82.mp4".split('/')[-1]
print(file_path, type(file_path))


#1 пробую создать объект filmwork без класса model_handler - работает
# object_data = {"title": "test", "certificate": "test"}
# file_path_new_2 = os.path.join("..", "files", "тест.mp4")
# fd_new_2 = open(file_path_new_2, 'rb')
# response = requests.post("http://127.0.0.1:8000/filmwork/", {"title": "test", "certificate": "test"},
#                          files={'file_path': fd_new_2})
#
# print(response.status_code, response.json())
# print(response.json().get('file_path'), response.json().get('id'))

#2 Получаю путь до файла и id фильма по id
# response = requests.get("http://127.0.0.1:8000/filmwork/15543a8e-8901-4393-aca8-f8199ec42e2a")
# file_path_to_convert, film_to_convert_id = response.json().get('file_path'),   response.json().get('id')
file_path_to_convert, film_to_convert_id = 'http://127.0.0.1:8000/media/film_works/%D1%82%D0%B5%D1%81%D1%82_2paQaxx.mp4', '41ed4163-f907-4b9c-9dd2-0947ec067dc3'
print(f'eto file_path_to_convert, film_to_convert_id: {file_path_to_convert, film_to_convert_id}')

#3 resize не делаю но сразу пишу в fileupload
object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5, 'fps': 1,
               'film': film_to_convert_id}
file_path_new_2 = file_path_to_convert

try:
    response = requests.post("http://127.0.0.1:8000/fileupload/", object_data,
                             files={'file_path': file_path_new_2})
    print(f' in fileupload response.status_code, response.json() : {response.status_code, response.json()}')
except Exception as e:
    print(f'exception in create_object_for_converted_video, CAUSE : {e.args}')
