from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from google.cloud import storage
from google.cloud import bigquery

# Función para subir datos a GCS
def upload_to_gcs():
    client = storage.Client()
    bucket = client.bucket("pipelines-datos-auto")
    blob = bucket.blob("raw/ventas.csv")
    blob.upload_from_filename("/opt/airflow/data/ventas.csv")
    print("Archivo subido a GCS")

# Función para cargar datos en BigQuery
def load_to_bigquery():
    client = bigquery.Client()
    table_id = "pipeline-de-datos-automatizado.sales_dataset.ventas"
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )
    uri = "gs://pipelines-datos-auto/raw/ventas.csv"
    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()
    print("Datos cargados en BigQuery")

# Definir el DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
    "email_on_failure": True,
    "email_on_retry": False,
    "email":["ig7steam@gmail.com"], # Reemplaza con tu correo
}

with DAG(
    "sales_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:
    upload_task = PythonOperator(
        task_id="upload_to_gcs",
        python_callable=upload_to_gcs,
    )

    load_task = PythonOperator(
        task_id="load_to_bigquery",
        python_callable=load_to_bigquery,
    )

    upload_task >> load_task
