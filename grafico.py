import pandas as pd
import streamlit as st 

st.title('Gráfico de Salários')

dados = pd.read_csv('grafico.csv')
st.dataframe(dados)
