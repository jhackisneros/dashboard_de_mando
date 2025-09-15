# pages/precog.py
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self):
        # Cargar shapefile de Madrid
        self.logic = PreCogLogic(shapefile_path="data/Distritos.shp")

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico 3D - Madrid")

        # Sliders para todos los factores
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)
        viento = st.slider("Velocidad del viento (km/h)", 0, 150, 30)
        temperatura = st.slider("Temperatura (°C)", -10, 40, 20)
        humedad = st.slider("Humedad (%)", 0, 100, 50)

        # Generar mapa de riesgo por distrito
        gdf = self.logic.generate_risk_map(velocidad, lluvia, viento, temperatura, humedad)

        # Layout con mapa y alertas
        col1, col2 = st.columns([3,1])

        with col1:
            # Mapa de calor interactivo
            fig = px.choropleth_mapbox(
                gdf,
                geojson=gdf.__geo_interface__,
                locations=gdf.index,
                color="nivel_riesgo",
                color_continuous_scale="RdYlGn_r",
                range_color=(0, 100),
                mapbox_style="carto-positron",
                zoom=10,
                center={"lat": 40.4168, "lon": -3.7038},
                opacity=0.6,
                hover_name="NOMBRE_DISTRICTO",
                hover_data={"nivel_riesgo": True}
            )

            # Semáforos como marcadores
            for _, row in gdf.iterrows():
                color = "green"
                if row.nivel_riesgo > 70: color = "red"
                elif row.nivel_riesgo > 40: color = "yellow"
                fig.add_scattermapbox(
                    lat=[row.geometry.centroid.y],
                    lon=[row.geometry.centroid.x],
                    mode='markers',
                    marker=dict(size=15, color=color),
                    text=row["NOMBRE_DISTRICTO"]
                )

            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Alertas por distritos")
            alerts = self.logic.get_alerts()
            st.markdown(f"**Rojos (alto riesgo):** {alerts['rojos']}")
            st.markdown(f"**Amarillos (medio riesgo):** {alerts['amarillos']}")
            st.markdown(f"**Verdes (bajo riesgo):** {alerts['verdes']}")
            st.markdown("---")
            st.markdown("Recomendaciones:")
            if alerts["rojos"] > 0:
                st.warning("¡Distritos con alto riesgo! Precaución máxima.")
            if alerts["amarillos"] > 0:
                st.info("Distritos con riesgo medio. Mantener vigilancia.")
            if alerts["verdes"] > 0:
                st.success("Distritos con bajo riesgo. Operaciones normales.")

        st.subheader("Ranking de distritos por nivel de riesgo")
        st.dataframe(
            gdf[["NOMBRE_DISTRICTO","nivel_riesgo"]]
            .sort_values(by="nivel_riesgo", ascending=False)
            .reset_index(drop=True)
        )

        # -------------------------------
        # Simulación de escenarios futuros
        st.subheader("Simulación de escenarios futuros (próximos 5 días)")
        dias = 5
        escenarios = []

        for dia in range(1, dias+1):
            # Simulación simple: fluctuaciones aleatorias de los factores
            delta_vel = np.random.randint(-10, 10)
            delta_lluvia = np.random.randint(-5, 5)
            delta_viento = np.random.randint(-5, 5)
            delta_temp = np.random.randint(-2, 2)
            delta_hum = np.random.randint(-5, 5)

            gdf_sim = self.logic.generate_risk_map(
                velocidad + delta_vel,
                lluvia + delta_lluvia,
                viento + delta_viento,
                temperatura + delta_temp,
                humedad + delta_hum
            )
            gdf_sim["dia"] = f"Día {dia}"
            escenarios.append(gdf_sim[["NOMBRE_DISTRICTO","nivel_riesgo","dia"]])

        df_escenarios = pd.concat(escenarios)

        # Gráfico de líneas para ver evolución de riesgo por distrito
        fig2 = px.line(
            df_escenarios,
            x="dia",
            y="nivel_riesgo",
            color="NOMBRE_DISTRICTO",
            markers=True,
            title="Evolución de riesgo en los distritos"
        )
        st.plotly_chart(fig2, use_container_width=True)
