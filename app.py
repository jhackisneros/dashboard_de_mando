import streamlit as st
from pages.precog import PrecogPage
from pages.chronos import ChronosPage
from pages.klang import KLangPage

st.set_page_config(page_title="ChronoLogistics Dashboard", layout="wide")
st.title("ChronoLogistics - Dashboard de Crisis")

# Instanciamos cada pestaña
precog_page = PrecogPage()
chronos_page = ChronosPage()
klang_page = KLangPage()

# Sidebar para navegar
page = st.sidebar.selectbox("Selecciona la pestaña:",
                            ["Precog", "Chronos", "K-Lang"])

if page == "Precog":
    precog_page.show()
elif page == "Chronos":
    chronos_page.show()
elif page == "K-Lang":
    klang_page.show()
