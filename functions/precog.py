import numpy as np
import geopandas as gpd

class PreCogLogic:
    def __init__(self, geojson_path="data/distritos_madrid.geojson"):
        # Cargar distritos de Madrid
        self.gdf = gpd.read_file(geojson_path)
    
    def generate_risk_map(self, velocidad, lluvia, viento, temperatura, humedad):
        """
        Genera un "mapa de riesgo" simplificado por distrito.
        """
        distritos = self.gdf["name"].values
        num_distritos = len(distritos)

        # Simulación de riesgo por distrito
        z = np.random.rand(num_distritos) * 50
        z += (velocidad + lluvia + viento)/5
        z = np.clip(z, 0, 100)

        # Determinar color según nivel de riesgo
        color = []
        for val in z:
            if val > 66:
                color.append("rojo")
            elif val > 33:
                color.append("amarillo")
            else:
                color.append("verde")

        # Contar niveles de riesgo
        resumen = {
            "rojo": color.count("rojo"),
            "amarillo": color.count("amarillo"),
            "verde": color.count("verde")
        }

        return distritos, z, color, resumen
