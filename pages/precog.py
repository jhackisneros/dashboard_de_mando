import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self):
        self.logic = PreCogLogic()
        self.distritos = [
            "Centro", "Arganzuela", "Retiro", "Salamanca", "Chamartín", 
            "Tetuán", "Chamberí", "Usera", "Moncloa-Aravaca", "Latina",
            "Carabanchel", "Fuencarral-El Pardo", "Hortaleza", "Villaverde",
            "Villa de Vallecas", "Vicálvaro", "San Blas-Canillejas", "Ciudad Lineal",
            "Moratalaz", "Puente de Vallecas", "Barajas"
        ]

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico 3D")

        # Sliders interactivos
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)
        viento = st.slider("Velocidad del viento (km/h)", 0, 150, 30)
        temperatura = st.slider("Temperatura (°C)", -10, 40, 20)
        humedad = st.slider("Humedad (%)", 0, 100, 50)

        # Crear dataframe de riesgo por distrito
        riesgos = []
        for distrito in self.distritos:
            base_riesgo = np.random.rand() * 10
            riesgo = np.clip((velocidad + lluvia + viento + temperatura + humedad)/5 + base_riesgo, 0, 100)
            riesgos.append({"Distrito": distrito, "Nivel de Riesgo (%)": round(riesgo, 1)})

        df_riesgos = pd.DataFrame(riesgos)

        # Alertas rápidas
        rojos = len(df_riesgos[df_riesgos["Nivel de Riesgo (%)"] >= 70])
        amarillos = len(df_riesgos[(df_riesgos["Nivel de Riesgo (%)"] >= 40) & (df_riesgos["Nivel de Riesgo (%)"] < 70)])
        verdes = len(df_riesgos[df_riesgos["Nivel de Riesgo (%)"] < 40])

        # Monitor lateral tipo alerta
        st.sidebar.header("Alertas Rápidas")
        st.sidebar.markdown(f"🔴 Distritos críticos: {rojos}")
        st.sidebar.markdown(f"🟡 Distritos medios: {amarillos}")
        st.sidebar.markdown(f"🟢 Distritos seguros: {verdes}")

        # Generamos mapa 3D con altura por riesgo
        num_distritos = len(self.distritos)
        x, y = np.meshgrid(range(5), range(5))  # Matriz para 21 distritos
        z = np.zeros_like(x, dtype=float)
        color = np.zeros_like(x, dtype=float)

        for i, riesgo in enumerate(df_riesgos["Nivel de Riesgo (%)"]):
            row = i // 5
            col = i % 5
            z[row, col] = riesgo / 2  # Altura proporcional al riesgo
            color[row, col] = riesgo  # Color según riesgo

        fig = go.Figure(data=[go.Bar3d(
            x=x.flatten(),
            y=y.flatten(),
            z=np.zeros_like(z.flatten()),
            dx=0.8,
            dy=0.8,
            dz=z.flatten(),
            color=color.flatten(),
            colorscale='RdYlGn_r',
            colorbar=dict(title="Nivel de Riesgo")
        )])

        st.plotly_chart(fig, use_container_width=True)

        # Tabla con riesgos por distrito
        st.subheader("Nivel de riesgo por distrito")
        st.dataframe(df_riesgos)
