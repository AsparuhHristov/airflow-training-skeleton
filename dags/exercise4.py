import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='exercise3',
    default_args=args,
    schedule_interval=None,
)

def print_execution_date(**context):
    print('The execution date is ', str(context['execution_date']))
    return

t1 = PythonOperator(
    task_id='print_execution_date',
    provide_context=True,
    python_callable=print_execution_date,
    dag=dag)

for i in [1,5,10]:
    wait = BashOperator(
        task_id='wait_{i}',
        depends_on_past=False,
        bash_command='sleep {i}',
        dag=dag)

t5 = DummyOperator(
    task_id='the_end',
    dag=dag,
)


t1 >> wait >> t5