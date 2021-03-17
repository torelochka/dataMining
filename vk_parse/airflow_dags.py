import datetime as dt

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

from database import main

args = {
    'owner': 'airflow',
    'start_date': dt.datetime.now(),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}

with DAG(dag_id='vk', default_args=args, schedule_interval=None) as dag:
    vk_parse_dag = PythonOperator(
        task_id='download_vk_words',
        python_callable=main,
        dag=dag
    )