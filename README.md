# Dashboard de Mando y Control - ChronoLogistics
https://github.com/jhackisneros/dashboard_de_mando.git
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
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

Las dependencias principales son:
- streamlit (UI principal)
- numpy, pandas (procesamiento de datos)
- matplotlib, seaborn (visualización)
- Pillow (imágenes)
- scikit-learn (modelos y simulaciones)

### 3. Ejecución Local

Simplemente ejecuta el siguiente comando y el sistema se encargará de todo:

```bash
streamlit run run.py
```

No necesitas preocuparte por rutas ni archivos principales, el dashboard se encargará de mostrar todos los módulos correctamente.

## Ejecución Automática Paso a Paso

1. **Abre una terminal** en la carpeta raíz del proyecto.

2. **Crea el entorno virtual** (solo la primera vez):
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual**:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta la aplicación**:
   ```bash
   streamlit run run.py
   ```

6. **Abre el navegador** en la dirección que aparece en la terminal (normalmente http://localhost:8501).

Si sigues estos pasos y no funciona, revisa la sección "Solución de Problemas" más abajo.

## Solución de Problemas

Si no se ejecuta correctamente:

1. **Verifica la instalación de dependencias**  
   Ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

2. **Comprueba que el archivo `main.py` existe**  
   Debe estar en la raíz del proyecto o en la carpeta del módulo que quieres ejecutar.

3. **Activa el entorno virtual**  
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instala Streamlit si falta**  
   ```bash
   pip install streamlit
   ```

5. **Verifica la versión de Python**  
   Debe ser 3.8 o superior:
   ```bash
   python --version
   ```

6. **Revisa los mensajes de error en la terminal**  
   Copia el mensaje y busca la solución o consulta con el equipo.

### 4. Despliegue

Se recomienda desplegar en Streamlit Community Cloud, Hugging Face Spaces o Heroku. Consulta la documentación de cada plataforma para más detalles.

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
4. El archivo principal debe ser `main.py` (no `run.py`).

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
