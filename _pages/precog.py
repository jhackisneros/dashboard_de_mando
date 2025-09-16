import streamlit as st
import plotly.graph_objects as go
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self):
        self.logic = PreCogLogic()

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico (Simulado)")

        # --- Sliders ---
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)
        viento = st.slider("Velocidad del viento (km/h)", 0, 100, 10)
        temperatura = st.slider("Temperatura (°C)", -10, 40, 20)
        humedad = st.slider("Humedad (%)", 0, 100, 50)

        # --- Riesgo ---
        distritos, x, y, z, color = self.logic.generate_risk_map(
            velocidad, lluvia, viento, temperatura, humedad
        )

        # --- Mapa 3D ---
        fig = go.Figure(data=[go.Scatter3d(
            x=x.flatten(),
            y=y.flatten(),
            z=z.flatten(),
            mode='markers',
            marker=dict(
                size=5,
                color=color.flatten(),
                colorscale='RdYlGn_r',
                colorbar=dict(title="Nivel de Riesgo")
            )
        )])
        st.plotly_chart(fig, use_container_width=True)

        # --- Monitor de alertas ---
        rojos = (distritos['riesgo'] > 70).sum()
        amarillos = ((distritos['riesgo'] >= 40) & (distritos['riesgo'] <= 70)).sum()
        verdes = (distritos['riesgo'] < 40).sum()
        st.info(f"⚠️ Alertas: 🔴 {rojos}  🟡 {amarillos}  🟢 {verdes}")
