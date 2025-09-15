# pages/chronos.py
import streamlit as st
import plotly.express as px
import pandas as pd

class ChronosPage:
    def __init__(self):
        self.texts = {
            "Fortaleza Verde": (
                "Invertir en sostenibilidad y energías renovables para asegurar la "
                "resiliencia a largo plazo de ChronoLogistics y proteger Madrid ante futuras crisis climáticas."
            ),
            "Bunker Tecnologico": (
                "Fortalecer infraestructuras tecnológicas y de seguridad para garantizar "
                "operaciones continuas, incluso ante desastres o ataques cibernéticos."
            )
        }

    def show(self):
        st.header("Chronos: Visión Estratégica 2040")

        estrategia = st.selectbox(
            "Selecciona la visión estratégica:",
            list(self.texts.keys())
        )

        # Mapa interactivo centrado en Madrid
        df = pd.DataFrame({"lat": [40.4168], "lon": [-3.7038], "name": ["Madrid"]})
        fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="name", zoom=10, height=400)
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(f"**Justificación:** {self.texts[estrategia]}")
