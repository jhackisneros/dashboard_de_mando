import streamlit as st
import plotly.express as px
import pandas as pd

class ChronosLogic:
    def __init__(self):
        # Estrategias disponibles con color y defensa
        self.estrategias = {
            "Fortaleza Verde": {
                "color": "green",
                "defensa": (
                    "Invertir en sostenibilidad y energías renovables para asegurar la "
                    "resiliencia a largo plazo de ChronoLogistics y proteger Madrid ante futuras crisis climáticas."
                ),
                "visual": "area"
            },
            "Búnker Tecnológico": {
                "color": "royalblue",
                "defensa": (
                    "Fortalecer infraestructuras tecnológicas y de seguridad para garantizar "
                    "operaciones continuas, incluso ante desastres o ataques cibernéticos."
                ),
                "visual": "radar"
            }
        }

    def render(self):
        st.header("Chronos: Visión Estratégica 2040")

        # --- Componente 1: Selector de Estrategia ---
        estrategia = st.selectbox(
            "Selecciona la estrategia:",
            list(self.estrategias.keys())
        )
        info = self.estrategias[estrategia]

        # --- Datos de ejemplo para las visualizaciones ---
        df = pd.DataFrame({
            "Factor": ["Resiliencia", "Innovación", "Seguridad", "Sostenibilidad", "Coste"],
            "Valor": [80, 70, 65, 90, 60] if estrategia == "Fortaleza Verde" else [70, 90, 95, 60, 85]
        })

        # --- Componente 2: Visualizador de futuros ---
        if info["visual"] == "area":
            fig = px.area(
                df,
                x="Factor",
                y="Valor",
                color_discrete_sequence=[info["color"]],
            )
        else:  # radar chart
            fig = px.line_polar(
                df,
                r="Valor",
                theta="Factor",
                line_close=True,
                color_discrete_sequence=[info["color"]],
            )
            fig.update_traces(fill="toself")

        fig.update_layout(
            showlegend=False,
            title=f"Visión: {estrategia}",
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

        # --- Componente 3: Mapa centrado en Madrid ---
        df_madrid = pd.DataFrame({
            "lat": [40.4168],
            "lon": [-3.7038],
            "Lugar": ["Madrid"]
        })

        mapa = px.scatter_mapbox(
            df_madrid,
            lat="lat",
            lon="lon",
            hover_name="Lugar",
            zoom=10,
            height=400,
            color_discrete_sequence=[info["color"]]
        )
        mapa.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(mapa, use_container_width=True)

        # --- Texto de justificación ---
        st.markdown(f"**Justificación:** {info['defensa']}")
