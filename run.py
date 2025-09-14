# run.py - Lanzador central del Dashboard de Mando y Control

import streamlit as st
import importlib
import sys
import os

# Añadir la carpeta raíz al sys.path
sys.path.append(os.path.dirname(__file__))


def mostrar_precog():
    # Cambia el import para usar ruta relativa
    from precog_monitor.main import main as precog_main
    precog_main()

st.set_page_config(page_title="Dashboard de Mando y Control", layout="wide")

st.sidebar.title("Navegación")
secciones = {
    "Precog: Monitor de Riesgo Táctico": mostrar_precog,
    "Chronos: Visión Estratégica 2040": lambda: st.info("Implementa la integración de Chronos en chronos_vision/main.py"),
    "K-Lang: Manual de Batalla Interactivo": lambda: st.info("Implementa la integración de K-Lang en klang_manual/main.py")
}
seccion = st.sidebar.radio("Ir a sección:", list(secciones.keys()))

secciones[seccion]()