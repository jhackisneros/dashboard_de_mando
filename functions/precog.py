# functions/precog.py
import numpy as np
import geopandas as gpd

class PreCogLogic:
    def __init__(self, shapefile_path="data/Distritos.shp"):
        # Cargar los distritos de Madrid
        self.gdf = gpd.read_file(shapefile_path)
        # Inicializamos el nivel de riesgo por distrito
        self.gdf["nivel_riesgo"] = 0

    def generate_risk_map(self, velocidad, lluvia, viento, temperatura, humedad):
        """
        Genera el nivel de riesgo para cada distrito usando los factores:
        velocidad, lluvia, viento, temperatura y humedad.
        """
        # Generar riesgo aleatorio base
        riesgo_base = np.random.rand(len(self.gdf)) * 30

        # Ajustar riesgo según factores (simple ejemplo)
        riesgo = riesgo_base + (velocidad + lluvia + viento) / 10 + (humedad / 5) + (temperatura / 20)
        riesgo = np.clip(riesgo, 0, 100)  # Limitar entre 0 y 100

        self.gdf["nivel_riesgo"] = riesgo

        # Calcular colores: rojo = alto riesgo, verde = bajo
        self.gdf["color"] = self.gdf["nivel_riesgo"].apply(lambda x: f"rgb({int(x*2.55)}, {int((100-x)*2.55)}, 0)")

        # Retornar GeoDataFrame con nivel de riesgo y color
        return self.gdf

    def get_alerts(self, umbral_rojo=70, umbral_amarillo=40):
        """
        Genera alertas por cantidad de distritos rojos, amarillos y verdes.
        """
        rojos = (self.gdf["nivel_riesgo"] >= umbral_rojo).sum()
        amarillos = ((self.gdf["nivel_riesgo"] >= umbral_amarillo) & (self.gdf["nivel_riesgo"] < umbral_rojo)).sum()
        verdes = (self.gdf["nivel_riesgo"] < umbral_amarillo).sum()
        return {"rojos": int(rojos), "amarillos": int(amarillos), "verdes": int(verdes)}
