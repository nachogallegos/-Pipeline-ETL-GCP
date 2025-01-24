from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from google.cloud import storage
from google.cloud import bigquery

# Función para enviar correos en caso de fallo
def send_failure_email(context):
    task_instance = context.get("task_instance")
    exception = context.get("exception")
    subject = f"Fallo en el DAG {task_instance.dag_id}"
    body = f"""
    <p>El DAG <b>{task_instance.dag_id}</b> ha fallado.</p>
    <p>Tarea: <b>{task_instance.task_id}</b></p>
    <p>Detalles: {exception}</p>
    """
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = "tucorreo@gmail.com"
    msg["To"] = "tucorreo@gmail.com"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("tucorreo@gmail.com", "tuclave")
            server.send_message(msg)
        print("Correo de fallo enviado con éxito")
    except Exception as e:
        print(f"Error al enviar correo: {e}")

# Función para subir datos a GCS
def upload_to_gcs():
    client = storage.Client()
    bucket = client.bucket("pipelines-datos-auto")
    blob = bucket.blob("raw/fifa_2021_cleaned.csv")
    blob.upload_from_filename("/opt/airflow/data/FIFA-21 Complete Cleaned.csv")
    print("Archivo limpio subido a GCS")

# Función para cargar datos en BigQuery
def load_to_bigquery():
    client = bigquery.Client()
    table_id = "pipeline-de-datos-automatizado.fifa_dataset.players"
    schema = [
        bigquery.SchemaField("player_id", "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField("name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("nationality", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("position", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("overall", "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField("age", "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField("hits", "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField("potential", "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField("team", "STRING", mode="NULLABLE"),
    ]
    job_config = bigquery.LoadJobConfig(
        schema=schema,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        field_delimiter=";",  # Especificar el separador correcto
        max_bad_records=100,  # Tolerar hasta 100 errores menores
    )
    uri = "gs://pipelines-datos-auto/raw/fifa_2021_cleaned.csv"
    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()
    print("Datos FIFA cargados en BigQuery")

# Configuración del DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
    "email_on_failure": False,
    "email_on_retry": False,
    "on_failure_callback": send_failure_email,
}

with DAG(
    "fifa_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    # Tarea para subir datos a GCS
    upload_task = PythonOperator(
        task_id="upload_to_gcs",
        python_callable=upload_to_gcs,
    )

    # Tarea para cargar datos en BigQuery
    load_task = PythonOperator(
        task_id="load_to_bigquery",
        python_callable=load_to_bigquery,
    )

    upload_task >> load_task