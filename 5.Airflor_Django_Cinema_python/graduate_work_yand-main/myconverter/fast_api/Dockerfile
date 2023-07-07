FROM tiangolo/uvicorn-gunicorn:python3.9-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc && apt-get install -y ffmpeg

EXPOSE 8001

WORKDIR /fast_api_converter

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /fast_api_converter/
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . /fast_api_converter/
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8001", "main:app"]
