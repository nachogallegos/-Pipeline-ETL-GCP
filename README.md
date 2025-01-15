# Pipeline ETL Automatizado con GCP

Este proyecto implementa un pipeline ETL utilizando herramientas de Google Cloud Platform como Airflow, Cloud Storage y BigQuery. Permite procesar y transformar grandes volúmenes de datos mediante flujos automatizados.

## Estructura del proyecto
- `dags/`: Contiene los DAGs de Airflow.
- `data/`: Archivos de datos utilizados en el proyecto (por ejemplo, `ventas.csv`).
- `scripts/`: Scripts auxiliares como `validador.py` para validaciones y pruebas.
- `.gitignore`: Define los archivos y carpetas ignorados por Git.

## Requisitos
- **Python 3.8+**
- Librerías:
  - pandas
- Herramientas configuradas en Google Cloud Platform:
  - Google Cloud Storage
  - BigQuery
  - Composer (Airflow)

## Cómo usar
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/nachogallegos/-Pipeline-ETL-GCP.git

2. Instalar las dependencias necesarias:

    pip install -r requirements.txt

3. Configurar las credenciales de GCP si es necesario.
    Ejecutar el script de validación:

        python scripts/validador.py

## Próximos pasos

    -- Completar la conexión entre las etapas del pipeline ETL.
    -- Optimizar el rendimiento para grandes volúmenes de datos.
    -- Agregar pruebas unitarias para los scripts.