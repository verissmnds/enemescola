import streamlit as st
import pandas as pd

dados = pd.read_csv('grafico.csv')

st.title('Empresa Cariocas')

dataframe = pd.DataFrame(dados)

dataframe.style.highlight_max(axis=0)

st.write(dataframe)

chart_data = dataframe[['pessoa', 'salario']]

st.bar_chart(chart_data.set_index('pessoa'))
