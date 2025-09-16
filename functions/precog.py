import geopandas as gpd
import numpy as np

class PreCogLogic:
    def __init__(self, geojson_path="data/distritos_madrid.geojson"):
        try:
            self.gdf = gpd.read_file(geojson_path)
        except Exception as e:
            raise RuntimeError(f"No se pudo cargar el archivo GeoJSON: {e}")

    def calcular_riesgo_distritos(self, velocidad, lluvia, viento, temperatura, humedad):
        distritos = []
        riesgos = []

        for _, row in self.gdf.iterrows():
            base_riesgo = (
                (velocidad * 0.3) +
                (lluvia * 0.25) +
                (viento * 0.2) +
                (temperatura * 0.15) +
                (humedad * 0.1)
            )
            ruido = np.random.uniform(-10, 10)
            riesgo = max(0, min(100, base_riesgo + ruido))

            distritos.append(row["NOMBRE"])  # El campo se llama así en el GeoJSON
            riesgos.append(riesgo)

        return distritos, riesgos, self.gdf
