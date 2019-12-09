import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(10),
}

dag3 = DAG(
    dag_id='exercise2c',
    default_args=args,
    schedule_interval=timedelta(minutes=90),
)

task1c = DummyOperator(
    task_id='task1c',
    dag=dag3,
)

task2c = DummyOperator(
    task_id='task2c',
    dag=dag3,
)

task3c = DummyOperator(
    task_id='task3c',
    dag=dag3,
)

task4c = DummyOperator(
    task_id='task4c',
    dag=dag3,
)

task5c = DummyOperator(
    task_id='task5c',
    dag=dag3,
)

task1c >> task2c  >> [task3c, task4c] >> task5c
