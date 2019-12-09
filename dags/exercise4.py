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
    task_id='t1',
    provide_context=True,
    python_callable=print_execution_date,
    dag=dag)

t2 = BashOperator(
    task_id='wait_5',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag)

t3 = BashOperator(
    task_id='wait_1',
    depends_on_past=False,
    bash_command='sleep 1',
    dag=dag)

t4 = BashOperator(
    task_id='wait_10',
    depends_on_past=False,
    bash_command='sleep 10',
    dag=dag)

t5 = DummyOperator(
    task_id='t5',
    dag=dag,
)


t1 >> [t2, t3, t4] >> t5