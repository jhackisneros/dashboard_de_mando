# run.py - Lanzador central del Dashboard de Mando y Control

import streamlit as st
import importlib

st.set_page_config(page_title="Dashboard de Mando y Control", layout="wide")

st.sidebar.title("Navegación")
seccion = st.sidebar.radio("Ir a sección:", [
    "Precog: Monitor de Riesgo Táctico",
    "Chronos: Visión Estratégica 2040",
    "K-Lang: Manual de Batalla Interactivo"
])

if seccion == "Precog: Monitor de Riesgo Táctico":
    precog = importlib.import_module("1_precog_monitor.main")
    if hasattr(precog, "main"):
        precog.main()
    else:
        st.warning("Implementa la función main() en 1_precog_monitor/main.py")

elif seccion == "Chronos: Visión Estratégica 2040":
    chronos = importlib.import_module("2_chronos_vision.main")
    if hasattr(chronos, "main"):
        chronos.main()
    else:
        st.warning("Implementa la función main() en 2_chronos_vision/main.py")

elif seccion == "K-Lang: Manual de Batalla Interactivo":
    klang = importlib.import_module("3_klang_manual.main")
    if hasattr(klang, "main"):
        klang.main()
    else:
        st.warning("Implementa la función main() en 3_klang_manual/main.py")