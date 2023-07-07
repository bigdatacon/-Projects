import phrases
from movies import get_film
from phrases import get_phrase
from fuzzywuzzy import fuzz

fake_films_persons_db_full = [
    {'film' : 'зеленая миля', 'rating' : '8.2', 'actor': 'Том Хэнкс', 'genre' : 'драма'},
    {'film' : 'криминальное чтиво', 'rating' : '7.7', 'actor': 'Джон Траволта', 'genre' : 'комедия'},
    {'film' : 'пираты карибского моря', 'rating' : '9.4', 'actor': 'Джони Депп', 'genre' : 'комедия'},
    {'film' : 'страх и ненависть в Лас-Вегасе', 'rating' : '6.5', 'actor': 'Джони Депп', 'genre' : 'комедия'}
]

#информация по названию фильма
def find_film_info(input_film: str):
    rating = None
    genre = None
    all = None
    for el in fake_films_persons_db_full:
        for k,v in el.items():
            if k == 'film':
                x = fuzz.WRatio(input_film.lower().replace(' ', ''), v.lower().replace(' ', ''),)
                if x>=90:
                    # print(f'here in full : {input_film} : {k}, {x}, {el}, {el.get("rating")}')
                    rating = el.get("rating")
                    genre = el.get("genre")
                    all = el
                    return rating, genre, all
    return rating, genre, all

#информация по актеру
def find_film_actor(input_actor: str):
    film_list = []
    all_list = []
    for el in fake_films_persons_db_full:
        for k, v in el.items():
            if k == 'actor':
                x = fuzz.WRatio(input_actor.lower().replace(' ', ''), v.lower().replace(' ', ''), )
                if x >= 90:
                    print(f'here in full actor : {input_actor} : {k}, {x}, {el}, {el.get("rating")}')
                    film = el.get("film")
                    rating = el.get("rating")
                    genre = el.get("genre")
                    all = el
                    film_list.append(film)
                    all_list.append(el)
    return film_list, all_list

def find_film_actor_match(input_actor: str):
    film_list = []
    all_list = []
    for el in fake_films_persons_db_full:
        for k, v in el.items():
            if k == 'actor':
                if input_actor.lower().replace(' ', '')==v.lower().replace(' ', ''):
                    print(f'here in full actor : {input_actor} : {k},  {el}, {el.get("rating")}')
                    film = el.get("film")
                    rating = el.get("rating")
                    genre = el.get("genre")
                    all = el
                    film_list.append(film)
                    all_list.append(el)
    return film_list[0]

def find_film_rating(input_rating: str):
    film_list = []
    for el in fake_films_persons_db_full:
        if float(el.get('rating')) >=float(input_rating):
            film_list.append(el)
    return film_list




def handler(event, context):
    fake_db = {
        "на кухне": "люстра",
        "в коридоре": "лампа"
    }
    fake_films_persons_db = {
        "зеленая миля": "том хэнкс",
        "криминальное чтиво": "джон траволта"
    }



    intents = event.get("request", {}).get("nlu", {}).get("intents", {})
    command = event.get("request", {}).get("command")

    text = get_phrase(phrases.INTRO)
    end_session = "false"

    if intents.get("exit"):
        text = get_phrase(phrases.EXIT)
        end_session = "true"
    elif intents.get("help"):
        text = get_phrase(phrases.HELP)
    elif intents.get("repeat"):
        text = get_phrase(phrases.REPEAT)

    elif intents.get("film.on"):
        value = intents.get('film.on').get("slots").get('where').get('value')
        for k, v in fake_films_persons_db.items():
            if k == value:
                text2 = v


    elif intents.get("actorm.on"):
        value = intents.get('actorm.on').get("slots").get('who').get('value')
        text2 = str(find_film_actor_match(value))
    elif intents.get("rating.on"):
        value = intents.get('rating.on').get("slots").get('who').get('value')
        text2 = str(find_film_rating(value))

    elif intents.get("turn.on"):
        text = 'том хэнкс turn.on'
        value = intents.get('turn.on').get("slots").get('where').get('value')
        for k, v in fake_db.items():
            if k == value:
                text2 = v


    elif command:
        text = get_phrase(phrases.UNSUCCESSFUL)

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
            'text': text2,
            # Don't finish the session after this response.
            'end_session': 'false'
        },

