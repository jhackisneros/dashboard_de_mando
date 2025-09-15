# pages/precog.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self):
        self.logic = PreCogLogic()

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico 3D")

        # Sliders interactivos
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)
        viento = st.slider("Velocidad del viento (km/h)", 0, 150, 30)

        # Generamos riesgo en 3D sobre una cuadrícula (simulación)
        lat_base = 40.4168  # Latitud Madrid
        lon_base = -3.7038  # Longitud Madrid
        x, y, z, color = self.logic.generate_risk_map(velocidad, lluvia, viento)

        # Alertas: contar colores
        rojos = np.sum(z > 70)
        amarillos = np.sum((z > 40) & (z <= 70))
        verdes = np.sum(z <= 40)

        # Mostrar alertas
        st.sidebar.subheader("Alertas de Riesgo")
        st.sidebar.info(f"Puntos rojos: {rojos}")
        st.sidebar.warning(f"Puntos amarillos: {amarillos}")
        st.sidebar.success(f"Puntos verdes: {verdes}")

        # Gráfico 3D interactivo
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
