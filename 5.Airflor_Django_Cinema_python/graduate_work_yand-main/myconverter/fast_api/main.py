import logging

import uvicorn
from core.logger import LOGGING
from fastapi import FastAPI, File, UploadFile
from api import  modelhandlerapi
import shutil
import requests


app = FastAPI()
app.include_router(modelhandlerapi.router, prefix='/api/v1/modelhandlerapi')


def main() -> None:
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8001,
        log_config=LOGGING,
        log_level=logging.DEBUG,  # TODO set level through env var
    )


if __name__ == '__main__':
    main()
