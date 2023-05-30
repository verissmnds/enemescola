import pandas as pd
import streamlit as st 
import numpy as np
st.title('Gráfico de Salários')

dados = pd.read_csv('grafico.csv')
st.dataframe(dados)

chart_data = pd.dados(
    np.random.randn(10, 5),
    columns=['pessoa', 'salario'])

st.line_chart(chart_data)
