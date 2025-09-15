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

        # --- Diseño de columnas ---
        col1, col2 = st.columns([3,1])  # col1: gráfico, col2: monitor/alertas

        with col1:
            # Gráfico 3D interactivo
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
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Monitor de Riesgo / Alertas")

            # Contar cuántos puntos en cada nivel de riesgo
            rojos = np.sum(z > 70)
            amarillos = np.sum((z > 40) & (z <= 70))
            verdes = np.sum(z <= 40)

            # Mensajes de alerta según los valores
            if rojos > 10:
                st.error(f"⚠️ ALERTA: Demasiados puntos rojos ({rojos})")
            elif amarillos > 20:
                st.warning(f"⚠️ Atención: muchos puntos amarillos ({amarillos})")
            else:
                st.success(f"✅ Riesgo bajo: {verdes} puntos verdes")

            # Información clave del monitor
            st.metric("Velocidad media (km/h)", velocidad)
            st.metric("Intensidad de lluvia (mm/h)", lluvia)
            st.metric("Nivel de Riesgo Promedio (%)", f"{int(np.mean(z))}%")
