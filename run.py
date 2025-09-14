# run.py - Lanzador central del Dashboard de Mando y Control

import streamlit as st

# Importa los módulos principales de cada sección
try:
    from precog_monitor.main import main as precog_main
except ImportError:
    def precog_main():
        st.warning("Precog Monitor no disponible.")

try:
    from chronos_vision.main import main as chronos_main
except ImportError:
    def chronos_main():
        st.warning("Chronos Vision no disponible.")

try:
    from klang_manual.main import main as klang_main
except ImportError:
    def klang_main():
        st.warning("Klang Manual no disponible.")

# Diccionario de secciones
secciones = {
    "Precog Monitor": precog_main,
    "Chronos Vision": chronos_main,
    "Klang Manual": klang_main,
}

def main():
    st.sidebar.title("Dashboard de Mando y Control")
    seccion = st.sidebar.selectbox("Selecciona módulo", list(secciones.keys()))
    st.title(seccion)
    # Ejecuta la función principal de la sección seleccionada
    secciones[seccion]()

if __name__ == "__main__":
    main()