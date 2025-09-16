import geopandas as gpd
import numpy as np

class PreCogLogic:
    def __init__(self):
        # Cargar directamente los distritos de Madrid desde GeoJSON online
        url = "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/madrid-districts.geojson"
        self.gdf = gpd.read_file(url)

    def generate_risk_map(self, velocidad, lluvia, viento, temperatura, humedad):
        """
        Calcula un nivel de riesgo para cada distrito de Madrid
        usando una fórmula de ejemplo.
        Devuelve un GeoDataFrame con una columna 'riesgo' añadida.
        """
        df = self.gdf.copy()

        # Fórmula de ejemplo de riesgo (puedes mejorarla según datos reales)
        riesgo = (
            0.4 * velocidad/200 * 100 +
            0.3 * lluvia/100 * 100 +
            0.1 * viento/100 * 100 +
            0.1 * (40-temperatura)/40 * 100 +  # temperatura baja aumenta riesgo
            0.1 * humedad/100 * 100
        )

        # Añadimos ruido aleatorio para simular variabilidad por distrito
        riesgo += np.random.randn(len(df)) * 5
        riesgo = np.clip(riesgo, 0, 100)  # limitar entre 0-100%
        df["riesgo"] = riesgo

        return df
