import numpy as np
import geopandas as gpd

class PreCogLogic:
    def __init__(self, geojson_path="data/distritos_madrid.geojson"):
        # Cargar los distritos de Madrid
        self.gdf = gpd.read_file(geojson_path)
    
    def generate_risk_map(self, velocidad, lluvia, viento, temperatura, humedad):
        """
        Genera un mapa de riesgo simulado para cada distrito.
        Retorna:
        - nombres de distritos
        - valores de riesgo (0-100)
        - colores asociados
        """
        distritos = self.gdf["name"].tolist()
        num_distritos = len(distritos)

        # Generar valores de riesgo aleatorios basados en los parámetros
        z = np.random.rand(num_distritos) * 50 + (velocidad + lluvia + viento + temperatura + humedad) / 5
        z = np.clip(z, 0, 100)

        # Asignar colores según nivel de riesgo
        color = []
        for val in z:
            if val > 70:
                color.append("red")
            elif val > 40:
                color.append("yellow")
            else:
                color.append("green")

        return distritos, z, color
