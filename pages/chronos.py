import streamlit as st
import pandas as pd
from PIL import Image

class ChronosPage:
    def __init__(self):
        # Pre-cargamos imágenes y textos
        self.strategies = {
            "Fortaleza Verde": {
                "image": "assets/fortaleza_verde.png",
                "desc": "Enfoque sostenible: inversión en energías renovables, reducción de emisiones y resiliencia climática."
            },
            "Búnker Tecnológico": {
                "image": "assets/bunker_tecnologico.png",
                "desc": "Alta inversión tecnológica: automatización, infraestructura crítica segura y redundancia digital."
            }
        }

    def show(self):
        st.header("Chronos: Visión Estratégica 2040")

        # Selector de estrategia
        strategy = st.selectbox("Selecciona la estrategia:", list(self.strategies.keys()))
        data = self.strategies[strategy]

        # Mostrar imagen y descripción
        col1, col2 = st.columns([2,1])
        with col1:
            st.image(data["image"], use_column_width=True)
        with col2:
            st.markdown(f"**Defensa de la estrategia:**\n\n{data['desc']}")

        # Ejemplo de KPIs
        st.subheader("Indicadores de impacto")
        kpi_data = pd.DataFrame({
            "Indicador": ["Reducción CO2", "Resiliencia de activos", "Inversión tecnológica"],
            "Valor": [80 if strategy=="Fortaleza Verde" else 50,
                      70 if strategy=="Fortaleza Verde" else 90,
                      60 if strategy=="Fortaleza Verde" else 95]
        })
        st.table(kpi_data)
