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

        # Calculamos el riesgo en 3D
        x, y, z, color = self.logic.generate_risk_map(velocidad, lluvia)

        # Gráfico 3D interactivo con colores
        fig = go.Figure(data=[go.Scatter3d(
            x=x.flatten(),
            y=y.flatten(),
            z=z.flatten(),
            mode='markers',
            marker=dict(
                size=5,
                color=color.flatten(),
                colorscale='RdYlGn_r',  # Rojo=alto, Verde=bajo
                colorbar=dict(title="Nivel de Riesgo")
            )
        )])
        st.plotly_chart(fig)
