# Proyecto 1: Pipeline ETL Automatizado con GCP

## Descripción
Este proyecto implementa un pipeline ETL (Extracción, Transformación y Carga) automatizado utilizando Google Cloud Platform (GCP). El pipeline procesa datos desde una fuente externa y los carga en BigQuery para su posterior análisis. El flujo está gestionado por Apache Airflow, utilizando un DAG para orquestar las tareas.

## Objetivos
1. Diseñar un pipeline ETL eficiente y escalable.
2. Automatizar el pipeline mediante Apache Airflow.
3. Implementar alertas por correo en caso de fallos.
4. Manejar datos transformados y almacenarlos en BigQuery.

## Tecnologías utilizadas
- **Google Cloud Platform**
  - Google Cloud Storage (GCS)
  - BigQuery
  - Cloud Composer (Apache Airflow gestionado)
- **Python**
  - Bibliotecas: pandas, requests, google-cloud-storage, google-cloud-bigquery
- **Apache Airflow**
- **Git/GitHub** para control de versiones

## Progreso actual
1. Configuración de Cloud Composer para gestionar los DAGs.
2. Creación de un DAG que realiza las siguientes tareas:
   - Extracción de datos desde una fuente externa (CSV/API).
   - Transformación de los datos utilizando scripts en Python.
   - Carga de los datos transformados en BigQuery.
3. **Implementación de notificaciones por correo en caso de fallos en los DAGs.**
4. Subida de los avances del proyecto al repositorio de GitHub.

## Próximos pasos
- Optimizar el rendimiento del pipeline para manejar grandes volúmenes de datos.
- Añadir pruebas unitarias para las funciones Python en el DAG.

## Notificaciones por correo
El pipeline ahora incluye notificaciones por correo en caso de fallos en los DAGs:
- Las notificaciones envían un email detallando el error y las tareas afectadas.
- Configuración: El correo está configurado en la sección `email` del DAG utilizando las opciones SMTP de Airflow.

## Cómo ejecutar este proyecto
1. Clona este repositorio:
   ```bash
   git clone <url-del-repositorio>
   ```
2. Sube los archivos del DAG al entorno de Cloud Composer.
3. Configura las credenciales de GCP necesarias para el acceso a BigQuery y GCS.
4. Activa el DAG desde la interfaz web de Airflow.
5. Supervisa la ejecución y revisa los logs en caso de errores.