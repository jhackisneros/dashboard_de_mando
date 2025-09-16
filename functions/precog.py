import geopandas as gpd
import numpy as np
import requests

class PreCogLogic:
    def __init__(self, geojson_url=None, weather_api_key=None):
        # Cargar GeoJSON de distritos de Madrid
        self.gdf = gpd.read_file(
            geojson_url or "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/madrid-districts.geojson"
        )
        self.weather_api_key = weather_api_key

    def fetch_weather(self):
        """Obtiene datos meteorológicos en tiempo real de Madrid"""
        if not self.weather_api_key:
            # Si no hay API key, devolvemos valores por defecto
            return {"temperatura": 20, "humedad": 50, "viento": 10, "lluvia": 0}

        url = f"http://api.openweathermap.org/data/2.5/weather?q=Madrid,ES&units=metric&appid={self.weather_api_key}"
        res = requests.get(url).json()
        temperatura = res["main"]["temp"]
        humedad = res["main"]["humidity"]
        viento = res["wind"]["speed"]
        lluvia = res.get("rain", {}).get("1h", 0)
        return {"temperatura": temperatura, "humedad": humedad, "viento": viento, "lluvia": lluvia}

    def generate_risk_map(self, velocidad=50, lluvia=None, viento=None, temperatura=None, humedad=None):
        """
        Calcula un nivel de riesgo por distrito usando datos en vivo si se proporcionan.
        """
        df = self.gdf.copy()

        # Si no se proporcionan datos, traemos en vivo
        weather = self.fetch_weather()
        temperatura = temperatura if temperatura is not None else weather["temperatura"]
        humedad = humedad if humedad is not None else weather["humedad"]
        viento = viento if viento is not None else weather["viento"]
        lluvia = lluvia if lluvia is not None else weather["lluvia"]

        # Riesgo basado en fórmula
        riesgo = (
            0.4 * velocidad/200 * 100 +
            0.3 * lluvia/100 * 100 +
            0.1 * viento/100 * 100 +
            0.1 * (40-temperatura)/40 * 100 +
            0.1 * humedad/100 * 100
        )

        # Ruido aleatorio por distrito
        riesgo += np.random.randn(len(df)) * 5
        riesgo = np.clip(riesgo, 0, 100)
        df["riesgo"] = riesgo

        # Añadimos riesgo simulado de tráfico por distrito (0-100)
        df["trafico"] = np.clip(np.random.normal(50, 15, len(df)), 0, 100)

        return df
