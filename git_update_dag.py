from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


# Default settings applied to all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('git_update_dag',
         start_date=datetime(2022, 1, 1),
         schedule_interval=None,  # https://airflow.apache.org/docs/stable/scheduler.html#dag-runs
         default_args=default_args,
         catchup=False # enable if you don't want historical dag runs to run
         ) as dag:
    
    BashOperator(
        task_id='git_pull_change',
        bash_command='git pull'
    )