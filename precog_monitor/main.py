import streamlit as st
try:
    from precog_monitor.componente1 import MapaCalorRiesgo
except ImportError:
    MapaCalorRiesgo = None
try:
    from precog_monitor.componente2 import Componente2Principal
except ImportError:
    Componente2Principal = None

def main():
    st.header("Precog Monitor")
    if MapaCalorRiesgo:
        mapa = MapaCalorRiesgo()
        if hasattr(mapa, "mostrar"):
            mapa.mostrar(st)
        else:
            st.warning("No se puede mostrar el mapa de calor de riesgo.")
    else:
        st.warning("Componente1 no disponible.")
    if Componente2Principal:
        componente2 = Componente2Principal()
        if hasattr(componente2, "mostrar"):
            componente2.mostrar(st)
        else:
            st.warning("No se puede mostrar el componente 2.")
    else:
        st.warning("Componente2 no disponible.")

if __name__ == "__main__":
    main()