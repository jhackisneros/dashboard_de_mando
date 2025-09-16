import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self):
        self.logic = PreCogLogic()

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico 3D por Distritos de Madrid")

        # --- Sliders para parámetros ---
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)
        viento = st.slider("Velocidad del viento (km/h)", 0, 100, 10)
        temperatura = st.slider("Temperatura (°C)", -10, 40, 20)
        humedad = st.slider("Humedad (%)", 0, 100, 50)

        # --- Generamos el GeoDataFrame con riesgo ---
        gdf = self.logic.generate_risk_map(velocidad, lluvia, viento, temperatura, humedad)

        # --- Mapa interactivo con Plotly ---
        fig = px.choropleth_mapbox(
            gdf,
            geojson=gdf.geometry,
            locations=gdf.index,
            color="riesgo",
            color_continuous_scale="RdYlGn_r",
            mapbox_style="carto-positron",
            center={"lat": 40.4168, "lon": -3.7038},
            zoom=10,
            opacity=0.6,
            hover_data={"name": True, "riesgo": True}
        )
        st.plotly_chart(fig, use_container_width=True)

        # --- Monitor de alertas robusto ---
        if "riesgo" in gdf.columns:
            riesgo = pd.to_numeric(gdf["riesgo"], errors='coerce').fillna(0)
            rojos = (riesgo > 70).sum()
            amarillos = ((riesgo > 40) & (riesgo <= 70)).sum()
            verdes = (riesgo <= 40).sum()
            st.info(f"⚠️ Alertas: 🔴 {rojos}  🟡 {amarillos}  🟢 {verdes}")
        else:
            st.warning("❌ La columna 'riesgo' no existe. Revisa la función generate_risk_map()")

        # --- Pronóstico de los próximos 7 días ---
        st.subheader("Pronóstico de riesgo para los próximos 7 días")
        days = pd.date_range(start=pd.Timestamp.today(), periods=7).strftime("%a %d/%m")
        forecast_data = []
        for _, row in gdf.iterrows():
            forecast_data.append({
                "Distrito": row['name'],
                **{day: np.clip(np.random.normal(row['riesgo'], 10), 0, 100) for day in days}
            })
        df_forecast = pd.DataFrame(forecast_data)
        st.dataframe(df_forecast.sort_values(by=days[-1], ascending=False))  # ordenar por último día

        # --- Tabla resumen ---
        st.subheader("Riesgo por distrito (actual)")
        st.dataframe(gdf[["name", "riesgo"]].sort_values(by="riesgo", ascending=False))
