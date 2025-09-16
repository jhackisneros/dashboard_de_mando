import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="ChronoLogistics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título del dashboard
st.markdown(
    """
    <h1 style='text-align: center; color: #2C3E50;'>
    ChronoLogistics - Dashboard de Crisis
    </h1>
    """, unsafe_allow_html=True
)

# Footer profesional
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray;'>
    © 2025 ChronoLogistics | Dashboard Operativo de Crisis
    </p>
    """, unsafe_allow_html=True
)
