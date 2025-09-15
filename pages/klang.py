import streamlit as st
import numpy as np

class KLangPage:
    def __init__(self):
        # Protocolos predefinidos
        self.protocols = {
            "VÍSPERA": {"trigger": "Lluvia intensa > 50mm", "actions": ["Aviso a equipos", "Preparar reservas"]},
            "CÓDIGO ROJO": {"trigger": "Viento > 90 km/h", "actions": ["Evacuación parcial", "Activar seguro crítico"]},
            "RENACIMIENTO": {"trigger": "Riesgo normalizado", "actions": ["Revisión de sistemas", "Informe final"]}
        }

    def show(self):
        st.header("K-Lang: Manual de Batalla Interactivo")

        protocol = st.selectbox("Selecciona el protocolo:", list(self.protocols.keys()))
        data = self.protocols[protocol]

        st.subheader("Ficha Técnica")
        st.write(f"**Disparador:** {data['trigger']}")
        st.write("**Secuencia de acciones:**")
        for act in data['actions']:
            st.write(f"- {act}")

        # Simulador de condiciones
        st.subheader("Simulador de condiciones")
        viento = st.slider("Velocidad del viento (km/h)", 0, 150, 30)
        lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 100, 20)
        nivel_rio = st.slider("Nivel del río (cm)", 0, 500, 100)

        # Determinar protocolo activo
        active = None
        if viento > 90:
            active = "CÓDIGO ROJO"
        elif lluvia > 50:
            active = "VÍSPERA"
        else:
            active = "RENACIMIENTO"

        if active == protocol:
            st.success(f"✅ PROTOCOLO ACTIVO: {protocol}")
        else:
            st.info(f"⚠️ Protocolo sugerido según condiciones: {active}")
