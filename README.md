# Pipeline ETL Automatizado con GCP

Este proyecto implementa un pipeline ETL utilizando herramientas de Google Cloud Platform como Airflow, Cloud Storage y BigQuery. Permite procesar y transformar grandes volúmenes de datos mediante flujos automatizados.

## Estructura del proyecto
- `dags/`: Contiene los DAGs de Airflow.
  - `sales_pipelines_dag.py`: DAG que sube datos a GCS y los carga en BigQuery.
- `data/`: Archivos de datos utilizados en el proyecto (por ejemplo, `ventas.csv`).
- `scripts/`: Scripts auxiliares como `validador.py`.
- `.gitignore`: Define los archivos y carpetas ignorados por Git.
- `docker-compose.yaml`: Configuración para desplegar los servicios necesarios con Docker.
- `.env`: Archivo con variables de entorno sensibles (no se sube al repositorio).

## Requisitos
- **Python 3.8+**
- Librerías Python necesarias:
  - pandas
  - apache-airflow
  - google-cloud-storage
  - google-cloud-bigquery
- Herramientas configuradas en Google Cloud Platform:
  - Google Cloud Storage
  - BigQuery
  - Composer (Airflow)

## Cómo usar
1. Sube el archivo CSV `ventas.csv` a la carpeta `data/`.
2. Configura las credenciales de GCP en el entorno de Airflow:
   - Asegúrate de tener un archivo `credentials.json` válido y de mapearlo correctamente en tu contenedor de Docker.
3. Activa el DAG `sales_pipeline` en la interfaz de Airflow.
4. Monitorea el progreso del DAG en la interfaz para confirmar que:
   - El archivo `ventas.csv` se sube a GCS.
   - Los datos se cargan correctamente en BigQuery.

## Configuración del entorno
1. Clona el repositorio:
   ```bash
   git clone https://github.com/nachogallegos/Pipeline-ETL-GCP.git
   cd Pipeline-ETL-GCP
 
 ## Próximos pasos

  - Implementar notificaciones por correo en caso de fallos en el DAG.
  - Optimizar el rendimiento del pipeline para manejar grandes volúmenes de datos.
  - Añadir pruebas unitarias para las funciones Python en el DA