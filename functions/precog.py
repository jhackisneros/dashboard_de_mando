# functions/precog.py
import numpy as np

class PreCogLogic:
    def __init__(self):
        pass

    def generate_risk_map(self, velocidad, lluvia, viento):
        # Cuadrícula 10x10
        x, y = np.meshgrid(np.linspace(-0.05, 0.05, 10), np.linspace(-0.05, 0.05, 10))
        # Riesgo: función simulada de velocidad, lluvia y viento
        z = np.random.rand(10, 10) * 50 + (velocidad + lluvia + viento)/5
        z = np.clip(z, 0, 100)
        color = z
        return x, y, z, color
