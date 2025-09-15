import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from functions.precog import PreCogLogic

class PrecogPage:
    def __init__(self):
        self.logic = PreCogLogic()
        if "hist_riesgo" not in st.session_state:
            st.session_state.hist_riesgo = []

    def show(self):
        st.header("Precog: Monitor de Riesgo Táctico 3D")

        # --- Sliders principales ---
        velocidad = st.slider("Velocidad media (km/h)", 0, 200, 50)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)

        # --- Variables avanzadas ---
        with st.expander("Variables Avanzadas"):
            temperatura = st.slider("Temperatura (°C)", -20, 50, 25)
            nivel_rio = st.slider("Nivel del río (cm)", 0, 500, 100)
            humedad = st.slider("Humedad (%)", 0, 100, 50)
            viento = st.slider("Velocidad del viento (km/h)", 0, 150, 30)

        # --- Botones de escenarios ---
        col_esc, _ = st.columns([1,3])
        with col_esc:
            if st.button("Simulación Tormenta"):
                velocidad, lluvia, temperatura, nivel_rio, humedad, viento = 120, 80, 15, 400, 90, 100
            if st.button("Escenario Crítico"):
                velocidad, lluvia, temperatura, nivel_rio, humedad, viento = 150, 100, 10, 450, 95, 120

        # --- Calcular riesgo ---
        x, y, z, color = self.logic.generate_risk_map(
            velocidad, lluvia, temperatura, nivel_rio, humedad, viento
        )

        promedio_riesgo = int(np.mean(z))
        st.session_state.hist_riesgo.append(promedio_riesgo)

        # --- Columnas para diseño ---
        col1, col2 = st.columns([3,1])

        with col1:
            # Gráfico 3D
            fig3d = go.Figure(data=[go.Scatter3d(
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
            st.plotly_chart(fig3d, use_container_width=True)

            # Heatmap 2D
            fig2d = go.Figure(data=go.Heatmap(
                z=z,
                colorscale='RdYlGn_r',
                colorbar=dict(title="Nivel de Riesgo")
            ))
            st.plotly_chart(fig2d, use_container_width=True)

        with col2:
            st.subheader("Monitor de Riesgo / Alertas")

            # Contar niveles
            rojos = np.sum(z > 70)
            amarillos = np.sum((z > 40) & (z <= 70))
            verdes = np.sum(z <= 40)

            # Alertas inteligentes
            if rojos > 10:
                st.error(f"⚠️ ALERTA: Demasiados puntos rojos ({rojos})")
            elif amarillos > 20:
                st.warning(f"⚠️ Atención: muchos puntos amarillos ({amarillos})")
            else:
                st.success(f"✅ Riesgo bajo: {verdes} puntos verdes")

            # Métricas
            st.metric("Velocidad media (km/h)", velocidad)
            st.metric("Intensidad de lluvia (mm/h)", lluvia)
            st.metric("Temperatura (°C)", temperatura)
            st.metric("Nivel del río (cm)", nivel_rio)
            st.metric("Humedad (%)", humedad)
            st.metric("Velocidad del viento (km/h)", viento)
            st.metric("Nivel de Riesgo Promedio (%)", f"{promedio_riesgo}%")

            # Descargar datos
            df_riesgo = pd.DataFrame(z, columns=[f"Col{i}" for i in range(z.shape[1])])
            st.download_button(
                "Descargar datos de riesgo",
                data=df_riesgo.to_csv(index=False),
                file_name="riesgo.csv",
                mime="text/csv"
            )

            # Histórico del riesgo
            if len(st.session_state.hist_riesgo) > 1:
                st.line_chart(st.session_state.hist_riesgo, height=150)
