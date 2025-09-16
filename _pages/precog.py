import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self, weather_api_key=None):
        self.logic = PreCogLogic(weather_api_key=weather_api_key)

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico en Madrid (En Vivo)")

        # --- Sliders opcionales ---
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)

        # --- Generar datos ---
        gdf = self.logic.generate_risk_map(velocidad=velocidad)

        # --- Mapa de riesgo por distrito ---
        fig_map = px.choropleth_mapbox(
            gdf,
            geojson=gdf.geometry,
            locations=gdf.index,
            color="riesgo",
            color_continuous_scale="RdYlGn_r",
            mapbox_style="carto-positron",
            center={"lat": 40.4168, "lon": -3.7038},
            zoom=10,
            opacity=0.6,
            hover_data={"name": True, "riesgo": True, "trafico": True}
        )
        st.plotly_chart(fig_map, use_container_width=True)

        # --- Monitor de alertas ---
        rojos = (gdf["riesgo"] > 70).sum()
        amarillos = ((gdf["riesgo"] > 40) & (gdf["riesgo"] <= 70)).sum()
        verdes = (gdf["riesgo"] <= 40).sum()
        st.info(f"⚠️ Alertas: 🔴 {rojos}  🟡 {amarillos}  🟢 {verdes}")

        # --- Pronóstico simulado 7 días ---
        st.subheader("Pronóstico semanal por distrito")
        days = pd.date_range(start=pd.Timestamp.today(), periods=7).strftime("%a %d/%m")
        forecast_data = []
        for _, row in gdf.iterrows():
            forecast_data.append({
                "Distrito": row["name"],
                **{day: np.clip(np.random.normal(row["riesgo"], 10), 0, 100) for day in days}
            })
        df_forecast = pd.DataFrame(forecast_data)
        st.dataframe(df_forecast)
