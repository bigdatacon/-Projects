from typing import List, Optional
from fastapi import APIRouter, Depends, Header, File, UploadFile
from alice_services.fake_db_handler import AliceHandler, get_alicehandler_service
import shutil
from fastapi import Query
import uuid

router = APIRouter()


@router.get("/return_film_data")
async def get_model_object_data(
        alice_handler_service: AliceHandler = Depends(get_alicehandler_service),
):
    result = await alice_handler_service.return_film_data()
    return result

@router.get("/find_actor_in_fake_db")
async def get_model_object(input_actor: str,
        alice_handler_service: AliceHandler = Depends(get_alicehandler_service),
):
    result = await alice_handler_service.find_actor_in_fake_db(input_actor)
    return result




@router.get("/find_actor_in_fake_db_json")
async def get_model_object_json(input_actor: dict,
        alice_handler_service: AliceHandler = Depends(get_alicehandler_service),
):
    result = await alice_handler_service.find_actor_in_fake_db_json(input_actor)
    return result