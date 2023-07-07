FROM python:3.10
WORKDIR /root/airflow
RUN pip install apache-airflow

RUN airflow db init
RUN airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

CMD ["airflow", "standalone"]
