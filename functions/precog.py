import numpy as np

class PreCogLogic:
    def __init__(self):
        pass  # Aquí se podrían cargar modelos reales

    def generate_risk_map(self, velocidad, lluvia, temperatura, nivel_rio, humedad, viento):
        """
        Genera una matriz de riesgo 10x10 basada en múltiples variables.
        Devuelve x, y, z y color para el gráfico 3D y heatmap.
        """
        x, y = np.meshgrid(range(10), range(10))

        # Cálculo de riesgo ponderado con viento
        riesgo_base = (velocidad * 0.3 + lluvia * 0.25 + temperatura * 0.1 +
                       nivel_rio * 0.1 + humedad * 0.1 + viento * 0.15)

        # Valores aleatorios alrededor del riesgo base
        z = np.random.rand(10, 10) * 20 + riesgo_base / 2
        z = np.clip(z, 0, 100)

        color = z
        return x, y, z, color
