from functools import lru_cache
# from fake_db import fake_films_persons_db
from fuzzywuzzy import fuzz

fake_films_persons_db = {
    "зеленая миля" : "Том Хэнкс",
    "криминальное чтиво" : "Джон Траволта"
}
#
# string = 'Зеленая миля'
# string_wrong = 'пары ры '
# string_near = 'зеленая ми'

class AliceHandler:
    def __init__(self):
        pass

    async def find_actor_in_fake_db(self, input_actor: str):
        res = False
        for k,v in fake_films_persons_db.items():
            x = fuzz.WRatio(input_actor.lower().replace(' ', ''), k.lower().replace(' ', ''),)
            if x>=90:
                print(f'here : {input_actor} : {k}, {x}')
                res = v
                return res
        return res

    async def find_actor_in_fake_db_json(self, input_actor: dict):
        res = False
        for k,v in fake_films_persons_db.items():
            x = fuzz.WRatio(input_actor.get('actor').lower().replace(' ', ''), k.lower().replace(' ', ''),)
            if x>=90:
                print(f'here : {input_actor} : {k}, {x}')
                res = v
                return res
        return res

    async def return_film_data(self):
        return fake_films_persons_db

example = AliceHandler()

# print(f' result of function : {example.find_actor_in_fake_db(string)}')
# print(f' result of wrong function : {example.find_actor_in_fake_db(string_wrong)}')
# print(f' result of near function : {example.find_actor_in_fake_db(string_near)}')
# print(f' result of function return_film_data : {example.return_film_data()}')


@lru_cache()
def get_alicehandler_service() -> AliceHandler:
    return AliceHandler()

