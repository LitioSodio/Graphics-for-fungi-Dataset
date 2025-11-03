# ===============================================================
# ANÁLISIS DE REGISTROS DE Fusarium EN SUDAMÉRICA (GBIF)
# Autor: Lina Gómez Cardona
# Fecha: 2025
# Descripción:
# Este script realiza un análisis exploratorio de datos (EDA)
# sobre los registros del género Fusarium descargados de GBIF.
# Incluye visualizaciones: histograma, lineplot, boxplot,
# scatter plot y mapa geográfico con geopandas.
# ===============================================================

# -----------------------------
# 1. CARGA DE LIBRERÍAS
# -----------------------------
import zipfile
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx

# -----------------------------
# 2. EXTRACCIÓN DEL ARCHIVO ZIP Y CARGA DEL CSV
# -----------------------------
zip_path = "fusarium.zip"  # Ruta del archivo ZIP

# Descomprimir el contenido
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("fusarium")

# Ruta del CSV dentro del ZIP
csv_path = "fusarium/0044453-251009101135966.csv"

# Cargar el CSV como DataFrame
df = pd.read_csv(csv_path, sep="\t", low_memory=False)
print("Datos cargados correctamente:", df.shape, "filas")

# -----------------------------
# 3. HISTOGRAMA: Especies más frecuentes por país
# -----------------------------
top_paises = df['countryCode'].value_counts().head(5).index
df_top = df[df['countryCode'].isin(top_paises)]

# Top 3 especies por país
top_especies_por_pais = (
    df_top.groupby(['countryCode', 'species'])
    .size()
    .reset_index(name='conteo')
)
top3 = top_especies_por_pais.groupby('countryCode').apply(
    lambda x: x.nlargest(3, 'conteo')
).reset_index(drop=True)

# Gráfico
sns.set_palette("Set2")
plt.figure(figsize=(10, 6))
sns.barplot(data=top3, x='countryCode', y='conteo', hue='species')
plt.title('Tres especies de Fusarium más frecuentes por país en Sudamérica')
plt.xlabel('País')
plt.ylabel('Número de registros')
plt.legend(title='Especie')
plt.tight_layout()
plt.show()

# -----------------------------
# 4. LINEPLOT: Frecuencia de registros por país
# -----------------------------
registros_pais = df['countryCode'].value_counts().reset_index()
registros_pais.columns = ['countryCode', 'n_registros']
registros_pais = registros_pais.sort_values('n_registros', ascending=False)

sns.set(style="whitegrid", palette="Set2")
plt.figure(figsize=(10, 6))
sns.lineplot(data=registros_pais, x='countryCode', y='n_registros', marker='o')
plt.title('Frecuencia de registros de Fusarium por país (GBIF)')
plt.xlabel('Código de país')
plt.ylabel('Número de registros')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 5. BOXPLOT: Dispersión de registros por país
# -----------------------------
country_counts = df.groupby("countryCode")["gbifID"].count().reset_index()
country_counts.columns = ["country", "records"]

sns.set(style="whitegrid", palette="Set2")
plt.figure(figsize=(10, 6))
sns.boxplot(y=country_counts["records"], color="skyblue")
plt.title("Dispersión del número de registros por país", fontsize=13)
plt.ylabel("Número de registros (por país)")
plt.tight_layout()
plt.show()

# -----------------------------
# 6. SCATTER PLOT: Distribución geográfica
# -----------------------------
sns.set(style="whitegrid", palette="Set2")
plt.figure(figsize=(10, 8))
sns.scatterplot(
    data=df,
    x='decimalLongitude',
    y='decimalLatitude',
    hue='countryCode',
    alpha=0.6,
    edgecolor=None
)
plt.title('Distribución geográfica de registros de Fusarium en Sudamérica')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.legend(title='País', bbox_to_anchor=(1.0, 0.9), loc='upper left')
plt.tight_layout()
plt.show()

# -----------------------------
# 7. MAPA GEOGRÁFICO CON GEOPANDAS
# -----------------------------
# Eliminar coordenadas vacías
df = df.dropna(subset=["decimalLatitude", "decimalLongitude"])

# Crear GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["decimalLongitude"], df["decimalLatitude"]),
    crs="EPSG:4326"
)

# Convertir proyección
gdf = gdf.to_crs(epsg=3857)

# Crear figura
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, alpha=0.5, markersize=10, color="red", label="Registros de Fusarium")

# Agregar mapa base (CartoDB)
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

# Ajustar límites de Sudamérica
ax.set_xlim([-9000000, -3500000])
ax.set_ylim([-6000000, 1500000])
ax.set_title("Distribución geográfica de registros de Fusarium en Sudamérica", fontsize=13)
ax.legend()
plt.tight_layout()
plt.show()
