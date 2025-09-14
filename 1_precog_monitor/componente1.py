class MapaCalorRiesgo:
    def __init__(self):
        import numpy as np
        import plotly.graph_objects as go
        self.np = np
        self.go = go

    def mostrar(self, st):
        st.subheader("Mapa de Calor de Clústeres de Riesgo")
        z = self.np.random.rand(10,10) * 100
        fig = self.go.Figure(data=[self.go.Heatmap(z=z, colorscale='YlOrRd')])
        triangulo_x = [2, 7, 5, 2]
        triangulo_y = [3, 2, 8, 3]
        fig.add_trace(self.go.Scatter(x=triangulo_x, y=triangulo_y, mode='lines+markers',
                         line=dict(color='red', width=4), marker=dict(size=12, color='red'), name='Triángulo del Peligro'))
        st.plotly_chart(fig, use_container_width=True)
