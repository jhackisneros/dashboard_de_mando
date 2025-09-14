import streamlit as st
from .componente1 import MapaCalorRiesgo
from precog_monitor.componente2 import SimuladorRiesgo

st.title("Precog: Monitor de Riesgo Táctico")

# Componente 1
mapa = MapaCalorRiesgo()
mapa.mostrar(st)

# Componente 2
simulador = SimuladorRiesgo()
simulador.mostrar(st)