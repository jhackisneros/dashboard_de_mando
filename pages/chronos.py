import streamlit as st
import matplotlib.pyplot as plt

class ChronosPage:
    def __init__(self):
        pass

    def _generate_future_image(self, kind="verde"):
        """Genera una visualización simple como placeholder para la estrategia."""
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.axis("off")

        if kind == "verde":
            ax.set_facecolor("honeydew")
            ax.text(0.5, 0.6, "FORTALEZA VERDE", ha="center", fontsize=18, weight="bold", color="green")
            ax.text(0.5, 0.4,
                    "Ciudades resilientes, logística sostenible\nTransporte eléctrico y corredores verdes",
                    ha="center", fontsize=10)
            circle = plt.Circle((0.2, 0.2), 0.1, color="green", alpha=0.5)
            ax.add_patch(circle)
        else:
            ax.set_facecolor("lightgray")
            ax.text(0.5, 0.6, "BÚNKER TECNOLÓGICO", ha="center", fontsize=18, weight="bold", color="black")
            ax.text(0.5, 0.4,
                    "Infraestructura endurecida, ciberseguridad\nAutomatización extrema y redundancias",
                    ha="center", fontsize=10)
            rect = plt.Rectangle((0.15, 0.15), 0.3, 0.15, color="gray", alpha=0.5)
            ax.add_patch(rect)

        plt.tight_layout()
        return fig

    def show(self):
        st.header("Chronos: Visión Estratégica 2040")
        st.write("Dirigido a la Junta Directiva e inversores — seleccionar visión y mostrar defensa argumentada")

        # Selector de estrategia
        strategy = st.selectbox("Selector de Estrategia", ["Fortaleza Verde", "Búnker Tecnológico"])

        # Visualización de futuros + defensa argumentada
        if strategy == "Fortaleza Verde":
            fig = self._generate_future_image("verde")
            st.pyplot(fig)
            st.markdown(
                "**Defensa de la visión 'Fortaleza Verde':**\n\n"
                "- Inversión en resiliencia urbana reduce costes operativos a medio plazo.\n"
                "- Corredores verdes y energía distribuida protegen rutas críticas en Madrid.\n"
                "- Preferible para reputación ESG (atracción de capital) y mitigación climática."
            )
        else:
            fig = self._generate_future_image("bunker")
            st.pyplot(fig)
            st.markdown(
                "**Defensa de la visión 'Búnker Tecnológico':**\n\n"
                "- Prioriza robustez operativa y redundancias ante ciber y fallos sistémicos.\n"
                "- Alta inversión en automatización y seguridad crítica; mayor CAPEX pero menor TTR.\n"
                "- Adecuada si el principal riesgo es la inseguridad sistémica o amenazas dirigidas."
            )