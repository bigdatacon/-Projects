import random
from typing import Optional
import phrases

from alice_services.fake_db import fake_films_persons_db
from api.search import SearchConnector
from phrases import get_phrase

api = SearchConnector("http://127.0.0.1:8002/api/v1/alice_api/")



def get_film(form):
    """Ищет фильм по названию и рассказывает о нем информацию."""
    api_req = {
        "film": form["slots"].get("film", {}).get("value"),
    }
    api_req = {k: v for k, v in api_req.items() if v}


    film = api.get_all_films()
    if not film:
        return "К сожалению, я не смогла найти этот фильм",

    return film.get('Зеленая миля')
