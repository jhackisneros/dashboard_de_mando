# functions/precog.py
import geopandas as gpd
import numpy as np

class PreCogLogic:
    def __init__(self):
        # Cargar los distritos de Madrid desde GeoJSON
        url = "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/madrid-districts.geojson"
        self.gdf = gpd.read_file(url)
        # Inicializar una columna de riesgo
        self.gdf['riesgo'] = 0.0

    def generate_risk_map(self, velocidad, lluvia, viento, temperatura, humedad):
        """
        Calcula un riesgo simulado por distrito usando los parámetros.
        Retorna el GeoDataFrame con la columna 'riesgo' actualizada.
        """
        # Función simple de riesgo basado en los parámetros
        for idx, row in self.gdf.iterrows():
            riesgo = (
                velocidad * 0.2 +
                lluvia * 0.3 +
                viento * 0.2 +
                max(0, 25 - temperatura) * 0.1 +
                humedad * 0.2
            )
            riesgo += np.random.normal(0, 5)  # Aleatoriedad
            self.gdf.at[idx, 'riesgo'] = np.clip(riesgo, 0, 100)

        return self.gdf
