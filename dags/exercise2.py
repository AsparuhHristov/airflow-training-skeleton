from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(10),
}

dag = DAG(
    dag_id='exercise2',
    default_args=args,
    schedule_interval='@daily',
)

task1 = DummyOperator(
    task_id='task1',
    dag=dag,
)

task2 = DummyOperator(
    task_id='task2',
    dag=dag,
)

task3 = DummyOperator(
    task_id='task3',
    dag=dag,
)

task4 = DummyOperator(
    task_id='task4',
    dag=dag,
)

task5 = DummyOperator(
    task_id='task5',
    dag=dag,
)

task1 >> task2  >> [task3, task4] >> task5

dag2 = DAG(
    dag_id='exercise2b',
    default_args=args,
    schedule_interval='45 13 * * 1,3,5',
)

task1b = DummyOperator(
    task_id='task1b',
    dag=dag2,
)

task2b = DummyOperator(
    task_id='task2b',
    dag=dag2,
)

task3b = DummyOperator(
    task_id='task3b',
    dag=dag2,
)

task4b = DummyOperator(
    task_id='task4b',
    dag=dag2,
)

task5b = DummyOperator(
    task_id='task5b',
    dag=dag2,
)

task1b >> task2b  >> [task3b, task4b] >> task5b

# dag3 = DAG(
#     dag_id='exercise2c',
#     default_args=args,
#     schedule_interval='@daily',
# )
#
# task1c = DummyOperator(
#     task_id='task1c',
#     dag=dag3,
# )
#
# task2c = DummyOperator(
#     task_id='task2c',
#     dag=dag3,
# )
#
# task3c = DummyOperator(
#     task_id='task3c',
#     dag=dag3,
# )
#
# task4c = DummyOperator(
#     task_id='task4c',
#     dag=dag3,
# )
#
# task5c = DummyOperator(
#     task_id='task5c',
#     dag=dag3,
# )
#
# task1c >> task2c  >> [task3c, task4c] >> task5c
