from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "manikanta",
    "start_date": datetime(2025, 1, 1),
}

with DAG(
    dag_id="weather_etl_pipeline",
    default_args=default_args,
    schedule="@hourly",
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract_weather",
        bash_command="cd ~/Desktop/weather_ETL_pipeline && python3 scripts/extract.py"
    )

    transform = BashOperator(
    task_id="transform_weather",
    bash_command="cd ~/Desktop/weather_ETL_pipeline && python3 scripts/transform.py"
)

    load = BashOperator(
    task_id="load_weather",
    bash_command="cd ~/Desktop/weather_ETL_pipeline && python3 scripts/load.py"
)

    extract >> transform >> load 