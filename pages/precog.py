# pages/precog.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self):
        self.logic = PreCogLogic()

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico 3D")

        # ---------------- Sliders interactivos ----------------
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)
        viento = st.slider("Velocidad del viento (km/h)", 0, 150, 30)
        temperatura = st.slider("Temperatura (°C)", -10, 45, 25)  # nuevo
        humedad = st.slider("Humedad (%)", 0, 100, 50)           # nuevo

        # ---------------- Generación de riesgo 3D ----------------
        x, y, z, color = self.logic.generate_risk_map(
            velocidad, lluvia, viento, temperatura, humedad
        )

        # ---------------- Alertas ----------------
        rojos = np.sum(z > 70)
        amarillos = np.sum((z > 40) & (z <= 70))
        verdes = np.sum(z <= 40)

        st.sidebar.subheader("Alertas de Riesgo")
        st.sidebar.info(f"Puntos rojos: {rojos}")
        st.sidebar.warning(f"Puntos amarillos: {amarillos}")
        st.sidebar.success(f"Puntos verdes: {verdes}")

        # ---------------- Gráfico 3D interactivo ----------------
        lat_base = 40.4168  # Madrid
        lon_base = -3.7038
        fig = go.Figure(data=[go.Scatter3d(
            x=x.flatten() + lon_base,
            y=y.flatten() + lat_base,
            z=z.flatten(),
            mode='markers',
            marker=dict(
                size=5,
                color=color.flatten(),
                colorscale='RdYlGn_r',
                colorbar=dict(title="Nivel de Riesgo")
            )
        )])
        fig.update_layout(scene=dict(
            xaxis_title='Longitud',
            yaxis_title='Latitud',
            zaxis_title='Nivel de Riesgo'
        ))
        st.plotly_chart(fig, use_container_width=True)

        # ---------------- Monitor adicional ----------------
        st.subheader("Monitor de Riesgo")
        total = rojos + amarillos + verdes
        st.markdown(f"- Total de puntos: {total}")
        st.markdown(f"- Rojo: {rojos} ({rojos/total*100:.1f}%)")
        st.markdown(f"- Amarillo: {amarillos} ({amarillos/total*100:.1f}%)")
        st.markdown(f"- Verde: {verdes} ({verdes/total*100:.1f}%)")

        # ---------------- Mapa de Madrid con riesgo ----------------
        df = px.data.gapminder().query("year==2007")  # placeholder dataframe
        df_map = {"lat": y.flatten() + lat_base, "lon": x.flatten() + lon_base, "risk": z.flatten()}
        fig_map = px.scatter_mapbox(
            df_map, lat="lat", lon="lon", color="risk", size="risk",
            color_continuous_scale="RdYlGn_r", zoom=10, height=400,
            hover_data={"lat":True, "lon":True, "risk":True}
        )
        fig_map.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig_map, use_container_width=True)
