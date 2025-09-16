from _pages.precog import PrecogPage
from _pages.chronos import ChronosPage
from _pages.klang import KLangPage
from _pages.chatbot import ChatBotPage
import streamlit as st

st.set_page_config(page_title="ChronoLogistics Dashboard", layout="wide")

st.sidebar.title("Navegación del Dashboard")
page_option = st.sidebar.selectbox(
    "Selecciona la pestaña:",
    ["Precog", "Chronos", "K-Lang", "ChatBot"]
)

# Instanciamos las páginas
precog_page = PrecogPage()
chronos_page = ChronosPage()
klang_page = KLangPage()
chatbot_page = ChatBotPage()

# Mostramos la página correspondiente
if page_option == "Precog":
    precog_page.show()
elif page_option == "Chronos":
    chronos_page.show()
elif page_option == "K-Lang":
    klang_page.show()
elif page_option == "ChatBot":
    chatbot_page.show()
