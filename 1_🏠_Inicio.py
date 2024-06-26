import streamlit as st
from params import *

st.set_page_config(page_title='Pluviómetros Ciudadanos DGF', layout="wide")

col1, col2 = st.columns([0.8, 0.2], gap='large')

with col1:
    st.header('Pluviómetros Ciudadanos DGF')
    st.markdown("""
                El proyecto Pluviómetros Ciudadanos (PPCC) es una iniciativa de ciencia ciudadana desarrollada inicialmente en el [Departamento de Geofísica (DGF)](http://www.dgf.uchile.cl/) de la [Facultad de Ciencias Físicas y Matemáticas (FCFM) de la Universidad de Chile](https://ingenieria.uchile.cl/).
                Su objetivo es estudiar los efectos topográficos sobre la distribución espacial de la precipitación en la Región Metropolitana, a partir de mediciones realizadas por observadores(as) voluntarios(as) y de observaciones en estaciones meteorológicas convencionales. A partir de 2024 el proyecto se ha ampliado a las regiones V y VI, a través de iniciativas que se impulsan desde la Universidad de Valparaiso y la Universidad de O ́Higgins.
                
                En este sitio se publica la información recopilada en los eventos de lluvia, y se proveen herramientas para la recopilación de la información y el despliegue de la misma en forma gráfica.
                """, )

with col2:
    st.image(f'static{path_sep}logo_dgf.png')
    st.divider()
    st.image(f'static{path_sep}logo_ppcc.png')
    st.divider()
    st.image(f'static{path_sep}logo_cr2.jpg')
