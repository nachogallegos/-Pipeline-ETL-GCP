# Proyecto 1: Pipeline ETL Automatizado con GCP

## Descripción
Este proyecto implementa un pipeline ETL (Extracción, Transformación y Carga) automatizado utilizando Google Cloud Platform (GCP). El pipeline procesa datos desde un dataset externo (FIFA 2021), los valida y limpia, y los carga en BigQuery para su posterior análisis. El flujo está gestionado por Apache Airflow, que orquesta todas las tareas del pipeline a través de un DAG (Directed Acyclic Graph).

## Objetivos
1. Diseñar un pipeline ETL eficiente y escalable.
2. Automatizar el pipeline mediante Apache Airflow.
3. Implementar alertas por correo en caso de fallos.
4. Manejar datos transformados y almacenarlos en BigQuery.
5. Cargar datos procesados en BigQuery para análisis avanzado.
6. Implementar validaciones y limpieza de datos.
7. Crear dashboards

## Tecnologías utilizadas
- **Google Cloud Platform**
  - Google Cloud Storage (GCS)
  - BigQuery
  - Cloud Composer (Apache Airflow gestionado)
- **Python**
  - Bibliotecas: pandas, google-cloud-storage, google-cloud-bigquery
- **Apache Airflow**
- **Git/GitHub** para control de versiones y CI/CD
- **Looker Studio** para creacion de dashboards

## Dataset Procesado
El proyecto utiliza el dataset de FIFA 2021, que incluye información de jugadores como:
- ID del jugador
- Nombre
- Nacionalidad
- Posición
- Valoración general (overall)
- Potencial (potential)
- Edad
- Equipo

- Antes de ser procesado por el pipeline, el dataset es validado y limpiado mediante un script de Python (“validador_fifa.py”). Esto incluye:
    Eliminación de filas duplicadas.
    Verificación de valores nulos y rangos esperados.
    Validación de posiciones y columnas importantes

## Resumen del proyecto
1. Configuración de Cloud Composer para gestionar los DAGs.
2. Creación de un DAG que realiza las siguientes tareas:
   - Extracción de datos desde un archivo CSV local.
   - Validación y limpieza de los datos utilizando un script en Python (validador).
   - Transformación de los datos para cumplir con el esquema de BigQuery.
   - Subida del archivo limpio a Google Cloud Storage.
   - Carga de los datos transformados en BigQuery.
3. Implementación de notificaciones por correo en caso de fallos en los DAGs.
4. Configuración de un pipeline CI/CD en GitHub Actions para pruebas automatizadas.
5. Creacion de Dashboard con Looker Studio
6. Subida de los avances del proyecto al repositorio de GitHub.

## Consultas Avanzadas en BigQuery
Se implementaron consultas avanzadas para analizar los datos procesados, incluyendo:
1. Top 5 jugadores con mayor potencial por nacionalidad.
2. Distribución de jugadores por posición y promedio de "overall".
3. Equipos con el mayor promedio de "overall".
4. Edad promedio, mínima y máxima de jugadores por posición.
5. Relación entre "overall" y "potential" para identificar diferencias por posición.

## Notificaciones por correo
El pipeline incluye notificaciones automáticas por correo en caso de fallos en los DAGs:
- Los correos detallan el error, la tarea afectada y el DAG correspondiente.
- Configuración: Se utilizó el servicio SMTP para enviar los correos desde Airflow.

## Pruebas automatizadas
- El proyecto incluye pruebas unitarias para validar el comportamiento del script “validador_fifa.py”:
- Verificación de valores válidos e inválidos en columnas críticas como "age", "overall" y "position".
- Simulación de la conexión a Google Cloud Storage (GCS) para evitar dependencias externas durante las pruebas.
- Configuración de un pipeline CI/CD en GitHub Actions para ejecutar las pruebas automáticamente en cada cambio.

## Cómo ejecutar este proyecto
1. Clona este repositorio:
   ```bash
   git clone <url-del-repositorio>
   ```
2. Coloca el dataset original (FIFA-21 Complete.csv) en la carpeta `data/`.
3. Ejecuta el script `validador_fifa.py` para validar y limpiar los datos:
   ```bash
   python validador_fifa.py
   ```
4. Sube los archivos del DAG al entorno de Cloud Composer o Airflow local.
5. Configura las credenciales de GCP necesarias para el acceso a BigQuery y GCS.
6. Activa el DAG desde la interfaz web de Airflow.
7. Supervisa la ejecución y revisa los logs en caso de errores.