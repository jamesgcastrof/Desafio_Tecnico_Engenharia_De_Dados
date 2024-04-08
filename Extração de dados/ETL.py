from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 8),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_newsapi',
    default_args=default_args,
    description='Extrai noticias relacionadas a uma palavra chave',
    schedule_interval=timedelta(hours=1),  # Executar uma vez por hora
)

# Definindo as tarefas
extract_task = BashOperator(
    task_id='extrair_dados',
    bash_command='~/extract.py',
    dag=dag,
)

transform_task = BashOperator(
    task_id='transformar_dados',
    bash_command='~/transform.py',
    dag=dag,
    schedule_interval=timedelta(days=1),  # Executar uma vez por dia
)

# Definindo a ordem das tarefas
extract_task >> transform_task
