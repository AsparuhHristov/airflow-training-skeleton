import random

import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from datetime import datetime, timedelta

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='exercise5',
    default_args=args,
    schedule_interval="@daily",
)

def print_weekday(**context):
    week_day = context['execution_date'].weekday()
    print(week_day)
    return week_day


print_weekday = PythonOperator(
    task_id='print_weekday',
    provide_context=True,
    python_callable=print_weekday,
    dag=dag)

options = ['branch_a', 'branch_b', 'branch_c', 'branch_d']

branching = BranchPythonOperator(
    task_id='branching',
    python_callable=lambda: random.choice(options),
    dag=dag,
)
print_weekday >> branching

join = DummyOperator(
    task_id='join',
    trigger_rule='one_success',
    dag=dag,
)

for option in options:
    t = DummyOperator(
        task_id=option,
        dag=dag,
    )

    dummy_follow = DummyOperator(
        task_id='follow_' + option,
        dag=dag,
    )

    branching >> t >> dummy_follow >> join
# import airflow
# from airflow.models import DAG
# from airflow.operators.bash_operator import BashOperator
# from airflow.operators.dummy_operator import DummyOperator
# from airflow.operators.python_operator import PythonOperator
# from airflow.operators.python_operator import BranchPythonOperator
# from datetime import datetime, timedelta
#
# args = {
#     'owner': 'Airflow',
#     'start_date': airflow.utils.dates.days_ago(2),
# }
#
# dag = DAG(
#     dag_id='exercise5',
#     default_args=args,
#     schedule_interval=None,
# )
#
# def print_weekday(**context):
#     week_day = context['execution_date'].weekday()
#     print(week_day)
#     return week_day
#
#
# t1 = PythonOperator(
#     task_id='print_weekday',
#     provide_context=True,
#     python_callable=print_weekday,
#     dag=dag)
#
# branching = BranchPythonOperator(
#         task_id='branching',
#         python_callable=print_weekday,
#         provide_context=True)
#
# t1 >> branching
#
# final_task = DummyOperator(
#     task_id='final_task',
#     trigger_rule='one_success',
#     dag=dag)
#
# for i in range(0, 6):
#     email = DummyOperator(task_id='branch_{i}')
#
#     branching >> email >> final_task