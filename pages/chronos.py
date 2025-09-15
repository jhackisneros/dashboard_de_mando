import streamlit as st

class ChronosPage:
    def __init__(self):
        # Diccionario con imágenes de placeholder para cada estrategia
        self.data = {
            "Fortaleza Verde": "https://via.placeholder.com/400x300.png?text=Fortaleza+Verde",
            "Bunker Tecnologico": "https://via.placeholder.com/400x300.png?text=Bunker+Tecnologico"
        }

        # Defensas argumentadas de cada estrategia
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

        # Selector de estrategia
        estrategia = st.selectbox(
            "Selecciona la visión estratégica:",
            list(self.data.keys())
        )

        # Mostrar la imagen correspondiente con use_container_width
        st.image(self.data[estrategia], use_container_width=True)

        # Mostrar la defensa argumentada
        st.markdown(f"**Justificación:** {self.texts[estrategia]}")
