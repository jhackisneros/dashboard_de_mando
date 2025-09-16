import streamlit as st
from _pages.precog import PrecogPage
from _pages.chronos import ChronosPage
from _pages.klang import KLangPage

# Configuración de la página
st.set_page_config(
    page_title="ChronoLogistics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título del dashboard
st.markdown(
    """
    <h1 style='text-align: center; color: #2C3E50;'>ChronoLogistics - Dashboard de Crisis</h1>
    """, unsafe_allow_html=True
)

# Barra lateral para navegación
st.sidebar.title("Navegación del Dashboard")
page_option = st.sidebar.selectbox(
    "Selecciona la pestaña:",
    ["Precog", "Chronos", "K-Lang"]
)

# Instanciamos las páginas
precog_page = PrecogPage()
chronos_page = ChronosPage()
klang_page = KLangPage()

# Mostramos la página correspondiente
if page_option == "Precog":
    precog_page.show()
elif page_option == "Chronos":
    chronos_page.show()
elif page_option == "K-Lang":
    klang_page.show()

# Footer profesional
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray;'>
    © 2025 ChronoLogistics | Dashboard Operativo de Crisis
    </p>
    """, unsafe_allow_html=True
)
