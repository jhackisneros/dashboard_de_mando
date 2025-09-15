import streamlit as st

class ChronosLogic:
    def __init__(self):
        # Estrategias disponibles
        self.estrategias = {
            "Fortaleza Verde": {
                "imagen": "assets/fortaleza_verde.png",
                "defensa": "La estrategia verde asegura sostenibilidad y resiliencia a largo plazo."
            },
            "Búnker Tecnológico": {
                "imagen": "assets/bunker_tecnologico.png",
                "defensa": "El búnker tecnológico protege los activos críticos mediante innovación y seguridad."
            }
        }
        self.estrategia_seleccionada = None

    def render(self):
        st.header("Chronos: Visión Estratégica 2040")
        # Selector de estrategia
        self.estrategia_seleccionada = st.selectbox(
            "Selecciona la estrategia:",
            list(self.estrategias.keys())
        )
        # Mostrar la información correspondiente
        info = self.estrategias[self.estrategia_seleccionada]
        st.image(info["imagen"], use_column_width=True)
        st.write(info["defensa"])
