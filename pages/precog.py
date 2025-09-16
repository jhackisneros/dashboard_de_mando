import streamlit as st
import plotly.graph_objects as go
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self):
        self.logic = PreCogLogic()

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico 3D - Madrid")

        # Sliders interactivos
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)
        viento = st.slider("Velocidad del viento (km/h)", 0, 100, 10)
        temperatura = st.slider("Temperatura (°C)", -10, 40, 20)
        humedad = st.slider("Humedad (%)", 0, 100, 50)

        # Generar mapa de riesgo
        distritos, z, color = self.logic.generate_risk_map(velocidad, lluvia, viento, temperatura, humedad)

        # Gráfico 3D de barras (cada distrito)
        fig = go.Figure(data=[go.Bar(
            x=distritos,
            y=z,
            marker_color=color
        )])
        fig.update_layout(
            title="Nivel de riesgo por distrito",
            xaxis_title="Distrito",
            yaxis_title="Nivel de riesgo (%)",
            yaxis=dict(range=[0, 100])
        )
        st.plotly_chart(fig, use_container_width=True)

        # Monitor de alertas
        rojos = sum(c == "red" for c in color)
        amarillos = sum(c == "yellow" for c in color)
        verdes = sum(c == "green" for c in color)

        st.subheader("Monitor de Alertas")
        st.markdown(f"- 🔴 Alto riesgo: {rojos} distritos")
        st.markdown(f"- 🟡 Riesgo medio: {amarillos} distritos")
        st.markdown(f"- 🟢 Bajo riesgo: {verdes} distritos")
