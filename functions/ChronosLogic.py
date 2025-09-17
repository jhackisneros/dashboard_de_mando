import streamlit as st

class ChronosLogic:
    def __init__(self):
        # Estrategias disponibles con imagen y defensa
        self.estrategias = {
            "Fortaleza Verde": {
                "imagen": "assets/fortaleza_verde.png",
                "defensa": (
                    "Invertir en sostenibilidad y energías renovables para asegurar la "
                    "resiliencia a largo plazo de ChronoLogistics y proteger Madrid ante futuras crisis climáticas."
                )
            },
            "Búnker Tecnológico": {
                "imagen": "assets/bunker_tecnologico.png",
                "defensa": (
                    "Fortalecer infraestructuras tecnológicas y de seguridad para garantizar "
                    "operaciones continuas, incluso ante desastres o ataques cibernéticos."
                )
            }
        }

    def render(self):
        st.header("Chronos: Visión Estratégica 2040")

        # --- Componente 1: Selector de Estrategia ---
        estrategia = st.selectbox(
            "Selecciona la estrategia:",
            list(self.estrategias.keys())
        )

        # --- Componente 2: Visualizador de futuros ---
        info = self.estrategias[estrategia]

        # Mostrar imagen (pre-generada por GAN y guardada en assets/)
        st.image(info["imagen"], use_column_width=True)

        # Mostrar defensa argumentada
        st.markdown(f"**Justificación:** {info['defensa']}")
