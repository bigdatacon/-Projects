import os
from logging import config as logging_config

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)

model_link = os.getenv('model_link', 'http://127.0.0.1:8000/')
