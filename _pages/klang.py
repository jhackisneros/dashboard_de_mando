import streamlit as st
from typing import Dict

# --- Definición mejorada de protocolos ---
PROTOCOLS: Dict[str, Dict] = {
    "VÍSPERA": {
        "short": "Vigilancia y Preparación",
        "trigger": "Condiciones elevadas: viento moderado o inundación localizada.",
        "triggers_detail": [
            "Velocidad del viento entre 30 y 89 km/h",
            "Nivel de inundación entre 30 y 69 cm",
            "Lluvia moderada (20–49 mm/h) o picos locales"
        ],
        "actions": [
            "1) Activar monitorización cada 15 minutos.",
            "2) Notificar equipos locales y servicios municipales.",
            "3) Preposicionar recursos (generadores, bombas, rutas).",
            "4) Comunicación preventiva a stakeholders."
        ],
        "color": "#f0ad4e"  # naranja
    },
    "CÓDIGO ROJO": {
        "short": "Respuesta Inmediata",
        "trigger": "Evento crítico: viento extremo o inundación severa.",
        "triggers_detail": [
            "Velocidad del viento ≥ 90 km/h",
            "Nivel de inundación ≥ 70 cm",
            "Lluvia muy intensa (≥ 80 mm/h) o múltiples alertas"
        ],
        "actions": [
            "1) Evacuación parcial/total por zonas según plan.",
            "2) Aislar suministros críticos.",
            "3) Movilizar equipos TITÁN y apoyo externo.",
            "4) Abrir centros de acogida y rutas seguras."
        ],
        "color": "#ff4b4b"  # rojo
    },
    "RENACIMIENTO": {
        "short": "Recuperación y Evaluación",
        "trigger": "Condiciones normalizadas y seguridad estable.",
        "triggers_detail": [
            "Velocidad del viento < 30 km/h",
            "Nivel de inundación < 30 cm",
            "Lluvia baja (< 20 mm/h) e infraestructura estable"
        ],
        "actions": [
            "1) Inspección técnica y evaluación de daños.",
            "2) Priorización de reparaciones por impacto.",
            "3) Comunicación de estado y seguimiento.",
            "4) Informe final y lecciones aprendidas."
        ],
        "color": "#4bbf7c"  # verde
    }
}

def _decide_protocol(viento: int, lluvia: int, nivel_rio: int):
    """
    Motor de decisión explicable (solo local a esta página).
    Devuelve: dict(protocol, reason, score)
    """
    score = {"CÓDIGO_ROJO": 0.0, "VÍSPERA": 0.0, "RENACIMIENTO": 0.0}

    # Viento
    if viento >= 90:
        score["CÓDIGO_ROJO"] += 100 + (viento - 90) * 0.5
    elif 30 <= viento < 90:
        score["VÍSPERA"] += 50 + (viento - 30) * 0.4
    else:
        score["RENACIMIENTO"] += 30

    # Inundación (nivel río como proxy)
    if nivel_rio >= 70:
        score["CÓDIGO_ROJO"] += 100 + (nivel_rio - 70) * 0.6
    elif 30 <= nivel_rio < 70:
        score["VÍSPERA"] += 50 + (nivel_rio - 30) * 0.3
    else:
        score["RENACIMIENTO"] += 30

    # Lluvia
    if lluvia >= 80:
        score["CÓDIGO_ROJO"] += (lluvia - 80) * 0.5 + 20
    elif 50 <= lluvia < 80:
        score["VÍSPERA"] += 35 + (lluvia - 50) * 0.2
    elif 20 <= lluvia < 50:
        score["VÍSPERA"] += 20
    else:
        score["RENACIMIENTO"] += 10

    best = max(score.items(), key=lambda kv: kv[1])[0]
    mapping = {"CÓDIGO_ROJO": "CÓDIGO ROJO", "VÍSPERA": "VÍSPERA", "RENACIMIENTO": "RENACIMIENTO"}
    active = mapping[best]

    # Explicación legible
    parts = []
    parts.append(f"Viento {'extremo' if viento>=90 else 'elevado' if viento>=30 else 'estable'} ({viento} km/h).")
    parts.append(f"Inundación {'severa' if nivel_rio>=70 else 'moderada' if nivel_rio>=30 else 'baja'} ({nivel_rio} cm).")
    parts.append(f"Lluvia {'muy intensa' if lluvia>=80 else 'intensa' if lluvia>=50 else 'moderada' if lluvia>=20 else 'baja'} ({lluvia} mm/h).")
    reason = " ".join(parts)

    return {"protocol": active, "reason": reason, "score": score}

class KLangPage:
    def __init__(self):
        self.protocols = {
            "VÍSPERA": PROTOCOLS["VÍSPERA"],
            "CÓDIGO ROJO": PROTOCOLS["CÓDIGO ROJO"],
            "RENACIMIENTO": PROTOCOLS["RENACIMIENTO"],
        }

    def show(self):
        st.header("K-Lang: Manual de Batalla Interactivo")

        col_left, col_right = st.columns([1.6, 1])

        # ---- Selector + Fichas (izquierda)
        with col_left:
            protocol = st.selectbox("Selecciona el protocolo:", list(self.protocols.keys()))
            data = self.protocols[protocol]

            st.subheader("Ficha Técnica")
            st.write(f"**Disparador:** {data['trigger']}")
            if data.get("triggers_detail"):
                with st.expander("Detalles del disparador"):
                    for d in data["triggers_detail"]:
                        st.write(f"- {d}")

            st.write("**Secuencia de acciones:**")
            for act in data["actions"]:
                st.write(f"- {act}")

            if st.button("Activar protocolo seleccionado (manual)"):
                st.success(f"✅ PROTOCOLO MANUAL ACTIVADO: {protocol}")
                st.caption("Simulación: notificaciones enviadas y pasos iniciados según plan.")

        # ---- Simulador + Indicador (derecha)
        with col_right:
            st.subheader("Simulador de condiciones")
            viento = st.slider("Velocidad del viento (km/h)", 0, 200, 30)
            lluvia = st.slider("Intensidad de lluvia (mm/h)", 0, 120, 20)
            nivel_rio = st.slider("Nivel del río / Inundación (cm)", 0, 300, 40)

            result = _decide_protocol(viento, lluvia, nivel_rio)
            active = result["protocol"]
            reason = result["reason"]
            color = self.protocols[active]["color"]

            # Indicador grande por color
            st.markdown(
                f"""
                <div style="padding:16px;border-radius:10px;background:{color};color:white;text-align:center;">
                    <h3 style="margin:6px 0">PROTOCOLO ACTIVO: {active}</h3>
                    <p style="margin:4px 0 0 0;font-weight:600">{reason}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("**Puntuaciones internas (transparencia):**")
            sc = result["score"]
            st.write(f"- CÓDIGO ROJO: {int(sc['CÓDIGO_ROJO'])}")
            st.write(f"- VÍSPERA: {int(sc['VÍSPERA'])}")
            st.write(f"- RENACIMIENTO: {int(sc['RENACIMIENTO'])}")

        st.caption("Nota: Motor de reglas explicable para la demo. Para producción: conectar al feed real de sensores.")


# --- renderizar la página ---
KLangPage().show()




