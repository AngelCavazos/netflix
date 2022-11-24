import streamlit as st
import pandas as pd

@st.cache
def data_load():
    df = pd.read_csv('movies.csv')
    return df

st.set_page_config(page_title="Nexflix App")

df=data_load()

st.title('Proyecto Netflix')
st.subheader('Creado por Angel Cavazos')
sidebar = st.sidebar

filmes = sidebar.checkbox('Visualizar todos los filmes')

if filmes:
    st.dataframe(df)

titulo = sidebar.text_input('Buscar por titulo (Escribe en mayusculas)')

buscar_tit = sidebar.button('Buscar filmes')

if buscar_tit:
    df_selection = df[df.name.str.contains(titulo)]
    registros = df_selection.shape[0]
    st.markdown(f'Registros totales: {registros}')
    st.dataframe(df_selection)


director_select = sidebar.selectbox('Director',df.director.unique())

director_fil = sidebar.button('Filtrar director')

if director_fil:
    df_selection = df[df.director == director_select]
    registros = df_selection.shape[0]
    st.markdown(f'Registros totales: {registros}')
    st.dataframe(df_selection)