import geopandas as gpd

# Usamos un dataset público de GeoPandas y lo filtramos a Madrid
# Fuente: cartografía de distritos del Instituto Geográfico Nacional
# (GeoPandas ya sabe leer directamente de la URL)
url = "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/madrid-districts.geojson"

# Cargar el GeoJSON desde la URL
gdf = gpd.read_file(url)

# Guardar en tu carpeta data/
output_path = "data/distritos_madrid.geojson"
gdf.to_file(output_path, driver="GeoJSON")

print(f"✅ Archivo creado correctamente en {output_path}")
print("Distritos disponibles:", gdf["name"].unique())
