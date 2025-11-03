Análisis de registros de Fusarium en Sudamérica

Este proyecto hace un análisis exploratorio de los registros del género Fusarium descargados desde GBIF (Global Biodiversity Information Facility).
El análisis incluye la carga, limpieza, visualización y mapeo geográfico de los datos para observar patrones de distribución y abundancia por país.

📂 Contenido del repositorio
├── fusarium.zip                  # Archivo original descargado de GBIF
├── Code.py                       # Script principal con todo el análisis
├── README.md                     # Este archivo

⚙️ Requisitos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes librerías de Python:

pip install pandas seaborn matplotlib geopandas contextily


💡 Se recomienda usar un entorno virtual (venv) o Conda para aislar dependencias.

🚀 Ejecución del script

Coloca el archivo fusarium.zip (descargado desde GBIF) en la misma carpeta del script.

Ejecuta el archivo principal:

python Convertir_a_tsv_y_analisis.py


El script realizará automáticamente:

La extracción del archivo .zip.

La lectura del CSV de GBIF.

La limpieza básica de los datos.

La generación de varios gráficos.

Gráficos generados

Histograma:
Muestra las tres especies de Fusarium más frecuentes por país.
Permite comparar cuáles especies son más reportadas.

Línea de frecuencia:
Representa el número total de registros por país, mostrando las diferencias de abundancia entre países.

Boxplot:
Visualiza la dispersión y variabilidad del número de registros por país.
Los puntos fuera del rango (outliers) indican países con muchos más registros que el promedio.

Gráfico de dispersión (scatter plot):
Representa la distribución de las coordenadas geográficas (latitud y longitud) de los registros.

Mapa geográfico:
Usa GeoPandas y Contextily para mostrar los puntos de presencia de Fusarium sobre un mapa base de Sudamérica.

Interpretación general

El conjunto de datos evidencia una concentración desigual de registros por país:
algunos (como Brasil o Colombia) presentan muchos más datos, mientras otros muestran registros escasos.
Esto puede reflejar tanto mayor esfuerzo de muestreo como condiciones ambientales favorables para el género Fusarium.

🧑‍💻 Autor

Lina Gómez Cardona
Proyecto para el curso de Programación para Ciencias Biológicas
Universidad [nombre de tu universidad] — 2025
