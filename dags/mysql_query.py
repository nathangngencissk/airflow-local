from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2020, 1, 1),
    'owner': 'Airflow',
    'email': 'owner@test.com'
}

with DAG(dag_id='mysql_query', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:
    
    query  = 'select * from employees'
    
    task = MySqlOperator(
            task_id='run_sql',
            sql= query,
            mysql_conn_id='mysql_con',
            dag=dag)
        