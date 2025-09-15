import numpy as np

class PreCogLogic:
    def __init__(self):
        pass  # Aquí se podrían cargar modelos reales

    def generate_risk_map(self, velocidad=50, lluvia=20, viento=30, temperatura=25, humedad=50):
        """
        Genera un mapa de riesgo 3D combinando varios factores.
        """
        # Crear cuadrícula 10x10
        x, y = np.meshgrid(range(10), range(10))

        # Función de riesgo combinando todos los factores
        z = np.random.rand(10, 10) * 50 + (velocidad + lluvia + viento + (temperatura/2) + (humedad/2)) / 5
        z = np.clip(z, 0, 100)  # Limitar entre 0-100%

        # Color = nivel de riesgo
        color = z
        return x, y, z, color
