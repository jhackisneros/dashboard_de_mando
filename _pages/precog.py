import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self):
        self.logic = PreCogLogic()

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico por Distrito")

        # --- Sliders ---
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)
        viento = st.slider("Velocidad del viento (km/h)", 0, 100, 10)
        temperatura = st.slider("Temperatura (°C)", -10, 40, 20)
        humedad = st.slider("Humedad (%)", 0, 100, 50)

        # --- Cálculo de riesgo ---
        gdf = self.logic.generate_risk_map(velocidad, lluvia, viento, temperatura, humedad)

        # --- Mapa de calor por distrito ---
        fig_map = px.choropleth(
            gdf,
            geojson=gdf.geometry,
            locations=gdf.index,
            color="riesgo",
            color_continuous_scale="RdYlGn_r",
            range_color=(0, 100),
            hover_name="name",
            labels={"riesgo": "Nivel de Riesgo (%)"}
        )
        fig_map.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig_map, use_container_width=True)

        # --- Monitor de alertas ---
        rojos = (gdf['riesgo'] > 70).sum()
        amarillos = ((gdf['riesgo'] >= 40) & (gdf['riesgo'] <= 70)).sum()
        verdes = (gdf['riesgo'] < 40).sum()
        st.info(f"⚠️ Alertas por distrito: 🔴 {rojos}  🟡 {amarillos}  🟢 {verdes}")

        # --- Pronóstico semanal por distrito (simulado) ---
        st.subheader("Pronóstico de riesgo semanal por distrito")
        days = pd.date_range(start=pd.Timestamp.today(), periods=7).strftime("%a %d/%m")
        forecast_data = []
        for _, row in gdf.iterrows():
            forecast_data.append({
                "Distrito": row['name'],
                **{day: np.clip(np.random.normal(row['riesgo'], 10), 0, 100) for day in days}
            })
        df_forecast = pd.DataFrame(forecast_data)
        st.dataframe(df_forecast)

        # --- Gráfico de líneas dinámico ---
        st.subheader("Evolución del riesgo por distrito")
        distrito_seleccionado = st.selectbox("Selecciona un distrito:", gdf['name'])
        df_line = df_forecast[df_forecast['Distrito'] == distrito_seleccionado].melt(
            id_vars='Distrito', value_vars=days,
            var_name='Día', value_name='Riesgo (%)'
        )
        fig_line = px.line(
            df_line,
            x='Día',
            y='Riesgo (%)',
            title=f"Evolución del riesgo: {distrito_seleccionado}",
            markers=True,
            range_y=[0, 100]
        )
        st.plotly_chart(fig_line, use_container_width=True)
