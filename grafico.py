import streamlit as st
import pandas as pd

dados = pd.read_csv('grafico.csv')

st.title('Empresa Cariocas')

dataframe = pd.DataFrame(dados)

chart_data = dados[['pessoa', 'salario']]
st.bar_chart(chart_data.set_index('pessoa'))
