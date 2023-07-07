import requests
# string = 'зеленая миля'
string = 'криминальное чтиво'


answer = requests.get(f"http://127.0.0.1:8002/api/v1/alice_api/find_actor_in_fake_db/?input_actor={string}")
print(f' eto answer.json for actor : {answer.json()}')


string_dict = {'actor' : 'Зеленая миля'}
# response =  requests.get('http://127.0.0.1:8002/api/v1/alice_api/find_actor_in_fake_db_json/', string_dict)
response =  requests.get('http://127.0.0.1:8002/api/v1/alice_api/find_actor_in_fake_db_json/', params=string_dict)
print(f' eto response.json for actor : {response.json()}')

#2 просто возвращаю fake_films_db
answer = requests.get(f"http://127.0.0.1:8002/api/v1/alice_api/return_film_data/")
print(f' eto answer.json all objects: answer.json(): {answer.json()}')