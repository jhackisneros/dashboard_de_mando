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
        self.days = pd.date_range(start=pd.Timestamp.today(), periods=7).strftime("%a %d/%m")
        forecast_data = []
        for _, row in self.gdf.iterrows():
            forecast_data.append({
                "Distrito": row['name'],
                **{day: np.clip(np.random.normal(row['riesgo'], 10), 0, 100) for day in self.days}
            })
        self.df_forecast = pd.DataFrame(forecast_data)

    def show(self):
        st.header("🤖 ChatBot FAQ de Precog")
        st.markdown("Selecciona una pregunta para recibir la respuesta automáticamente:")

        preguntas = [
            "¿Qué distrito tiene más riesgo actualmente?",
            "¿Qué distrito tiene menos riesgo actualmente?",
            "Resumen de alertas por color",
            "Pronóstico de riesgo para el próximo lunes",
            "Pronóstico de riesgo para el próximo miércoles"
        ]

        pregunta_seleccionada = st.selectbox("Elige una pregunta:", preguntas)
        if pregunta_seleccionada:
            respuesta = self.answer_question(pregunta_seleccionada)
            st.markdown(f"**Respuesta:** {respuesta}")

    def answer_question(self, pregunta):
        if pregunta == "¿Qué distrito tiene más riesgo actualmente?":
            max_riesgo = self.gdf["riesgo"].max()
            distrito = self.gdf.loc[self.gdf["riesgo"].idxmax(), "name"]
            return f"El distrito con más riesgo actualmente es **{distrito}** con {max_riesgo:.1f}% de riesgo."

        elif pregunta == "¿Qué distrito tiene menos riesgo actualmente?":
            min_riesgo = self.gdf["riesgo"].min()
            distrito = self.gdf.loc[self.gdf["riesgo"].idxmin(), "name"]
            return f"El distrito con menos riesgo actualmente es **{distrito}** con {min_riesgo:.1f}% de riesgo."

        elif pregunta == "Resumen de alertas por color":
            rojos = (self.gdf["riesgo"] > 70).sum()
            amarillos = ((self.gdf["riesgo"] > 40) & (self.gdf["riesgo"] <= 70)).sum()
            verdes = (self.gdf["riesgo"] <= 40).sum()
            return f"⚠️ Alertas: 🔴 {rojos} distritos en rojo, 🟡 {amarillos} en amarillo, 🟢 {verdes} en verde."

        elif "Pronóstico de riesgo para el próximo" in pregunta:
            # Extraemos el día de la pregunta
            if "lunes" in pregunta.lower():
                day = self.days[0]
            elif "miércoles" in pregunta.lower():
                day = self.days[2]
            else:
                day = self.days[0]

            max_row = self.df_forecast.loc[self.df_forecast[day].idxmax()]
            return f"El día **{day}**, el distrito con mayor riesgo será **{max_row['Distrito']}** con {max_row[day]:.1f}% de riesgo."
