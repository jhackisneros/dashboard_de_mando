class SimuladorRiesgo:
    def __init__(self):
        pass

    def predecir_riesgo(self, velocidad_media, intensidad_lluvia):
        riesgo = 0.5 * velocidad_media + 0.5 * intensidad_lluvia
        nivel = "BAJO"
        if riesgo > 80:
            nivel = "ALTO"
        elif riesgo > 50:
            nivel = "MEDIO"
        return f"{int(riesgo)}% - {nivel}"

    def mostrar(self, st):
        st.subheader("Simulador de Riesgo Interactivo")
        velocidad_media = st.slider("Velocidad Media (km/h)", 0, 120, 50)
        intensidad_lluvia = st.slider("Intensidad de Lluvia (mm/h)", 0, 100, 30)
        nivel_riesgo = self.predecir_riesgo(velocidad_media, intensidad_lluvia)
        st.markdown(f"### Nivel de Riesgo en Cascada: **{nivel_riesgo}**")
