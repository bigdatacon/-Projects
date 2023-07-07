import logging

import uvicorn
from fastapi import FastAPI
from api import alice_api
import shutil
import requests


app = FastAPI()
app.include_router(alice_api.router, prefix='/api/v1/alice_api')


def main() -> None:
    uvicorn.run(
        'alice_main:app',
        host='0.0.0.0',
        port=8002,
    )


if __name__ == '__main__':
    main()
