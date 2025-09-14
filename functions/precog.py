import numpy as np

class PreCogLogic:
    def __init__(self):
        pass  # Aquí se pueden cargar modelos reales

    def generate_risk_map(self, velocidad, lluvia):
        # Crear una cuadrícula 10x10 para el ejemplo
        x, y = np.meshgrid(range(10), range(10))

        # Ejemplo de cálculo de riesgo: función simple de velocidad y lluvia
        z = np.random.rand(10, 10) * 50 + (velocidad + lluvia) / 5
        z = np.clip(z, 0, 100)  # limitar entre 0-100%

        # Color = nivel de riesgo
        color = z  # Plotly usa este valor para el colorscale
        return x, y, z, color
