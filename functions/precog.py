import numpy as np
import pandas as pd

class PreCogLogic:
    def __init__(self):
        # Definir los distritos simulados como un ejemplo
        self.distritos = [
            "Centro", "Arganzuela", "Retiro", "Salamanca", "Chamartín",
            "Tetuán", "Chamberí", "Fuencarral-El Pardo", "Moncloa-Aravaca",
            "Latina", "Carabanchel", "Usera", "Puente de Vallecas", "Moratalaz",
            "Ciudad Lineal", "Hortaleza", "Villaverde", "Villa de Vallecas",
            "Vicálvaro", "San Blas-Canillejas", "Barajas"
        ]

    def generate_risk_map(self, velocidad, lluvia, viento, temperatura, humedad):
        # Crear cuadrícula 10x10
        x, y = np.meshgrid(range(10), range(10))
        # Riesgo simulado por combinación de factores
        z = np.random.rand(10, 10) * 50 + (velocidad + lluvia + viento) / 5
        z = np.clip(z, 0, 100)
        color = z

        # Generar DataFrame de distritos para el monitor de alertas
        distritos = pd.DataFrame({
            "name": self.distritos,
            "riesgo": np.random.rand(len(self.distritos)) * 100
        })

        return distritos, x, y, z, color
