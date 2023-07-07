
FROM python:3.9.9-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get install -y ffmpeg
#RUN apt-get install -y postgresql-client
RUN apt install -y netcat

COPY requirements.txt /usr/src/app
COPY files /usr/src/app/files
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir
COPY modelhandler.py /usr/src/app
#COPY ../mysite/files/тест.mp4 /usr/src/app
COPY ./тест.mp4 /usr/src/app
#RUN pip install -r dev.txt
#
#COPY ./entrypoint.dev.sh .
#RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.dev.sh
#RUN chmod +x /usr/src/app/entrypoint.dev.sh
#
#COPY ./src .
#
#ENTRYPOINT ["/usr/src/app/entrypoint.dev.sh"]
#
CMD ["python", "modelhandler.py"]