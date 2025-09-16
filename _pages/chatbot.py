import streamlit as st
import pandas as pd
import numpy as np
from functions.precog import PreCogLogic

class ChatBotPage:
    def __init__(self):
        self.logic = PreCogLogic()
        # Generamos un GeoDataFrame de ejemplo con valores por defecto
        self.gdf = self.logic.generate_risk_map(
            velocidad=50, lluvia=20, viento=10, temperatura=20, humedad=50
        )
        # Pronóstico simulado de 7 días
        days = pd.date_range(start=pd.Timestamp.today(), periods=7).strftime("%a %d/%m")
        forecast_data = []
        for _, row in self.gdf.iterrows():
            forecast_data.append({
                "Distrito": row['name'],
                **{day: np.clip(np.random.normal(row['riesgo'], 10), 0, 100) for day in days}
            })
        self.df_forecast = pd.DataFrame(forecast_data)
        self.days = days

    def show(self):
        st.header("🤖 ChatBot de Precog")
        st.markdown("Haz preguntas sobre los distritos y niveles de riesgo de Madrid.")

        user_input = st.text_input("Tu pregunta:", "")

        if user_input:
            response = self.answer_question(user_input)
            st.markdown(f"**Bot:** {response}")

    def answer_question(self, text):
        text = text.lower()

        if "más riesgo" in text:
            max_riesgo = self.gdf["riesgo"].max()
            distrito = self.gdf.loc[self.gdf["riesgo"].idxmax(), "name"]
            return f"El distrito con más riesgo actualmente es **{distrito}** con un nivel de riesgo del {max_riesgo:.1f}%."

        elif "menos riesgo" in text:
            min_riesgo = self.gdf["riesgo"].min()
            distrito = self.gdf.loc[self.gdf["riesgo"].idxmin(), "name"]
            return f"El distrito con menos riesgo actualmente es **{distrito}** con un nivel de riesgo del {min_riesgo:.1f}%."

        elif "riesgo" in text and any(day.lower() in text for day in self.days):
            day_match = [day for day in self.days if day.lower() in text][0]
            max_row = self.df_forecast.loc[self.df_forecast[day_match].idxmax()]
            return f"El día **{day_match}**, el distrito con más riesgo será **{max_row['Distrito']}** con {max_row[day_match]:.1f}%."

        else:
            return "Lo siento, no entiendo tu pregunta. Puedes preguntar cosas como 'qué distrito tiene más riesgo hoy' o 'cómo está el riesgo el próximo lunes'."
