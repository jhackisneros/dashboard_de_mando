# Dashboard de Mando y Control - ChronoLogistics

## Estructura del Proyecto

El proyecto está organizado en tres módulos principales, cada uno gestionado por un equipo diferente:

- `1_precog_monitor/` — Precog: Monitor de Riesgo Táctico
- `2_chronos_vision/` — Chronos: Visión Estratégica 2040
- `3_klang_manual/` — K-Lang: Manual de Batalla Interactivo

Cada carpeta contiene el código, assets y documentación específica de su sección.

## Instalación y Puesta en Marcha

### 1. Requisitos Previos
- Python 3.8 o superior
- Git

### 2. Instalación de Dependencias

Se recomienda el uso de un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Las dependencias principales son:
- streamlit (UI principal)
- numpy, pandas (procesamiento de datos)
- matplotlib, seaborn (visualización)
- Pillow (imágenes)
- scikit-learn (modelos y simulaciones)

### 3. Ejecución Local

```bash
streamlit run main.py
```

### 4. Despliegue

Se recomienda desplegar en Streamlit Community Cloud, Hugging Face Spaces o Heroku. Consultar la documentación de cada plataforma para detalles.

## Mapas de Calor 3D y Despliegue en Hugging Face Spaces

### Mapas de Calor 3D
Para visualizaciones avanzadas, se recomienda usar la librería `plotly`:

```bash
pip install plotly
```

Ejemplo de uso en Streamlit:
```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure(data=[go.Surface(z=[[1,2],[3,4]])])
st.plotly_chart(fig)
```

### Despliegue en Hugging Face Spaces
1. Crea una cuenta en [Hugging Face](https://huggingface.co/).
2. Sube tu repositorio y selecciona "Space" tipo Streamlit.
3. Añade un archivo `requirements.txt` con las dependencias.
4. El archivo principal debe ser `run.py`.

Más información: https://huggingface.co/docs/hub/spaces

## Buenas Prácticas de Desarrollo

- Cada equipo trabaja en su carpeta (`1_precog_monitor`, `2_chronos_vision`, `3_klang_manual`).
- Usar control de versiones (Git) y realizar commits frecuentes y descriptivos.
- Documentar funciones y módulos con docstrings claros.
- Mantener el código modular y reutilizable.
- Realizar pruebas unitarias de las funciones críticas.
- Revisar el código de los compañeros antes de hacer merge a la rama principal.

## Colaboración

- Sincronizar cambios diariamente.
- Usar issues y pull requests para coordinar tareas y revisiones.
- Mantener comunicación constante entre equipos para integración de módulos.

## Contacto y Soporte

Para dudas técnicas, contactar al CTO o al responsable de cada módulo.

---

Este proyecto es crítico para la respuesta a crisis de ChronoLogistics. La calidad y robustez del código es prioritaria.