# functions/precog.py
import numpy as np

class PreCogLogic:
    def __init__(self):
        pass

    def generate_risk_map(self, velocidad, lluvia, viento=0, temperatura=25, humedad=50):
        # Crear cuadrícula 10x10
        x, y = np.meshgrid(range(10), range(10))

        # Función de riesgo combinando todos los factores
        z = np.random.rand(10, 10) * 50 + (velocidad + lluvia + viento) / 5
        z = np.clip(z, 0, 100)

        # Color = nivel de riesgo
        color = z
        return x, y, z, color
