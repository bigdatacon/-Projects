import datetime
import os
import requests

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2022, 10, 15),
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=1),
    'depends_on_past': False
}

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://127.0.0.1:8001/")
FILM_UUID = os.getenv("FILM_TEST_UUID", "9f4bc97f-917c-4f1d-b099-cd1d16ec7269")


def do_resize():
    requests.post(f"{FASTAPI_URL}api/v1/modelhandlerapi/resize_full/?file_id={FILM_UUID}")


with DAG(dag_id='Resize', default_args=args, schedule_interval='@hourly', start_date=datetime.datetime(2022, 10, 15)) as dag:
    resize = PythonOperator(
        task_id='do_resize', python_callable=do_resize, dag=dag
    )
