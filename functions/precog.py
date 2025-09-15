import numpy as np

class PreCogLogic:
    def __init__(self):
        pass  # Aquí se pueden cargar modelos reales o modelos ML

    def generate_risk_map(self, velocidad, lluvia, temperatura, nivel_rio, humedad, viento):
        """
        Genera un mapa de riesgo 3D basado en múltiples variables.
        Devuelve x, y, z (nivel de riesgo) y color para visualización.
        """
        x, y = np.meshgrid(range(10), range(10))

        # Riesgo ponderado por factor
        riesgo_base = (velocidad * 0.25 + lluvia * 0.25 + temperatura * 0.1 +
                       nivel_rio * 0.15 + humedad * 0.1 + viento * 0.15)

        # Valores aleatorios alrededor del riesgo base
        z = np.random.rand(10, 10) * 20 + riesgo_base / 2
        z = np.clip(z, 0, 100)

        color = z
        return x, y, z, color
